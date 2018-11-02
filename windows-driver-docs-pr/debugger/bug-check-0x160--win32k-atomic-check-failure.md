---
title: Bug Check 0x160 WIN32K_ATOMIC_CHECK_FAILURE
description: The WIN32K_ATOMIC_CHECK_FAILURE bug check has a value of 0x00000160. This indicates that a Win32k function has violated an ATOMICCHECK.
ms.assetid: 81EEC1ED-367A-477D-B008-2295C7D7D1B4
keywords: ["Bug Check 0x160 WIN32K_ATOMIC_CHECK_FAILURE", "WIN32K_ATOMIC_CHECK_FAILURE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WIN32K_ATOMIC_CHECK_FAILURE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x160: WIN32K\_ATOMIC\_CHECK\_FAILURE


The WIN32K\_ATOMIC\_CHECK\_FAILURE bug check has a value of 0x00000160. This indicates that a Win32k function has violated an ATOMICCHECK.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## WIN32K\_ATOMIC\_CHECK\_FAILURE Parameters


| Parameter | Description                                                             |
|-----------|-------------------------------------------------------------------------|
| 1         | Count of functions on the stack currently inside of an ATOMIC operation |
| 2         | Reserved                                                                |
| 3         | Reserved                                                                |
| 4         | Reserved                                                                |

 

 

 




