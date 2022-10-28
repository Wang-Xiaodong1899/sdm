class_labels = ['Alarm Clock', 'Backpack', 'Batteries', 'Bed', 'Bike', 'Bottle', 'Bucket', 'Calculator', 'Calendar',
'Candles', 'Chair', 'Clipboards', 'Computer', 'Couch', 'Curtains', 'Desk Lamp', 'Drill', 'Eraser', 'Exit Sign', 'Fan',
'File Cabinet', 'Flipflops', 'Flowers', 'Folder', 'Fork', 'Glasses', 'Hammer', 'Helmet', 'Kettle', 'Keyboard',
'Knives', 'Lamp Shade', 'Laptop', 'Marker', 'Monitor', 'Mop', 'Mouse', 'Mug', 'Notebook', 'Oven', 'Pan',
'Paper Clip', 'Pen', 'Pencil', 'Postit Notes', 'Printer', 'Push Pin', 'Radio', 'Refrigerator', 'ruler',
'Scissors', 'Screwdriver', 'Shelf', 'Sink', 'Sneakers', 'Soda', 'Speaker', 'Spoon', 'Table', 'Telephone',
'Toothbrush', 'Toys', 'Trash Can', 'TV', 'Webcam']

f = open('prompts_office_home.txt','a')
for label in class_labels:
    for d in ['artistic painting', 'Clipart', 'Product', 'Real World']:
        prompt = f'a {label} in the style of {d}'
        f.write(prompt+'\n')
f.close()