# Run pings and traceroute with IOS XE

**NOTE: due to issues with lab, the final script has not been tested. The script will be tested ASAP and possible bugs fixed.** 

> *Note*: The livetools YANG actions available on IOS XE v. 17.15 - the script won't work against an older version.

1. Create a file `.env` from the `env.template`
    ```bash
    cp env.template .env
    ```

1. Fill in the data to the `.env`.

1. Run the script with `flask`:
```bash
flask --app main.py run
```
