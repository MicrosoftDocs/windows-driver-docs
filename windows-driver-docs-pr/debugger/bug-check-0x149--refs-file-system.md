---
title: Bug Check 0x149 REFS\_FILE\_SYSTEM
description: The REFS\_FILE\_SYSTEM bug check has a value of 0x00000149. This indicates that a file system error has occurred.
ms.assetid: 899E89E7-46CD-4143-B1DC-7959F01643CF
keywords: ["Bug Check 0x149 REFS_FILE_SYSTEM", "REFS_FILE_SYSTEM"]
topic_type:
- apiref
api_name:
- REFS_FILE_SYSTEM
api_type:
- NA
---

# Bug Check 0x149: REFS\_FILE\_SYSTEM


The REFS\_FILE\_SYSTEM bug check has a value of 0x00000149. This indicates that a file system error has occurred.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](http://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## REFS\_FILE\_SYSTEM Parameters


| Parameter | Description                          |
|-----------|--------------------------------------|
| 1         | \_\_LINE\_\_                         |
| 2         | ExceptionRecord                      |
| 3         | ContextRecord                        |
| 4         | ExceptionRecord-&gt;ExceptionAddress |

 

| Parameter | Description |
|-----------|-------------|
| 1         | Message     |
| 2         | Reserved    |
| 3         | Reserved    |
| 4         | Reserved    |

 

Resolution
----------

If you see RefsExceptionFilter on the stack then the 2nd and 3rd parameters are the exception record and context record. Do a .exr on the 2nd parameter to view the exception information. Do a .cxr on the 3rd parameter and then kb to obtain a more informative stack trace.

 

 




