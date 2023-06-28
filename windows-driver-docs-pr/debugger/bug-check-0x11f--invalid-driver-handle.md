---
title: Bug Check 0x11F INVALID_DRIVER_HANDLE
description: The INVALID_DRIVER_HANDLE bug check has a value of 0x0000011F. This indicates that someone has closed the initial handle for a driver between inserting the driver object and referencing the handle.
keywords: ["Bug Check 0x11F INVALID_DRIVER_HANDLE", "INVALID_DRIVER_HANDLE"]
ms.date: 01/30/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- INVALID_DRIVER_HANDLE
api_type:
- NA
---

# Bug Check 0x11F: INVALID\_DRIVER\_HANDLE


The INVALID\_DRIVER\_HANDLE bug check has a value of 0x0000011F. This indicates that someone has closed the initial handle for a driver between inserting the driver object and referencing the handle.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## INVALID\_DRIVER\_HANDLE Parameters


| Parameter | Description                                         |
|-----------|-----------------------------------------------------|
| 1         | The handle value for the driver object.             |
| 2         | The status returned trying to reference the object. |
| 3         | The address of the PDRIVER\_OBJECT.                 |
| 4         | Reserved                                            |

 

 

 




