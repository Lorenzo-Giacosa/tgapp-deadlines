from tg import expose

@expose('deadlines.templates.little_partial')
def something(name):
    return dict(name=name)