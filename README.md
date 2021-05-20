# curriculumVitae

CV's are a great source of structured data, and automating the process seems like a logical next step. 

Here is my approach:

CV2tex.py converts the yaml structured data into a templated LaTeX script. PDFTex is then ran on the output. 


### How to install

Copy the package from here. After that, only a few packages are needed. Python 3+ of course, including jinja2

Then you have to grab a copy of LaTeX:

On macOS, get pdflatex via: http://www.tug.org/mactex/ (Note: this is a big download, and there are lighter versions)

You can confirm this installs what you need with: `which pdflatex` where you should see the path to the right file. 

On linux, you can install it with the steps outlined [here](https://www.tug.org/texlive/quickinstall.html). The full install of TeX Live is recomended, and for full functionality, XeTeX is reccomended. 


