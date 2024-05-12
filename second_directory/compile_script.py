# compile_script.py
import py_compile

def compile_script(source_file):
    py_compile.compile(source_file, cfile=source_file + "c")

if __name__ == "__main__":
    compile_script("file1.py")
