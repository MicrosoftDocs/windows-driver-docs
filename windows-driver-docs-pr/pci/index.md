---
title: PCI driver programming guide
description: PCI driver programming guide
ms.assetid: 014f6243-6166-42e1-9f0f-1a438c77fd78
keywords:
- PCI WDK buses
- buses WDK , PCI
- Peripheral Component Interconnect WDK buses
- PCI Local Bus specification WDK
- configuration space WDK PCI
- device-specific configuration space WDK PCI
- requesting configuration space information WDK PCI
- power management WDK PCI
- querying power management capability data
- headers WDK PCI
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PCI driver programming guide

The following table summarizes the PCIe features that are supported by different versions of Windows. For details, see the specified sections in the [official PCIe specification](https://pcisig.com/specifications/review-zone).

|Feature|Minimum Windows version|
|----|----|
|Resizable BAR capability</br>See section 7.22.|Windows 10|
|Atomic Operations</br>See section 6.15.|Windows 10|
|ACPI additions for FW latency optimizations</br>See [ACPI Additions for FW Latency Optimizations](https://pcisig.com/specifications)|Windows 10|
|ATS/PRI</br>-  [ATS specification](https://go.microsoft.com/fwlink/p/?LinkId=787061)</br>-  [Errata for the PCI Express&#174; Base Specification Revision 3.1, Single Root I/O Virtualization and Sharing Revision 1.1, Address Translation and Sharing Revision 1.1, and M.2 Specification Revision 1.0](https://pcisig.com/specifications/iov/)|Windows 10|
|Optimized Buffer Flush/Fill (OBFF)</br>See section 6.19.|-  Windows 8</br>-  Windows Server 2012|
|Latency Tolerance Reporting (LTR) Capability</br>See section 7.25.|- Windows 8</br>-  Windows Server 2012|
|Alternative Routing-ID Interpretation (ARI)</br>See section 6.13.|-  Windows 8</br>-  Windows Server 2012|
|Message Signaled Interrupt (MSI/MSI-X) Support</br>See section 6.1.4.|-  Windows Vista</br>-  Windows Server 2008 R2|
|TLP Processing Hints (TPH)</br>See section 6.17.|-  Windows 8</br>-  Windows Server 2012|
|Single Root I/O Virtualization (SR-IOV)</br>See [Single Root I/O Virtualization (SR-IOV)](../network/single-root-i-o-virtualization--sr-iov-.md).|-  Windows 8</br>-  Windows Server 2012|

## In this section

- [PCI Power Management and Device Drivers](./pci-power-management-and-device-drivers.md)
- [Accessing PCI Device Configuration Space](./accessing-pci-device-configuration-space.md)
- [I/O Resource Usage Reduction](./i-o-resource-usage-reduction.md)
- [Order of Resources in Start-Device IRP](./order-of-resources-in-start-device-irp.md)
- [PCI Express FAQ for Graphics](./pci-express-faq-for-graphics.yml)
- [PCI Sample](./pci-sample.md)

## See Also

[Official PCIe specification](https://pcisig.com/specifications/review-zone)
