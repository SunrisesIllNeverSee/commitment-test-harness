# config.py

# Configuration settings for the commitment test harness project

class Config:
    # Model paths
    HUGGINGFACE_MODEL_PATH = "facebook/bart-large-cnn"  # Example model for summarization
    SPACY_MODEL = "en_core_web_sm"  # spaCy model for extraction

    # Extraction parameters
    EXTRACTION_PARAMS = {
        "min_length": 5,
        "max_length": 100,
        "do_sample": False,
    }

    # Plotting settings
    PLOTTING_SETTINGS = {
        "title": "Commitment Fidelity vs Compression Threshold",
        "xlabel": "Compression Threshold",
        "ylabel": "Fidelity",
        "xlim": (0, 1),
        "ylim": (0, 1),
        "grid": True,
    }