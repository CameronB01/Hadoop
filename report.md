# Analysis of Gender Pronouns in Text Corpus

## Introduction

In this study, we aim to explore the differences in the usage frequencies of feminine and masculine personal pronouns in a given corpus. Specifically, we will be looking at two Charles Dickens novels: A Tale of Two Cities and Great Expectations. We will determine whether there is a statistically significant difference between the frequencies of these pronouns when used as subjects versus objects. 

## Methodology

### Dataset

We used a small sample of novels from Charles Dickens and this will allow us to analyze the usage of personal pronouns in different contexts.

### Technologies

To process and analyze the text data, we use the following tools and technologies:

- **SparkNLP**: An open-source library that provides state-of-the-art natural language processing capabilities.
- **Matplotlib**: A plotting library for creating visualizations in Python.
- **Scipy**: A popular statistical package in Python.

## Hypothesis

**Null Hypothesis**: There is not a statistically significant difference in the frequencies of feminine and masculine personal pronouns used as subjects versus objects.

## Evaluation

### Findings:
 - Overall, there was a greater amount of male pronouns (both subject and object)
 - Our p value < 0.05 indicated that there is a statistically significant difference between the groups. 

### Conclusion for Dickens:
Becuase our p-value is less than 0.05, we can reject the null hypothesis and conclude that there is a statistically significant difference between the groups. This result suggests that the usage of feminine and masculine personal pronouns as subjects versus objects is not equal, pointing to potential patterns or biases in pronoun usage.

### Conclusion for Alcott:
Becuase our p-value is less than 0.05, we can reject the null hypothesis and conclude that there is a statistically significant difference between the groups. This result suggests that the usage of feminine and masculine personal pronouns as subjects versus objects is not equal, pointing to potential patterns or biases in pronoun usage.


## Source code for Charles Dickens Example
```python
# Import packages
!wget http://setup.johnsnowlabs.com/colab.sh -O - | bash
import sparknlp
spark = sparknlp.start()
from sparknlp.pretrained import PretrainedPipeline
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
import scipy.stats as stats

pipeline = PretrainedPipeline("explain_document_ml")

# Download books
!curl "https://www.gutenberg.org/cache/epub/98/pg98.txt" -o dickens1.txt
!curl "https://www.gutenberg.org/cache/epub/1400/pg1400.txt" -o dickens2.txt

# Read in books and concatenate
louisa1 = open('dickens1.txt').read()
louisa2 = open('dickens2.txt').read()

all_male_authros = dickens1 + dickens2

# Split into sentences
male_sentences = all_male_authros.split(".")

# Annotate
male_dfs = [pipeline.annotate(hl) for hl in tqdm(male_sentences)]

male_tok_tag = [(df['token'],df['pos']) for df in male_dfs]
male_zips = [list(zip(tt[0], tt[1])) for tt in male_tok_tag]

# This function takes a list of sentences, where each sentence is a list of words with their corresponding part-of-speech tags. It counts the occurrences of feminine and masculine pronouns used as subjects and objects.
def get_gender(text):
  feminine_subjects = 0
  feminine_objects = 0
  masculine_subjects = 0
  masculine_objects = 0

  for sentence in text:
    for word in sentence:
      token = word[0].rstrip('\n')
      if token.lower() == "she" and word[1] == "PRP":
          feminine_subjects += 1
      elif token.lower() == "her" and word[1] == "PRP":
          feminine_objects += 1
      elif token.lower() == "he" and word[1] == "PRP":
          masculine_subjects += 1
      elif token.lower() == "him" and word[1] == "PRP":
          masculine_objects += 1
      else:
        pass

  print("Feminine Subjects: " + str(feminine_subjects))
  print("Feminine Objects: " + str(feminine_objects))
  print("Masculine Subjects: " + str(masculine_subjects))
  print("Masculine Objects: " + str(masculine_objects))

  return feminine_subjects, masculine_subjects, feminine_objects, masculine_objects

feminine_subjects, masculine_subjects, feminine_objects, masculine_objects = get_gender(male_zips)

# Plot counts
sns.barplot(x=['F_Subject', 'M_Subject', 'F_Object', 'M_Object'], y=[feminine_subjects, masculine_subjects, feminine_objects, masculine_objects])
plt.title('Subject and Object Frequency Comparison')
plt.ylabel('Frequency')
plt.xlabel('Gender and POS')
plt.show()

# See if the different counts are statistically significant
observed = [[feminine_subjects, feminine_objects], [masculine_subjects, masculine_objects]]

chi2, p, dof, expected = stats.chi2_contingency(observed)

print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)

if p < 0.05:
    print("There is a significant difference between the frequencies.")
else:
    print("There is no significant difference between the frequencies.")
```


