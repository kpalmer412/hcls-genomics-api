from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class GenomicPanel(BaseModel):
    panel_id: str
    sample_id: str
    sequence_type: str
    variants: List[str]

@app.get("/panels")
def get_panels():
    return [
        GenomicPanel(
            panel_id="P001",
            sample_id="S10042",
            sequence_type="DNA",
            variants=["BRCA1", "TP53"]
        ),
        GenomicPanel(
            panel_id="P002",
            sample_id="S10043",
            sequence_type="RNA",
            variants=["EGFR", "ALK"]
        )
    ]