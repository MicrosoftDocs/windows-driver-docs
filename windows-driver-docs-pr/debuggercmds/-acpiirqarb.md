---
title: "!acpiirqarb"
description: "The !acpiirqarb extension displays the contents of the ACPI IRQ arbiter structure, which contains the configuration of I/O devices to system interrupt controller inputs and processor IDT entries."
keywords: ["!acpiirqarb Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- acpiirqarb
api_type:
- NA
---

# !acpiirqarb

The **!acpiirqarb** extension displays the contents of the Advanced Configuration and Power Interface (ACPI) IRQ arbiter structure, which contains the configuration of I/O devices to system interrupt controller inputs and processor interrupt dispatch table (IDT) entries.

```dbgcmd
!acpiirqarb
```

## DLL

Kdexts.dll

## Additional Information

For information about the ACPI, see the Microsoft Windows Driver Kit (WDK) documentation, the Windows SDK documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. Also see [ACPI Debugging](../debugger/acpi-debugging.md) for information about other extensions that are associated with the ACPI.
