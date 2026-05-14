document.getElementById("myForm").addEventListener("submit", async function(e) {

    e.preventDefault();

    const textarea =
        document.getElementById("user_input");

    const fileInput =
        document.getElementById("sequence_file");

    const resultDiv =
        document.getElementById("overall-gc");

    let sequence = textarea.value;

    // ===== READ FILE IF SELECTED =====
    if (fileInput.files.length > 0) {

        const file = fileInput.files[0];

        sequence = await readFile(file);
    }

    // ===== REMOVE FASTA HEADERS =====
    sequence = sequence
        .split("\n")
        .filter(line => !line.startsWith(">"))
        .join("")
        .replace(/\s/g, "")
        .toUpperCase();

    if (!sequence) {

        resultDiv.innerHTML =
            "<p style='color:red;'>No DNA sequence found</p>";

        return;
    }

    resultDiv.innerHTML = "Processing...";

    try {

        const response = await fetch("/analyze", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                sequence: sequence
            })
        });

        const data = await response.json();

        if (data.error) {

            resultDiv.innerHTML =
                `<p style="color:red;">${data.error}</p>`;

        } else {

            resultDiv.innerHTML = `
                <p><strong>Length Multiple of 9:</strong> ${data.valid_length}</p>

                <p><strong>DNA Length:</strong> ${data.length}</p>

                <p><strong>Protein:</strong></p>

                <div style="
                    word-wrap: break-word;
                    background:#111827;
                    padding:10px;
                    border-radius:8px;
                    margin-top:10px;
                ">
                    ${data.protein}
                </div>
            `;
        }

    } catch(error) {

        console.error(error);

        resultDiv.innerHTML =
            "<p style='color:red;'>Server error</p>";
    }
});


// ===== FILE READER =====

function readFile(file) {

    return new Promise((resolve, reject) => {

        const reader = new FileReader();

        reader.onload = function(e) {
            resolve(e.target.result);
        };

        reader.onerror = function() {
            reject("Error reading file");
        };

        reader.readAsText(file);
    });
}