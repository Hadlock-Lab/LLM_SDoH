# Using Large Language Models to Annotate Complex Cases of Social Determinants of Health in Longitudinal Clinical Records

## Overview

Social Determinants of Health (SDoH) such as housing insecurity are known to be intricately linked to patients’ health status. Large language models (LLMs) have shown potential for performing complex annotation tasks on unstructured clinical notes. Our work assessed the performance of LLMs (GPT-4 and GPT-3.5) in identifying temporal aspects of housing insecurity, and compared performance between original and de-identified notes.

2024 medRxiv pre-print: ["Using Large Language Models to Annotate Complex Cases of Social Determinants of Health in Longitudinal Clinical Records"](https://www.medrxiv.org/content/10.1101/2024.04.25.24306380v1)

## Table of Contents
 * [Main Findings](#main-findings)
 * [Figures](#figures)
 * [Models](#models)
 * [Data Availability](#data-availability)
 * [Contact](#contact)

### Main Findings

1.	Compared with GPT-3.5 and a named entity recognition (NER) model, GPT-4 had the highest performance and had a much higher recall than human annotators in identifying patients experiencing current or past housing instability.
2.	In most cases, the evidence output by GPT-4 was similar or identical to that of human annotators, and there was no evidence of hallucinations in any of the outputs from GPT-4.
3.	GPT-4 precision improved slightly on de-identified versions of the same notes, while recall dropped.

### Figures

<p align="center">
  <img width="500" src="https://github.com/Hadlock-Lab/LLM_SDoH/blob/main/Figures/model_comparison_current_past_HI.png" alt="Comparison of recall and precision for Regex, GPT-3.5, GPT-4, and manual annotation in identifying notes with current or past housing instability, measured on 539 manually annotated notes.">
  <figcaption>Comparison of recall and precision for Regex, GPT-3.5, GPT-4, and manual annotation in identifying notes with current or past housing instability, measured on 539 manually annotated notes.</figcaption>
</p>

<p align="center">
  <img width="500" src="https://github.com/Hadlock-Lab/LLM_SDoH/blob/main/Figures/model_comparison_current_past_HI.png" alt="Comparison of recall and precision for Regex, GPT-3.5, GPT-4, and manual annotation in identifying notes with current or past housing instability, measured on 539 manually annotated notes.">
  <img width="500" src="https://github.com/Hadlock-Lab/LLM_SDoH/blob/main/Figures/recall_precision_gpt35_housing_labels.png" alt="Description of the second image">
</p>
<p align="center">
  <figcaption>Recall and precision metrics for GPT-4 and GPT-3.5 for each housing label.</figcaption>
</p>

<p align="center">
  <img width="500" src="https://github.com/Hadlock-Lab/LLM_SDoH/blob/main/Figures/deid_housing_noted.png" alt="Comparison of recall and precision for Regex, GPT-3.5, GPT-4, and manual annotation in identifying notes with current or past housing instability, measured on 539 manually annotated notes.">
  <img width="500" src="https://github.com/Hadlock-Lab/LLM_SDoH/blob/main/Figures/deid_current_past.png" alt="Description of the second image">
</p>
<p align="center">
  <figcaption>Comparison of GPT-4 performance in identifying general housing status or current and past housing instability from three different versions of the same set of 539 notes. Notes were either complete (original) patient notes, completely de-identified notes, or de-identified notes with no date shift.
</figcaption>
</p>

### Models

We compared the ability of GPT-3.5 and GPT-4 to identify instances of both current and past housing instability, as well as general housing status, from 25,217 notes from 795 pregnant women. Results were compared with manual annotation, a named entity recognition (NER) model, and regular expressions (RegEx). [The detailed annotation guidelines are here](https://github.com/Hadlock-Lab/LLM_SDoH/blob/main/Annotation%20Guidelines%20and%20LLM%20Prompt.pdf).

#### GPT-4 and GPT-3.5
GPT-4 version 0613 had a 32K token window, while GPT-3.5 Turbo version 0613 had a 16K token window. Both GPT models were run using LangChain and OpenAI libraries. You can find the script for running final prompt in [GPT_prompt.py](https://github.com/Hadlock-Lab/LLM_SDoH/blob/main/models/GPT_prompt.py).

#### John Snow Labs NER Model
The [John Snow Labs (JSL) NER model](https://nlp.johnsnowlabs.com/2023/06/13/ner_sdoh_en.html) is an SDoH model designed to detect and label SDoH entities within text data. The housing-specific label includes entities related to the conditions of the patient’s living spaces, for example: homeless, housing, small apartment, etc.

### Data Availability
The data used in this study contains identifiable protected health information and therefore cannot be shared publicly. Investigators from Providence Health and Services and affiliates (PHSA) with an appropriate IRB approval can contact the authors directly regarding data access.

### Contact

For further information or queries, please contact: 
- Alexandra Ralevski (alexandra.ralevski@gmail.com)
