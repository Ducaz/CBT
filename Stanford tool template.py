# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:27:19 2016

@author: ZHULI
"""

# Stanford CoreNLP ships with a built-in server, which requires only the CoreNLP dependencies. 
# To run this server, simply run:
# Run the server using all jars in the current directory (e.g., the CoreNLP home directory)
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer [port] [timeout]
# If no value for port is provided, port 9000 will be used by default. You can then test your server by visiting 
# http://localhost:9000/

import re, random
from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')

def GetAnnotation(text):
    result = nlp.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,depparse,parse',
                                            'outputFormat': 'json'})
#    result = nlp.annotate(text, properties={'annotators': 'parse',
#                                            'outputFormat': 'json'})
    return result

filename = '..\..\..\..\CBTest Datasets\CBTest\data\cbtest_CN_test_2500ex.txt'
file = open(filename,'r')
RLineNum = re.compile('^\d+')
R20 = re.compile('^\d+ (.*)')
R21 = re.compile('^\d+ (.+)\t+([\S]+)\t+([\S]+)$')

for line in file:
    mLineNum = RLineNum.search(line)
    if(mLineNum):
        print (mLineNum)
        if(int(mLineNum.group(0)) != 21):
            #20 sentences
            sentence = R20.search(line).group(1)
            output=GetAnnotation(line)
            print(output['sentences'][0]['parse'])
        else:
            #21st sentence
            m21 = R21.search(line)
            Question = m21.group(1)
            Candidates = m21.group(3).split('|')
            CorrectAnswer = m21.group(2)
            #print('Q:',Question)
            #print('A:',CorrectAnswer)
            #print('C:',Candidate)
    else:
        #blank line
        break
file.close()