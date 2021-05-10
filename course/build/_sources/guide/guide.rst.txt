Guide
=====

Welcome to the teacher's guide of this learning package. It will take you through:
1. **Requirements** - a brief list of important background knowledge and materials needed to teach this course "as is".
2. **How to Use this Resource** - a quick walk through course material, how to use it, and how to prepare for teaching it.
3. **Structure of Source Material** - an introduction to the folder structure of the source material, so you know where's what.

Requirements
------------

Knowledge of Topics
...................

In order to effectively teach this course, the instructors are required to have knowledge of the following topics:

* **Physical climatology**: Knowledge of orbital forcing, radiative fluxes, drivers/mechanisms of atmospheric circulation, atmospheric stability and precipitation and other topics of generaly physical climatology is a requirement.

* **Statistical climatology**: Knowledge of the application of statistics and machine learning to problems in climatology is highly beneficial. It allows for competent supervision of exercises and projects, as well as for giving examples of applications in climatology to enhance the provided lecture materials.

* **Probability and statistics**: Knowledge of important concepts in Bayesian and frequentist statistics, such as central limit theorem, confidence intervals, etc. is a requirement to teach this course.

* **Statitical and classic machine learning techniques**: Knowledge of different regression techniques and Bayesian classification, analysis of variance, principal component analysis/empirical orthogonal functions, random forests, discrimination analysis and similar techniques ensures effective supervision of exercises.

* **Programming**: Basic knowledge of Python programming (and common packages like numpy and sklearn) is required to effectively supervise exercises and projects. 

* **Raspberry Pi**: Basic knowledge of Raspberry Pis, electronics (experience with breadboards, soldering, sensors, jumper cables) is required for phase 3.

Teachers are advised to carefully study the :doc:`syllabus section<../general/syllabus>` to determine if the course contents matches their qualifications. 


Hardware and Software
.....................

* `Anaconda 3.7 <https://www.anaconda.com/download/>`_ (Python 3.7 distribution, including Spyder IDE, numpy and matplotlib).
* One computer per student is required if they are to be provided to students. Alternatively students can bring their own laptops to exercises. The software needed is platform-agnostic and free. It is therefore easy for each student to work on their own Linux, Windows or OSX machine.
* A Raspberry Pi Zerow W with all gear listed in the phase 3 exercise instructions, as well as material for soldering.


Technical Know-How for Editing Course
.....................................

The course website is built with Python (3.7) and the tool sphinx, which allows you to build simple, beautiful html-based documentation (that can be used as a website for the course) from simple text and a Python configuration script. The user of this package is advised to familiarise themselves with the basics of Python, bash and `sphinx <https://www.sphinx-doc.org/en/master/>`_ if they intend to edit the content. 


How to Use this Resource
------------------------

The material can be used "as is" or adapted to suit the requirements of the teacher or institution. 


Use "As Is" - A Quick Walkthrough
..................................

The compiled website can be used "as is" (either online or offline) for the entire course by both students and instructors. Let's start with a quick walk through all sections on the website (in order from top to bottom) and what needs to be done by the instructor before using it as teaching material for their own classes. This is followed by a suggestion for the teaching schedule.

**Starting Page**

The starting page comes with a short description of the course, information for teachers and students, as well as an automatically generated table of contents with links to all pages of the website. No action needs to be taken here. You can always return to the starting page by clicking on the INTEGRATE logo. 

.. figure:: img/startingPage.jpg  
   :align: center
   
   This is what the top of the starting page should look like.

**Course Information** 

