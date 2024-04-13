---
title: Bug Check 0x40 TARGET_MDL_TOO_SMALL
description: The TARGET_MDL_TOO_SMALL bug check has a value of 0x00000040. This indicates that a driver has improperly used IoBuildPartialMdl.
keywords: ["Bug Check 0x40 TARGET_MDL_TOO_SMALL", "TARGET_MDL_TOO_SMALL"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- TARGET_MDL_TOO_SMALL
api_type:
- NA
---

# Bug Check 0x40: TARGET\_MDL\_TOO\_SMALL


The TARGET\_MDL\_TOO\_SMALL bug check has a value of 0x00000040. This indicates that a driver has improperly used **IoBuildPartialMdl**.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## TARGET\_MDL\_TOO\_SMALL Parameters


None

## Cause

This is a driver bug. A driver has called the **IoBuildPartialMdl** function and passed it an MDL to map part of a source MDL, but the target MDL is not large enough to map the entire range of addresses requested.

## Resolution

The source and target MDLs, as well as the address range length to be mapped, are the first, second, and fourth arguments to the **IoBuildPartialMdl** function. Therefore, doing a stack trace on this particular function might help during the debugging process. Ensure that your code is correctly calculating the necessary size for the target MDL for the address range length that you are passing to this function.

 

 




