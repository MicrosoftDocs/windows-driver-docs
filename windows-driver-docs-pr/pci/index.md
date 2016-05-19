---
title: PCI driver programming guide
description: PCI driver programming guide
MS-HAID:
- 'pcidg\_b844ab1f-d0d6-4f3a-ac41-d6c7abefffa6.xml'
- 'PCI.pci\_bus\_design\_guide'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 014f6243-6166-42e1-9f0f-1a438c77fd78
keywords: ["PCI WDK buses", "buses WDK , PCI", "Peripheral Component Interconnect WDK buses", "PCI Local Bus specification WDK", "configuration space WDK PCI", "device-specific configuration space WDK PCI", "requesting configuration space information WDK PCI", "power management WDK PCI", "querying power management capability data", "headers WDK PCI"]
---

# PCI driver programming guide


## Supported PCIe features in Windows


The following table summarizes the PCIe features that are supported by different versions of Windows. For details, see the specified sections in the [official PCIe specification](http://www.pcisig.com/specifications/pciexpress/review_zone/).

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
<p>See [ACPI Additions for FW Latency Optimizations]( http://go.microsoft.com/fwlink/p/?LinkId=787058)</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>ATS/PRI</p>
<ul>
<li>[ATS specification](http://go.microsoft.com/fwlink/p/?LinkId=787061)</li>
<li>[Errata for the PCI Express® Base Specification Revision 3.1, Single Root I/O Virtualization and Sharing Revision 1.1, Address Translation and Sharing Revision 1.1, and M.2 Specification Revision 1.0](http://go.microsoft.com/fwlink/p/?LinkId=787060)</li>
</ul></td>
<td><p>Windows 10</p></td>
</tr>
</tbody>
</table>

 

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
<td><p>Optimized Buffer Flush/Fill (OBFF)</p>
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
<p>See [Single Root I/O Virtualization (SR-IOV)](https://msdn.microsoft.com/library/windows/hardware/hh440235).</p></td>
<td><p>Windows 8</p>
<p>Windows Server 2012</p></td>
</tr>
</tbody>
</table>

 

## <a href="" id="ddk-pci-design-guide-kg"></a>


## In this section


-   [PCI Power Management and Device Drivers](https://msdn.microsoft.com/library/windows/hardware/dn607302)
-   [Accessing PCI Device Configuration Space](https://msdn.microsoft.com/library/windows/hardware/ff536890)
-   [I/O Resource Usage Reduction](https://msdn.microsoft.com/library/windows/hardware/ff537424)
-   [Order of Resources in Start-Device IRP](https://msdn.microsoft.com/library/windows/hardware/ff537445)
-   [PCI Express FAQ for Graphics](https://msdn.microsoft.com/library/windows/hardware/dn653979)
-   [PCI Sample](https://msdn.microsoft.com/library/windows/hardware/hh450892)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpci\buses%5D:%20PCI%20driver%20programming%20guide%20%20RELEASE:%20%285/19/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




