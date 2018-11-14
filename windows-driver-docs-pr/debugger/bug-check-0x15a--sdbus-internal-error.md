---
title: Bug Check 0x15A SDBUS_INTERNAL_ERROR
description: The SDBUS_INTERNAL_ERROR bug check has a value of 0x0000015A. This indicates that an unrecoverable hardware failure has occurred on an SD-attached device.
ms.assetid: C5FBE617-DADD-452C-A1BC-A0DE228FF2DE
keywords: ["Bug Check 0x15A SDBUS_INTERNAL_ERROR", "SDBUS_INTERNAL_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SDBUS_INTERNAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x15A: SDBUS\_INTERNAL\_ERROR


The SDBUS\_INTERNAL\_ERROR bug check has a value of 0x0000015A. This indicates that an unrecoverable hardware failure has occurred on an SD-attached device.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SDBUS\_INTERNAL\_ERROR Parameters


| Parameter | Description                                                    |
|-----------|----------------------------------------------------------------|
| 1         | Pointer to the internal SD work packet that caused the failure |
| 2         | Pointer the controller socket information                      |
| 3         | Pointer to the SD request packet sent down to the bus driver   |
| 4         | Reserved                                                       |

 

 

 




