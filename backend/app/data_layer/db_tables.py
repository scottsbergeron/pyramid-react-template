from sqlalchemy import table, column

song = table(
    'songs',
    column('id'),
    column('name'),
    column('artist'),
    column('genre'),
    column('date_created')
)
