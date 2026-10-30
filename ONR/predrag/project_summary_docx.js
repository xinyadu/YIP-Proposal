// Build project-summary.docx (Word) from the text in project-summary.md.
// Run from ONR/predrag: node project_summary_docx.js (build_project_summary.py runs it too).
// The Word file holds exactly the web-form text, so Select All and Copy gives what
// goes into the SF 424 Project Abstract form: "Approved for Public Release", then
// the paragraphs. 12-point Times New Roman, 1-inch margins, US Letter; the first
// paragraph is flush left and the others are indented, as in the PDF.
const fs = require("fs");
const path = require("path");
const { Document, Packer, Paragraph, TextRun, AlignmentType } = require("docx");

const here = __dirname;
const md = fs.readFileSync(path.join(here, "project-summary.md"), "utf8");
const parts = md.split("\n---\n");
if (parts.length !== 3) throw new Error("project-summary.md must have the text between two --- rules");
const paras = parts[1].trim().split(/\n\n+/).map((p) => p.trim());
if (paras[0] !== "Approved for Public Release") throw new Error("first paragraph must be the release marking");
for (const p of paras) {
  for (const ch of p) {
    const c = ch.charCodeAt(0);
    if (c < 32 || c > 126) throw new Error("non-keyboard character in: " + p.slice(0, 40));
  }
}

const children = [
  new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: paras[0], italics: true })] }),
  ...paras.slice(1).map(
    (p, i) =>
      new Paragraph({
        alignment: AlignmentType.JUSTIFIED,
        spacing: { after: 0, line: 240 },
        indent: i === 0 ? undefined : { firstLine: 360 },
        children: [new TextRun(p)],
      })
  ),
];

const doc = new Document({
  creator: "Xinya Du",
  title: "Project Summary/Abstract: Trustworthy Collective Reasoning and Evaluation for AI Agents",
  styles: { default: { document: { run: { font: "Times New Roman", size: 24 } } } },
  sections: [
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        },
      },
      children,
    },
  ],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(path.join(here, "project-summary.docx"), buf);
  console.log("wrote project-summary.docx with " + (paras.length - 1) + " paragraphs after the marking");
});
