#!/usr/bin/env bash

#source /etc/spark2/conf/spark-env.sh

export SPARK_HOME=/opt/cloudera/parcels/SPARK2/lib/spark2
export QUEUE=default

# set environment variables (if not already done)
export PYTHON_ROOT=./NLP/nlp_env
export PYSPARK_PYTHON=${PYTHON_ROOT}/bin/python

# 环境变量
# eg: spark.executorEnv.JAVA_HOME 和 spark.yarn.appMasterEnv.JAVA_HOME，这分别为Spark的Executor和Driver指定JDK路径

# submit task
${SPARK_HOME}/bin/spark-submit \
--conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=$PYSPARK_PYTHON \
--conf spark.yarn.appMasterEnv.PYSPARK_DRIVER_PYTHON=$PYSPARK_PYTHON \
--master yarn \
--deploy-mode cluster \
--queue ${QUEUE} \
--num-executors 1 \
--executor-memory 4G \
--files configs/etl_config.json \
--py-files dependencies.zip \
--archives nlp_env.zip#NLP \
jobs/etl_job.py
