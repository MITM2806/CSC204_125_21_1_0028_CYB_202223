from linkedlists.single_linked_list import SingleLinkedList

if __name__ == "__main__":
    elements = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    linked_list = SingleLinkedList()
    for element in elements:
        linked_list.insert(element)

    linked_list.display()

    max_data, min_data = linked_list.find_max_min()
    print(f"Max Data: {max_data}")
    print(f"Min Data: {min_data}")

    # Convert the list to a binary search tree
    root_of_bst = linked_list.list_to_bst(elements)
