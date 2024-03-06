---
title: "!acpicache (WinDbg)"
description: "The !acpicache extension displays all of the Advanced Configuration and Power Interface (ACPI) tables cached by the HAL."
keywords: ["!acpicache Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- acpicache
api_type:
- NA
---

# !acpicache

The **!acpicache** extension displays all of the Advanced Configuration and Power Interface (ACPI) tables cached by the HAL.

```dbgcmd
!acpicache [DisplayLevel]
```

## Parameters


<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Specifies the detail level of the display. This value is either 0 for an abbreviated display or 1 for a more detailed display. The default value is 0.

## DLL

Kdexts.dll

 

### Additional Information

For information about the ACPI, see the Microsoft Windows Driver Kit (WDK) documentation, the Windows SDK documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These books and resources may not be available in some languages and countries.) Also see [ACPI Debugging](../debugger/acpi-debugging.md) for information about other extensions that are associated with the ACPI.

 

 





