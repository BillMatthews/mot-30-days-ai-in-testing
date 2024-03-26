# Ministry of Testing - 30 Days of AI in Testing
This repository contains a set of exercises prepared for Day 28 of the challenge. The focus of these exercises is to expose you to more advanced methods of interacting with Large Language Models (LLMs) that address some of the concerns that were identified during earlier days of the challenge.

Each walkthrough is stand-alone and you are free to tackle as many of these as you want. While these contain Python code, there is no need for you to be able to understand Python code to complete the walkthroughs. The code is included for information purposes only and to demonstrate how we can interact and use LLM models in different ways.

The walkthroughs use Google Colaboratory (or Colab for short) and it is highly recommended that you watch the Introduction to Colaboratory  - https://www.youtube.com/watch?v=inN8seMm7UI. In particular you need to understand how to run the cells in the notebook.



# Walkthroughs
## Walkthrough 1: Running your own local LLM for Chat
In this walkthrough you will deploy a (small) Open-Source Large Language Model to your local machine using the LlamaFile Project (https://github.com/Mozilla-Ocho/llamafile). This is one approach you could adopt to address the challenge of data privacy when using public services such as Chat-GPT, Bing Copilot etc.

You can access this walkthrough via the following link: <a target="_blank" href="https://colab.research.google.com/github/BillMatthews/mot-30-days-ai-in-testing/blob/main/walkthrough/walkthrough-1-running-local-llms.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


## Walkthrough 2: Interacting with open-source LLM models
In this walkthrough you will use the HuggingFace Transformer library to programmatically interact with an open-source Large Language Model. The HuggingFace libraries simplify the downloading and interacting with pre-trained models including Open Source Language Models.

The ability to interact with LLMs (and other models) programmatically expands our options beyond using chat style interfaces and allows us to chain models together, standardize prompts and use external tools. This expands the scope of how we can build and integrate AI into tools that support Testing.

You can access this walkthrough via the following link: <a target="_blank" href="https://colab.research.google.com/github/BillMatthews/mot-30-days-ai-in-testing/blob/main/walkthrough/walkthrough-2-interacting-with-llms.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


## Walkthrough 3: Chatting with your own documents
During earlier challenge days, a number of participants noted that LLMs don’t really understand their context 

In this walkthrough we will use an approach called Retrieval Augmented Generation that will allow us to provide context specific documents that are automatically injected into our prompt to improve the quality of the output generated. 

You can access this walkthrough via the following link: <a target="_blank" href="https://colab.research.google.com/github/BillMatthews/mot-30-days-ai-in-testing/blob/main/walkthrough/walkthrough-3-chatting-with-your-docs.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
