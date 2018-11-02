---
title: Bug Check 0x40 TARGET_MDL_TOO_SMALL
description: The TARGET_MDL_TOO_SMALL bug check has a value of 0x00000040. This indicates that a driver has improperly used IoBuildPartialMdl.
ms.assetid: bd154c1f-6c74-424e-bc32-22c9a93efae5
keywords: ["Bug Check 0x40 TARGET_MDL_TOO_SMALL", "TARGET_MDL_TOO_SMALL"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- TARGET_MDL_TOO_SMALL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x40: TARGET\_MDL\_TOO\_SMALL


The TARGET\_MDL\_TOO\_SMALL bug check has a value of 0x00000040. This indicates that a driver has improperly used **IoBuildPartialMdl**.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## TARGET\_MDL\_TOO\_SMALL Parameters


None

Cause
-----

This is a driver bug. A driver has called the **IoBuildPartialMdl** function and passed it an MDL to map part of a source MDL, but the target MDL is not large enough to map the entire range of addresses requested.

Resolution
----------

The source and target MDLs, as well as the address range length to be mapped, are the first, second, and fourth arguments to the **IoBuildPartialMdl** function. Therefore, doing a stack trace on this particular function might help during the debugging process. Ensure that your code is correctly calculating the necessary size for the target MDL for the address range length that you are passing to this function.

 

 




