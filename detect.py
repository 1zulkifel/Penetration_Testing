import os
import sys
import hashlib

compromised="compromised"
original="original"
walk_dir = compromised

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    #print('--\nroot = ' + root)
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    print('list_file_path = ' + list_file_path)

    with open(list_file_path, 'wb') as list_file:
        #for subdir in subdirs:
           # print('\t- subdirectory ' + subdir)

        for filename in files:
            compromised_file_path = os.path.join(root, filename)
            #print(original,file_path.replace("compromised".""))
           # print('\t- file %s (full path: %s)' % (filename, file_path))
            original_file_path=original + compromised_file_path.replace(compromised,original)
            try:

                compromised_md5=hashlib.md5( open(compromised_file_path,'r').read().encode('utf-8'))
                original_md5=hashlib.md5(open(original_file_path,'r').read().encode('utf-8'))
                print(original_md5)
            except(Exception):
                print("[#] newly created file detected:\t%s"%compromised_file_path)
            #result = hashlib.md5(b'GeeksforGeeks')
                
            with open(compromised_file_path, 'rb') as f:
                f_content = f.read()
                list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
                list_file.write(f_content)
                list_file.write(b'\n')