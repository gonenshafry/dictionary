import json;
import difflib;

data = json.load(open("data.json"));

def translate(w):
 w = w.lower();

 if w in data:
  return data[w];

 elif len(difflib.get_close_matches(w,data.keys())) > 0:
  ww = input("Did you mean %s ?" % 
difflib.get_close_matches(w, 
data.keys())[0]);
  if ww.lower() == "y":
   return data[difflib.get_close_matches(w, 
data.keys())[0]];
  elif ww.lower() == "n":
   return "This word doesn't exist.";

 else:
  return "This word doesn't exist.";

word = input("Enter word: ");

output = translate(word);

if type(output) == list:
 for item in output:
  print(item);
else:
 print(output);
