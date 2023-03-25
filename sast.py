#!/usr/local/bin/python3

import glob
import re
import argparse
import time


class PrintInColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHT_PURPLE = '\033[94m'
    PURPLE = '\033[95m'
    END = '\033[0m'

    @classmethod
    def red(cls, s, **kwargs):
        print(cls.RED + s + cls.END, **kwargs)

    @classmethod
    def green(cls, s, **kwargs):
        print(cls.GREEN + s + cls.END, **kwargs)

    @classmethod
    def yellow(cls, s, **kwargs):
        print(cls.YELLOW + s + cls.END, **kwargs)

    @classmethod
    def lightPurple(cls, s, **kwargs):
        print(cls.LIGHT_PURPLE + s + cls.END, **kwargs)

    @classmethod
    def purple(cls, s, **kwargs):
        print(cls.PURPLE + s + cls.END, **kwargs)


lang_dict =	{
  "python": ".py",
  "java": ".java",
  "c#": ".cs",
  "node.js": ".js"
}

list_vuln1=[]
list_vuln2=[]
list_vuln3=[]
list_vuln4=[]
list_vuln5=[]
list_vuln6=[]

def search_extension(dir):
    for lang in lang_dict.values():
        if len(glob.glob(dir + f'/**/*{lang}', recursive=True))>0:
            result_id = list(lang_dict.values()).index(lang)
            
    result=list(lang_dict.keys())[result_id]
    return result


def python_regex_search(dir,ext):
    for f in glob.glob(dir + f'/**/*{ext}', recursive=True):
        with open(f) as _file:
            for i, line in enumerate(_file.readlines()):
                if re.search(r'PASSWORD|key|token|Password|passwd|password|secret_key', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln5.append(str(i))
                if re.search(r'request.form|request.args.get|get|post|input|val', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln1.append(str(i))
                if re.search(r'select|SELECT|insert|Insert|\+|@|connector|connect|db|query|join', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln2.append(str(i))
                if re.search(r'@csrf|app.route|token|param', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln3.append(str(i))
                if re.search(r'@app|@app.route', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln4.append(str(i))
                if re.search(r'upload|UPLOAD_FOLDER|folder|path|PATH|file|FILE|absolut|form|dir', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln6.append(str(i))


def java_regex_search(dir,ext):
    for f in glob.glob(dir + f'/**/*{ext}', recursive=True):
        with open(f) as _file:
            for i, line in enumerate(_file.readlines()):
                if re.search(r'PASSWORD|key|token|Password|passwd|password|setAtribute', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                if re.search(r'get|post|input|val|InputStream|formData|param', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln1.append(str(i))
                if re.search(r'select|SELECT|insert|Insert|\+|@|query|join', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln2.append(str(i))
                if re.search(r'getParameter|token|FORM_TOKEN|TOKEN', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln3.append(str(i))
                if re.search(r'url-pattern|servlet-mapping|GetMapping|PostMapping|put|delete|reponse', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln4.append(str(i))
                if re.search(r'upload|UPLOAD_FOLDER|folder|path|PATH|file|FILE|absolut|form|getAbsolutePath|fileName|dir', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln6.append(str(i))

def csharp_regex_search(dir,ext):
    for f in glob.glob(dir + f'/**/*{ext}', recursive=True):
        with open(f) as _file:
            for i, line in enumerate(_file.readlines()):
                if re.search(r'PASSWORD|key|token|Password|passwd|password|setAtribute', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                if re.search(r'get|post|input|val|InputStream|formData|param', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln1.append(str(i))
                if re.search(r'select|SELECT|insert|Insert|\+|@|query|join', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln2.append(str(i))
                if re.search(r'HttpPost|HttpPut|HttpGet|HttpDelete|token|FORM_TOKEN|TOKEN', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln3.append(str(i))
                if re.search(r'url-pattern|servlet-mapping|GetMapping|PostMapping|put|delete|reponse', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln4.append(str(i))
                if re.search(r'upload|UPLOAD_FOLDER|folder|path|PATH|file|FILE|absolut|form|getAbsolutePath|fileName|dir', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln6.append(str(i))

def node_regex_search(dir,ext):
    for f in glob.glob(dir + f'/**/*{ext}', recursive=True):
        with open(f) as _file:
            for i, line in enumerate(_file.readlines()):
                if re.search(r'PASSWORD|key|token|Password|passwd|password', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                if re.search(r'request.form|request.args.get|get|post|input|val|setAttribute|param', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln1.append(str(i))
                if re.search(r'select|SELECT|insert|Insert|\+|@|query|join|connect|db', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln2.append(str(i))
                if re.search(r'token|param|form|app.post', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln3.append(str(i))
                if re.search(r'app|app.get|app.post|app.put|app.delete|app.all', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln4.append(str(i))
                if re.search(r'upload|UPLOAD_FOLDER|folder|path|PATH|file|FILE|absolut|form|dir', line):
                    PrintInColor.green( f"In file {f} matched: {line.rstrip()} at position: {i}")
                    list_vuln6.append(str(i))


def vuln_count(list_vuln1,list_vuln2,list_vuln3,list_vuln4,list_vuln5,list_vuln6,lang):

    PrintInColor.yellow("\n=====Vulnerabilities======\n")
    print(" XSS: " +str(len(list_vuln1))+"\n", 
    "SQLi: " +str(len(list_vuln2))+"\n", 
    "CSRF: " +str(len(list_vuln3))+"\n", 
    "Auth:" +str(len(list_vuln4))+"\n", 
    "Password: " +str(len(list_vuln5))+"\n",
    "Path Traversal: " +str(len(list_vuln6))
    )
    PrintInColor.yellow("\n =======Informations======\n")
    print(" Language:"+lang.upper())


def use_regex(dir,lang):
    ext=lang_dict[lang]
    if lang == "python":
        python_regex_search(dir,ext)
    elif lang == "java":
        java_regex_search(dir,ext)
    elif lang == "c#":
        csharp_regex_search(dir,ext)
    else:
        node_regex_search(dir,ext)


def print_header():
    PrintInColor.lightPurple("""
  _____          _____ _______  __      __   _ _     _       _             
 / ____|  /\    / ____|__   __| \ \    / /  | (_)   | |     | |            
| (___   /  \  | (___    | |     \ \  / /_ _| |_  __| | __ _| |_ ___  _ __ 
 \___ \ / /\ \  \___ \   | |      \ \/ / _` | | |/ _` |/ _` | __/ _ \| '__|
 ____) / ____ \ ____) |  | |       \  / (_| | | | (_| | (_| | || (_) | |   
|_____/_/    \_\_____/   |_|        \/ \__,_|_|_|\__,_|\__,_|\__\___/|_|   
""")

        



if __name__ == '__main__':

    start_time = time.time()
  
    parser = argparse.ArgumentParser(
        usage='%(prog)s --directory PATH --language LANG',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("-d", "--directory",type=str, required=True)
    parser.add_argument("-l", "--language",type=str, required=False)

    args = parser.parse_args()

    print_header()

    if args.language is not None:
        language=args.language
    else:
        language = search_extension(args.directory)

    use_regex(args.directory,language)
    vuln_count(list_vuln1,list_vuln2,list_vuln3,list_vuln4,list_vuln5,list_vuln6,language)

    print(" Time Execution: %s seconds" % (time.time() - start_time))

