# Attention Backend

### User WS Messages:

url: /websocket/connect_user

### From user
##### Camera
```json
   {
    "type": "url",
    "camera_id": int
    "camera_url": str
   }
```
##### Camera status
```json
   {
    "type": "status",
    "status": "active" or "not_active"
   }
``` 
### To User
##### Labels
 ```json
 {
    "type": "labels",
    "camera_id": int,
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
  "camera_id": int,
  "type": "warning",
  "object_name": str
  "warning_type": "error" or "warning"
}

```