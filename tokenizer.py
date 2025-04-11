import json
import os

from lxml import etree
from PIL import Image, ImageDraw, ImageFont


def parse_messages(xml_path: str) -> list:
    tree = etree.parse(xml_path)
    root = tree.getroot()

    messages = []

    for message in root.findall("message"):
        emotion = message.findtext("emotion")
        text_elem = message.find("text")

        if emotion is None or text_elem is None:
            continue

        text = text_elem.text
        align = text_elem.get("align", "left")
        size = int(text_elem.get("size", 24))

        messages.append({
            "emotion": emotion,
            "text": text,
            "align": align,
            "size": size,
        })

    return messages


def load_emotion_schema(schema_path: str) -> dict:
    with open(schema_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("emotions", {})


def render_message_to_image(
    text: str,
    font_path: str,
    align: str = "left",
    size: int = 32,
    output_path: str = "output/output.png",
):
    width, height = 512, 128
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(font_path, size)

    if align == "center":
        text_width = draw.textlength(text, font=font)
        x = (width - text_width) // 2
    elif align == "right":
        text_width = draw.textlength(text, font=font)
        x = width - text_width - 10
    else:
        x = 10
    y = (height - size) // 2

    draw.text((x, y), text, font=font, fill="black")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)


def process_messages(messages: list, schema: dict, output_dir: str = "output"):
    os.makedirs(output_dir, exist_ok=True)

    for i, message in enumerate(messages):
        emotion = message["emotion"]
        entry = schema.get(emotion)

        if not entry:
            print(f"[warn] Emotion '{emotion}' is not defined in emotion_schema.json")
            continue

        font_name = entry.get("font_name")
        if not font_name:
            print(f"[warn] Emotion '{emotion}' has no associated font name.")
            continue

        font_path = os.path.join("fonts", font_name)
        output_path = os.path.join(output_dir, f"output_{i}.png")

        render_message_to_image(
            text=message["text"],
            font_path=font_path,
            align=message.get("align", "left"),
            size=message.get("size", 24),
            output_path=output_path,
        )


if __name__ == "__main__":
    schema = load_emotion_schema("data/emotion_schema.json")
    messages = parse_messages("sample_message.xml")
    process_messages(messages, schema)
