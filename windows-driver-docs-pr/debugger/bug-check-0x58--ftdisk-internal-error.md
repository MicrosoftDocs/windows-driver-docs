---
title: Bug Check 0x58 FTDISK_INTERNAL_ERROR
description: The FTDISK_INTERNAL_ERROR bug check has a value of 0x00000058. This is issued if the system is booted from the wrong copy of a mirrored partition.
ms.assetid: c8de6a04-740d-415e-bf23-b28da066a225
keywords: ["Bug Check 0x58 FTDISK_INTERNAL_ERROR", "FTDISK_INTERNAL_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- FTDISK_INTERNAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x58: FTDISK\_INTERNAL\_ERROR


The FTDISK\_INTERNAL\_ERROR bug check has a value of 0x00000058. This is issued if the system is booted from the wrong copy of a mirrored partition.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## FTDISK\_INTERNAL\_ERROR Parameters


None

Cause
-----

The hives are indicating that the mirror is valid, but it is not. The hives should actually be pointing to the shadow partition.

This is almost always caused by the primary partition being revived.

Resolution
----------

Reboot the system from the shadow partition.

 

 




