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
author: EliotSeattle
---

# PCI driver programming guide

The following table summarizes the PCIe features that are supported by different versions of Windows. For details, see the specified sections in the [official PCIe specification](http://pcisig.com/specifications/review-zone).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Feature</th>
<th>Minimum Windows version</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Resizable BAR capability</p>
<p>See section 7.22.</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Atomic Operations</p>
<p>See section 6.15.</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="odd">
<td><p>ACPI additions for FW latency optimizations</p>
<p>See <a href="https://go.microsoft.com/fwlink/p/?LinkId=787058" data-raw-source="[ACPI Additions for FW Latency Optimizations]( https://go.microsoft.com/fwlink/p/?LinkId=787058)">ACPI Additions for FW Latency Optimizations</a></p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>ATS/PRI</p>
<ul>
<li><a href="https://go.microsoft.com/fwlink/p/?LinkId=787061" data-raw-source="[ATS specification](https://go.microsoft.com/fwlink/p/?LinkId=787061)">ATS specification</a></li>
<li><a href="https://go.microsoft.com/fwlink/p/?LinkId=787060" data-raw-source="[Errata for the PCI Express&#174; Base Specification Revision 3.1, Single Root I/O Virtualization and Sharing Revision 1.1, Address Translation and Sharing Revision 1.1, and M.2 Specification Revision 1.0](https://go.microsoft.com/fwlink/p/?LinkId=787060)">Errata for the PCI Express® Base Specification Revision 3.1, Single Root I/O Virtualization and Sharing Revision 1.1, Address Translation and Sharing Revision 1.1, and M.2 Specification Revision 1.0</a></li>
</ul></td>
<td><p>Windows 10</p></td>
</tr><td><p>Optimized Buffer Flush/Fill (OBFF)</p>
<p>See section 6.19.</p></td>
<td><p>Windows 8</p>
<p>Windows Server 2012</p></td>
</tr>
<tr class="even">
<td><p>Latency Tolerance Reporting (LTR) Capability</p>
<p>See section 7.25.</p></td>
<td><p>Windows 8</p>
<p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td><p>Alternative Routing-ID Interpretation (ARI)</p>
<p>See section 6.13.</p></td>
<td><p>Windows 8</p>
<p>Windows Server 2012</p></td>
</tr>
<tr class="even">
<td><p>Message Signaled Interrupt (MSI/MSI-X) Support</p>
<p>See section 6.1.4.</p></td>
<td><p>Windows Vista</p>
<p>Windows Server 2008 R2</p></td>
</tr>
<tr class="odd">
<td><p>TLP Processing Hints (TPH)</p>
<p>See section 6.17.</p></td>
<td><p>Windows 8</p>
<p>Windows Server 2012</p></td>
</tr>
<tr class="even">
<td><p>Single Root I/O Virtualization (SR-IOV)</p>
<p>See <a href="https://docs.microsoft.com/windows-hardware/drivers/network/single-root-i-o-virtualization--sr-iov-" data-raw-source="[Single Root I/O Virtualization (SR-IOV)](https://docs.microsoft.com/windows-hardware/drivers/network/single-root-i-o-virtualization--sr-iov-)">Single Root I/O Virtualization (SR-IOV)</a>.</p></td>
<td><p>Windows 8</p>
<p>Windows Server 2012</p></td>
</tr>
</tbody>
</table>

## In this section

- [PCI Power Management and Device Drivers](https://docs.microsoft.com/windows-hardware/drivers/pci/pci-power-management-and-device-drivers)
- [Accessing PCI Device Configuration Space](https://docs.microsoft.com/windows-hardware/drivers/pci/accessing-pci-device-configuration-space)
- [I/O Resource Usage Reduction](https://docs.microsoft.com/windows-hardware/drivers/pci/i-o-resource-usage-reduction)
- [Order of Resources in Start-Device IRP](https://docs.microsoft.com/windows-hardware/drivers/pci/order-of-resources-in-start-device-irp)
- [PCI Express FAQ for Graphics](https://docs.microsoft.com/windows-hardware/drivers/pci/pci-express-faq-for-graphics)
- [PCI Sample](https://docs.microsoft.com/windows-hardware/drivers/pci/pci-sample)

## See Also

- [Official PCIe specification](http://pcisig.com/specifications/review-zone)
