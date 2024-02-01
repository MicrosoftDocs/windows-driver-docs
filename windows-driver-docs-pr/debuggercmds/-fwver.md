---
title: "!fwver (WinDbg)"
description: The fwver extension displays the Itanium firmware version.
keywords: ["fwver Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- fwver
api_type:
- NA
---

# !fwver

The **!fwver** extension displays the Itanium firmware version.

```dbgcmd
!fwver 
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

## DLL

Windows XP and later - Kdexts.dll

This extension command can only be used with an Itanium target computer.

### Additional Information

For more information, consult an Intel architecture manual.

## Remarks

Here is an example of the output from this extension:

```dbgcmd
kd> !fwver

Firmware Version

   Sal Revision:        0
   SAL_A_VERSION:       0
   SAL_B_VERSION:       0
   PAL_A_VERSION:       6623
   PAL_B_VERSION:       6625
   smbiosString:        W460GXBS2.86E.0117A.P08.200107261041
```

 

 





