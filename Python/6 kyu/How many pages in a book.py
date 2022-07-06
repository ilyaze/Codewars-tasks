def amount_of_pages(summary):
    pages = 0
    page_num = 1
    while summary > 0:
        summary -= len(str(page_num))
        pages += 1
        page_num += 1
    return pages
