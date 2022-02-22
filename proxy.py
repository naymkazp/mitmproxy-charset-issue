from mitmproxy import ctx
from mitmproxy.script import concurrent
import sys
import re


@concurrent
def response(flow):
    if flow.request.path.find('index.b37193db.js') >= 0 or flow.request.path.find('csdn.js') >= 0:
        regex = r" e\}\)\(e\)\}s=function\(e\)\{\"use strict\";var t=\{1:(.{15})"
        matches = re.finditer(regex, flow.response.text, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            print("Match {matchNum} was found at {start}-{end}: {match}".format(
                matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))