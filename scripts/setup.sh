#!/usr/bin/env bash

set -ex

# create conda environment for distribution
conda create -n nlp_env --copy -y -q python=3.6 gensim tensorflow pip
source activate nlp_env

pip install jieba
pip install pyltp

cd ~/.conda/envs/
zip -r ../../nlp_env.zip nlp_env

cd ~/