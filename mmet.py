import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ui_mmet import Ui_MainWindow
import json
import shutil
import getpass
import zipfile


def make_zip(dirpath, outFullName):
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        fpath = path.replace(dirpath, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename),
                      os.path.join(fpath, filename))
    zip.close()


class mmet(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.on_setup()
        self.pb_s1.clicked.connect(self.on_pb_s1)
        self.pb_s2.clicked.connect(self.on_pb_s2)
        self.cb_s3_all.clicked.connect(self.on_cb_s3_all)
        self.pushButton.clicked.connect(self.on_export_clicked)
        self.show()

    def on_setup(self):
        self.groupBox_2.setEnabled(False)
        self.groupBox_3.setEnabled(False)
        self.groupBox_4.setEnabled(False)

    def on_pb_s1(self):
        self.versions_path = QFileDialog.getExistingDirectory(
            self, "选择 versions 文件夹", os.getcwd())
        if self.versions_path[-8:-1] == "version":
            self.pb_s1.setText(self.versions_path)
            self.groupBox.setEnabled(False)
            self.groupBox_2.setEnabled(True)
        else:
            QMessageBox.warning(self, "错误", "选择的文件夹无效")

    def on_pb_s2(self):
        versions_list = os.listdir(self.versions_path)
        version = QInputDialog.getItem(
            self, "选择游戏版本", '请选择一个将导出的游戏版本', versions_list, 0, False)
        self.game_version = version[0]
        if version[1]:
            self.pb_s2.setText(self.game_version)
            self.groupBox_2.setEnabled(False)
            self.groupBox_3.setEnabled(True)
            self.groupBox_4.setEnabled(True)

    def on_cb_s3_all(self):
        e_all = self.cb_s3_all.isChecked()
        if e_all:
            self.cb_s3_config.setEnabled(False)
            self.cb_s3_servers.setEnabled(False)
            self.cb_s3_options.setEnabled(False)
            self.cb_s3_resourcepacks.setEnabled(False)
            self.cb_s3_saves.setEnabled(False)
            self.cb_s3_shaderpacks.setEnabled(False)
        else:
            self.cb_s3_config.setEnabled(True)
            self.cb_s3_servers.setEnabled(True)
            self.cb_s3_options.setEnabled(True)
            self.cb_s3_resourcepacks.setEnabled(True)
            self.cb_s3_saves.setEnabled(True)
            self.cb_s3_shaderpacks.setEnabled(True)

    def on_export(self):
        QMessageBox.information(
            self, "准备导出", "按下 [OK] 以开始导出\n导出时可能会未响应,请耐心等待!")
        game_folder_path = self.versions_path+os.sep+self.game_version
        PCL_ini_path = game_folder_path+os.sep+"PCL"+os.sep+"Setup.ini"
        if not os.path.exists(PCL_ini_path):
            loader_version = QInputDialog.getText(
                self, '输入mod加载器信息', '无法自动读取mod加载器信息\n请手动输入mod加载器名称及其版本\n例如: fabric-0.13.2')
        else:
            with open(PCL_ini_path, "r", encoding="utf-8") as f:
                ini = f.readlines()
                VersionFabric = ini[6].replace(
                    "VersionFabric:", "").replace("\n", "")
                VersionForge = ini[9].replace(
                    "VersionForge:", "").replace("\n", "")
                if VersionFabric != "":
                    loader_version = "fabric-"+VersionFabric
                else:
                    loader_version = "forge-"+VersionForge
        game_json_path = game_folder_path+os.sep+self.game_version+".json"
        with open(game_json_path, "r", encoding="utf-8") as f:
            game_json = json.load(f)
            client_version = game_json["clientVersion"]
        # QMessageBox.information(self,"debug",f"loader_version:{loader_version}\nclient_version:{client_version}\nVersionFabric:{VersionFabric}\nVersionForge:{VersionForge}")
        e_config = self.cb_s3_config.isChecked()
        e_servers = self.cb_s3_servers.isChecked()
        e_options = self.cb_s3_options.isChecked()
        e_resourcepacks = self.cb_s3_resourcepacks.isChecked()
        e_saves = self.cb_s3_saves.isChecked()
        e_shaderpacks = self.cb_s3_shaderpacks.isChecked()
        e_all = self.cb_s3_all.isChecked()
        os.mkdir("temp")
        os.mkdir("temp"+os.sep+"overrides")
        manifest_json = {"minecraft": {"version": client_version, "modLoaders": [{"id": loader_version, "primary": True}]}, "manifestType": "minecraftModpack",
                         "manifestVersion": 1, "name": self.game_version, "version": "1.0.0", "author": "MinecraftModpackExportTool "+getpass.getuser(), "files": [], "overrides": "overrides"}
        json.dump(manifest_json, open("temp"+os.sep +
                  "manifest.json", "w", encoding="utf-8"))
        if not e_all:
            shutil.copytree(game_folder_path+os.sep+"mods",
                            "temp"+os.sep+"overrides"+os.sep+"mods")
            if e_config:
                shutil.copytree(game_folder_path+os.sep+"config",
                                "temp"+os.sep+"overrides"+os.sep+"config")
            if e_servers:
                shutil.copy(game_folder_path+os.sep+"servers.dat",
                            "temp"+os.sep+"overrides")
            if e_options:
                shutil.copy(game_folder_path+os.sep+"options.txt",
                            "temp"+os.sep+"overrides")
            if e_resourcepacks:
                shutil.copytree(game_folder_path+os.sep +
                                "resourcepacks", "temp"+os.sep+"overrides"+os.sep+"resourcepacks")
            if e_saves:
                shutil.copytree(game_folder_path+os.sep+"saves",
                                "temp"+os.sep+"overrides"+os.sep+"saves")
            if e_shaderpacks:
                shutil.copytree(game_folder_path+os.sep+"shaderpacks",
                                "temp"+os.sep+"overrides"+os.sep+"shaderpacks")
        else:
            shutil.copytree(game_folder_path, "temp"+os.sep+"overrides")
        make_zip("temp", self.game_version+".zip")
        shutil.rmtree("temp")
        QMessageBox.information(
            self, "导出整合包成功", "已导出整合包文件:\n"+os.path.abspath(self.game_version+".zip"))

    def on_export_clicked(self):
        try:
            self.on_export()
        except Exception as e:
            QMessageBox.critical(self, "导出失败", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mmet()
    sys.exit(app.exec_())
