import os
# print(os.listdir('barnacle'))

# name_dict = {}
# dir_names = ['intertidal_crab', 'nudibranch', 'intertidal_anemone', 'sea_star', 'barnacle', 'bivalves']
# dir_abbrev = ['crab', 'nudi', 'anem', 'star', 'barn', 'biv']
#
# for dir,abbrev in list(zip(dir_names, dir_abbrev)):
#     name_dict[dir] = abbrev
#
# def rename_files(dir):
#     path = '/Users/noah/Github_repos/Project_5/'+dir+'/'
#     for filename in os.listdir(dir):
#         old_path = path + filename
#         new_name = str(name_dict[dir]+filename)
#         new_path = path + new_name
#         os.rename(old_path, new_path)
#
# for dir in dir_names:
#     rename_files(dir)



def rem_xml(dir):
    path = '/Users/noah/Github_repos/Project_5/'+dir+'/'
    for filename in os.listdir(dir):
        if filename.endswith('.xml.txt'):
            old_path = path + filename
            new_name = filename.replace('.xml', '')
            new_path = path + new_name
            os.rename(old_path, new_path)

dir = 'obj'
rem_xml(dir)


# def rem_space(dir):
#     path = '/Users/noah/Github_repos/Project_5/'+dir+'/'
#     for filename in os.listdir(dir):
#         old_path = path + filename
#         new_name = filename.strip().replace(' ', '')
#         new_path = path + new_name
#         os.rename(old_path, new_path)
#
# dir = 'obj'
# rem_space(dir)

# def add_digit(dir):
#     path = '/Users/noah/Github_repos/Project_5/'+dir+'/'
#     for iter, filename in enumerate(os.listdir(dir)):
#         old_path = path + filename
#         new_name = str(iter) + 'NEW_NEW_train' + filename.strip().replace(' ', '')
#         new_path = path + new_name
#         os.rename(old_path, new_path)
#
# dir = 'crab_round_2'
# add_digit(dir)


# def file_ending(dir):
#     path = '/Users/noah/Github_repos/Project_5/'+dir+'/'
#     for filename in os.listdir(dir):
#         if filename.endswith('.png'):
#             old_path = path + filename
#             new_name = filename.replace('.png', '.jpg')
#             new_path = path + new_name
#             os.rename(old_path, new_path)
#         elif filename.endswith('.jpeg'):
#             old_path = path + filename
#             new_name = filename.replace('.jpeg', '.jpg')
#             new_path = path + new_name
#             os.rename(old_path, new_path)
#
# dir = 'obj'
# file_ending(dir)









########
