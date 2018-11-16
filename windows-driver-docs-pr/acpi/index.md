---
title: ACPI design guide
description: This section describes how device drivers can interface an Advanced Configuration and Power Interface (ACPI) device. ACPI devices are defined by the Advanced Configuration and Power Interface (ACPI) Specification.
ms.assetid: 294f4b43-2b3e-4afa-8fa8-74a6719131c7
ms.author: windowsdriverdev
ms.date: 01/24/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ACPI design guide


This section describes how device drivers can interface with an Advanced Configuration and Power Interface (ACPI) device. 
ACPI devices are defined by the [Advanced Configuration and Power Interface (ACPI) Specification](https://go.microsoft.com/fwlink/p/?linkid=866846).

## In this section


| Section | Description |
| --- | --- |
| [Supporting ACPI Devices](supporting-acpi-devices.md) | Provides information about how to use a Windows Driver Model (WDM) function driver to enhance the functionality of an ACPI device. |
| [Evaluating ACPI Control Methods](evaluating-acpi-control-methods.md) | Provides information about how device drivers that comply with the requirements of [Kernel-Mode Driver Framework (KMDF)](https://docs.microsoft.com/windows-hardware/drivers/kernel), [User-Mode Driver Framework (UMDF)](https://docs.microsoft.com/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2), or [Windows Driver Model (WDM)](https://docs.microsoft.com/windows-hardware/drivers/kernel/windows-driver-model) can evaluate ACPI control methods. |
| [How to Identify the Windows Version in ACPI by Using _OSI](winacpi-osi.md) | Provides information about the ACPI Source Language (ASL) Operating System Interface Level (\_OSI) method used to identify the host operating system. |


## Related sctions

-   [ACPI DDI reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_acpi)

 



