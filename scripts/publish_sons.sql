/*
20180704
psql
This script is meant to make sounds available to the frontpage of sonov.fr by checking the
"date to publish" chosen by the user. If the date is due at the time of the script execution
then the "is_visible" value is set to true. 
*/
update main_son 
set is_visible = true 
where 
	created_date < current_timestamp 
	and is_visible = false
;
