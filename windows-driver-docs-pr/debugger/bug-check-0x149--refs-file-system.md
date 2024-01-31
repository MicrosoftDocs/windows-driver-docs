---
title: Bug Check 0x149 REFS_FILE_SYSTEM
description: The REFS_FILE_SYSTEM bug check has a value of 0x00000149. This indicates that a file system error has occurred.
keywords: ["Bug Check 0x149 REFS_FILE_SYSTEM", "REFS_FILE_SYSTEM"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- REFS_FILE_SYSTEM
api_type:
- NA
---

# Bug Check 0x149: REFS\_FILE\_SYSTEM


The REFS\_FILE\_SYSTEM bug check has a value of 0x00000149. This indicates that a file system error has occurred.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## REFS\_FILE\_SYSTEM Parameters


| Parameter | Description                          |
|-----------|--------------------------------------|
| 1         | \_\_LINE\_\_                         |
| 2         | ExceptionRecord                      |
| 3         | ContextRecord                        |
| 4         | ExceptionRecord-&gt;ExceptionAddress |


 

## Resolution

If you see RefsExceptionFilter on the stack then the 2nd and 3rd parameters are the exception record and context record. Do a [**.exr**](../debuggercmds/-exr--display-exception-record-.md) on the 2nd parameter to view the exception information, then do a [**.cxr**](../debuggercmds/-cxr--display-context-record-.md) on the 3rd parameter and [**kb**](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md)  to obtain a more informative stack trace.

 
## See also

[Bug Check Code Reference](bug-check-code-reference2.md)


 




