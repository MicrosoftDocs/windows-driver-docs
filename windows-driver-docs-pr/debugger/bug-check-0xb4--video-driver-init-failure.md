---
title: Bug Check 0xB4 VIDEO_DRIVER_INIT_FAILURE
description: The VIDEO_DRIVER_INIT_FAILURE bug check has a value of 0x000000B4. This indicates that Windows was unable to enter graphics mode.
keywords: ["Bug Check 0xB4 VIDEO_DRIVER_INIT_FAILURE", "VIDEO_DRIVER_INIT_FAILURE"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- VIDEO_DRIVER_INIT_FAILURE
api_type:
- NA
---

# Bug Check 0xB4: VIDEO\_DRIVER\_INIT\_FAILURE


The VIDEO\_DRIVER\_INIT\_FAILURE bug check has a value of 0x000000B4. This indicates that Windows was unable to enter graphics mode.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## VIDEO\_DRIVER\_INIT\_FAILURE Parameters


None

## Cause

The system was not able to go into graphics mode because no display drivers were able to start.

This usually occurs when no video miniport drivers are able to load successfully.

## See Also

[Bug Check Code Reference](bug-check-code-reference2.md) 

