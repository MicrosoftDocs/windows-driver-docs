---
title: Bug Check 0x11F INVALID_DRIVER_HANDLE
description: The INVALID_DRIVER_HANDLE bug check has a value of 0x0000011F. This indicates that someone has closed the initial handle for a driver between inserting the driver object and referencing the handle.
ms.assetid: A669256B-737D-4215-8E0E-5500D7704F4E
keywords: ["Bug Check 0x11F INVALID_DRIVER_HANDLE", "INVALID_DRIVER_HANDLE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- INVALID_DRIVER_HANDLE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x11F: INVALID\_DRIVER\_HANDLE


The INVALID\_DRIVER\_HANDLE bug check has a value of 0x0000011F. This indicates that someone has closed the initial handle for a driver between inserting the driver object and referencing the handle.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## INVALID\_DRIVER\_HANDLE Parameters


| Parameter | Description                                         |
|-----------|-----------------------------------------------------|
| 1         | The handle value for the driver object.             |
| 2         | The status returned trying to reference the object. |
| 3         | The address of the PDRIVER\_OBJECT.                 |
| 4         | Reserved                                            |

 

 

 




