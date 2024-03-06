---
title: gbl (WinDbg)
description: The gbl extension displays header information from the ACPI BIOS Root System Description (RSDT) table of the target computer.
keywords: ["ACPI (Advanced Configuration and Power Interface), RSDT header information", "global lock", "gbl Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- gbl
api_type:
- NA
---

# !gbl


The **!gbl** extension displays header information from the ACPI BIOS Root System Description (RSDT) table of the target computer.

```dbgcmd
!gbl [-v]
```

## Parameters


<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Verbose. Displays detailed information about the table.

## DLL

Windows XP and later - Kdexts.dll

 

### Additional Information

For information about the ACPI and ACPI tables, see [Other ACPI Debugging Extensions](../debugger/other-acpi-debugging-extensions.md) and the [ACPI Specification](https://uefi.org/specifications) Web site. Also see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

 

 





