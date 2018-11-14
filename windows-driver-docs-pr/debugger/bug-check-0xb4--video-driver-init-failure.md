---
title: Bug Check 0xB4 VIDEO_DRIVER_INIT_FAILURE
description: The VIDEO_DRIVER_INIT_FAILURE bug check has a value of 0x000000B4. This indicates that Windows was unable to enter graphics mode.
ms.assetid: 37c2d07d-f351-42d0-ba88-9b9a2a3d19f8
keywords: ["Bug Check 0xB4 VIDEO_DRIVER_INIT_FAILURE", "VIDEO_DRIVER_INIT_FAILURE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- VIDEO_DRIVER_INIT_FAILURE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xB4: VIDEO\_DRIVER\_INIT\_FAILURE


The VIDEO\_DRIVER\_INIT\_FAILURE bug check has a value of 0x000000B4. This indicates that Windows was unable to enter graphics mode.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## VIDEO\_DRIVER\_INIT\_FAILURE Parameters


None

Cause
-----

The system was not able to go into graphics mode because no display drivers were able to start.

This usually occurs when no video miniport drivers are able to load successfully.

 

 




