#!/usr/bin/env python3
"""
Generates a high-resolution architecture diagram graphic for Kane Intake.
"""
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = BASE_DIR / "Docs" / "images" / "architecture_diagram.png"
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# 1920x1080 canvas
W, H = 1920, 1080
img = Image.new("RGBA", (W, H), (15, 23, 42, 255)) # Dark slate bg
draw = ImageDraw.Draw(img)

# Try loading fonts or fallback
def get_font(size, bold=False):
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for p in font_paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

title_font = get_font(52, bold=True)
subtitle_font = get_font(26, bold=False)
box_title_font = get_font(24, bold=True)
box_body_font = get_font(18, bold=False)
code_font = get_font(16, bold=False)
badge_font = get_font(16, bold=True)

# Grid lines background texture
for x in range(0, W, 60):
    draw.line([(x, 0), (x, H)], fill=(30, 41, 59, 100), width=1)
for y in range(0, H, 60):
    draw.line([(0, y), (W, y)], fill=(30, 41, 59, 100), width=1)

# Header
draw.text((120, 80), "Kane Intake — Autonomous Closed-Loop Architecture", fill=(248, 250, 252), font=title_font)
draw.text((120, 150), "TestMu AI Hackathon 2026 · Real Browser QA (Kane CLI) ⟷ Coding Agent (Hermes)", fill=(148, 163, 184), font=subtitle_font)

# Badges on top right
def draw_badge(x, y, text, bg_color, fg_color):
    bbox = badge_font.getbbox(text)
    bw, bh = bbox[2] - bbox[0] + 24, bbox[3] - bbox[1] + 14
    draw.rounded_rectangle([(x, y), (x + bw, y + bh)], radius=8, fill=bg_color, outline=(71, 85, 105), width=1)
    draw.text((x + 12, y + 6), text, fill=fg_color, font=badge_font)
    return x + bw + 15

bx = 1200
bx = draw_badge(bx, 85, "Django 6 + HTMX", (30, 41, 59), (226, 232, 240))
bx = draw_badge(bx, 85, "Djinn UI (PyPI)", (30, 41, 59), (226, 232, 240))
bx = draw_badge(bx, 85, "pip-audit Passed", (6, 78, 59), (52, 211, 153))

# Draw Step Boxes
boxes = [
    {
        "num": "01",
        "title": "Document Intake App",
        "sub": "Django 6 + HTMX + Djinn UI",
        "points": [
            "• Invoice PDF / Image upload",
            "• Ground-truth mock fixture (₦12,500)",
            "• Zero-latency local HTMX rendering"
        ],
        "color": (59, 130, 246),
        "rect": (120, 280, 420, 680)
    },
    {
        "num": "02",
        "title": "Browser QA Engine",
        "sub": "Kane CLI (@testmuai/kane-cli)",
        "points": [
            "• Launches real headless Chrome",
            "• Clicks 'Run Mock Invoice Flow'",
            "• Asserts: total shows ₦12,500",
            "• Multi-modal visual + DOM analysis"
        ],
        "color": (16, 185, 129),
        "rect": (480, 280, 780, 680)
    },
    {
        "num": "03",
        "title": "Evidence & Regression",
        "sub": "Kane Catches Calculation Bug",
        "points": [
            "• Found: ₦1,250.00 (Planted bug)",
            "• Expected: ₦12,500.00",
            "• Exit Code 1 (Assertion Failed)",
            "• Dumps failure.yaml + CDP screenshots"
        ],
        "color": (239, 68, 68),
        "rect": (840, 280, 1140, 680)
    },
    {
        "num": "04",
        "title": "Hermes Coding Agent",
        "sub": "Autonomous Self-Healing",
        "points": [
            "• Ingests Kane CLI failure logs",
            "• Identifies error in services.py",
            "• Generates & applies surgical patch",
            "• Re-triggers Kane verification"
        ],
        "color": (168, 85, 247),
        "rect": (1200, 280, 1500, 680)
    },
    {
        "num": "05",
        "title": "Verified Convergence",
        "sub": "100% Pass in 48 Seconds",
        "points": [
            "• Kane CLI confirms total: ₦12,500",
            "• Exit Code 0 (Passed)",
            "• TestMu AI Cloud Session recorded",
            "• Closed-loop QA proven end-to-end"
        ],
        "color": (14, 165, 233),
        "rect": (1560, 280, 1860, 680)
    }
]

for b in boxes:
    x1, y1, x2, y2 = b["rect"]
    # Box background
    draw.rounded_rectangle([(x1, y1), (x2, y2)], radius=16, fill=(30, 41, 59, 230), outline=b["color"], width=2)
    # Step header pill
    draw.rounded_rectangle([(x1 + 20, y1 + 20), (x1 + 70, y1 + 55)], radius=8, fill=b["color"])
    draw.text((x1 + 30, y1 + 25), b["num"], fill=(255, 255, 255), font=box_title_font)
    
    # Title & Sub
    draw.text((x1 + 20, y1 + 75), b["title"], fill=(248, 250, 252), font=box_title_font)
    draw.text((x1 + 20, y1 + 115), b["sub"], fill=(148, 163, 184), font=box_body_font)
    draw.line([(x1 + 20, y1 + 155), (x2 - 20, y1 + 155)], fill=(51, 65, 85), width=1)
    
    # Bullet points
    py = y1 + 180
    for pt in b["points"]:
        draw.text((x1 + 20, py), pt, fill=(203, 213, 225), font=box_body_font)
        py += 45

# Draw flow arrows between boxes
for i in range(len(boxes) - 1):
    x1 = boxes[i]["rect"][2]
    x2 = boxes[i + 1]["rect"][0]
    mid_y = 480
    draw.line([(x1 + 5, mid_y), (x2 - 15, mid_y)], fill=(100, 116, 139), width=3)
    draw.polygon([(x2 - 15, mid_y - 8), (x2 - 2, mid_y), (x2 - 15, mid_y + 8)], fill=(100, 116, 139))

# Return loop arrow from Box 4 back to Box 2
draw.arc([(630, 720), (1350, 880)], start=0, end=180, fill=(168, 85, 247), width=4)
draw.polygon([(630, 800), (630, 785), (615, 800)], fill=(168, 85, 247))
draw.text((910, 890), "Autonomous Retry & Verification Loop", fill=(192, 132, 252), font=box_title_font)

# Bottom quote banner
quote_rect = [(120, 950), (1800, 1020)]
draw.rounded_rectangle(quote_rect, radius=12, fill=(15, 23, 42), outline=(51, 65, 85), width=1)
quote_text = '“No slides. No mocked test runners. Real headless Chrome, real CDP screenshots, and a real code fix.”'
draw.text((150, 970), quote_text, fill=(56, 189, 248), font=box_title_font)

img.save(OUTPUT_PATH, "PNG")
print(f"Generated architecture graphic: {OUTPUT_PATH}")
