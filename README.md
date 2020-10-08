# User Story
As a desk assistant, I send a lot of emails to many individuals and groups. I want to be able to measure my email's tone; postive, negative, or nuetral. After receiving the overall tone of my email I want to be able to determine the specific section in which my email carries this tone or at least is most affected so I can modify it as needed.

## Set-up
1. First you create a google cloud account and install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) and the necessary packages for [client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries)
2. set up a project using either the Google Cloud Console on the web browser or the gcloud command for the Google Cloud SDK Shell
3. Create a service account and make the service account the account linked to the authorization keys (from this step you should recieve a json file)
4. clone this github and fill in the required fields (json file path and the string of characters that are being analyzed)
5. run the code on Google SDK shell. 

## How it works

The process begins with a string of characters. This string can be a few words, a sentences, or paragraphs. That depends on what wants to be analyzed. Next, the string as a whole is put through the Google NLP API for sentiment analysis. The output of this API is a magnitude score and sentiment score. The sentiment score provides the overall emotional level of the string, which in this case will give the overall emotional level of the text as a whole. 

That sentiment score is stored for later use and the string is processed to be seperated into sentences. The individual sentences are then processed by the Google NLP API for sentiment analysis and each of the scores are used for further processing.

The scores of each of the sentences are then evalulated to extract the sentance with the maximum sentiment score. The sentiment score of the overall text is printed and the sentiment score of the sentence with the largest emotional level is printed along with the sentence number so the user can refer back to that sentence if needed.

![Program Blck diagram](https://github.com/huda-irs/Project-2-Part-1b/blob/master/Proj_diagram.png)

## Important Note:
When retrieving json file project created, if this project were to be further modified to export data or important data from another one of Google Cloud APIs then the scopes will have to added accordingly.

Be sure to import all libraries that are not already imported into Google Cloud Shell

## Possible Future Work:
-[ ] incorporate magnitude score to get a greater understanding of the impact of emotion of each sentence to the overall text
-[ ] ask the user what the desired overall emotional level is wanted and list the sentenes that achieve that so those do not get tweeked by the user
