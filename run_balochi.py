import sys
import stanza
from stanza.utils.conll import CoNLL
import os


if len(sys.argv) != 2:
    print("Usage: python run_balochi.py <text_file.txt>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

nlp = stanza.Pipeline(
    lang="en",  # Dummy language (Balochi is not officially supported)
    processors="tokenize,pos,lemma,depparse",
    tokenize_model_path="../models/bal_test_nocharlm_tokenizer.pt",
    pos_model_path="../models/bal_test_nopretrain_tagger.pt",
    depparse_model_path="../models/bal_test_nopretrain_parser.pt",
    use_gpu=False,
)

doc = nlp(text)

print(doc.to_dict())

doc = nlp(text)

# Output filename
output_file = os.path.splitext(input_file)[0] + ".conllu"

# Write CoNLL-U file
CoNLL.write_doc2conll(doc, output_file)

print(f"CoNLL-U output written to: {output_file}")

