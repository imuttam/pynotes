line = 'asdf fjdk; afed, fjek,asdf, foo'
import re

pattern = r"[;,\s]\s*"
splited = re.split(pattern, line)
print(splited)