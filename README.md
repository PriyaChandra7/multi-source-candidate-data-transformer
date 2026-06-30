# Multi-Source Candidate Data Transformer

## Overview

This project transforms candidate information from multiple sources into a single canonical candidate profile.

It supports:

- Structured source: Recruiter CSV
- Unstructured source: Resume PDF

The pipeline extracts candidate information, normalizes data, merges records, computes confidence scores, tracks provenance, validates the output schema, and generates configurable JSON output.

---

## Project Structure

```
Eightfold/
│
├── config/
│   └── default.json
│
├── input/
│   ├── recruiter.csv
│   └── resume.pdf
│
├── output/
│   ├── canonical_profile.json
│   └── final_output.json
│
├── src/
│   ├── file_parser.py
│   ├── extractor.py
│   ├── normalizer.py
│   ├── merger.py
│   ├── confidence.py
│   ├── projector.py
│   ├── validator.py
│   └── main.py
│
└── README.md
```

---

## Pipeline

Recruiter CSV
+
Resume PDF

↓

Parser

↓

Extractor

↓

Normalizer

↓

Merger

↓

Confidence Scoring

↓

Projection Engine

↓

Schema Validation

↓

Output JSON

---

## Features

- CSV parsing
- Resume PDF parsing
- Regex-based field extraction
- Phone normalization (E.164)
- Email normalization
- Skill extraction
- Merge strategy
- Provenance tracking
- Confidence scoring
- Configurable output
- CLI support
- JSON validation

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

```bash
cd src

python main.py
```

or

```bash
python main.py --csv ../input/recruiter.csv --resume ../input/resume.pdf --config ../config/default.json
```

---

## Output

The program generates:

- output/canonical_profile.json
- output/final_output.json

---

## Future Improvements

- LinkedIn API integration
- GitHub API integration
- OCR support
- Better skill extraction using NLP
- ML-based confidence scoring