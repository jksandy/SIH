# Repository - Finalists at Smart India Hackathon 2022 #

## Problem statement: ##

Al based solution for predicting major law & order incidents: The solution should be able to use inputs such as: PCR Call key words, Time of call, location, month, calendar of festivals/political events, community involved, distribution of similar PCR Calls, etc. to allow Command Room officers to indicators of serious law & order issue at the very initial stages for timely intervention.

![image](https://github.com/jksandy/SIH/assets/86236260/b3dfb7c2-dd42-476e-b652-0570d6ab7bf1)


## Approach ##

* Initially, the PCR call taker receives the call and responds to the victim. 
* The call is recorded in the background. 
* Then the background is separated from the audio and extracted to obtain the foreground speech. 
* The background is classified to predict the possible event scenario.
* The foreground speech is converted to text.
* The keywords are extracted from the text to find the incident and the details are summarized
* The report generated is sent as messages to the police of the nearest station and the PCR patrol vehicle.
* Calendar event Portal is used monitor and keep check over the current events.
* A portal for the crime monitoring with the distribution of calls and the weight updating is done here. 
* Actions are taken for the ones that can be intervened on time to prevent any exaggeration.
* Finally by priority the requests are served.

## Tech stack ##

* Background Foreground Separation using REPET      
* Background Classification using YAMNet                                            
* Speech to Text Transcription with SpeechRecognition
* Keyword Extraction using keyBERT
* Named Entity Recognition with NLP
* Calendar portal and Reporting portal developed with MEAN
* Messaging the report using Fast2SMS
 
