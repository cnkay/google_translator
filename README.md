# Google Translate Bot with Selenium API
<img src="https://github.com/cnkay/google_translator/blob/master/images/build.svg"> <img src="https://github.com/cnkay/google_translator/blob/master/images/python.svg"> <img src="https://github.com/cnkay/google_translator/blob/master/images/os.svg"> <img src="https://github.com/cnkay/google_translator/blob/master/images/license.svg">


Console application for word or sentence translate.

**!!!In order for the program to work properly, you need to download the compatible web driver to the same folder as the google.py.**

## Dependencies
```
pip3 install selenium
```
## Run
```
python3 google.py
```
### Attention!
**Browser's and web drivers versions must be the same!**

## Check Browser Version

For Firefox : Open menu > Help > About Firefox

<img src="https://github.com/cnkay/google_translator/blob/master/images/about_firefox.png">

For Chrome/Chromium : chrome://settings/help

<img src="https://github.com/cnkay/google_translator/blob/master/images/about_chrome.png">

## Download Compatible Web Driver

For Firefox : https://github.com/mozilla/geckodriver/releases

For Chrome/Chromium : https://chromedriver.chromium.org/downloads

## How program works?

- When the translation operation starts, program opens browser on background and scrapes translated word with XPath.
More information about XPath : https://www.w3schools.com/xml/xml_xpath.asp

## Supported Languages
| #    | Language                      |
| :--- | :---------------------------- |
| 1    | Afrikaans                     |
| 2    | Albanian                      |
| 3    | Arabic                        |
| 4    | Armenian                      |
| 5    | Azerbaijani                   |
| 6    | Basque                        |
| 7    | Belarusian                    |
| 8    | Bengali                       |
| 9    | Bosnian                       |
| 10   | Bulgarian                     |
| 11   | Catalan                       |
| 12   | Cebuano                       |
| 13   | Chinese (Simplified)          |
| 14   | Chinese (Traditional)         |
| 15   | Corsican                      |
| 16   | Croatian                      |
| 17   | Czech                         |
| 18   | Danish                        |
| 19   | Dutch                         |
| 20   | English                       |
| 21   | Esperanto                     |
| 22   | Estonian                      |
| 23   | Finnish                       |
| 24   | French                        |
| 25   | Frisian                       |
| 26   | Galician                      |
| 27   | Georgian                      |
| 28   | German                        |
| 29   | Greek                         |
| 30   | Gujarati                      |
| 31   | Haitian Creole                |
| 32   | Hausa                         |
| 33   | Hawaiian                      |
| 34   | Hebrew                        |
| 35   | Hindi                         |
| 36   | Hmong                         |
| 37   | Hungarian                     |
| 38   | Icelandic                     |
| 39   | Igbo                          |
| 40   | Indonesian                    |
| 41   | Irish                         |
| 42   | Italian                       |
| 43   | Japanese                      |
| 44   | Javanese                      |
| 45   | Kannada                       |
| 46   | Kazakh                        |
| 47   | Khmer                         |
| 48   | Korean                        |
| 49   | Kurdish                       |
| 50   | Kyrgyz                        |
| 51   | Lao                           |
| 52   | Latin                         |
| 53   | Latvian                       |
| 54   | Lithuanian                    |
| 55   | Luxembourgish                 |
| 56   | Macedonian                    |
| 57   | Malagasy                      |
| 58   | Malay                         |
| 59   | Malayalam                     |
| 60   | Maltese                       |
| 61   | Maori                         |
| 62   | Marathi                       |
| 63   | Mongolian                     |
| 64   | Nepali                        |
| 65   | Norwegian                     |
| 66   | Nyanja (Chichewa)             |
| 67   | Pashto                        |
| 68   | Persian                       |
| 69   | Polish                        |
| 70   | Portuguese (Portugal, Brazil) |
| 71   | Punjabi                       |
| 72   | Romanian                      |
| 73   | Russian                       |
| 74   | Samoan                        |
| 75   | Scots Gaelic                  |
| 76   | Serbian                       |
| 77   | Sesotho                       |
| 78   | Shona                         |
| 79   | Sindhi                        |
| 80   | Sinhala (Sinhalese)           |
| 81   | Slovak                        |
| 82   | Slovenian                     |
| 83   | Somali                        |
| 84   | Spanish                       |
| 85   | Sundanese                     |
| 86   | Swahili                       |
| 87   | Swedish                       |
| 88   | Tagalog (Filipino)            |
| 89   | Tajik                         |
| 90   | Tamil                         |
| 91   | Telugu                        |
| 92   | Thai                          |
| 93   | Turkish                       |
| 94   | Ukrainian                     |
| 95   | Urdu                          |
| 96   | Uzbek                         |
| 97   | Vietnamese                    |
| 98   | Welsh                         |
| 99   | Yiddish                       |
| 100  | Yoruba                        |
| 101  | Zulu                          |

## Mode Selection Menu
```
  __ _  ___   ___   __ _| | ___ 
 / _` |/ _ \ / _ \ / _` | |/ _ \
| (_| | (_) | (_) | (_| | |  __/
 \__, |\___/ \___/ \__, |_|\___|
 |___/             |___/        
 _                       _       _       
| |_ _ __ __ _ _ __  ___| | __ _| |_ ___ 
| __| '__/ _` | '_ \/ __| |/ _` | __/ _ \
| |_| | | (_| | | | \__ \ | (_| | ||  __/
 \__|_|  \__,_|_| |_|___/_|\__,_|\__\___|
            


**********************
*                    *
*   Mode Selection   *
*                    *
**********************

0) Test All Languages
1) Multiple Word Translate
2) Single Word Translate

Selection : 

```
## Multiple Word Translation Result

```
  __ _  ___   ___   __ _| | ___ 
 / _` |/ _ \ / _ \ / _` | |/ _ \
| (_| | (_) | (_) | (_| | |  __/
 \__, |\___/ \___/ \__, |_|\___|
 |___/             |___/        
 _                       _       _       
| |_ _ __ __ _ _ __  ___| | __ _| |_ ___ 
| __| '__/ _` | '_ \/ __| |/ _` | __/ _ \
| |_| | | (_| | | | \__ \ | (_| | ||  __/
 \__|_|  \__,_|_| |_|___/_|\__,_|\__\___|
            



***************************
Mode : Multiple
From : English
To : Turkish
Word Count : 2999
Input File Path : /home/cenk/Desktop/3000CleanEnglish.txt
Input File Seperator : endline
Output File Name : result.txt
Output File Seperator : endline
Start Time : 15:41:04
***************************

Percent: [------------------->] 100%
3000 words translated and saved to result.txt file!

Start Time : 15:41:04
End Time : 16:01:56

```


