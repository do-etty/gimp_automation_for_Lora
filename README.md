"# gimp_automation_for_Lora" 

# name

gimp_automation_for_Lora

## 概要
このプラグインは、gimpで画像のリサイズや保存の作業を効率化するためのものです。
Stable DiffusionでLora作成のための下処理作業を念頭に置いています。
FitSizeToLargerは画像サイズを、幅と高さの大きい方に合わせます。
ResizeSaveImageは正方形に切り取られた画像を、特性のサイズ（デフォルトではv1系の512に設定）にリサイズし、連番になるようにリネームしてPNGで出力します。

## Requirement
- windows
- gimp

## Usage
このプラグインはgimp内で動作します。
gimp内部では、Python 2.7.18で動いているようですが、外部に影響を与えないため、気にしなくてよいと思います。

gimp内で動作させるには、gimpにプラグインの場所を設定する必要があります。
コードの配置完了後、gimpを起動して「編集＞設定＞フォルダー＞プラグイン」を開きます。
画面の真ん中あたりで、コードを配置したフォルダを選択し、コードの追加をします。
その後、gimpを再起動すると、「pyplugin」という項目がツールバーに表示され、プラグインが使えるようになります。

キーボードショットカットも設定しておくと便利です。
gimpを開き「編集＞キーボードショートカット＞プラグイン」からResizeSaveImageとFitSizeToLargerに好きなキーを割り当ててください。

## Features
FitSizeToLargerは画像の幅と高さを取得し、正方形になるようにリサイズします。
縦横比率を維持してリサイズし、短辺の余った領域は単色で埋められます。。
レイヤーも併せてリサイズします。


ResizeSaveImageは特性のサイズ（デフォルトでは512×512に設定）にリサイズし、
連番になるようにリネームしてPNGで出力します。
縦横比率は維持しないので、正方形になっている画像に対して使用してください。
画像を出力するファイルは、コードを開いて自分で指定します。（22行目）
（小文字のrは消さないでください！）
デフォルトではオフにしていますが、xcfファイル（gimpの編集用データ）も保存できます。

使用例
1.学習させるデータダウンロードし、gimpで開く。
2.画像で必要な部分のみを長方形に切り出す。
3.FitSizeToLargerで正方形にし、ResizeSaveImageで保存。
4.背景画像の除去（transparent-backgroundや、PBRemToolsなど）
5.4で作成した画像を手動でgimpの消しゴムツール等を用いて修正。
（必要な場合のみ。イラスト系は手動修正がほぼ必須な印象です。）
6.5をResizeSaveImageで再び保存。
7.Loraを作成。

## Reference
https://www.youtube.com/watch?v=K0tV0Rnp8PI
https://www.youtube.com/watch?v=p9A1oVXneAE
https://citrus-designs.com/gimp-speedup-techniques/


## Author

[twitter](https://twitter.com/SD_Helper)

## Licence

[MIT](https://......)