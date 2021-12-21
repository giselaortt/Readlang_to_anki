# Readlang_to_anki
this script parses the files from [Readlang](https://readlang.com/) website in order to create a better importation on [Anki](https://apps.ankiweb.net/) desktop application, and save many hours of my time.


### Context:
  - Anki is a Spaced Repetition System, wich I use every day to learn and practice new languages. 
  - Readlang is an website and chrome extention. It provides an interface to automatically translate unknown words from a foregn language.

### Motivation:
  Both applications are really useful to learn languages, and belong to my routine of studies, however, Readlang does not provide a good importation system. It does export the new words to a .txt file, but has many problems. This python script parses the file and improves the importation.
  Through this integration I can easily and automatically create new anki flashcards while reading content in Readlang, a process that I used to do automatically up to now.


### How to use:
  You need to have python3 installed.
  
  Download the file parser.py to your computer. At Readlang, go to libery and export all your cards. Through the terminal, access the location in witch you've downloaded the script, than run the script passing the file of the Readlang .txt though command line, for example:  `python3 parser.py 2021-12-19_ReadlangWords.txt`
  
  A new file will be created with the cards parsed. Import this new file in anki, you need to select "allow HTML in cards" option, and use ";" as a delimiter.