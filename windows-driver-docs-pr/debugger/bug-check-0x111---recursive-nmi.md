---
title: Bug Check 0x111 RECURSIVE_NMI
description: The RECURSIVE_NMI bug check has a value of 0x00000111. This bug check indicates that a non-maskable-interrupt (NMI) occurred while a previous NMI was in progress.
ms.assetid: 1f275db1-ac79-4bd2-85c5-cb64342911d1
keywords: ["Bug Check 0x111 RECURSIVE_NMI", "RECURSIVE_NMI"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- RECURSIVE_NMI
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x111: RECURSIVE\_NMI


The RECURSIVE\_NMI bug check has a value of 0x00000111. This bug check indicates that a non-maskable-interrupt (NMI) occurred while a previous NMI was in progress.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

Remarks
-------

This bug check occurs when there is an error in the system management interrupt (SMI) code, and an SMI interrupts an NMI and enables interrupts. Execution then continues with NMIs enabled, and another NMI interrupts the NMI in progress.

 

 




