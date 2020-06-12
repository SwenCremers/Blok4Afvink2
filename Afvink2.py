from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from Bio.Data import CodonTable
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def translate():
    ''' translates a dna sequence
    :return: renders html template
    '''

    # retrieves sequence from page
    seq = request.args.get("dna", "")
    try:

        # creates sequence object and translates it with the standard
        # translation table
        bio_dna = Seq(seq, IUPAC.ambiguous_dna)
        standard_trans_table = CodonTable.ambiguous_dna_by_name["Standard"]
        translate = bio_dna.translate(table=standard_trans_table)
    except:
        translate = "Geen geldige dna sequentie"
    return render_template("Afvink2html.html", dna=seq, translate=translate)

def main():
    app.run(debug=True)

main()