copy main_tag(
	  uid
	, title
    )
from
    '/home/common/sonov_django/main/scripts/export_tags.csv'
    with null as ''     -- empty csv cells will be considered as null
    delimiter as ';'    -- must match the csv configuration (either space or ;)
    csv                 -- tells that the input file is csv
    header              -- to ignore the first row of the csv file, with column names
;