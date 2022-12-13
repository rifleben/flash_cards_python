# flash_cards_python

Flashcard program that uses CSV data. Once you click the "check", that data is removed from the CSV. This allows users to only focus on things that are unknown to them.



![](https://github.com/rifleben/flash_cards_python/blob/main/images/flash_card.gif)


## Summary:

The program uses data from a CSV file with words from English to French translation. The program then presents a "flashcard" to the user and, after 3 seconds, shows the translation. If the user knows the card, they can select the "check", which will remove that dataset from the CSV file. If not, the user can select the "cross", to indicate that they do not know the current selection, and the data will remain in the CSV.


### Tools Used:
- Python Packages:
  - tkinter (GUI interface)
  - random
  - pandas
  - JSON
- IDE:
  - PyCharm
