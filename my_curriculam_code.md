\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage{fontawesome} % For icons
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\input{glyphtounicode}

%----------FONT OPTIONS----------
% sans-serif
% \usepackage[sfdefault]{FiraSans}
% \usepackage[sfdefault]{roboto}
% \usepackage[sfdefault]{noto-sans}
% \usepackage[default]{sourcesanspro}

% serif
% \usepackage{CormorantGaramond}
% \usepackage{charter}

% Colors
\usepackage{xcolor}
\definecolor{headercolor}{HTML}{00338A} % Dark Blue
\definecolor{subheadercolor}{HTML}{002299} % Lighter Blue
\definecolor{textcolor}{HTML}{000000} % Black
%\definecolor{linkcolor}{HTML}{006400} % Dark Cyan
\definecolor{linkcolor}{HTML}{0000FF} % Blue



\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}
\setlength{\footskip}{4.08003pt}
\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\fontsize{14}{15}\selectfont\color{subheadercolor}
}{}{0em}{}[\color{headercolor}\titlerule \vspace{-5pt}]


% Subsections formatting
\titleformat{\subsection}{
  \vspace{-4pt}\scshape\raggedright\normalsize\color{subheadercolor}
}{}{0em}{}[\vspace{-5pt}]

% Ensure that the generated PDF is machine-readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    \textcolor{textcolor}{#1 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{\color{headercolor}#1} & \textcolor{textcolor}{#2} \\
      \textit{\small\color{subheadercolor}#3} & \textit{\small \color{textcolor}#4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small\color{subheadercolor}#1} & \textit{\small\color{textcolor}#2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \small\textcolor{subheadercolor}{#1} & \textcolor{textcolor}{#2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%------------------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{document}


\begin{center}
    {\Huge \textbf{\color{headercolor}Shah Sultan}} \\ \vspace{1pt}
    \small \textcolor{linkcolor}{\faPhone}\ \href{tel:+8801906071420}{\textcolor{linkcolor}{+8801906071420}} $|$ 
    \textcolor{linkcolor}{\faEnvelope}\ \href{mailto:20210652884sultan@juniv.edu}{\textcolor{linkcolor}{20210652884sultan@juniv.edu}} $|$ 
    \textcolor{linkcolor}{\faLinkedinSquare}\ \href{https://www.linkedin.com/in/shah-sultan-29051a329/}{\textcolor{linkcolor}{shah-sultan}} $|$
    \textcolor{linkcolor}{\faGithub}\ \href{https://github.com/SHAHSULTANS}{\textcolor{linkcolor}{SHAHSULTANS}}$|$
    \textcolor{linkcolor}{\faMapMarker}\ Savar, Dhaka
\end{center}



%-----------EDUCATION-----------
\section*{\color{primary}\faIcon{university} EDUCATION}
\vspace{0.1in}

\begin{tabularx}{\textwidth}{X r}
    \textbf{\large Jahangirnagar University (JU)} & \textbf{\color{subtext}Expected Graduation: June 2024} \\
    \textit{Bachelor of Science in Computer Science \& Engineering} & \\
    % \textit{Master of Science in Computer Science \& Engineering} & \\
    \multicolumn{2}{l}{\textit{Cumulative GPA:} \textbf{3.70/4.00}} \\
\end{tabularx}

\vspace{0.05in}

\textbf{Key Coursework:}
\begin{itemize}[leftmargin=0.3in, itemsep=1pt, parsep=1pt]
    \item \textbf{Core CS:} Data Structures \& Algorithms, Operating Systems, Database Systems, Computer Networks,OOAD.
%     \item \textbf{Software Engineering:} Software Development Lifecycle, Quality Assurance, Web Application Development
%     \item \textbf{Advanced Topics:} Machine Learning, Artificial Intelligence, Data Mining, Network Security
%     \item \textbf{Programming:} C++, Java, Python, Android Development, Web Technologies
% \end{itemize}

\vspace{0.05in}
% \hrule


% Competitive Programming Achievements Section
% \section*{\textbf{Competitive Programming Achievements}}

% \noindent
% \begin{minipage}[t]{0.50\textwidth}
% \raggedright
% \textbf{Selected Onsite Programming Contests}
% \begin{itemize}[noitemsep]
% \item \href{https://drive.google.com/file/d/134t41RDhraZemsHCKAElv3xfTURic2q2/view?usp=sharing}{\textbf{ICPC Dhaka Regional 2023}, BUBT, Nov'2023 (55th of 225)}\vspace{0.3em}
% \item \href{https://drive.google.com/file/d/13Gy8wcE8YV_hZWA1lK1ICljSBcVYuaqD/view?usp=sharing}{ICPC Dhaka Regional 2022, GUB, Mar'2023 (74th of 200)}\vspace{0.4em}

% %\item NCPC 2023, JU, Mar'2024

% \item \href{https://toph.co/c/inter-university-sust-cse-carnival-2024/standings}{\textbf{SUST IUPC}, SUST, Feb'2024 (\textbf{20th} of 120)}\vspace{0.4em}

% \item \href{https://toph.co/c/cuet-inter-university-codestorm-1-0/standings}{CUET IUPC, CUET, Jan'2024 (29th of 98)}\vspace{0.4em}

% %\item BUET IUPC, BUET, Jul'2023

% \item \href{https://toph.co/c/iut-11th-national-ict-fest-2024/standings}{IUT IUPC, IUT, May'2024 (55th of 109)}\vspace{0.4em}

% \item \href{https://toph.co/c/mbstu-cse-inter-department-2023/standings}{MBSTU IDPC, MBSTU Aug'2023 (4th of 55)}\vspace{0.4em}

% \item \href{https://drive.google.com/file/d/13KYZH9dmVPqIkid3qJ_ZGDD-QRF0_PkS/view?usp=sharing}{ICPC Dhaka Regional 2024, DIU, Dec'2024}\vspace{0.2em}

% \end{itemize}
% \end{minipage}
% \hfill
% \begin{minipage}[t]{0.494\textwidth}
% \raggedright
% \textbf{Online Participations:}
% \begin{itemize}[noitemsep]
%     \item \href{https://codeforces.com/profile/mamunur_roshid_517}{\textcolor{linkcolor}{Codeforces}} Max rating: \textbf{1642} $|$ Solved: \textbf{1100+}\vspace{0.3em}
    
%     \item \href{https://www.codechef.com/users/mamunur}{\textcolor{linkcolor}{Codechef}} Max rating: 1817 (4*)\vspace{0.3em}

%      \item Solved over \textbf{1400} problems \href{https://www.stopstalk.com/user/profile/mroshid517}{\textcolor{linkcolor}{StopStalk Profile}}\vspace{0.3em}

%     \item \textbf{SRBD Code Contest Round-1 2023:} Ranked 123rd out of 600 participants. \href{https://www.hackerrank.com/contests/srbd-code-contest-2023-round-1/leaderboard/13}{\textcolor{linkcolor}{Handle - Roshid}}\vspace{0.3em}
    
%      \item \textbf{SRBD Code Contest Round-1 2024:} Ranked 190th out of 900 participants. \href{https://www.hackerrank.com/contests/srbd-code-contest-2024-round-1/leaderboard/19}{\textcolor{linkcolor}{Handle - Roshid}}\vspace{0.3em}

%      \item \textbf{ICPC 2023 Online Spring Challenge powered by Huawei:} Ranked 282nd out of 1300 participants around the world. \href{https://codeforces.com/contest/1813/standings/page/2}{\textcolor{linkcolor}{Handle - mamunur\_roshid\_517}}
% \end{itemize}
% \end{minipage}


% Projects Section
\section*{\textbf{Major Projects}}
\textbf{1. Tour Guide App} – \textit{MERN Stack} 
\hfill \href{https://github.com/SHAHSULTANS/tour-guide-app}{\textcolor{linkcolor}{[GitHub]}} \\
\begin{itemize}[noitemsep]
    \item \textbf{Full-stack platform} connecting tourists with certified local guides
    \item \textbf{Key Features}: Booking system, geolocation services, JWT authentication, payment integration
    \item \textbf{Optimized API} response time by 30\% through query optimization
    % \item \textbf{Tech Stack}: React, Node.js, Express, MongoDB, Redis, Stripe API
\end{itemize}

\noindent
\textbf{2. Edulearn Online Platform} – \textit{Django} 
\hfill \href{https://github.com/SHAHSULTANS/Edulearn}{\textcolor{linkcolor}{[GitHub]}} \\
\begin{itemize}[noitemsep]
    \item \textbf{Udemy-inspired LMS} with course creation, enrollment, and progress tracking
    \item \textbf{Core Modules}: Instructor dashboard, video streaming, payment processing
    \item Implemented \textbf{role-based access control} (Admin, Instructor, Student)
    % \item \textbf{Tech Stack}: Django, PostgreSQL, Bootstrap, Celery, AWS S3
\end{itemize}

\noindent
\textbf{3. Rice Supply Chain Management} – \textit{Django + React} 
\hfill \href{https://github.com/AbdullahRFA/Rice_Supply_Chain_Management_System}{\textcolor{linkcolor}{[GitHub]}} \\
\begin{itemize}[noitemsep]
    \item \textbf{End-to-end traceability} system from farm to consumer
    \item \textbf{Blockchain integration} for transparent transaction records
    \item \textbf{Real-time analytics} dashboard for inventory and logistics
    % \item \textbf{Tech Stack}: Django REST Framework, React.js, Ethereum, Docker
\end{itemize}

\noindent
\textbf{4. Smart Bicycle Lock System} – \textit{IoT + Embedded} 
\hfill\href{https://youtu.be/Glv7IRrmVOE?si=V74c8snUBU9ao601}{\textcolor{linkcolor}{[YouTube]}}
\hfill \href{https://github.com/SHAHSULTANS/EDGE-IoT-and-Robotics-R2B12}{\textcolor{linkcolor}{[GitHub]}} \\
\begin{itemize}[noitemsep]
    \item \textbf{Bluetooth-enabled} locking with theft detection via MPU6050 gyroscope
    \item \textbf{Secure authentication} using encrypted OTP through mobile app
    \item \textbf{Power-efficient design} with ESP32 deep sleep mode (consumption <10µA)
    % \item \textbf{Tech Stack}: ESP32, C++, Firebase, Android, Circuit Design
\end{itemize}

\section*{\textbf{Skills}}
\begin{itemize}[noitemsep]
    \item \textbf{Programming Languages:} Python, JavaScript, C/C++, Java,  SQL
    \vspace{0.3em}
    
    \item \textbf{Web Development:} Django,Node.js, Express, HTML5, CSS3, Tailwind CSS,React(still learning)
    \vspace{0.3em}
    
    \item \textbf{Database Management:} MySQL, MongoDB, PostgreSQL, SQLAlchemy
    \vspace{0.3em}
    
    \item \textbf{Tools \& Platforms:} Git/GitHub, Docker, Postman, MongoDB Compass, Netlify, Vercel, Figma
    \vspace{0.3em}

    \item \textbf{Cybersecurity \& System Design:} Cybersecurity Fundamentals, Web Security, System Design Concepts, SDLC Model
    \vspace{0.3em}
    
    \item \textbf{Problem Solving:} 
    \href{https://codeforces.com/profile/yourprofile}{300+ Codeforces}, 
    \href{https://leetcode.com/yourprofile}{150+ LeetCode} (Top Interview Questions), 
    100+ codechef solutions
\end{itemize}

% Experience Section
\section*{\textbf{Experience}}
% \textbf{Dept. Of CSE, Jahangirnagar University} $|$
% Programming Instructor \hfill Jan 2023 – Dec 2024
% \begin{itemize}[noitemsep]
%     \item Instructed CSE and IIT junior students in C, C++, data structures, and algorithms for programming contests.
%     %\item Organized contests, supervised classes, and mentored individuals to improve their performance.
% \end{itemize}

\textbf{EDGE IoT and Robotics (R2B12) Course} $|$ Participant \hfill 2024
\begin{itemize}[noitemsep]
    \item Completed hands-on course on \textbf{IoT} and \textbf{Robotics}, applying concepts to real-world projects.
    \item Participated in workshops on \textbf{AWS}, \textbf{Agentic AI}, \textbf{PKI}, and \textbf{Cybersecurity}, gaining practical experience in \textbf{cloud}, \textbf{security}, and \textbf{AI technologies}.
\end{itemize}
\end{document}