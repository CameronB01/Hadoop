# Analysis of Gender Pronouns in Text Corpus

## Introduction

In this study, we aim to explore the differences in the usage frequencies of feminine and masculine personal pronouns in a given corpus. Specifically, we seek to determine whether there is a statistically significant difference between the frequencies of these pronouns when used as subjects versus objects. Additionally, we investigate whether the gender distribution of the authors within the corpus has a meaningful impact on these results.

## Methodology

### Dataset

We use a corpus of news articles that contain metadata including the text of the article, the authors, and their genders. This dataset allows us to analyze the usage of personal pronouns in different contexts and correlate these findings with the gender of the authors.

### Technologies

To process and analyze the text data, we use the following tools and technologies:

- **SparkNLP**: An open-source library that provides state-of-the-art natural language processing capabilities.
- **Pandas**: A Python library used for data manipulation and analysis.
- **Matplotlib**: A plotting library for creating static, animated, and interactive visualizations in Python.

## Hypothesis

1. **Primary Hypothesis**: There is a statistically significant difference in the frequencies of feminine and masculine personal pronouns used as subjects versus objects.
2. **Secondary Hypothesis**: The gender distribution of the authors within the corpus significantly impacts the observed frequencies of these pronouns.

## Evaluation

### Data Processing

We use SparkNLP to preprocess the text data, identify personal pronouns, and categorize them as either subjects or objects. The steps include:

1. **Tokenization**: Splitting the text into individual words.
2. **Part-of-Speech Tagging**: Identifying the grammatical role of each word in the sentence.
3. **Pronoun Extraction**: Extracting and categorizing personal pronouns as subjects or objects.
