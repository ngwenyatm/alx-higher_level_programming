#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        los = len(sentence)
    else:
        los = 0
    prod = (los, sentence if not sentence else sentence[:1])
    return prod
