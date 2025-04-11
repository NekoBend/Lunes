# 🌙 Lunes - A Visual Language Model with Emotion-Driven Typography

**Lunes** is an experimental **visual language model** that generates emotionally expressive imagery using font-based text rendering.

Unlike traditional NLP models that tokenize and process words, Lunes focuses on **visualized communication**, where **emotion is embedded directly into typography**.
Each emotion is mapped to a specific Japanese font, allowing the same text to carry entirely different tones when rendered.

The goal is to explore **non-verbal nuance** in text generation — capturing not just *what is said*, but *how it feels*.

Lunes outputs styled image representations of emotional messages described via XML, enabling an entirely new modality for computational expression.

## 📦 Project Structure

``` bash
Lunes/
    ├── fonts/                 # Local font files (excluded from repo)
    ├── output/                # Generated image output
    ├── data/
    │   └── emotion_schema.json  # Emotion → Font mapping
    ├── sample_message.xml     # Test message for visual rendering
    ├── tokenizer.py           # XML → Image generator
    └── README.md              # You're here
```

## 🔤 Fonts (Not Included)

Due to licensing and size constraints, font files are **not included** in this repository.

Please manually download the following fonts and place the `.ttf` or `.otf` files in the `fonts/` directory:

### ▶ Google Fonts

| Font Label | Google Fonts Link | Emotion |
|------------|--------------------|---------|
| Kosugi Maru | [Kosugi Maru](https://fonts.google.com/specimen/Kosugi+Maru) | `playfulness` |
| M PLUS 1p | [M PLUS 1p](https://fonts.google.com/specimen/M+PLUS+1p) | `anger` |
| M PLUS Rounded 1c | [M PLUS Rounded 1c](https://fonts.google.com/specimen/M+PLUS+Rounded+1c) | `gentleness` |
| Noto Sans JP | [Noto Sans JP](https://fonts.google.com/specimen/Noto+Sans+JP) | `neutral` (base font) |
| Noto Serif JP | [Noto Serif JP](https://fonts.google.com/specimen/Noto+Serif+JP) | `anxiety` |

### ▶ GitHub-distributed Fonts

| Font Label | GitHub Release Link | Emotion |
|------------|----------------------|---------|
| Source Han Serif JP | [Source Han Serif](https://github.com/adobe-fonts/source-han-serif/releases) | `sadness` |
| UDEV Gothic 35LG | [UDEV Gothic](https://github.com/yuru7/udev-gothic/releases) | `irony` |

**Folder structure:**

``` bash
fonts/
    ├── KosugiMaru-Regular.ttf
    ├── MPLUS1p-Regular.ttf
    ├── MPLUSRounded1c-Regular.ttf
    ├── NotoSansJP-Regular.ttf
    ├── NotoSerifJP-Regular.ttf
    ├── SourceHanSerif-Regular.otf
    ├── UDEVGothic35LG-Regular.ttf
```

## 📄 Sample XML Format

```xml
<message>
  <emotion value="gentleness" />
  <text align="center" size="32">今日はゆっくりしてね</text>
</message>
```

## ⚖️ Status

Lunes is under active development.Currently focusing on:

- XML parser → font-rendered image output

- Emotion schema design

- Minimal generative visual logic

## 📜 License

MIT License Fonts must follow their own respective licenses (Google Fonts are typically under OFL).

## ✨ Created by

[NekoBend](https://github.com/NekoBend)

---

## 🧭 日本語での説明

## 🌙 Lunes（ルネス）— 感情と書体で語る、視覚的言語モデル

Lunes は、感情に応じてフォントを変えることで、文字そのものに**「語り方」や「心のトーン」を与える、実験的な視覚言語モデル**です。

従来の自然言語処理（NLP）モデルが「単語を分解して解析する」のに対し、
Lunes は「文字の見た目＝声色や感情」として扱い、非言語的ニュアンスを視覚的に表現します。

XMLで記述された感情付きメッセージを読み取り、
対応する日本語フォントで画像として出力することで、
「何を言うか」だけでなく「どう言うか」まで含めたコミュニケーションを目指します。

## 📦 プロジェクト構成

```bash
Lunes/
    ├── fonts/                 # ローカルフォントファイル（リポジトリに含めず）
    ├── output/                # 画像出力用ディレクトリ
    ├── data/
    │   └── emotion_schema.json  # 感情 → フォントのマッピング定義
    ├── sample_message.xml     # ビジュアル出力用のサンプルXML
    ├── tokenizer.py           # XML → 画像のレンダラー
    └── README.md              # このファイル
```

## 🔤 フォントについて（Fonts - 含まれていません）

ライセンスやファイルサイズの都合により、フォントファイルはリポジトリには含まれていません。

以下のリンクから .ttf または .otf ファイルを手動でダウンロードし、fonts/ ディレクトリに配置してください：

### ▶ Google Fonts

| フォント名 | ダウンロードリンク | 対応する感情 |
|------------|--------------------|---------|
| Kosugi Maru | [Kosugi Maru](https://fonts.google.com/specimen/Kosugi+Maru) | `playfulness`（無邪気さ） |
| M PLUS 1p | [M PLUS 1p](https://fonts.google.com/specimen/M+PLUS+1p) | `anger`（怒り） |
| M PLUS Rounded 1c | [M PLUS Rounded 1c](https://fonts.google.com/specimen/M+PLUS+Rounded+1c) | `gentleness` （やさしさ） |
| Noto Sans JP | [Noto Sans JP](https://fonts.google.com/specimen/Noto+Sans+JP) | `neutral` （ベースフォント） |
| Noto Serif JP | [Noto Serif JP](https://fonts.google.com/specimen/Noto+Serif+JP) | `anxiety`（不安） |

### ▶ GitHub配布フォント

| フォント名 | GitHubリリースリンク | 対応する感情 |
|------------|----------------------|---------|
| Source Han Serif JP | [Source Han Serif](https://github.com/adobe-fonts/source-han-serif/releases) | `sadness`（寂しさ・哀愁） |
| UDEV Gothic 35LG | [UDEV Gothic](https://github.com/yuru7/udev-gothic/releases) | `irony`（皮肉・乾いた笑い） |

**フォルダ構造:**

``` bash
fonts/
    ├── KosugiMaru-Regular.ttf
    ├── MPLUS1p-Regular.ttf
    ├── MPLUSRounded1c-Regular.ttf
    ├── NotoSansJP-Regular.ttf
    ├── NotoSerifJP-Regular.ttf
    ├── SourceHanSerif-Regular.otf
    ├── UDEVGothic35LG-Regular.ttf
```

## 📄 サンプルXML形式

```xml
<message>
  <emotion value="gentleness" />
  <text align="center" size="32">今日はゆっくりしてね</text>
</message>
```

## ⚖️ 開発ステータス

現在のLunesは開発中です。以下の要素を中心に構築が進んでいます：

- XML構文 → フォント出力レンダリング

- 感情スキーマの設計・運用

- 最小限の視覚生成ロジック

## 📜 ライセンス

このリポジトリのコードは MITライセンス に基づいて公開されています。
ただし、使用するフォントはそれぞれのライセンスに従ってください（Google Fontsは通常OFLです）。

## ✨ 作者

[NekoBend](https://github.com/NekoBend)
