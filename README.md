# flashcards

The TOP_136 words come from merging most frequent word forms and most frequent lemmas found on wikipedia.

https://en.wikipedia.org/wiki/Most_common_words_in_Spanish

The TOP_1000 words come from strommeninc.

https://strommeninc.com/1000-most-common-spanish-words-frequency-vocabulary/


### The purpose of this project
The primary objective was to create something I can use to learned spanish words as well as to learn
and practice my programming skills in the process.

- SQL queries have been practiced.

- A decorator was created to check for SQL errors.

- Tkinter has been practiced.

### How it Works

1. **Word Selection:**
   - Choose a category of words.
   - Categories and the number of remaining words to learn are fetched from the database.
   - Reset the progress if needed.
   - Press "Continue" to move to the next screen.

2. **Learning Process:**
   - The next word is randomly selected from the chosen category, marked as not learned.
   - The word is pronounced in Spanish.
   - After a set time (controlled by the TIMER constant in `window.py`), the back of the card is shown.
   - The word is then pronounced in English.

   **Note:**
   - Pronunciation functionality using `os.system("say -v ...")` is specific to macOS.
   - If you are using a different operating system, you may need to modify the pronunciation functionality.

3. **Interaction:**
   - Press ❌ or ✅︎ buttons to mark the word as not learned or learned, respectively.
   - The next word in the list is displayed.

### Encountered Issues and Solution
Issue:
- After adding pronunciation of words it became possible to crash the app by pressing learned / not learned buttons
too fast.

Solution:

- Buttons are disabled before next card is drawn and a word is pronounced and before
card back is shown and a word is pronounced.

- Buttons are re-enabled after word is pronounced.

### Dependencies

- Python 3.7+


### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rafald1/flashcards.git
   cd flashcards

2. Run the application:
   ```bash
    python main.py
