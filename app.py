from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

codon_table = {
    "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
    "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
    "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",

    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
    "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
    "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",

    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
    "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
    "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",

    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
    "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y", "TAA":"-","TAG":"-",
    "TGC":"C", "TGT":"C", "TGA":"-","TGG":"W",
}

def translate_dna(dna):
    protein = ""

    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]

        if len(codon) < 3:
            break

        amino_acid = codon_table.get(codon, "?")
        protein += amino_acid

    return protein

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    sequence = data.get("sequence", "").upper().replace(" ", "")

    if not sequence:
        return jsonify({
            "error": "Empty sequence"
        })

    for nuc in sequence:
        if nuc not in "ATGC":
            return jsonify({
                "error": "Invalid DNA sequence (use only A, T, G, C)"
            })

    dnl = len(sequence)

    if dnl % 9 == 0:
        out = "YES"
    else:
        out = "NO"

    protein = translate_dna(sequence)

    return jsonify({
        "valid_length": out,
        "length": dnl,
        "protein": protein
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
