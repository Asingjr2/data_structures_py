"""Definitions module containing information on structures and concepts.

    Current definitions include: shallow copy; deep copy

"""
import copy

definitions = {}

definitions["shallow_copy"] = "a list that creates references to same elements as original list" 
definitions["deep_copy"] = "a list that creates new elements using deepcopy function from original list"

book_list = ["harry potter", "who moved my cheese"]
shallow_book_list = copy.copy(book_list)
deep_book_list = copy.deepcopy(book_list)


definitions["dynamic_array"] = "arary that increases size in bunches as array increases.  Not fized like other langauges."

definitions["amortized_analysis"] = "refers to algorithm used to increased dynamic array size.  Doubling size of arrays allows computer to simply add value into longer array without have to recreate..so you save item once and next memory slot.  Very benecificial at higher len(n)."






# for k,v in definitions.items(): #python3 no longer has iteritems
#     print(k,"\t", v)

