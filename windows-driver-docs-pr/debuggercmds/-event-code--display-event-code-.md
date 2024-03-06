---
title: .event_code (Display Event Code)
description: The .event_code command displays the current event instructions.
keywords: [".event_code (Display Event Code) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .event_code (Display Event Code)
api_type:
- NA
---

# .event\_code (Display Event Code)


The **.event\_code** command displays the current event instructions.

```dbgcmd
.event_code 
```

### Environment

|  Item       | Description               |
|-----------|------------------------|
| Modes     | user mode, kernel mode |
| Targets   | live debugging only    |
| Platforms | all                    |

 

## Remarks

The **.event\_code** command displays the hexadecimal instructions at the current event's instruction pointer. The display includes up to 64 bytes of instructions if they are available.

 

 





