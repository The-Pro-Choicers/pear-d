# **Endpoints Format**
So the major restaurant endpoints that have been implemented include:
## <ins>Filtering Endpoints</ins>

Return Format:

- List of JSON objects with fields `id, name, address, url, price_level, rating, photo_reference, and booleans for the 3 social categories`

These are the endpoints that you will use for filtering restaurant data based on the 3 social categories + price-level. Additional categories could be added in the future but for now let's just focus on these since each additionally filter we add increases the amount of links exponentially.

The way that the filtering endpoints are structured is they are all through the ```restaurants/socialfilter/``` path. The relative path after that path is formatted as ```e=[int]ph=[int]m=[int]p=[int]/``` where:

1. ```e``` represents the value for environmentally conscious, which is 0 or 1
2. ```ph``` is for philanthropic filtering
3. ```m``` is for whether to filter on minority owned
4. ```p``` determines the price level to filter on, which should be b/w 1-3

You can have variations where one of the filters is missing, but the link will always follow the order ```e -> ph -> m -> p``` meaning that if say you aren't filtering on ```ph```, then the ```e``` will have to come first in the endpoint address, then ```m``` and then ```p```. Examples provided here:

- ```restaurants/socialfilter/e=1ph=0m=1p=2/```
- ```restaurants/socialfilter/e=1m=0p=1/```
- ```restaurants/socialfilter/m=1p=2/```
- ```restaurants/socialfilter/e=1p=2/```
- ```restaurants/socialfilter/ph=0m=1/```

## <ins>Restaurant Details Endpoint</ins>

The restaurant details endpoint is called at ```restaurants/detailed/[int]/``` where the ```[int]``` will actually be the `number_id` associated with the restaurant in the database. So once we figure out what restaurant the user wants to see we can just grab the ```id``` and pass it into this endpoint

Examples:

- `restaurants/detailed/1/`
- `restaurants/detailed/32/`
