---
title: ACPI design guide
description: This section describes how device drivers can interface an Advanced Configuration and Power Interface (ACPI) device. ACPI devices are defined by the Advanced Configuration and Power Interface (ACPI) Specification.
ms.date: 03/17/2023
---

# ACPI design guide

This section describes how device drivers can interface with an Advanced Configuration and Power Interface (ACPI) device.

ACPI devices are defined by the [Advanced Configuration and Power Interface (ACPI) Specification](https://uefi.org/specifications).

## In this section

| Section | Description |
|---|---|
| [Supporting ACPI Devices](supporting-acpi-devices.md) | Provides information about how to use a Windows Driver Model (WDM) function driver to enhance the functionality of an ACPI device. |
| [Evaluating ACPI Control Methods](evaluating-acpi-control-methods.md) | Provides information about how device drivers that comply with the requirements of [Kernel-Mode Driver Framework (KMDF)](../kernel/index.md), [User-Mode Driver Framework (UMDF)](../wdf/getting-started-with-umdf-version-2.md), or [Windows Driver Model (WDM)](../kernel/introduction-to-wdm.md) can evaluate ACPI control methods. |
| [How to Identify the Windows Version in ACPI by Using _OSI](winacpi-osi.md) | Provides information about the ACPI Source Language (ASL) Operating System Interface Level (\_OSI) method used to identify the host operating system. |

## Related sections

- [ACPI DDI reference](/windows-hardware/drivers/ddi/_acpi)
