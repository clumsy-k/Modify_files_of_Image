# Modify_files_of_Image
This program is program to convert from '.jpg' to '.tiff'.

1.準備
  1-1. pipをインストール
  
    ダウンロード先：https://bootstrap.pypa.io/get-pip.py よりget-pip.pyを任意のディレクトリに保存

  1-2. 保存したディレクトリで下記コマンドを実行する
  
    python3 get-pip.py

  1-3. pipのバージョンを確認 (下記コマンド実行)
  
    pip -v

  1-4. Pillowをインストール (下記コマンド実行)
  
    参照：https://pillow.readthedocs.io/en/latest/installation.html
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade Pillow

2.テストプログラム実行 (下記コマンド実行)

    python3 convert_one_file.py your_image_file.jpg
    your_image_file.tiffが出力されていれば成功

3.プログラム実行 (下記コマンド実行)

    python3 convert_multi_files.py *.jpg
