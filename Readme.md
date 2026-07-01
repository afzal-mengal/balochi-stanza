# Balochi NLP with Stanza

This repository provides a custom Stanza pipeline for processing **Balochi** text using models trained on the **UD_Balochi-TEST** treebank.

The project includes trained models for:

- Tokenization
- Part-of-Speech (POS) Tagging
- Lemmatization
- Dependency Parsing

> **Note:** Balochi (`bal`) is not currently an officially supported language in Stanza. This repository provides custom models and a custom inference script to enable processing Balochi text.

---

## Features

- Process plain-text (`.txt`) Balochi files
- Predict POS tags
- Predict lemmas
- Predict dependency parses
- Export results in Stanza's standard format

---

## Requirements

- Python 3.10+
- Stanza
- PyTorch

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Repository Structure

```text
.
├── models/                 # Custom trained Stanza models
├── run_balochi.py          # Inference script
├── sample.txt              # Example input
├── requirements.txt
├── README.md
```

---

## Usage

git clone git@github.com:stanfordnlp/stanza.git
mv sample.txt stanza/
mv run_balochi.py stanza/
cd stanza
source scripts/config.sh

Run the pipeline on a text file:

```bash
python run_balochi.py sample.txt
```

or

```bash
python run_balochi.py path/to/your_file.txt
```

The script loads the custom Balochi models and prints the linguistic analysis for each sentence.

---

## Example

Input (`sample.txt`):

```text
Bādišāay saray dardam kapt.
```

Example output:

```text
Token: Bādišāay
UPOS: NOUN
Head: 4
Relation: nsubj

Token: saray
UPOS: NOUN
Head: 4
Relation: obj

Token: dardam
UPOS: NOUN
Head: 4
Relation: nsubj

Token: kapt.
UPOS: VERB
Head: 0
Relation: root
```

---

## Models

The models included in this repository were trained using the Stanza training utilities on the **UD_Balochi-TEST** dataset.

---

## Limitations

- These are custom models and are **not part of the official Stanza model collection**.
- Accuracy depends on the quality and size of the training data.
- The models are intended for research and experimentation.

---

## Citation

If you use this repository in your research, please cite:

- The Stanza toolkit
- The Universal Dependencies project
- The UD_Balochi-TEST treebank (if applicable)

---

## License

This repository is released under the same license specified in this repository unless otherwise noted.
