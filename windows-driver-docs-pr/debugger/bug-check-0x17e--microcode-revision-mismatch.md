---
title: Bug Check 0x17E MICROCODE_REVISION_MISMATCH
description: The MICROCODE_REVISION_MISMATCH bug check has a value of 0x0000017E. It indicates that that one or more processors in the multiprocessor configuration have inconsistent microcode loaded.  
keywords: ["Bug Check 0x17E MICROCODE_REVISION_MISMATCH", "MICROCODE_REVISION_MISMATCH"]
ms.date: 01/14/2019
topic_type:
- apiref
api_name:
- MICROCODE_REVISION_MISMATCH
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x17E: MICROCODE\_REVISION\_MISMATCH

The MICROCODE\_REVISION\_MISMATCH bug check has a value of 0x0000017E. It indicates that one or more processors in the multiprocessor configuration have inconsistent microcode loaded.  

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 

## MICROCODE\_REVISION\_MISMATCH Parameters

|Parameter|Description|
|-------- |---------- |
|1| The processor CPUID signature value of the processor that mismatched. |
|2| The expected microcode revision for the processor. |
|3| The actual, reported microcode revision for the processor. |
|4| The processor index of the mismatching processor.|


## ## Cause
One or more processors in the multiprocessor configuration have inconsistent microcode loaded. 
This bugcheck indicates that faulty system firmware has mistakenly applied a microcode update to only a subset of processors in the host configuration. System firmware must apply microcode updates to all processors in a uniform fashion. 

## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

