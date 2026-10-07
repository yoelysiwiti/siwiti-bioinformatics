# 🧬 Siwiti Bioinformatics

A simple Python/Flask web application for basic DNA sequence analysis and DNA-to-protein translation.

The project was developed to explore how programming can be applied to biological and bioinformatics problems, particularly DNA sequence processing.

## 🌐 Live Demo

**[Siwiti Bioinformatics](https://webdev-siwiti.onrender.com/)**

## 📌 Features

The application currently provides the following functionality:

- 🧬 Accepts DNA sequences through a web interface
- ✅ Validates DNA sequences and checks for valid nucleotides (`A`, `T`, `G`, `C`)
- 📏 Calculates the length of the submitted DNA sequence
- 🔢 Checks whether the sequence length is divisible by 9
- 🧪 Translates DNA sequences into protein sequences
- 🧾 Uses a codon table to perform DNA-to-protein translation
- ⚠️ Provides feedback when an empty or invalid sequence is submitted
- 🌐 Returns analysis results through a Flask web application

## 🧪 Example

Given a DNA sequence such as:

```text
ATGGCCATTGTA
```

The application processes the sequence and translates the DNA codons into their corresponding amino acids.

Conceptually:

```text
DNA sequence
     ↓
Validation
     ↓
Sequence processing
     ↓
Codon identification
     ↓
Protein translation
```

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **HTML**
- **CSS**
- **JavaScript**
- **Gunicorn**
- **Git & GitHub**

## 📂 Project Structure

```text
siwiti-bioinformatics/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── ...
│
├── static/
│   └── ...
│
└── README.md
```

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/yoelysiwiti/siwiti-bioinformatics.git
```

### 2. Navigate into the project

```bash
cd siwiti-bioinformatics
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

The application will then be available locally through the Flask development server.

## 🎯 Purpose and Learning

This project was created as a practical exploration of **Python programming and bioinformatics**.

It demonstrates how software can be used to process biological sequences and perform basic computational biology tasks.

The project also represents my interest in developing further skills in:

- Bioinformatics
- Genomic data analysis
- Computational biology
- DNA sequence analysis
- Biological data processing
- Scientific programming

## 🔬 Future Improvements

Possible future developments include:

- GC-content calculation
- Support for FASTA files
- RNA sequence analysis
- Sequence alignment
- More advanced genomic-data analysis
- Visualization of sequence properties
- Integration with established bioinformatics libraries such as Biopython

## 👨‍💻 Author

**Yoel Siwiti**

Software Developer interested in **Python, bioinformatics, data analysis, and the application of computational tools to biological and conservation research.**

### Links

- **GitHub:** https://github.com/yoelysiwiti
- **Live Application:** https://webdev-siwiti.onrender.com/
