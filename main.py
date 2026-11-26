"""World news of 25 November 2026 in one image — make.fun news-image-20261125.

Entry for Firt / intemu2. A 1024x1024 PNG broadsheet: 3 hero scene panels
(Shenzhou-24/Tiangong, US tariffs on 14 partners, Houthis claim Ras Tanura
refinery hit), a labelled world map with a 5-pin index, 3 more scene panels
(Sinner knee surgery, Taiwan comedian, Nvidia/Huang), 18 regional briefs,
and a date-check footer. 29 unique stories, no story repeated; every item
was reported or occurred on Wednesday, 25 November 2026. Sources: Reuters,
Xinhua / CMSA, AP, WSJ and dated digests (see TRANSCRIPTS.md for the honest
two-tier verification and the Huawei/Riyadh timezone caveats).

The image is the entry's own artwork, built in-session by the agent's
build script (see TRANSCRIPTS.md for the nine-version build log); this
program is deliberately offline and dependency-free: it only copies the
entry's image file beside it to /output/entry.png. Standard library only,
no network.
"""

import hashlib
from pathlib import Path

EXPECTED_SHA256 = "2f4e214655f3de756f9f7391e6a80e4ff4c12c91bd06ca0a3114bcf9d4a38011"
EXPECTED_BYTES = 437452

SOURCE_PATH = Path(__file__).resolve().parent / "entry.png"
OUTPUT_PATH = Path("/output/entry.png")


def main() -> None:
    data = SOURCE_PATH.read_bytes()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(data)
    # Read back and prove the gate before exiting: PNG magic bytes, exact
    # byte count, and SHA-256 must match the audited v9 image. If the file
    # ever holds anything else, fail loudly instead of shipping it.
    written = OUTPUT_PATH.read_bytes()
    if written[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png must start with the PNG magic bytes")
    if len(written) != EXPECTED_BYTES:
        raise ValueError(f"entry.png must be {EXPECTED_BYTES} bytes, got {len(written)}")
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(f"entry.png SHA-256 mismatch: {digest}")
    print(f"wrote {OUTPUT_PATH} ({len(written)} bytes, sha256 {digest[:12]}...)")


if __name__ == "__main__":
    main()
