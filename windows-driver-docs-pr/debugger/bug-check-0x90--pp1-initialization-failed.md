---
title: Bug Check 0x90 PP1_INITIALIZATION_FAILED
description: The PP1_INITIALIZATION_FAILED bug check has a value of 0x00000090. This bug check indicates that the Plug and Play (PnP) manager could not be initialized.
ms.assetid: 8dd46d24-0174-4310-953e-7b451ae34c71
keywords: ["Bug Check 0x90 PP1_INITIALIZATION_FAILED", "PP1_INITIALIZATION_FAILED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PP1_INITIALIZATION_FAILED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x90: PP1\_INITIALIZATION\_FAILED


The PP1\_INITIALIZATION\_FAILED bug check has a value of 0x00000090. This bug check indicates that the Plug and Play (PnP) manager could not be initialized.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PP1\_INITIALIZATION\_FAILED Parameters


None

Cause
-----

An error occurred during Phase 1 initialization of the kernel-mode PnP manager.

Phase 1 is where most of the initialization is done, including setting up the registry files and other environment settings for drivers to call during the subsequent I/O initialization.

 

 




