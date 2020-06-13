# curriculumVitae

CV's are a great source of structured data, and automating the process seems like a logical next step. 

Here is my approach:

CV2tex.py converts the yaml structured data into a templated LaTeX script. PDFTex is then ran on the output. 

On macOS, get pdflatex via: `$ brew cask install basictex`

You can confirm this installs what you need with: `which pdflatex` where you should see the path to the right file. 