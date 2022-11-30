## to collect all contacts run command

`python contact.py`

## to create a new group update create_group with group names and participants in it separated by a ';'.

`python create_group.py`

## to find participants in a group add the group name in the group.xlsx file and run groups_read.py file it will create separate excel files for each group. Command-

`python groups_read.py`

## to add participants fill the excel file named add_participants.xlsx make sure that the group in which you're adding participants to have the file containing all the current particiipants. now run add_participants.py file

## to remove participants update the remove_participants.xlsx file and run the command

`python remove_participants.py`

## to add participants update the add_participants.xlsx file and run command

`python add_participants.py`

## to give admin rights update the add_admin.xlsx file and run command

`python make_admin.py`

## to revoke admin rights update the remove_admin.xlsx file and run command

`python remove_admin.py`

## to modify and manage group message send rights, update admin_only_send_message.xlsx file and run command

`python admin_rights.py`

## to send message update message.xlsx files for sending multiple files. Note: input to the Name column is not necessary.

`python send_message_v3.py`
