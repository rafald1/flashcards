# flashcards

The TOP_136 words come from merging most frequent word forms and most frequent lemmas found on wikipedia.

https://en.wikipedia.org/wiki/Most_common_words_in_Spanish

The TOP_1000 words come from strommeninc.

https://strommeninc.com/1000-most-common-spanish-words-frequency-vocabulary/


### The purpose of this project
The purpose of this project was to create something I can use to learned spanish words as well as to learn
and practice my programming skills in the process.

SQL queries have been practiced.

A decorator was created to check for SQL errors.

Tkinter has been practiced.


### How does it work
First you choose the category of words. The number in parentheses indicates how many words there are left to learn.
Categories and the numbers of not learned words are fetched from database.
You can reset the progress if needed. Press "Continue" to go to the next screen. Press ❌ or ✅︎ button to start.

The next word is selected randomly from the list created by fetching words from the database from the chosen category
that are marked as not learned.

The word is pronounced in Spanish and after indicated time by TIMER constance in window.py the back of card is shown
and the word is pronounced in English.

You press ❌ or ✅︎ button to not mark or to mark the word as learned and the next word is shown.


### Encountered issues
After adding pronunciation of words it became possible to crash the app by pressing learned / not learned buttons
too fast.

Solution:

Buttons are disabled before:

* next card is drawn and a word is pronounced,

* card_back is shown and a word is pronounced.

Buttons are enabled after word is pronounced.
