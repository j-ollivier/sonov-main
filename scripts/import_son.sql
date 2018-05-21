copy main_son(
      uid
    , title
    , source_site
    , source_id_string
    , thumbnail
    , is_visible
    , created_date
    , modified_date
    , short_desc
    , posted_by_id
    )
from
    '/home/common/sonov_django/main/scripts/export_son.csv'
    with null as ''     -- empty csv cells will be considered as null
    delimiter as ';'    -- must match the csv configuration (either space or ;)
    csv                 -- tells that the input file is csv
    header              -- to ignore the first row of the csv file, with column names
;