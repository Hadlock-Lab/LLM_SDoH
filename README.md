# Using Large Language Models to Annotate Complex Cases of Social Determinants of Health in Longitudinal Clinical Records

## Overview

This repository contains the code for the paper ["Using Large Language Models to Annotate Complex Cases of Social Determinants of Health in Longitudinal Clinical Records"](https://www.medrxiv.org/content/10.1101/2024.04.25.24306380v1), currently available in medRxiv (2024). 

Social Determinants of Health (SDoH) such as housing insecurity are known to be intricately linked to patients’ health status. Large language models (LLMs) have shown potential for performing complex annotation tasks on unstructured clinical notes. 

### Main Findings

1.	Compared with GPT-3.5 and a named entity recognition (NER) model, GPT-4 had the highest performance and had a much higher recall than human annotators in identifying patients experiencing current or past housing instability.
2.	In most cases, the evidence output by GPT-4 was similar or identical to that of human annotators, and there was no evidence of hallucinations in any of the outputs from GPT-4.
3.	GPT-4 precision improved slightly on de-identified versions of the same notes, while recall dropped.

The data used in this study contains identifiable protected health information and therefore cannot be shared publicly. Investigators from Providence Health and Services and affiliates (PHSA) with an appropriate IRB approval can contact the authors directly regarding data access.

### Models

We compared the ability of GPT-3.5 and GPT-4 to identify instances of both current and past housing instability, as well as general housing status, from 25,217 notes from 795 pregnant women. Results were compared with manual annotation, a named entity recognition (NER) model, and regular expressions (RegEx).[The detailed annotation guidelines are here](https://github.com/Hadlock-Lab/LLM_SDoH/blob/main/Annotation%20Guidelines%20and%20LLM%20Prompt.pdf).

#### GPT-4 and GPT-3.5
GPT-4 version 0613 had a 32K token window, while GPT-3.5 Turbo version 0613 had a 16K token window. Both GPT models were run using LangChain and OpenAI libraries. You can find the script for running final prompt in [GPT_prompt.py](https://github.com/Hadlock-Lab/LLM_SDoH/blob/main/models/GPT_prompt.py).

#### John Snow Labs NER Model
The [John Snow Labs (JSL) NER model](https://nlp.johnsnowlabs.com/2023/06/13/ner_sdoh_en.html) is an SDoH model designed to detect and label SDoH entities within text data. The housing-specific label includes entities related to the conditions of the patient’s living spaces, for example: homeless, housing, small apartment, etc.
