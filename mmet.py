import sys
import os
from tkinter import E
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from ui_mmet import Ui_MainWindow
import json
import shutil
import getpass
import zipfile
import webbrowser as wb
import traceback
import pyperclip
import platform


def make_zip(dirpath, outFullName):
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        fpath = path.replace(dirpath, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename),
                      os.path.join(fpath, filename))
    zip.close()


def iconFromBase64(base64):
    pixmap = QPixmap()
    pixmap.loadFromData(QByteArray.fromBase64(base64.encode()))
    icon = QIcon(pixmap)
    return icon


class mmet(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.on_setup()
        self.pb_s1.clicked.connect(self.on_pb_s1)
        self.pb_s2.clicked.connect(self.on_pb_s2)
        self.cb_s3_all.clicked.connect(self.on_cb_s3_all)
        self.pushButton.clicked.connect(self.on_export_clicked)
        self.action_MMET.triggered.connect(self.show_about)
        self.action_GitHub.triggered.connect(self.open_github)
        self.action_2.triggered.connect(self.bug_report)
        self.setWindowIcon(iconFromBase64("iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAgklEQVQ4y2NgGLTAxcXlPzomSTMI3Lhx4//BgwfBGMQGiXuaif7P8JP7T5QhEhIScAwzqDNd/b+GHPd/kr0EshnmIpCBJGsGORtkM8w7RBsC0ozsbJh3iDIA2WaYGNEGoNuMbABBL2CzGdkAEMBpAC6b0Q0h2WaSQ5tkANJItmZKAABzO4WhWjcV2gAAAABJRU5ErkJggg=="))
        self.show()

    def on_setup(self):
        self.groupBox_2.setEnabled(False)
        self.groupBox_3.setEnabled(False)
        self.groupBox_4.setEnabled(False)

    def on_pb_s1(self):
        self.versions_path = QFileDialog.getExistingDirectory(
            self, "选择 versions 文件夹")
        if self.versions_path[-8:-1]+self.versions_path[-1] == "versions":
            self.pb_s1.setText(self.versions_path)
            self.groupBox.setEnabled(False)
            self.groupBox_2.setEnabled(True)
        else:
            QMessageBox.warning(self, "错误", "选择的文件夹无效")

    def on_pb_s2(self):
        versions_list = os.listdir(self.versions_path)
        for i in versions_list:
            if not os.path.isdir(self.versions_path+os.sep+i):
                versions_list.remove(i)
        version = QInputDialog.getItem(
            self, "选择游戏版本", '请选择一个将要导出的游戏版本', versions_list, 0, False)
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
            self, "准备导出", "点击 [OK] 以开始导出\n导出时可能会未响应,请耐心等待!")
        self.game_folder_path = self.versions_path+os.sep+self.game_version
        game_json_path = self.game_folder_path+os.sep+self.game_version+".json"
        PCL_ini_path = self.game_folder_path+os.sep+"PCL"+os.sep+"Setup.ini"
        if os.path.exists(PCL_ini_path):
            with open(PCL_ini_path, "r", encoding="utf-8") as f:
                ini = f.readlines()
                for i in range(len(ini)):
                    if ini[i][:14] == "VersionFabric:":
                        ini_fabric_line = i
                    if ini[i][:13] == "VersionForge:":
                        ini_forge_line = i
                VersionFabric = ini[ini_fabric_line].replace(
                    "VersionFabric:", "").replace("\n", "")
                VersionForge = ini[ini_forge_line].replace(
                    "VersionForge:", "").replace("\n", "")
                if VersionFabric != "":
                    self.loader_version = "fabric-"+VersionFabric
                else:
                    self.loader_version = "forge-"+VersionForge
            with open(game_json_path, "r", encoding="utf-8") as f:
                game_json = json.load(f)
                self.client_version = game_json["clientVersion"]
        else:
            try:
                with open(game_json_path, "r", encoding="utf-8") as f:
                    game_json = json.load(f)
                    self.loader_version = game_json["patches"][1]["id"] + \
                        "-"+game_json["patches"][1]["version"]
            except:
                self.loader_version = QInputDialog.getText(
                    self, '输入mod加载器信息', '无法自动读取mod加载器信息<br>请手动输入mod加载器名称及其版本<br>例如: <strong>fabric-0.14.6</strong>')
            try:
                self.client_version = game_json["patches"][0]["version"]
            except:
                self.client_version = QInputDialog.getText(
                    self, '输入游戏版本信息', '无法自动读取游戏版本信息<br>请手动输入游戏版本<br>例如: <strong>1.16.5</strong>')
        # QMessageBox.information(self,"debug",f"loader_version:{self.loader_version}\nclient_version:{self.client_version}\nVersionFabric:{VersionFabric}\nVersionForge:{VersionForge}")
        e_config = self.cb_s3_config.isChecked()
        e_servers = self.cb_s3_servers.isChecked()
        e_options = self.cb_s3_options.isChecked()
        e_resourcepacks = self.cb_s3_resourcepacks.isChecked()
        e_saves = self.cb_s3_saves.isChecked()
        e_shaderpacks = self.cb_s3_shaderpacks.isChecked()
        e_all = self.cb_s3_all.isChecked()
        manifest_json = {"minecraft": {"version": self.client_version, "modLoaders": [{"id": self.loader_version, "primary": True}]}, "manifestType": "minecraftModpack",
                         "manifestVersion": 1, "name": self.game_version, "version": "1.0.0", "author": "MinecraftModpackExportTool "+getpass.getuser(), "files": [], "overrides": "overrides"}
        os.mkdir("mmet_temp")
        json.dump(manifest_json, open("mmet_temp"+os.sep +
                  "manifest.json", "w", encoding="utf-8"))
        if not e_all:
            os.mkdir("mmet_temp"+os.sep+"overrides")
            shutil.copytree(self.game_folder_path+os.sep+"mods",
                            "mmet_temp"+os.sep+"overrides"+os.sep+"mods")
            if e_config:
                shutil.copytree(self.game_folder_path+os.sep+"config",
                                "mmet_temp"+os.sep+"overrides"+os.sep+"config")
            if e_servers:
                shutil.copy(self.game_folder_path+os.sep+"servers.dat",
                            "mmet_temp"+os.sep+"overrides")
            if e_options:
                shutil.copy(self.game_folder_path+os.sep+"options.txt",
                            "mmet_temp"+os.sep+"overrides")
            if e_resourcepacks:
                shutil.copytree(self.game_folder_path+os.sep +
                                "resourcepacks", "mmet_temp"+os.sep+"overrides"+os.sep+"resourcepacks")
            if e_saves:
                shutil.copytree(self.game_folder_path+os.sep+"saves",
                                "mmet_temp"+os.sep+"overrides"+os.sep+"saves")
            if e_shaderpacks:
                shutil.copytree(self.game_folder_path+os.sep+"shaderpacks",
                                "mmet_temp"+os.sep+"overrides"+os.sep+"shaderpacks")
        else:
            shutil.copytree(self.game_folder_path, "mmet_temp"+os.sep+"overrides")
            try:
                shutil.rmtree("mmet_temp"+os.sep+"overrides" +os.sep+"PCL")
            except:
                pass
            os.remove("mmet_temp"+os.sep+"overrides" +os.sep+self.game_version+".jar")
            os.remove("mmet_temp"+os.sep+"overrides" +os.sep+self.game_version+".json")
        if os.path.exists("mmet_temp"+os.sep+"overrides"+os.sep+"config"+os.sep+"ias.json"):
            r = QMessageBox.warning(
                self, "盗号警告", "<h3>是否忽略ias.json?</h3><hr>由于你在整合包中使用了此mod:<br><strong>[游戏内账号切换]InGameAccountSwitcher</strong><br>你的账号登录信息会被储存在配置文件<strong>ias.json</strong>中<br><strong><font color=\"red\">如果你登录了正版，在整合包内保留将会导致别人登上你的账号！</font></strong>", QMessageBox.Yes | QMessageBox.No)
            if r == QMessageBox.Yes:
                os.remove("mmet_temp"+os.sep+"overrides" +
                          os.sep+"config"+os.sep+"ias.json")
        make_zip("mmet_temp", self.game_version+".zip")
        shutil.rmtree("mmet_temp")
        QMessageBox.information(
            self, "导出整合包成功", "已导出整合包文件:\n"+os.path.abspath(self.game_version+".zip"))

    def on_export_clicked(self):
        try:
            self.on_export()
        except Exception as e:
            back = traceback.format_exc()
            back = back.replace("\n", "<br>").replace(" ", "&nbsp;")
            r=QMessageBox.critical(self, "导出失败", back +
                                 "<hr>你可以去此项目的 GitHub 上寻求帮助！(点击 [Yes] 复制错误信息)",QMessageBox.Yes | QMessageBox.Ok)
            if r==QMessageBox.Yes:
                pyperclip.copy(back.replace("<br>","\n").replace("&nbsp;"," ")+f"\nclient_version: {self.client_version}\nloader_version: {self.loader_version}\ngame_folder_path: {self.game_folder_path}\nSystem: {platform.platform()}")
            shutil.rmtree("mmet_temp")

    def show_about(self):
        QMessageBox.about(
            self, "关于 MMET", "<strong>MinecraftModpackExportTool</strong><hr><p>作者: xxtg666</p><p>版本 1.0.6</p>")

    def open_github(self):
        wb.open("https://github.com/xxtg666/MinecraftModpackExportTool")

    def bug_report(self):
        wb.open("https://github.com/xxtg666/MinecraftModpackExportTool/issues")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mmet()
    sys.exit(app.exec_())
