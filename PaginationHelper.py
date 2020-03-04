class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self._collection = collection
        self._items_per_page = items_per_page

    def item_count(self):
        return len(self._collection)

    def page_count(self):
        return self.item_count() / self._items_per_page if self.item_count() % self._items_per_page == 0 \
            else self.item_count() / self._items_per_page + 1

    def page_item_count(self, page_index):
        print(page_index , self._items_per_page )
        if page_index >= self.page_count() or page_index < 0:
            return -1
        elif page_index+1 == self.page_count():
            return self.item_count() % self._items_per_page
        else:
            return self._items_per_page

    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.item_count():
            return -1
        elif item_index < self._items_per_page:
            return 0
        else:
            return item_index / self._items_per_page


collection = range(1,25)
helper = PaginationHelper(collection, 10)
helper.page_item_count(3)
