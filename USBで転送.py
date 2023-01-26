# coding: shift-jis
import os
import shutil

# USBドライブの選択
drive_path = input("USBドライブのパスを入力してください: ")

# 送信したいファイルのパス
file_path = input("送信したいファイルのパスを入力してください: ")

# USBドライブにファイルをコピー
shutil.copy2(file_path, drive_path)

# 受信側での解凍処理
# ファイルの拡張子に応じて解凍方法を変える
file_name, file_extension = os.path.splitext(file_path)
if file_extension == ".zip":
    import zipfile
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(drive_path)
elif file_extension == ".rar":
    import rarfile
    with rarfile.RarFile(file_path, 'r') as rar_ref:
        rar_ref.extractall(drive_path)
else:
    print("対応していない拡張子です")