## Source Code For Louisa May Alcott Example (This is basically the exact same as above with the books and some variable names switched)
```python
# Import packages
!wget http://setup.johnsnowlabs.com/colab.sh -O - | bash
import sparknlp
spark = sparknlp.start()
from sparknlp.pretrained import PretrainedPipeline
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
import scipy.stats as stats

pipeline = PretrainedPipeline("explain_document_ml")

# Download books
!curl "https://www.gutenberg.org/cache/epub/37106/pg37106.txt" -o louisa1.txt
!curl "https://www.gutenberg.org/cache/epub/2787/pg2787.txt" -o louisa2.txt

# Read in books and concatenate
louisa1 = open('louisa1.txt').read()
louisa2 = open('louisa2.txt').read()

all_female_authros = louisa1 + louisa2

# Split into sentences
female_sentences = all_female_authros.split(".")

# Annotate
female_dfs = [pipeline.annotate(hl) for hl in tqdm(female_sentences)]

fem_tok_tag = [(df['token'],df['pos']) for df in female_dfs]
fem_zips = [list(zip(tt[0], tt[1])) for tt in fem_tok_tag]

# This function takes a list of sentences, where each sentence is a list of words with their corresponding part-of-speech tags. It counts the occurrences of feminine and masculine pronouns used as subjects and objects.
def get_gender(text):
  feminine_subjects = 0
  feminine_objects = 0
  masculine_subjects = 0
  masculine_objects = 0

  for sentence in text:
    for word in sentence:
      token = word[0].rstrip('\n')
      if token.lower() == "she" and word[1] == "PRP":
          feminine_subjects += 1
      elif token.lower() == "her" and word[1] == "PRP":
          feminine_objects += 1
      elif token.lower() == "he" and word[1] == "PRP":
          masculine_subjects += 1
      elif token.lower() == "him" and word[1] == "PRP":
          masculine_objects += 1
      else:
        pass

  print("Feminine Subjects: " + str(feminine_subjects))
  print("Feminine Objects: " + str(feminine_objects))
  print("Masculine Subjects: " + str(masculine_subjects))
  print("Masculine Objects: " + str(masculine_objects))

  return feminine_subjects, masculine_subjects, feminine_objects, masculine_objects

feminine_subjects, masculine_subjects, feminine_objects, masculine_objects = get_gender(fem_zips)

# Plot counts
sns.barplot(x=['F_Subject', 'M_Subject', 'F_Object', 'M_Object'], y=[feminine_subjects, masculine_subjects, feminine_objects, masculine_objects])
plt.title('Subject and Object Frequency Comparison')
plt.ylabel('Frequency')
plt.xlabel('Gender and POS')
plt.show()

# See if the different counts are statistically significant
observed = [[feminine_subjects, feminine_objects], [masculine_subjects, masculine_objects]]

chi2, p, dof, expected = stats.chi2_contingency(observed)

print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)

if p < 0.05:
    print("There is a significant difference between the frequencies.")
else:
    print("There is no significant difference between the frequencies.")

```






