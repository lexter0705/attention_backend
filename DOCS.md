# Attention Backend

### User WS Messages:

url: /websocket/connect_user

### From user
##### Image
```json
   {
    "image": base64
   }
``` 
### To User
##### Labels
 ```json
 {
    "type": "labels",
    "labels": [
      {
        "name": str,
        "x1": float,
        "x2": float,
        "y1": float,
        "y2": float
      },
      ...
    ]
 }
 ```

##### Warning
```json
{
  "type": "warning",
  "object_name": str
  "warning_type": "error" or "warning"
}

```