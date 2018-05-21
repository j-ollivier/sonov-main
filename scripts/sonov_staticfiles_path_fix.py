# python 3.6.3
# During the sonov migration to the new server, some paths have been changed to store static data.
# Postgres stores the path of each static file in a string value so we simply change it.
# This script is meant to be executed in the django environment, through shell or import.

from main.models import Son

sons = Son.objects.all()
for son in sons:
    # change the path string into a list
    son_img_path = str(son.thumbnail).split('/')
    # change the directory names to the static files
    son_img_path[1] = 'main'
    son_img_path[2] = 'img'
    # recreate the new path as string
    son_img_path_new = '/'.join(son_img_path)
    # change object value
    son.thumbnail = son_img_path_new
    # save it to db
    son.save()
