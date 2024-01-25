---
title: Bug Check 0X111 RECURSIVE_NMI
description: The RECURSIVE_NMI bug check has a value of 0x00000111. This bug check indicates that a non-maskable-interrupt (NMI) occurred while a previous NMI was in progress.
keywords: ["Bug Check 0x111 RECURSIVE_NMI", "RECURSIVE_NMI"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- RECURSIVE_NMI
api_type:
- NA
---

# Bug Check 0x111: RECURSIVE\_NMI


The RECURSIVE\_NMI bug check has a value of 0x00000111. This bug check indicates that a non-maskable-interrupt (NMI) occurred while a previous NMI was in progress.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## Remarks

This bug check occurs when there is an error in the system management interrupt (SMI) code, and an SMI interrupts an NMI and enables interrupts. Execution then continues with NMIs enabled, and another NMI interrupts the NMI in progress.

 

 




