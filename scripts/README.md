Scripts to help integration like loading output into postgres
-----------

```
signalkgen --num-boats 300 --nautical-miles 15 --iterations 100 | jq | python3 ./scripts/load_db.py signalk 
```

