%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Medium Length Professional CV - RESUME CLASS FILE
%
% This class file defines the structure and design of the resume,
% now including the enhanced header functionality for name, surname, phone number, and links.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\ProvidesClass{resume}[2023/03/26 v1.2 Resume class with enhanced header]

\LoadClass[11pt,letterpaper]{article} % Font size and paper type

\usepackage[parfill]{parskip} % Remove paragraph indentation
\usepackage{array} % Required for boldface (\bf and \bfseries) tabular columns
\usepackage{ifthen} % Required for ifthenelse statements
\usepackage{hyperref} % For hyperlinks
\usepackage{enumitem} % Customize list environments

\pagestyle{empty} % Suppress page numbers

%----------------------------------------------------------------------------------------
% HEADINGS COMMANDS
% Defines commands for printing name and address
%----------------------------------------------------------------------------------------

\def\name#1{\def\@name{#1}} % Defines the \name command to set name
\def\@name{} % Sets \@name to empty by default

\def\addressSep{$\diamond$} % Set default address separator to a diamond

% Initialize address lines to be empty
\let\@addressone\relax
\let\@addresstwo\relax
\let\@addressthree\relax

% \address command for setting addresses
\def\address#1{
  \@ifundefined{@addresstwo}{
    \def\@addresstwo{#1}
  }{
    \@ifundefined{@addressthree}{
      \def\@addressthree{#1}
    }{
      \def\@addressone{#1}
    }
  }
}

% Command for printing an address line
\def\printaddress#1{
  \begingroup
    \def\\{\addressSep\ }
    \centerline{#1}
  \endgroup
  \addressskip
}

% Command for printing the name as a page header
\def\printname{
  \begingroup
    \hfil{\MakeUppercase{\namesize\bfseries\@name}}\hfil
    \nameskip\break
  \endgroup
}

%----------------------------------------------------------------------------------------
% PRINT THE HEADING LINES
% Enhanced to print additional contact information and links
%----------------------------------------------------------------------------------------

\let\ori@document=\document
\renewcommand{\document}{
  \ori@document  % Begin document
  \printname % Print the name specified with \name
  \@ifundefined{@addressone}{}{ % Print the first address if specified
    \printaddress{\@addressone}}
  \@ifundefined{@addresstwo}{}{ % Print the second address if specified
    \printaddress{\@addresstwo}}
  \@ifundefined{@addressthree}{}{ % Print the third addresxs if specified
    \printaddress{\@addressthree}}
}

%----------------------------------------------------------------------------------------
% SECTION FORMATTING
% Defines the rSection environment for the large sections within the CV
%----------------------------------------------------------------------------------------

\newenvironment{rSection}[1]{ % 1 input argument - section name
  \sectionskip
  \MakeUppercase{\bfseries #1} % Section title
  \sectionlineskip
  \hrule % Horizontal line
  \begin{list}{}{ % List for each individual item in the section
    \setlength{\leftmargin}{0em} % Margin within the section
    \setlength{\itemsep}{0pt} % Reduce space between items
    \setlength{\parsep}{0pt} % Reduce space between paragraphs within an item
    \setlength{\topsep}{0pt} % Reduce space before and after list
  }
  \item[]
}{
  \end{list}
}

%----------------------------------------------------------------------------------------
% WORK EXPERIENCE FORMATTING
% Defines the formatting for the work experience section
%----------------------------------------------------------------------------------------

\newenvironment{rSubsection}[4]{ % 4 input arguments - company name, year(s) employed, job title and location
  {\bfseries #1} \hfill {#2} % Bold company name and date on the right
  \ifthenelse{\equal{#3}{}}{}{
    \\
    {\emph #3} \hfill {\emph #4} % Italic job title and location
  }\smallskip
  \begin{itemize}[leftmargin=*,label=$\cdot$]
    \setlength{\itemsep}{-1pt} % Reduce space between bullet points
}{
  \end{itemize}
  \vspace{0.5em} % Some space after the list of bullet points
}

%----------------------------------------------------------------------------------------
% SPACING DEFINITIONS
% Defines the space used in various parts of the document
%----------------------------------------------------------------------------------------

\def\namesize{\large} % Size of the name at the top of the document
\def\addressskip{\smallskip} % Space between address lines
\def\sectionlineskip{\smallskip} % Space above the horizontal line for each section
\def\nameskip{\smallskip} % Space after the name at the top
\def\sectionskip{\smallskip} % Space after the heading section
