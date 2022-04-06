def check_if_empty(lst):
    if len(lst) == 0:
        return False
    return True


class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item

    def get_by_category(self, category):
        list_by_cat = [item for item in self.inventory if item.category == category]
        if len(list_by_cat) == 0:
            return False
        return list_by_cat

    def swap_items(self, person, item_to_person, item_to_self):
        '''
        This method removes items from Vendor inventory and appends it to
        person's inventory.  If this is successful, then the method returns
        True.  Else, False.
        '''
        if (item_to_person not in self.inventory) or (item_to_self not in person.inventory):
            return False

        self.inventory.remove(item_to_person)
        person.inventory.append(item_to_person)

        person.inventory.remove(item_to_self)
        self.inventory.append(item_to_self)
        return True

    def swap_first_item(self, person):
        if check_if_empty(self.inventory) and check_if_empty(person.inventory):
            self.swap_items(person, self.inventory[0], person.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self, category):
        list_by_cat = self.get_by_category(category)

        if list_by_cat == False:
            return None

        max_qual = 0.0
        best_item = None
        for item in list_by_cat:
            if item.condition > max_qual:
                max_qual = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        item_to_self = other.get_best_by_category(my_priority)
        item_to_other = self.get_best_by_category(their_priority)

        if not (item_to_self and item_to_other):
            return False

        self.swap_items(other, item_to_other, item_to_self)
        return True
