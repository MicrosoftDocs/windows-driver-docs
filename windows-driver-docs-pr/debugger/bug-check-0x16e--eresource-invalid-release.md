---
title: Bug Check 0x16E ERESOURCE_INVALID_RELEASE
description: The ERESOURCE_INVALID_RELEASE bug check has a value of 0x0000016E. This indicates that the target thread pointer supplied to ExReleaseResourceForThreadLite was invalid.
ms.assetid: F180D28D-70B7-4E78-9E04-C5DC19A41EB9
keywords: ["Bug Check 0x16E ERESOURCE_INVALID_RELEASE", "ERESOURCE_INVALID_RELEASE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ERESOURCE_INVALID_RELEASE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x16E: ERESOURCE\_INVALID\_RELEASE


The ERESOURCE\_INVALID\_RELEASE bug check has a value of 0x0000016E. This indicates that the target thread pointer supplied to ExReleaseResourceForThreadLite was invalid.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## ERESOURCE\_INVALID\_RELEASE Parameters


| Parameter | Description                                    |
|-----------|------------------------------------------------|
| 1         | The resource being released                    |
| 2         | The current thread                             |
| 3         | The incorrect target thread that was passed in |
| 4         | Reserved                                       |

 

Cause
-----

This bugcheck will hit if a call to ExSetOwnerPointerEx was skipped by the API client (if a cross-thread release was intended) or if the caller accidentally passed in a value other that supplied by ExGetCurrentResourceThread.

 

 




