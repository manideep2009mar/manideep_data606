# Decoding Infant Cries: An Investigation using the Donate-a-cry Corpus

- *Author:* Manideep Akam
- *Term:* Summer 2023

## Abstract
Understanding and interpreting the sounds of infant cries is essential for effective infant care and early detection of health issues. This project aims to explore and analyze the DonateaCry Corpus, a comprehensive dataset of infant cry sounds collected from infants with varying health conditions. By leveraging this dataset, we investigate the patterns, characteristics, and potential indicators of distress encoded within infant cries.

The project employs various techniques for data analysis, including audio processing, feature extraction, and machine learning algorithms. We load the audio recordings using the librosa library and extract relevant features from the cry signals. Subsequently, we apply machine learning models to classify different types of cries, such as hunger cries, pain cries, and discomfort cries.

Additionally, we examine metadata associated with each cry, such as age, gender, and health status, to uncover potential correlations between these factors and cry characteristics. Exploratory data analysis techniques are utilized to gain insights into the distributions, durations, and frequencies of the cries, as well as any variations based on the metadata fields.

The results of this project contribute to the understanding of infant distress signals and provide valuable insights for healthcare professionals, caregivers, and researchers. By identifying distinctive features and patterns within infant cries, we can improve early detection of health issues, develop more effective intervention strategies, and enhance the overall well-being of infants.

## Problem statement
Accurately identifying and interpreting the different types of infant cries poses a significant challenge, hindering timely and appropriate responses to infant distress. The lack of comprehensive understanding and systematic analysis of cry patterns, coupled with the influence of contextual factors like age and health status, restricts our ability to effectively address infant needs. There is a need for robust methodologies and insights to classify cries and uncover correlations with contextual factors, enabling improved recognition and response to infant distress.

## About Data
DonateaCry Corpus, a valuable resource consisting of audio recordings of infant cries collected from infants with diverse health conditions. The dataset offers a rich and comprehensive collection of cry sounds, encompassing different types of distress, such as hunger cries, pain cries, and discomfort cries. It serves as an invaluable tool for investigating the characteristics, patterns, and potential indicators of infant distress.

### Source: 
https://github.com/gveres/donateacry-corpus/

### Data Overview:
Dataset has 457 instances of recording of duration around 7 seconds. 

File naming convention
The audio files should contain baby cry samples, with the corresponding tagging information encoded in the filenames. The samples were tagged by the contributors themselves. So here's how to parse the filenames.

#### iOS:
0D1AD73E-4C5E-45F3-85C4-9A3CB71E8856-1430742197-1.0-m-04-hu.caf
app instance uuid (36 chars)-unix epoch timestamp-app version-gender-age-reason
So, the above translates to:

the sample was recorded with the app instance having the unique id 0D1AD73E-4C5E-45F3-85C4-9A3CB71E8856. These ids are generated upon installation, so they identify an installed instance, not a device or a user
the recording was made at 1430742197 (unix time epoch) , which translates to Mon, 04 May 2015 12:23:17 GMT
version 1.0 of the mobile app was used
the user tagged the recording to be of a boy
the baby is 0-4 weeks old according to the user
the suspected reason of the cry is hunger
#### Android:
0c8f14a9-6999-485b-97a2-913c1cbf099c-1431028888092-1.7-m-26-sc.3gp
The structure is the same with the exception that the unix epoch timestamp is in milliseconds
#### Tags
Gender
- m - male
- f - female

Age
- 04 - 0 to 4 weeks old
- 48 - 4 to 8 weeks old
- 26 - 2 to 6 months old
- 72 - 7 month to 2 years old
- 22 - more than 2 years old

Reason
- hu - hungry
- bu - needs burping
- bp - belly pain
- dc - discomfort
- ti - tired
- lo - lonely
- ch - cold/hot
- sc - scared
- dk - don't know
