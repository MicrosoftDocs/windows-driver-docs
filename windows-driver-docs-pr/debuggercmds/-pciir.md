---
title: "!pciir (WinDbg)"
description: "The !pciir extension displays the contents of the hardware routing of peripheral component interconnect (PCI) devices to interrupt controller inputs."
keywords: ["PCI IRQ routing table", "peripheral component interconnect (PCI)", "!pciir Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- pciir
api_type:
- NA
---

# !pciir

The **!pciir** extension displays the contents of the hardware routing of peripheral component interconnect (PCI) devices to interrupt controller inputs.

```dbgcmd
!pciir
```

## DLL

Windows XP - Kdexts.dll

Windows Vista and later - Unavailable

## Additional Information

This extension command can only be used with an x86-based target computer that does not have the Advanced Configuration and Power Interface (ACPI) enabled.

For similar information on any ACPI-enabled computer, use the [**!acpiirqarb**](-acpiirqarb.md) extension.

