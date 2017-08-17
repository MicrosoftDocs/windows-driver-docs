---
title: Bug Check 0x6 INVALID_PROCESS_DETACH_ATTEMPT
description: The INVALID_PROCESS_DETACH_ATTEMPT bug check has a value of 0x00000006. This bug check appears very infrequently.
ms.assetid: f468b348-6576-4430-aa8f-b6100a689fee
keywords: ["Bug Check 0x6 INVALID_PROCESS_DETACH_ATTEMPT", "INVALID_PROCESS_DETACH_ATTEMPT"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- INVALID_PROCESS_DETACH_ATTEMPT
api_type:
- NA
---

# Bug Check 0x6: INVALID\_PROCESS\_DETACH\_ATTEMPT


The INVALID\_PROCESS\_DETACH\_ATTEMPT bug check has a value of 0x00000006.

This bug check appears very infrequently. This bug check can be caused by calling the KeStackAttachProcess and subsequently calling KeUnstackDetachProcess in a LOAD_IMAGE_NOTIFY_ROUTINE callback. The callback for LOAD_IMAGE_NOTIFY_ROUTINE runs in a thread of the process the image is being loaded into.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](http://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

 

 




