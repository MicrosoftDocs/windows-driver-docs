---
title: Bug Check 0x18E KERNEL_PARTITION_REFERENCE_VIOLATION
description: The KERNEL_PARTITION_REFERENCE_VIOLATION bug check has a value of 0x0000018E.
keywords: ["Bug Check 0x18E KERNEL_PARTITION_REFERENCE_VIOLATION",  "KERNEL_PARTITION_REFERENCE_VIOLATION"]
ms.author: domars
ms.date: 05/23/2018
topic_type:
- apiref
api_name:
- KERNEL_PARTITION_REFERENCE_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check Bug Check 0x18E: KERNEL\_PARTITION\_REFERENCE\_VIOLATION

The KERNEL_PARTITION_REFERENCE_VIOLATION bug check has a value of 0x0000018E. 

This error indicates that a partition was improperly dereferenced. This normally occurs when a kernel-mode driver doesn't properly dereference partition objects. It can also occur when a serious data corruption occurs in the kernel.


**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## KERNEL\_PARTITION\_REFERENCE\_VIOLATION Parameters

The following parameters are displayed on the blue screen.

Parameter 1 indicates the type of failure. The meaning of the other parameters depends on the value of Parameter 1.

Parameter 1 | Parameter 2 | Parameter 3 | Parameter 4
|-----------|-------------|-------------|-------------|
| 0x0 : A partition with a non-zero hard reference count is being deleted. | Pointer to the partition. | Number of outstanding hard references. | Reserved|
| 0x1 : The system partition is being deleted | Pointer to the partition. | Reserved | Reserved |
| 0x2 :  A partition with outstanding ex work queue items is being deleted. | Pointer to the partition. |Pointer to the ex work queue with outstanding items. | Reserved |
 






