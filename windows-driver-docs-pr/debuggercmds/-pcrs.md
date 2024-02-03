---
title: pcrs (WinDbg)
description: The pcrs extension displays the Intel Itanium-specific processor control registers.
keywords: ["processor control register (PCR)", "PCR (processor control register)", "pcrs Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- pcrs
api_type:
- NA
---

# !pcrs


The **!pcrs** extension displays the Intel Itanium-specific processor control registers.

```dbgcmd
!pcrs Address
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of a processor control registers file.

## DLL

Windows XP and later - Kdexts.dll

 

This extension command can only be used with an Itanium-based target computer.

## Remarks

Do not confuse the **!pcrs** extension with the [**!pcr**](-pcr.md) extension, which displays the current status of the processor control region.

 

 





