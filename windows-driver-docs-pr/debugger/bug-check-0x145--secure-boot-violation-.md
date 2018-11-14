---
title: Bug Check 0x145 SECURE_BOOT_VIOLATION
description: The SECURE_BOOT_VIOLATION bug check has a value of 0x00000145. This indicates that the secure Boot policy enforcement could not be started.
ms.assetid: C877C655-D94D-45B5-82DB-1361F0B020D2
keywords: ["Bug Check 0x145 SECURE_BOOT_VIOLATION", "SECURE_BOOT_VIOLATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SECURE_BOOT_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x145: SECURE\_BOOT\_VIOLATION


The SECURE\_BOOT\_VIOLATION bug check has a value of 0x00000145. This indicates that the secure Boot policy enforcement could not be started due to an invalid policy or a required operation not being completed.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SECURE\_BOOT\_VIOLATION Parameters


| Parameter | Description                        |
|-----------|------------------------------------|
| 1         | The status code of the failure.    |
| 2         | Address of the Secure Boot policy. |
| 3         | Size of the Secure Boot policy.    |
| 4         | Reserved                           |

 

 

 




