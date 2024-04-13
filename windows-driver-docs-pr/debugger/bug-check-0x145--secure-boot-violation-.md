---
title: Bug Check 0x145 SECURE_BOOT_VIOLATION
description: The SECURE_BOOT_VIOLATION bug check has a value of 0x00000145. This indicates that the secure Boot policy enforcement could not be started.
keywords: ["Bug Check 0x145 SECURE_BOOT_VIOLATION", "SECURE_BOOT_VIOLATION"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- SECURE_BOOT_VIOLATION
api_type:
- NA
---

# Bug Check 0x145: SECURE\_BOOT\_VIOLATION


The SECURE\_BOOT\_VIOLATION bug check has a value of 0x00000145. This indicates that the secure Boot policy enforcement could not be started due to an invalid policy or a required operation not being completed.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## SECURE\_BOOT\_VIOLATION Parameters


| Parameter | Description                        |
|-----------|------------------------------------|
| 1         | The status code of the failure.    |
| 2         | Address of the Secure Boot policy. |
| 3         | Size of the Secure Boot policy.    |
| 4         | Reserved                           |

 
## See also

[Bug Check Code Reference](bug-check-code-reference2.md)

 

 




