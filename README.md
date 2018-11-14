# ScoobyBot
A simple Twitter bot that posts a random frame of video from episodes of Scooby-Doo!

## Current Lexicon
| Series | Seasons |
|---|---|
| The Scooby-Doo Show! | 1,2 |
| Scooby-Doo, Where are You! | 1,2 |

## Developer Information
So as to not reveal my secret keys to the world, this bot leverages environment variables. These environment variables are implemented in code and largely self-explanatory.

**CONSUMER_KEY**, **CONSUMER_SECRET**, **ACCESS_TOKEN**, **ACCESS_TOKEN_SECRET** are used to create the tweepy oauth token.

**SCOOBYLEXICON** is merely the folder path of the lexicon of Scooby vids.

### Lexicon Structure

The script requires a specific folder structure to properly attribute episodes to their series. This structure is referenced in the **seriesMap** variable. This variable should be modified to add or remove series as necessary.

E.g. the folder **WhereAreYou** in the **SCOOBYLEXICON** folder is mapped to the text string 'Scooby-Doo Where are You!' which is used in creating the tweet text.

Rather than this folder structure, the code could trivially be changed to interpret exlusively the filename of each episode where the filename also includes the series name.