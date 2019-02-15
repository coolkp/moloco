import json
def popular(filename = 'data_json.json'):
    """
        Had to write some code to convert the downloaded CSV file to JSON file
    """
    # with open('data.txt') as old, open('data_json.json', 'w') as new:
    #     for line in old:
    #         new_line = ''
    #         for c in range(1,len(line)-2):
    #             if line[c] == '"' and line[c+1] == '"':
    #                 continue
    #             new_line += line[c]
    #         print(new_line)
    #         new.write(new_line+'\n')
    products_quant = {} # key(product_id) ==> value(total quantity of product)
    products_user = {} # key(product_id) => value (dict{key(user_id) => value(bool)})
    most_quant = (0,'') # Tuple (quantity of products, product_id)
    list_most_quant = {}
    most_uniq = (0,'') # Tuple (Number of unique users of product, product_id)
    list_most_uniq = {}
    # Process JSON file line by line or entry by entry
    with open(filename) as json_file:
        for line in json_file:
            # Convert string to object
            d = json.loads(line)
            pid = d['product_id']
            uid = d['user_id']
            if pid not in products_quant:
                products_quant[pid] = 0
            products_quant[pid] += d['quantity']
            if most_quant[0] < products_quant[pid] :
                most_quant = (products_quant[pid],pid)
                list_most_quant = {pid:True}
            elif most_quant[0] == products_quant[pid]:
                list_most_quant[pid] = True
            if pid not in products_user:
                products_user[pid] = {}
            if uid not in products_user[pid]:
                products_user[pid][uid] = True
            if len(products_user[pid]) > most_uniq[0]:
                most_uniq = (len(products_user[pid]),pid)
                list_most_uniq = {pid:True}
            elif len(products_user[pid]) == most_uniq[0]:
                list_most_uniq[pid] = True
    print("Most popular product(s) based on the quantity of goods sold: ", list(list_most_quant.keys()))
    print("Most popular product(s) based on the number of purchasers: ", list(list_most_uniq.keys()))
popular()
