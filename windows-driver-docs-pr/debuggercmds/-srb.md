---
title: "!srb (WinDbg)"
description: "The !srb extension displays information about a SCSI Request Block (SRB)."
keywords: ["!srb Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- srb
api_type:
- NA
---

# !srb

The **!srb** extension displays information about a SCSI Request Block (SRB).

```dbgcmd
!srb Address 
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the SRB on the target computer.

## DLL

Kdexts.dll

## Additional Information

For information about SRBs, see the Windows Driver Kit (WDK) documentation.

## Remarks

An SRB is a system-defined structure used to communicate I/O requests from a SCSI class driver to a SCSI port driver.