General information about the course ("General"), detailed syllabus ("Syllabus"), licenes and terms of use for course materials ("License") and acknowledgements to contributors of the course ("Credits) can be found in the "Course Information" supersection. We recommend that the instructor takes the following actions before they start teaching:

* Edit the "general information" section for students to get an overview. This should include information such as module credits awarded, eligibility, contact details of the instructors, online platforms used for student submission and any other vital information. If the instructor is unfamiliar with sphinx and therefore unable to update the appropriate document and recompile the website, this information can be provided to students directly in class instead.
* Study the "Syllabus" section carefully to ensure you are familiar with the course structure and learning goals of the course. This will also give the instructor an idea of how qualified you are to teach the course. If the taught contents only partially overlaps with the expertise of the instructor, the course may be taught by multiple instructors. Alternatively, the instructor may decide to only teach part of the course and integrate those into their own course.
* Adjust the information on grading in the "Syllabus" section if you intend to deviate from the suggested (and tested) grading scheme. 
* Consult the license section carefully to make sure you give appropriate credit when using this learning resource. 

**Lectures**

.. figure:: img/lectures.jpg  
   :figwidth: 150px
   :width: 150px
   :align: left
   
The lecture supersection includes a short introduction to the lecture series ("Intro"), followed by a series of well-tested lectures. The lecture series ("Building a Climate") successively builds a basic and quantitative understanding of large-to-small scale drivers and processes of the climate system. It is strongly recommended that all lectures are taught in the proposed order. 

Each chapter (page) of the "Building a Climate" corresponds roughly to a 45-60 minute lecture. Adding more example calculations and additional explanations or demonstrations that serve to deepen the knowledge of each chapter topic can quickly result in higher time requirements. However, it has been our experience that at least 45-60 minutes should be dedicated to each chapter to ensure that they are adequately covered. Within a chapter, each sub-heading (usually ending with a **note** admonition) can correspond to 1-2 lecture slides. This will strongly depend on lecturing style, however. 

We recommend that the instructor takes the following actions before they start teaching:

* Go through the learning goals (listed at the top of each lecture) and lectures carefully. The instructor should ensure that they can sufficiently contribute to discussions and answer questions encouragedd by the admonitions labelled "note". These are interjected throughout each lecture. 

* If the instructor prefers to use traditional lecture slides instead of the website, they are encouraged to copy images and text as needed. See section below ("Use Modules or Specific Elements") for more information. Either way, students may use lectures on the website as a personal resource to complement the instructor's teaching.

* The lecture chapters on the course website may alternatively be used as a resource for students in a **flipped classroom** approach. The time spent with the instructor may then serve for discussion and answering questions students have.

**Exercises**

.. figure:: img/exercises.jpg  
   :figwidth: 150px
   :width: 150px
   :align: left

The exercise supersection includes a short introduction ("Intro"), followed several pages that each correspond to one exercise. Each exercise page includes an introduction to the exercise, information about the learning goals, detailed instructions, examples and a clear description of the students' tasks and expected submissions. The entire exercise series are subdivided into 3 phases. The first two letters of the page titles indicate which phase the exercise belongs to. P1, P2, P3 correspond to phase 1, 2 and 3 respectively. All exercises are meant to be worked on in class as a computer practical session under the supervision of the teacher. Exercises of phase 1 and 2 can be completed within one 2h practical session and are to be conducted by students individually. The phase 3 exercise is greater in scope and should be given 3-4 2h practical sessions. It is to be conducted in small groups of 2-4 students.

* Phase 1 consists of exercises (P1-E001 to P1-E005) that introduce the students to basic concepts of programming. Even though these concepts are mostly programming language agnostic, they are introduced through the use of Python3. The teacher is advised to make sure all necessary software and hardware is ready to use.
* Phase 2 allows the students to apply their new programming skills to work on a set of climatological problems. P2-E001 to P2-E004 have a heavy focus on statistics. The introduction to these exercises include a list of statistical background knowledge that is required to complete the exercise. Students are encouraged to prepare for each exercise by familiarising themselves with the listed concepts prior to the supervised practical session. The practical session then allows students to test their knowledge by conducting the exercise, and to ask the teacher questions about the theoretical background that could not be answered through autodidactic means. The theoretical background for P1-E005 is already covered in the lecture and students are advised to re-visit lecture material prior to the exercise. The exercise itself consists of an implementation of a simplified enery balance model for Earth. The teacher is advised to make sure all necessary software and hardware is ready to use. Furthermore, the teacher should study the goals and theoretical background carefully prior to class. 
* Phase 3 consists of one exercise that involves the use of a Raspherry Pi, atmospheric sensors and Python scripting. The goal is to construct a simple measurement system, record atmospheric data and visualise it. Prior to this exercise, the teacher is advised to make sure all necessary software and hardware is ready to use. The exercise will involve some soldering.

It is recommended that the teacher identifies recurring problems, questions and uncertainties over the course of each exercise while helping individual students. These ought to be explained by the teacher during or at the end of each exercise to ensure that the students finish the practical with a correct understanding of the underlying theory. Submission of individual solutions to each exercise (Phase 1-2) will allow the teacher to review those and get a better sense of the students' skills and understanding of the subject matter. It is recommended that the findings from each review are taken into consideration for the subsequent exercise and teaching plans are adjusted dynamically to allow for re-visits of topics or exercises students struggled with.

**Projects**

The projects represent the last phase of the course. All teaching should be completed before entering this phase. The projects allow the students to tackle a bigger climatological problem through the use of more advanced statistics or one machine learning technique. Students are expected to organise themselves into groups of 2-4 and work mostly independently on the projects over the course of 2-3 weeks. Students are expected to familiarise themselves with the method suggested in their project. Scheduled practical sessions can serve as a means for the teacher to provide some assistance where necessary. This may include answering questions about theoretical backgrounds that remain after the students' autodidactic learning. The compiled course material includes 9 suggested and successfully tested projects. The teacher is advised to study these, make sure that they overlap with the teacher's expertise and adjust or replace projects where needed.

**Suggested Teaching Schedule**

.. figure:: img/coursePlan.png  
   :figwidth: 350px
   :width: 350px
   :align: right
   
   Suggestion for a course schedule that fits into a 14 weeks semester.

The time requirements for the lecture series is ~1-2h per lecture, depending on the level of depth and interaction for each lecture. The time requirements for supervised computer practicals are 2h for each Phase 1-2 exercise, ~6-8h for the Phase 3 exercise, and ~6-10h for the projects. To ensure that students are well-equipped with climatological background knowledge, the lecture series should be completed prior to the beginning of the Phase 3 exercise. As long as these requirements are fulfilled, the course can be taught over an entire semester or as a more intense 2 weeks workshop/summer school. 

If the course is taught over a ~14 weeks semester, which has succesfully been tested, it is recommended that 2 time slots per week are arranged. In the first 10 weeks, the lecture and phase 1-2 exercise series are taught in parallel. Both time slots for weeks 11-12 should then be dedicated to the Phase 3 exercise. In week 12, the students' group projects may already be allocated to give students some time to prepare before the first supervised practical session dedicated to the projects. Weeks 13-14 should be used exclusively to work on the projects. The 2 time slots per week give students a chance to get additional guidance from the teacher if needed.

Use Modules or Specific Elements
................................

Due to the modular nature of the course, it is relatively easy to decouple (most) exercises, lectures and projects and use them as part of a different course. The exercise series has been successfully used as a stand-alone by students to teach themselves about programming (phase 1) and applications (phase 2). The projects (phase 4) we list are example projects that have been successfully tested in class. However, they may be replaced by projects taylored to the expertise of the teacher or the learning goals of a course programme without compromising the rest of the course.

Individual images for the lectures can be found in the respective lecture's folder. Latex code for all equations are part of the text (.rst) file for the lecture.

Teachers are invited to deviate from the proposed format and grading to suit their specific academic environment, course programmes and expertise. Individual elements may also be incorporated into existing courses. Please consult the :doc:`license <../general/license>` and :doc:`credits <../general/credits>` sections before doing so. 


Structure of Source Material
----------------------------

The entire course is packaged as a **git repository**. 

**Parent Folder**

The parent folder **integrate/** includes a short description of the learning package (*README.md*), a license file for the instructional materials (*LICENSE*) and the **course/** folder containing the actual course. Note that the license file is only for the git respository. Please consult :doc:`license <../general/license>` to find out about the (very permissive) licenses for individual elements of the teaching package. Furthermore, the file *sphinxBuild.sh* contains the (1-line) Python command used to compile the course as a website. It should be executed from this parent folder.

**Course Folder**

The course folder contains 2 folders:

- **course/build/** - Nothing should be manually edited in this folder. It is the destination folder for compiling the course website (you are currently viewing). It contains the compiled hmtl files, (copied) images and everything needed for a full-fledged website. You can open the starting page for the compiled course by opening the html file **course/build/index.html** in any browser. It can be used offline in a browser or uploaded as an online website. We will not discuss contents of this folder further, since it is a result of the compilation of everything in *course/source/*.

- **course/source/** - This folder contains all source files for the course (website). This includes simple text files (.rst) that will be compiled as webpages, images, code, exercise solutions, etc. All edits should be made to contents in this folder (not the *course/build/* folder).

**Source Folder**

.. figure:: img/sourceFolder.jpg  
   :align: center
   
   Contents of the Source folder. "index.rst" will be compiled to become the starting page.

- **course/source/_static/** - This folder contains some manual (css style) formatting options for the theme of the website. Nothing needs to be edited here.
- **course/source/exercises/** - This folder contains all exercises. It contains everything needed for the "Exercises" supersection of the course website (incl. images and code).  
- **course/source/general/** - This folder contains the everything for the "Course Information" supersection of the course website.
- **course/source/guide/** - This folder contains the files for the "teacher guide" you are currently viewing.
- **course/source/img/** - This folder contains images for the starting page (*index.rst*).
- **course/source/lectures/** - This folder contains all lectures. It contains everything needed for the "Lectures" supersection of the course website (incl. images).  
- **course/source/projects/** - This folder contains the instructions for group projects. The text file for project 1 is *course/source/projects/P001/P001_info.rst*, the text file for project 2 is *course/source/projects/P002/P002_info.rst*, a.s.o.. The project instructions can be edited or replaced by editing the respective .rst files and recompiling the course website.
- **course/source/resources/** - This folder contains everything for the "resources" supersection of the course website.
- **course/source/index.rst** - This is the text file for the starting page. If lectures, exercises or any additional pages are added to the course website, the name of the .rst file should be added in the document tree in the same manner that others are.
- **course/source/conf.py** - This is the configuration script used in the compilation of the course website.

**Lectures Folder**

.. figure:: img/lectureFolder.jpg  
   :align: center
   
   Contents of the Lecture folder.

The *info.rst* file contains general information about lectures and is compiled as the introduction for lectures. All lectures in the **course/source/lectures/** folder are given their own subfolder (A001, A002, etc.). The numbering corresponds to the order in which they are displayed on the course website. Each lecture folder contains a .rst text file that contains all text and code (e.g. for equations). It will be converted into an html file after compilation. Each folder also contains an *img/* folder that contains all images used in the lecture. Instructors are free to use these images in their own lecture materials (under the condition of giving proper credit). 

**Exercises Folder**

Analogously to lectures, each exercise is given its own subfolder. Phase 1 exercise folders are named E001, E002, etc.  and phase 2 exercise folders are named E101, E102, etc.. The folders contain images, code and a .rst file that compiles as the exercise's webpage. Furthermore, each exercise folder contains a folder called *submissions* with a Python example solution for each exercise. If you intend to distribute the compiled website to students, it is recommended that you remove these scripts before compilation.

**Project Folder**

Analogously to lectures and exercises, each project is given its own subfolder. These will only include an .rst text file with a project description that will be compiled as one web page.


