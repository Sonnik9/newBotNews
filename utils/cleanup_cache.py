import shutil
import tempfile 
import os

def cleanup_cachee():
    # print('hello')
    try:        
        try:
            cache_dir = tempfile.mkdtemp()
        except Exception as ex:
            # print(f"386____{ex}")
            pass    
        try:
            if os.path.exists("./__pycache__"):
                shutil.rmtree("./__pycache__")
        except Exception as ex:
            print(f"392____{ex}")
            pass  
        try:
            if os.path.exists("./utils/__pycache__"):
                shutil.rmtree("./utils/__pycache__")
        except Exception as ex:
            print(f"445____{ex}")
            pass 
        try:
            if os.path.exists("./parsers/__pycache__"):
                shutil.rmtree("./parsers/__pycache__")
        except Exception as ex:
            print(f"451____{ex}")
            pass 
 
        try:
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
        except Exception as ex:
            # print(f"396____{ex}")
            pass
    except Exception as ex:
        print(f"551____{ex}") 