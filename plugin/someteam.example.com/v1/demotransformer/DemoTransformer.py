#!/usr/bin/env python3

import yaml
import os
import sys
import json

def isKptFunction(inputYAML):
  return inputYAML['kind'] == 'ResourceList'

def getNewValue(inputYAML):
  if isKptFunction(inputYAML):
    return inputYAML['functionConfig']['data']['value']
  else:
    return sys.argv[2]

if __name__ == '__main__':
  #print(os.environ['KUSTOMIZE_PLUGIN_CONFIG_STRING'], file=sys.stderr)
  input = sys.stdin.read()
  #print(input, file=sys.stderr)
  inputYAML = yaml.load(input, Loader=yaml.FullLoader)
  newValue = getNewValue(inputYAML)
  if isKptFunction(inputYAML):
    for item in inputYAML['items']:
      item['data']['key1'] = newValue
  else:
    inputYAML['data']['key1'] = newValue
  print(yaml.dump(inputYAML))
