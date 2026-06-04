from fastapi import FastAPI

app = FastAPI()

@app.get("/panels")
def get_panels():
    return [
        {
            "panel_id": "P001",
            "sample_id": "S10042",
            "sequence_type": "DNA",
            "variants": ["BRCA1", "TP53"]
        },
        {
            "panel_id": "P002",
            "sample_id": "S10043",
            "sequence_type": "RNA",
            "variants": ["EGFR", "ALK"]
        }
    ]

    