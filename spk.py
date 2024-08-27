
import sys,requests,zipfile,shutil,os


def install(url:str):
    SPK_INFO = 'SPK! 3.0 info:'
    global k
    filename = url.split('/')[-1]
    print(SPK_INFO + '''Installing ''' + repr(filename))
    k = filename.split('.')[0]
    
    
    r = requests.get(url,stream=True)

    with open(filename,'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        if not f:
            n = None                 
        else:
            n = filename
 





    
    
    if filename.split('.')[1] == 'zip':

        trget = './modules'    

        z = zipfile.ZipFile(filename)
        z.extractall(trget + k)    
    elif not filename.split('.')[1] == 'tar':

        trget = './modules/'            
        shutil.move('./' + filename,trget + filename)    
    MSG = 'Installation is complete.'     
    print(SPK_INFO + MSG)

      
  
    return n        
    

def remove(name):
    shutil.rmtree(name)
     
   




if sys.argv[1] == 'install':

    install(sys.argv[2])


elif sys.argv[1] == 'remove':
    remove(sys.argv[2])

