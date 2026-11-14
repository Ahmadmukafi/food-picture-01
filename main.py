import base64
from pathlib import Path

here = Path(__file__).resolve().parent
text = (here / "entry.b64").read_text().strip()
data = base64.b64decode(text)
if not (data.startswith(b"\x89PNG\r\n\x1a\n") or data.startswith(b"\xff\xd8\xff")):
    raise ValueError("decoded data is not a PNG or JPEG image (bad magic bytes)")
out = Path("/output/entry.png")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(data)
print(f"wrote {out} ({len(data)} bytes)")
