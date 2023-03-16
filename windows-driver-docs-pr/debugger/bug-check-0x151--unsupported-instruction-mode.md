---
title: Bug Check 0x151 UNSUPPORTED_INSTRUCTION_MODE
description: The UNSUPPORTED_INSTRUCTION_MODE bug check has a value of 0x00000151.
keywords: ["Bug Check 0x151 UNSUPPORTED_INSTRUCTION_MODE", "UNSUPPORTED_INSTRUCTION_MODE"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- UNSUPPORTED_INSTRUCTION_MODE
api_type:
- NA
---

# Bug Check 0x151: UNSUPPORTED\_INSTRUCTION\_MODE


The UNSUPPORTED\_INSTRUCTION\_MODE bug check has a value of 0x00000151. This indicates that an attempt was made to execute code using an unsupported processor instruction mode (for example, executing classic Arm instructions instead of ThumbV2 instructions). This is not permitted.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## UNSUPPORTED\_INSTRUCTION\_MODE Parameters


| Parameter | Description                                    |
|-----------|------------------------------------------------|
| 1         | Program counter when the problem was detected. |
| 2         | Trap Frame                                     |
| 3         | Reserved                                       |
| 4         | Reserved                                       |

 
## See also

[Bug Check Code Reference](bug-check-code-reference2.md)


 

 




