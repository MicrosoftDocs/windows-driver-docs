---
title: Bug Check 0x135 REGISTRY_FILTER_DRIVER_EXCEPTION
description: The REGISTRY_FILTER_DRIVER_EXCEPTION bug check has a value of 0x00000135. This bugcheck is caused by an unhandled exception in a registry filtering driver.
ms.assetid: 99E171F4-5629-405F-993C-51287AD7D2C8
keywords: ["Bug Check 0x135 REGISTRY_FILTER_DRIVER_EXCEPTION", "REGISTRY_FILTER_DRIVER_EXCEPTION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- REGISTRY_FILTER_DRIVER_EXCEPTION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x135: REGISTRY\_FILTER\_DRIVER\_EXCEPTION


The REGISTRY\_FILTER\_DRIVER\_EXCEPTION bug check has a value of 0x00000135. This bugcheck is caused by an unhandled exception in a registry filtering driver.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## REGISTRY\_FILTER\_DRIVER\_EXCEPTION Parameters


| Parameter | Description                                                              |
|-----------|--------------------------------------------------------------------------|
| 1         | Exception Code                                                           |
| 2         | Address of the context record for the exception that caused the bugcheck |
| 3         | The driver's callback routine address                                    |
| 4         | Reserved                                                                 |

 

Cause
-----

This bugcheck indicates that a registry filtering driver didn't handle an exception inside its notification routine.

Resolution
----------

Identify the offending driver by using the 3rd parameter.

 

 




