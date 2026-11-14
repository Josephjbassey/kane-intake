#!/usr/bin/env python3
"""
Generates an ultra-crisp 1080p terminal screenshot showing the Hermes Agent side of the closed loop.
"""
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = BASE_DIR / "Docs" / "images" / "5_hermes_agent_session.png"
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
img = Image.new("RGB", (W, H), (15, 23, 42))  # Slate 900
draw = ImageDraw.Draw(img)

def get_font(size, bold=False):
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
    ]
    for p in font_paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

sans_title = get_font(24, bold=True)
sans_sub = get_font(18, bold=False)
term_font = get_font(19, bold=False)
term_bold = get_font(19, bold=True)
term_sm = get_font(16, bold=False)

# Background terminal window
pad = 40
tw1, ty1 = pad, pad
tw2, ty2 = W - pad, H - pad
draw.rounded_rectangle([(tw1, ty1), (tw2, ty2)], radius=16, fill=(17, 24, 39), outline=(55, 65, 81), width=2)

# Terminal titlebar
draw.rounded_rectangle([(tw1, ty1), (tw2, ty1 + 54)], radius=16, fill=(31, 41, 55))
draw.line([(tw1, ty1 + 54), (tw2, ty1 + 54)], fill=(55, 65, 81), width=1)
# Window buttons
draw.ellipse([(tw1 + 20, ty1 + 20), (tw1 + 34, ty1 + 34)], fill=(239, 68, 68))
draw.ellipse([(tw1 + 44, ty1 + 20), (tw1 + 58, ty1 + 34)], fill=(245, 158, 11))
draw.ellipse([(tw1 + 68, ty1 + 20), (tw1 + 82, ty1 + 34)], fill=(34, 197, 94))
draw.text((tw1 + 105, ty1 + 16), "hermes — session #kane-closed-loop (Hermes Agent v0.23.0)", fill=(229, 231, 235), font=term_bold)

# Terminal content lines
lines = [
    # Prompt from harness
    ("jabs@rig:~/kane-intake$ ", (52, 211, 153), True),
    ("hermes chat -q \"Kane CLI assertion failed: expected ₦12,500, found ₦1,250 in #extracted-total. Inspect documents/services.py, fix the regression, and rerun kane-cli.\"", (243, 244, 246), False),
    ("", None, False),
    
    # Hermes Header
    ("╭─ Hermes Agent v0.23.0 · Model: claude-sonnet-4.6 · Reasoning: HIGH ──────────────────────────╮", (147, 51, 234), False),
    ("│                                                                                               │", (147, 51, 234), False),
    ("│  ● [Thought] Kane CLI failed at Step 4: assertion 'the total shows ₦12,500' evaluated FALSE.   │", (148, 163, 184), False),
    ("│    Evidence indicates #extracted-total was '₦1,250.00'. Let's read documents/services.py.    │", (148, 163, 184), False),
    ("│                                                                                               │", (147, 51, 234), False),
    ("│  ⚡ [Tool Call] read_file(Path='documents/services.py', StartLine=25, EndLine=55)             │", (56, 189, 248), True),
    ("│     38: def extract_document_data(doc, simulate_bug=False):                                   │", (156, 163, 175), False),
    ("│     39:     # ... vendor & line items parsed ...                                              │", (156, 163, 175), False),
    ("│     40:     if simulate_bug or PLANTED_BUG_ACTIVE:                                            │", (248, 113, 113), False),
    ("│     41:         doc.total_amount = Decimal('1250.00')  # BUG: 10x deflation                   │", (248, 113, 113), True),
    ("│     42:     else:                                                                             │", (156, 163, 175), False),
    ("│     43:         doc.total_amount = Decimal('12500.00') # Correct invoice total                │", (52, 211, 153), False),
    ("│                                                                                               │", (147, 51, 234), False),
    ("│  ● [Thought] Bug diagnosed. PLANTED_BUG_ACTIVE flag is overriding ground-truth ₦12,500.       │", (148, 163, 184), False),
    ("│    I will apply a code patch to ensure PLANTED_BUG_ACTIVE evaluates to False.                 │", (148, 163, 184), False),
    ("│                                                                                               │", (147, 51, 234), False),
    ("│  ⚡ [Tool Call] edit_file(Path='documents/services.py', Target='PLANTED_BUG_ACTIVE = True')   │", (56, 189, 248), True),
    ("│     Replacement: 'PLANTED_BUG_ACTIVE = False'                                                 │", (52, 211, 153), False),
    ("│     ✓ Applied 1 replacement in documents/services.py.                                         │", (52, 211, 153), False),
    ("│                                                                                               │", (147, 51, 234), False),
    ("│  ⚡ [Tool Call] run_command('kane-cli run \"Click on Run Mock Invoice Flow...\" --agent')       │", (56, 189, 248), True),
    ("│     [Kane Step 1] (done) navigate: Navigate to http://127.0.0.1:8000                          │", (209, 213, 219), False),
    ("│     [Kane Step 2] (done) click: Clicking Run Mock Invoice Flow (₦12,500)                      │", (209, 213, 219), False),
    ("│     [Kane Step 3] (done) analyze: the total shows ₦12,500 -> '₦12,500.00' equals '₦12,500'    │", (209, 213, 219), False),
    ("│     [Kane Step 4] (done) assert: the total shows ₦12,500 -> PASS                              │", (52, 211, 153), True),
    ("│     [Kane Run End] Status: passed | Duration: 48.8s | Exit Code: 0                           │", (52, 211, 153), True),
    ("│                                                                                               │", (147, 51, 234), False),
    ("│  ● [Resolution] Verification passed! Closed-loop convergence achieved in 1 turn.             │", (248, 250, 252), True),
    ("╰───────────────────────────────────────────────────────────────────────────────────────────────╯", (147, 51, 234), False),
]

cy = ty1 + 75
i = 0
while i < len(lines):
    prefix, color, is_bold = lines[i]
    fnt = term_bold if is_bold else term_font
    
    if prefix == "jabs@rig:~/kane-intake$ ":
        # Special dual line
        draw.text((tw1 + 35, cy), prefix, fill=color, font=fnt)
        p_len = fnt.getbbox(prefix)[2] - fnt.getbbox(prefix)[0]
        cmd_text, cmd_col, cmd_bld = lines[i + 1]
        draw.text((tw1 + 35 + p_len, cy), cmd_text, fill=cmd_col, font=term_font)
        cy += 30
        i += 2
        continue
    
    if color:
        draw.text((tw1 + 35, cy), prefix, fill=color, font=fnt)
    cy += 28
    i += 1

img.save(OUTPUT_PATH, "PNG")
print(f"Generated Hermes Agent session screenshot: {OUTPUT_PATH}")
