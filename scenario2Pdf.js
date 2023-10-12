const fs = require('fs');
const {exec} = require("child_process");

createDirectory = async (scenarioName) => {
    if (!fs.existsSync('data/scenarios/' + scenarioName + '/pdf')) {
        try {
            await  exec('mkdir data/scenarios/' + scenarioName + '/pdf');
        } catch (error) {
            console.error(error);
        }
    }
    if (!fs.existsSync('data/scenarios/' + scenarioName + '/html')) {
        try {
            await  exec('mkdir data/scenarios/' + scenarioName + '/html');
        } catch (error) {
            console.error(error);
        }
    }
};

translate2LaTeX = async (scenarioName) => {
    var data;
    try {
        data = fs.readFileSync('data/scenarios/' + scenarioName + '/' + scenarioName + '.json', 'utf8');
    } catch (err) {
        console.error(err);
    }
    var body = JSON.parse(data);
    const PREAMBLE = "% ----------------------------------------------------------------------------\n" +
            "% File: " + scenarioName + ".tex+ \n" +
            "% Usage: Latex2e\n" +
            "% Creation :  21 janv 2022 sergemorvan29@gmail.com\n" +
            "% Revised:   \n" +
            "% Revised:   \n" +
            "% ----------------------------------------------------------------------------\n" +
            "\\documentclass[12pt, report]{article}\n" +
            "% ----------------------------------------------------------------------------\n" +
            "%-------------------------------------------------------------------------\n" +
            "\\usepackage{helvet}\n" +
            "\\usepackage[utf8]{inputenc}\n" +
            "\\usepackage[french]{babel}\n" +
            "\\usepackage{moreverb}\n" +
            "\\usepackage{eurosym}\n" +
            "\\usepackage{textcomp}\n" +
            "\\usepackage{index}\n" +
            "\\usepackage{amsfonts}\n" +
            "\\usepackage{graphics}\n" +
            "\\usepackage{listings}\n" +
            "\\usepackage{hyperref}\n" +
            "\\usepackage{multimedia}\n" +
            "\\usepackage{pgfpages}\n" +
            "\\usepackage{pgf,xcolor,tikz}\n" +
            "\\usepackage{rotating}\n" +
            "\\usepackage{framed}\n" +
            "\\usepackage[framed,hyperref,standard]{ntheorem}\n" +
            "\\usepackage{fancyhdr,lastpage}\n" +
            "\\usepackage{fancyvrb}\n" +
            "\\usepackage{geometry}\n" +
            "\\geometry{margin=40pt}\n" +
            "\\begin{document}\n";
    const TITLE = "\\begin{center}\n" +
            "\\begin{minipage}{16cm}\n" +
            "\n" +
            "\\begin{center}\n" +
            "{\\sc\\bf\\LARGE Scénario " + body.title + " }\\\\\n" +
            "\\vspace{2cm}\n";
    const END = "\\end{document}";
    var latex = PREAMBLE;
    latex += TITLE;

    const options = {weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'};
    latex += "Auteur : " + body.origin + " \\hfill " + new Date().toLocaleDateString('fr-FR', options) + "\n" +
            "\n" +
            "\\end{center}\n" +
            "\\end{minipage}\n" +
            "\\end{center}\n" +
            "\n" +
            "\\vspace{2cm}\n";
    //  "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n" +
    //   "\\section*{Introduction} \n";
    //    latex += body.introduction.text + "\n";
    latex += "\\section*{\bf Boxing box : }" + body.bbox + "\n";
    body.questions.map(function (section) {
        latex += "\n" +
                "\\section{Question}\n";
        var text = section.text;
        text = text.replace('°', '\\textdegree{}');
        latex += text + "\n";
        latex += "\\subsection*{Réponse}\n";
        text = section.response.text;
        text = text.replace('°', '\\textdegree{}');
        latex += text + "\n";
        if (section.response.Images !== undefined) {
            section.response.Images.map(function (image) {
                latex += "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n" +
                        "\\begin{center}\n" +
                        "\\framebox[1\\width]{\n" +
                        "	\\includegraphics[ width=10cm]{" + image.path + "}\n" +
                        "}\n" +
                        "\\begin{figure}[ht]\n" +
                        "\\caption{\\textit{" + image.description + "}}\n" +
                        "\\end{figure}\n" +
                        "\\end{center}\n" +
                        "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n";
            });
        }
    });
    latex += END;
    var response = await fs.writeFileSync('data/scenarios/' + scenarioName + '/' + scenarioName + '.tex', latex);
}
;

laTeX2Pdf = async (scenarioName) => {

    try {
        exec('pdflatex -output-directory=data/scenarios/' + scenarioName + '/pdf' + ' data/scenarios/' + scenarioName + '/' + scenarioName + '.tex');
    } catch (error) {
        console.error(error);
    }
}
;
async function process(scenarioName) {
    //  const SCENARIO_URL = 'http://93.90.200.21/data/scenarios/';
    const SCENARIO_URL = 'file:/data/scenarios/';
    var response;

    response = await createDirectory(scenarioName);
    response = await translate2LaTeX(scenarioName);
    //response = await laTeX2Pdf(scenarioName);

}
;
module.exports = {
    createDirectory,
    translate2LaTeX,
    laTeX2Pdf,
    process
};