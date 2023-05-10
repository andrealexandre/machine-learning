# Example of Machine Learning/AI training coding

References for the code in this repository.

## Python Environment
Run `./setup.sh` to setup the python environment and necessary library to run the code in this repository.

## Samples

* Basic Tensorflow tutorial (Help setup environment) - [tensor_test.py](tensor_test.py)
* Fashion tutorial - [fashion_model.py](fashion_model.py)
* ChatGPT tutorial - [chatgpt.py](chatgpt.py)

## Setup for your own OpenAI API key
Get your own API key from `https://platform.openai.com/account/api-keys` and then run the following commands to setup your environment.
```bash
touch .env
echo "export OPENAI_API_KEY=\"<OPENAI_KEY>\"" >.env
```