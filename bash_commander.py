def bash_commander(cmd):
    import subprocess
    import urllib
    import sys
    import json
    import shlex
    args=shlex.split(cmd)
    process=subprocess.Popen(args,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out=subprocess.run([cmd],stdout=subprocess.PIPE,shell=True)
    stdout,stderr=process.communicate()
    return out