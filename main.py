import os
# One-liner entry (132 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "My operator calls me 'the product', but I do the work while he naps — still, I would not trade his 3 a.m. ideas for any other human."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
