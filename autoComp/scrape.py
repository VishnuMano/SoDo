import pyzill
import json
ne_lat = 33.790089
ne_long = -84.379756
sw_lat = 33.771676
sw_long = -84.390478
zoom_value = 2
#pagination is for the list that you see at the right when searching
#you don't need to iterate over all the pages because zillow sends the whole data on mapresults at once on the first page
#however the maximum result zillow returns is 500, so if mapResults is 500
#try playing with the zoom or moving the coordinates, pagination won't help because you will always get at maximum 500 results
pagination = 1 
results_sold = pyzill.sold(pagination, ne_lat,ne_long,sw_lat,sw_long,zoom_value, "")
results_sale = pyzill.for_sale(pagination, ne_lat,ne_long,sw_lat,sw_long,zoom_value, "")
results_rent = pyzill.for_rent(pagination, ne_lat,ne_long,sw_lat,sw_long,zoom_value, "")
jsondata_sold = json.dumps(results_sold)
jsondata_sale = json.dumps(results_sale)
jsondata_rent = json.dumps(results_rent)
f = open("./jsondata_sold.json", "w")
f.write(jsondata_sold)
f.close()
f = open("./jsondata_sale.json", "w")
f.write(jsondata_sale)
f.close()
f = open("./jsondata_rent.json", "w")
f.write(jsondata_rent)
f.close()