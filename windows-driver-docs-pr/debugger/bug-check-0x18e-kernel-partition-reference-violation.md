---
title: Bug Check 0x18E KERNEL_PARTITION_REFERENCE_VIOLATION
description: The KERNEL_PARTITION_REFERENCE_VIOLATION bug check has a value of 0x0000018E.
keywords: ["Bug Check 0x18E KERNEL_PARTITION_REFERENCE_VIOLATION",  "KERNEL_PARTITION_REFERENCE_VIOLATION"]
ms.author: domars
ms.date: 04/18/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- PROFILER_CONFIGURATION_ILLEGAL
api_type:
- NA
---

# Bug Check Bug Check 0x18E: KERNEL\_PARTITION\_REFERENCE\_VIOLATION

The KERNEL_PARTITION_REFERENCE_VIOLATION bug check has a value of 0x0000018E. 

This error indicates that a partition was improperly dereferenced. This normally occurs when a kernel-mode driver doesn't properly dereference partition objects. It can also occur when a serious data corruption occurs in the kernel.


**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](http://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PROFILER\_CONFIGURATION\_ILLEGAL Parameters

Arguments:

Arg1: 0000000000000000, A partition with a non-zero hard reference count is being deleted.

Arg2: 0000000000000000, Pointer to the partition.

Arg3: 0000000000000000, Number of outstanding hard references.

Arg4: 0000000000000000, Reserved.
 

 




