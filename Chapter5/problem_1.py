def mixBits(app, source, start, end):
    mask = (~0) << end + 1
    mask = (mask | (1 << start)) - 1
    app = app << start
    source = source & mask
    return app | source
