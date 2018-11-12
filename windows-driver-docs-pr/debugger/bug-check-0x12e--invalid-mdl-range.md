---
title: Bug Check 0x12E INVALID_MDL_RANGE
description: The INVALID_MDL_RANGE bug check has a value of 0x0000012E.
ms.assetid: 911192DC-17B8-4D75-A96E-2E310B30348F
keywords: ["Bug Check 0x12E INVALID_MDL_RANGE", "INVALID_MDL_RANGE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- INVALID_MDL_RANGE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x12E: INVALID\_MDL\_RANGE


The INVALID\_MDL\_RANGE bug check has a value of 0x0000012E. This indicates that a driver has called the IoBuildPartialMdl() function and passed it an MDL to map part of a source MDL, but the virtual address range specified is outside the range in the source MDL. This is typically a driver bug.

The source and target MDLs, as well as the address range length to be mapped are the arguments to the IoBuildPartialMdl() function, i.e.;) .

```cpp
IoBuildPartialMdl(
        IN PMDL SourceMdl,
        IN OUT PMDL TargetMdl,
        IN PVOID VirtualAddress,
        IN ULONG Length
```

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## INVALID\_MDL\_RANGE Parameters


| Parameter | Description    |
|-----------|----------------|
| 1         | SourceMdl      |
| 2         | TargetMdl      |
| 3         | VirtualAddress |
| 4         | Length         |

 

 

 




