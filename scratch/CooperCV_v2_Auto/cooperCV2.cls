

%----------------------------------------------------------------------------------------
%	CLASS CONFIG
%----------------------------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cooperCV2}[2021/04/23 CV class v2.0]
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{extarticle}} % Pass through any options to the base class
\ProcessOptions\relax  % Process given options
\LoadClass{article}



% update to:  RequirePackage
%----------------------------------------------------------------------------------------
%	FONTS
%----------------------------------------------------------------------------------------

%\usepackage{helvetica} 
\usepackage{roboto}
%\usepackage[default]{raleway} % OG
%\usepackage{times} % OG
\renewcommand{\familydefault}{\sfdefault}

\usepackage{moresize}                    % Provides more font size commands (\HUGE and \ssmall)
\usepackage[utf8]{inputenc}   	 % Required for inputting international characters
\usepackage[T1]{fontenc}      	 % Output font encoding for international characters
\usepackage{fontawesome}           % Required for FontAwesome icons
\usepackage{graphicx}                     % for images and the orcid logo

\renewcommand\emph[1]{#1}
%\renewcommand\textit[1]{\underline{#1}}
\usepackage{calc}                  % Puts math inside length specifications
\usepackage[shortcuts]{extdash}    % Helps LaTeX auto-hyphenate hyphenated words 

\newcommand{\orcid}{\includegraphics[width=10pt]{img/orcid.png}} % cutom for orcidID



%----------------------------------------------------------------------------------------
%	COLORS
%----------------------------------------------------------------------------------------
\usepackage{xcolor}
\definecolor{darkblue}{rgb}{0.0,0.0,0.3}
\definecolor{silver}{RGB}{128,128,128}
\definecolor{lightsilver}{RGB}{190,190,190}
\definecolor{ultramarine}{RGB}{0,32,96}
\definecolor{grey}{RGB}{70,70,70}


%----------------------------------------------------------------------------------------
%	DOCUMENT LAYOUT
%----------------------------------------------------------------------------------------

\reversemarginpar                  % Layout: Puts the section titles on left side of page

% changes the layout for CV style section headings as marginal notes. 
\usepackage[paper=letterpaper,
            %includefoot,             % Uncomment to put page number above margin
            marginparwidth=1.0in,     % Length of section titles
            marginparsep=.06in,       % Space between titles and text
            margin=1in,               % 1 inch margins
            includemp]{geometry}

\setlength{\parindent}{0in}                       % Get rid of indenting throughout entire document
\usepackage[shortlabels]{enumitem}    % Provides special list environments and macros to create new ones


%----------------------------------------------------------------------------------------
%	BIB LAYOUT
%----------------------------------------------------------------------------------------

\usepackage{etaremune} % reverse numbering
\renewcommand{\labelenumi}{[\theenumi]}

% Simple bibsections for CV sections
\makeatletter
\newlength{\bibhang}
\setlength{\bibhang}{1em}
\newlength{\bibsep}
 {\@listi \global\bibsep\itemsep \global\advance\bibsep by\parsep}

\newlist{bibsection}{itemize}{3}
\setlist[bibsection]{label=,leftmargin=\bibhang,%
        itemindent=-\bibhang,
        itemsep=\bibsep,parsep=\z@,partopsep=0pt,
        topsep=0pt}

\newlist{bibenum}{enumerate}{3}
\setlist[bibenum]{label=[\arabic*],resume,leftmargin={\bibhang+\widthof{[999]}},%
        itemindent=-\bibhang,
        itemsep=\bibsep,parsep=\z@,partopsep=0pt,
        topsep=0pt}
\let\oldendbibenum\endbibenum
\def\endbibenum{\oldendbibenum\vspace{-.6\baselineskip}}
\let\oldendbibsection\endbibsection
\def\endbibsection{\oldendbibsection\vspace{-.6\baselineskip}}
\makeatother

% Code to break and resume a reverse ennumerated list
% I get the function is like almost 50 years old, but come on mannn
% https://tex.stackexchange.com/a/438744
\usepackage{etoolbox} %% For \AtEndEnvironment

\makeatletter %% <- change @ so that it can be used in macro names
  %% Define the resume key for etaremune:
  \define@boolkey[EM]{etaremune}{resume}[true]{}
  \presetkeys[EM]{etaremune}{resume=false}{} %% <- false by default

  %% Increase starting value of previous etaremune environment if resuming
  \AtEndEnvironment{etaremune}{%
    \ifEM@etaremune@resume
      \EM@resumewrite{\csname EM@prevlist@\@roman{\@enumdepth}\endcsname}{\EM@currlist}%
    \fi
    \expandafter\xdef\csname EM@prevlist@\@roman{\@enumdepth}\endcsname{\EM@currlist}%
  }
  \newcommand*\EM@resumewrite[2]{% %% Expand arguments and then call EM@resume@write@
    \begingroup
      \edef\temp{\noexpand\EM@resumewrite@
        {\expandafter\string\csname etaremune@#1\endcsname}%
        {\expandafter\string\csname etaremune@#2\endcsname}}%
      \temp
    \endgroup
  }
  \newcommand*\EM@resumewrite@[2]{% %% Write to aux file
    \immediate\write\@auxout{\xdef#1{\string\noexpand\string\the\numexpr#1+\string\noexpand#2 }}%
  }
\makeatother %% <- change @ back



%% add the reversed environment
%% https://tex.stackexchange.com/a/154300
%\newenvironment{bibenum*}
%  {\renewcommand\labelenumi{[\theenumi]}%
%   \etaremune[resume,
%     topsep=0pt,
%     itemsep=\bibsep,
%     parsep=0pt,partopsep=0pt,
%     itemindent=-\bibhang,
%     leftmargin={\bibhang+\widthof{[999]}}]}
%  {\endetaremune}



%----------------------------------------------------------------------------------------
%	FOOTER LAYOUT
%----------------------------------------------------------------------------------------

% Setup header and footer and adjust for margin
\usepackage{fancyhdr, lastpage}
\pagestyle{fancy}
\fancyfoot{}


%\pagestyle{empty}      % Uncomment to get rid of page numbers
\fancyhf{}\renewcommand{\headrulewidth}{0pt}
\fancyfootoffset{\marginparsep+\marginparwidth}
\newlength{\footpageshift}
\setlength{\footpageshift}
          {0.5\textwidth+0.5\marginparsep+0.5\marginparwidth-2in}

%%%% PAGES 2--9 NUMBERING:
%% These lines put page number in bottom (center) of pages 2--end
\cfoot{\hspace{\footpageshift}%
       \parbox{4in}{\hspace*{-2\footpageshift} \hfil
	\emph{\footnotesize\textcolor{grey}{curriculum vitae ~~~·~~~ K. W. Cooper}} \hfill }}

\rfoot{\hspace{\footpageshift}%
       \parbox{4in}{\hspace*{2\footpageshift}\hfil \small\textcolor{grey}{\arabic{page}} \hfil}
	 }


% first page can have a special numbering:
\makeatletter
\let\oldps@plain\ps@plain
\renewcommand{\ps@plain}{\oldps@plain%
\renewcommand{\@evenfoot}{\hspace*{-\footpageshift}\hfil %
   \small\textcolor{grey}{Page~\arabic{page} of \protect\pageref*{LastPage}} \hfil \,}%

\renewcommand{\@oddfoot}{\@evenfoot}}
\makeatother

%----------------------------------------------------------------------------------------
%	MISC LAYOUT
%----------------------------------------------------------------------------------------

% Finally, give us PDF bookmarks and colored links
\usepackage{color,hyperref}
\hypersetup{breaklinks,colorlinks,
            linkcolor=black,urlcolor=black,
            anchorcolor=black,citecolor=black,
            %linkcolor=darkblue,urlcolor=darkblue,
            %anchorcolor=darkblue,citecolor=darkblue,
            %draft
            }

% Define a helper command for the rule, pass color if wish to change
\newcommand{\myRule}[3][lightsilver]{\textcolor{#1}{\rule{#2}{#3}}}

% Use for page breaking section tables  
% instead of moving them to the next page
\usepackage{longtable} 
\setlength\LTleft{0pt} \setlength\LTright{0pt} % Define table margins
\setlength\LTpre{0pt} \setlength\LTpost{-1pt}  % Define table margins

% Use to push the section headings to a new page if none of the entries can make it
% under the heading. May need to figit with the push length a bit
\usepackage{needspace} 
\newlength\headerpush\setlength\headerpush{2em}

%%%%%%%%%%%%%%%%%%%%%%%% End Document Setup %%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%% Helper Commands %%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% SECTION HEADINGS

% The section headings. Flush left in small caps down pseudo-margin. Draw rule
\renewcommand{\section}[1]{\pagebreak[3]%
    \vspace{1.2\baselineskip}%

	\needspace{\headerpush}
	\myRule{\columnwidth}{1pt}\\

    \phantomsection\addcontentsline{toc}{section}{#1}%
    \noindent\llap{\scshape\smash{\parbox[t]{\marginparwidth}{\hyphenpenalty=10000\raggedright #1}}}%
    \vspace{-.5\baselineskip}\par}

% The section headings. Flush left in small caps down pseudo-margin.
\renewcommand{\subsection}[1]{\pagebreak[3]%
    \vspace{1.3\baselineskip}%

    \phantomsection\addcontentsline{toc}{section}{#1}%
    \noindent\llap{\scshape\smash{\parbox[t]{\marginparwidth}{\hyphenpenalty=10000\raggedright #1}}}%
    \vspace{-\baselineskip}\par}


%%% LISTS

% This macro alters a list by removing some of the space that follows the list
% (is used by lists below)
\newcommand*\fixendlist[1]{%
    \expandafter\let\csname preFixEndListend#1\expandafter\endcsname\csname end#1\endcsname
    \expandafter\def\csname end#1\endcsname{\csname preFixEndListend#1\endcsname\vspace{-0.6\baselineskip}}}

% These macros help ensure that items in outer-type lists do not get
% separated from the next line by a page break
% (they are used by lists below)
\let\originalItem\item
\newcommand*\fixouterlist[1]{%
    \expandafter\let\csname preFixOuterList#1\expandafter\endcsname\csname #1\endcsname
    \expandafter\def\csname #1\endcsname{\let\oldItem\item\def\item{\pagebreak[2]\oldItem}\csname preFixOuterList#1\endcsname}
    \expandafter\let\csname preFixOuterListend#1\expandafter\endcsname\csname end#1\endcsname
    \expandafter\def\csname end#1\endcsname{\let\item\oldItem\csname preFixOuterListend#1\endcsname}}
\newcommand*\fixinnerlist[1]{%
    \expandafter\let\csname preFixInnerList#1\expandafter\endcsname\csname #1\endcsname
    \expandafter\def\csname #1\endcsname{\let\oldItem\item\let\item\originalItem\csname preFixInnerList#1\endcsname}
    \expandafter\let\csname preFixInnerListend#1\expandafter\endcsname\csname end#1\endcsname
    \expandafter\def\csname end#1\endcsname{\csname preFixInnerListend#1\endcsname\let\item\oldItem}}

% An itemize-style list with lots of space between items
%
% Usage:
%   \begin{outerlist}
%       \item ...    % (or \item[] for no bullet)
%   \end{outerlist}
\newlist{outerlist}{itemize}{3}
    \setlist[outerlist]{label=\enskip\textbullet,leftmargin=*}
    \fixendlist{outerlist}
    \fixouterlist{outerlist}

% An environment IDENTICAL to outerlist that has better pre-list spacing
% when used as the first thing in a \section
%
% Usage:
%   \begin{lonelist}
%       \item ...    % (or \item[] for no bullet)
%   \end{lonelist}
\newlist{lonelist}{itemize}{3}
    \setlist[lonelist]{label=\enskip\textbullet,leftmargin=*,partopsep=0pt,topsep=0pt}
    \fixendlist{lonelist}
    \fixouterlist{lonelist}

% An itemize-style list with little space between items
%
% Usage:
%   \begin{innerlist}
%       \item ...    % (or \item[] for no bullet)
%   \end{innerlist}
\newlist{innerlist}{itemize}{3}
    \setlist[innerlist]{label=\enskip\textbullet,leftmargin=*,parsep=0pt,itemsep=0pt,topsep=0pt,partopsep=0pt}
    \fixinnerlist{innerlist}

% An environment IDENTICAL to innerlist that has better pre-list spacing
% when used as the first thing in a \section
%
% Usage:
%   \begin{loneinnerlist}
%       \item ...    % (or \item[] for no bullet)
%   \end{loneinnerlist}
\newlist{loneinnerlist}{itemize}{3}
    \setlist[loneinnerlist]{label=\enskip\textbullet,leftmargin=*,parsep=0pt,itemsep=0pt,topsep=0pt,partopsep=0pt}
    \fixendlist{loneinnerlist}
    \fixinnerlist{loneinnerlist}

%%% EXTRA SPACE

% To add some paragraph space between lines.
% This also tells LaTeX to preferably break a page on one of these gaps
% if there is a needed pagebreak nearby.
\newcommand{\blankline}{\quad\pagebreak[3]}
\newcommand{\halfblankline}{\quad\vspace{-0.5\baselineskip}\pagebreak[3]}

%%% FORMATTING MACROS

% Provides a linked \doi{#1} that links doi:#1 to http://dx.doi.org/#1
\usepackage{doi}
% To change the text before the DOI, adjust this command
%\renewcommand\doitext{doi:}

% Provides a linked \url{#1} that doesn't require escape characters
\usepackage{url}


%%%%%%%%%%%%%%%%%%%%%%%% End Helper Commands %%%%%%%%%%%%%%%%%%%%%%%%

%----------------------------------------------------------------------%
% The following is copyright and licensing information for
% redistribution of this LaTeX source code; it also includes a liability
% statement. If this source code is not being redistributed to others,
% it may be omitted. It has no effect on the function of the above code.
%----------------------------------------------------------------------%
% Copyright (c) 2021 by Keiland W. Cooper
%
% Unless otherwise expressly stated, this work is licensed under the
% Creative Commons Attribution-Noncommercial 3.0 United States License. To
% view a copy of this license, visit
% http://creativecommons.org/licenses/by-nc/3.0/us/ or send a letter to
% Creative Commons, 171 Second Street, Suite 300, San Francisco,
% California, 94105, USA.
%
% THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
% OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
% MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
% IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
% CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
% TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
% SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
%----------------------------------------------------------------------%

