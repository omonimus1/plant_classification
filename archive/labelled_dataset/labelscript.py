import os

os.chdir('/Users/davide/Desktop/university/honours/plant_classification/archive/labelled_dataset/roses')
print(os.getcwd())

for count, f in enumerate(os.listdir(os.getcwd())):
    f_name, f_ext = os.path.splitext(f)
    f_name = "roses" + '.jpg'

    new_name = f_name + f_ext
    os.rename(f,f_name)
