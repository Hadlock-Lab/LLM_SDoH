spark.conf.set("spark.databricks.io.cache.enabled", "true")

import json
import os
from pyspark.ml import Pipeline, PipelineModel
from pyspark.sql import SparkSession

from sparknlp.annotator import *
from sparknlp_jsl.annotator import *
from sparknlp.base import *
from sparknlp.functions import *
import sparknlp_jsl
import sparknlp

from sparknlp.util import *
from pyspark.sql import functions as F
from pyspark.sql.functions import col

import pandas as pd
import string
import numpy as np

pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)

print('sparknlp_jsl.version : ', sparknlp_jsl.version())
print('sparknlp.version: ', sparknlp.version())

pd.set_option('max_colwidth', 100)

def create_pipeline():
  fp_ner_sdoh = "dbfs:/mnt/datascience/jsl_models/ner_sdoh_en_4.4.3_3.0_1686654976160"
  sdoh_white_list = "Housing"
  
  document_assembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")
  
  sentence_detector = SentenceDetectorDLModel.load(fp_sentence_detector_dl_32030)\
      .setInputCols(["document"])\
      .setOutputCol("sentence")
  
  tokenizer = Tokenizer()\
      .setInputCols(["sentence"])\
      .setOutputCol("token")\
      .setSplitChars(["-", "\/"])
  
  word_embeddings = WordEmbeddingsModel.load(fp_embeddings_clinical_24024)\
      .setInputCols(["sentence","token"])\
      .setOutputCol("embeddings")
  
  ## ner_sdoh
  ner_sdoh = MedicalNerModel.load(fp_ner_sdoh) \
      .setInputCols(["sentence", "token", "embeddings"]) \
      .setOutputCol("ner_sdoh")
  
  ner_sdoh_converter = NerConverterInternal() \
      .setInputCols(["sentence", "token", "ner_sdoh"]) \
      .setOutputCol("ner_chunk_sdoh") \
      .setWhiteList(sdoh_white_list)
  
  
  ner_stages = [document_assembler,
      sentence_detector,
      tokenizer,
      word_embeddings,
      ner_sdoh,
      ner_sdoh_converter,
  ]
  
  ner_pipeline_sdoh = Pipeline(stages=ner_stages)
  
  empty_data = spark.createDataFrame([[""]]).toDF("text")
  
  ner_model_sdoh = ner_pipeline_sdoh.fit(empty_data)

  return ner_model_sdoh

### USAGE ###
# Repartition for speed
#df = df.repartition(100)

# Run the pipeline - rename text column to "text
#result = ner_model_sdoh.transform(df.withColumnRenamed("<name of column with the patient notes>", "text"))

# Parse out the results
# df_result = result.select("pat_id", "note_id", "name", "date_of_service", 
#                          F.explode(F.arrays_zip(result.ner_chunk_sdoh.result, 
#                                     result.ner_chunk_sdoh.metadata)).alias("cols")) \
#                .select("pat_id", "note_id", "name", "date_of_service",
#                        F.expr("cols['0']").alias("chunk"),
#                        F.expr("cols['1']['entity']").alias("ner_label"),
#                        F.expr("cols['1']['confidence']").alias("confidence"))
