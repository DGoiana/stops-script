## STCP Stops Script

The script starts by opening an headless Firefox instance and starts intercepting requests from
```
https://www.stcp.pt/pt/viajar/horarios/?paragem={stop}&t=smsbus
```

It then searches for a specific request made to
```
https://www.stcp.pt/pt/itinerarium/
```
where a <code>p8321</code> token is retrieved.

That token is then used to request information from another page where real-time information is parsed and displayed.

## Usage

```
python3 buses.py
```
