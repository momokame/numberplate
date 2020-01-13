import os
import glob
from PIL import Image
path1=('sign_test_pic')
path2=('/mnt/500GBHDD/taro/plate/pic_32/no_plate_32')
files = glob.glob(os.path.join(path1,'*.png'))
files2 = glob.glob(os.path.join(path2,'*.png'))
i =1
"""
for d, f in enumerate(files):
    print(f)
    os.rename(f, os.path.join('img_'+'{0:03d}'.format(i) +'.png' ))
    i=i+1
"""
for n, t in enumerate(files):
#for y in files:
    print(i)
    img = Image.open(t)
    #img = Image.open('/mnt/500GBHDD/taro/Traffic_Signs/nosign_test/pst'+str(n+6000)+'.png')
    #img.save(os.path.join(path+'_bkup','img_'+'{0:03d}'.format(i)+'.png'))
    img.save(os.path.join(path1,'p_'+'{0:03d}'.format(i)+'.png'))
    #t_00000_c5.png
    i=i+1
    if n == 3001:
        break
"""    
for n, t in enumerate(files2):
    print(i)
    #img = Image.open(t)
    img = Image.open('/mnt/500GBHDD/taro/plate/pic_32/no_plate_32/no'+str(n+6000)+'.png')
    #img.save(os.path.join('empty',path,'img_'+'{0:03d}'.format(i)+'.png'))
    img.save(os.path.join(path2+'v','v_'+'{0:05d}'.format(i)+'_c1.png'))
    i=i+1
    if n == 3001:
        break
"""
