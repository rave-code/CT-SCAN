import shutil
from pathlib import Path

SRC = Path("D:\\3eme\\IA\\projet_tp\\archive.zip") 
DST = Path("dataset")
MAP = {"notumor": "no_tumor", "glioma": "tumor",
       "meningioma": "tumor", "pituitary": "tumor"}

for split in ("Training", "Testing"):
    for src_name, dst_name in MAP.items():
        out = DST / dst_name
        out.mkdir(parents=True, exist_ok=True)
        for f in (SRC / split / src_name).glob("*"):
            if f.is_file():
                shutil.copy(f, out / f"{split[:2]}_{src_name}_{f.name}")