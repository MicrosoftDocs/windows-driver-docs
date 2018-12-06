---
title: PCI Express FAQ for Graphics
description: This paper provides information about PCI Express Graphics for Microsoft Windows operating systems, and answers frequently asked questions.
ms.assetid: 30FC1CF9-B642-4E00-869C-63009BA3F128
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PCI Express FAQ for Graphics


**Last updated:**

-   June 30, 2004
-   Archived paper. No warranty is made as to technical accuracy of content of currency of URLs.

**Applies to:**

-   Microsoft Windows Vista
-   Microsoft Windows Server 2003
-   Microsoft Windows XP
-   Microsoft Windows 2000

This paper provides information about PCI Express Graphics for Microsoft Windows operating systems, and answers frequently asked questions.

**PCI Express**

PCI Express (PCIe) is an I/O bus technology that was designed to replace Peripheral Component Interconnect (PCI), PCI-X, and Accelerated Graphics Port (AGP). By providing advanced features and increased bandwidth, PCIe addresses many of the shortcomings of PCI, PCI-X, and AGP. PCIe retains full software compatibility with PCI Local Bus Specification 2.3, and it replaces the parallel multidrop bus architecture of PCI and PCI-X with a serial, point-to-point connection bus architecture.

Two PCIe devices are connected by a link, and each link is made up of one or more lanes. Each lane consists of two low-voltage, differential signal pairs carrying 2.5 Gbps of traffic in opposite directions. One pair is used for transmitting, and the other pair is used for receiving. To further increase the bandwidth of a link, multiple lanes can be placed in parallel (x1, x2, x4, x8, x12, x16, or x32 lanes) between two PCIe devices to aggregate the bandwidth of each individual lane.

PCIe hardware is backwards compatible with PCI software on the Microsoft Windows 2000 and Microsoft Windows XP operating systems. Advanced PCIe features are natively supported only in Windows Vista and later versions of Windows.

**Definitions**

-   XPDM: The Windows XP Display Driver Model.

-   WDDM: The Windows Vista Display Driver Model. WDDM is a significant evolution of the graphics driver infrastructure and is backwards compatible with XPDM drivers.

-   GART: Graphics address relocation table, hardware that presents the display adapter with a linearized view of nonlinear memory.

-   DCT: Display compatibility tests. Video drivers need to pass these tests in order to comply with the Windows Certification Program and be digitally signed by Microsoft.

-   WHQL: Windows Hardware Quality Laboratories. The organization within Microsoft that is responsible for the Windows Certification Program for hardware.

 

**PCI Express Graphics**

It is well known that graphics can always use more bandwidth than what is available. Graphics data transfers cause maximum traffic on the PCI bus. The continual increase in graphics demand and complexity eventually made the PCI bus insufficient, which led to the invention of AGP. Now we are pushing the limits of what AGP can deliver, and we need a better solution. PCIe surpasses AGP in bandwidth availability, with more room for expansion in the near future. By increasing the number of lanes in a link, graphics adapters can take advantage of increased bandwidth and faster data transfer. For example, a graphics adapter that uses an X16 link has bandwidth of 4 Gbps in each direction.

Given the higher bandwidth offered by PCIe, systems are already moving away from AGP to PCIe. Typically, a system does not provide both AGP and PCIe connectors.

**PCI Express Graphics in Vista**

The Windows Vista Display Driver Model (WDDM) has specific requirements for PCIe graphics adapters, for example that the 64-bit addressing mode be supported by the GPU. However, a minimum of 40 bits of physical address bits must be implemented. The unimplemented bits should be forced to zero. These requirements are not applicable to the Windows XP display driver model.

**PCIe Graphics & AGP**

In addition to the bandwidth considerations mentioned above, there are several other differences between AGP and PCIe.

By definition, AGP requires a chipset with a graphics address relocation table (GART), which provides a linear view of nonlinear system memory to the graphics device. PCIe, however, requires that the memory linearization hardware exist on the graphics device itself instead of on the chipset. Consequently, driver support for memory linearization in PCIe must exist in the video driver, instead of as an AGP-style separate GART miniport driver. Graphics hardware vendors who want to use nonlocal video memory in their Windows XP driver model (XPDM) drivers must implement both memory linearization hardware and the corresponding software. All PCIe graphics adapters that are compatible with the WDDM must support memory linearization in hardware and software.

AGP was dedicated to graphics adapters, and no other device class used it. PCIe is intended to be used by all device classes that previously used PCI. With AGP, a number of video drivers were directly programming the chipset, which gave rise to severe ill effects such as crashing and memory corruption in the graphics stack. Because PCIe will be used for all devices in the system, it is even more important that video drivers not program the chipset directly.

 

**Frequently Asked Questions**

**Will a PCIe video card work on Windows XP?**

Yes. PCIe is software compatible with PCI. PCIe hardware works on operating systems that support PCI.

**Does PCIe graphics coexist with AGP?**

Some chipsets support both AGP and X16 PCIe. Some motherboards have both AGP and X16 PCIe slots using such a chipset.

**Will multimonitor configurations work on PCIe graphics?**

Multimonitor configurations of PCIe are expected to work just like PCI. Whether they do will depend on the motherboard manufacturers. For example, x16, x8, and x8 triple monitor configuration will necessitate the existence of one x16 and two x8 slots on the motherboard.

**What are the performance implications of using PCIe Graphics?**

High-speed PCIe graphics solutions have better performance than AGP. Typically, PCIe graphics cards use the x16 PCIe slot. This translates into a bandwidth of 4 Gbps. This is already a twofold increase over AGP 8X. In this case, "x1" means that the slot has one PCIe lane, which will give it a bandwidth of 264 Mbps. This is equal to the bandwidth provided by AGP 1X and twice that of PCI (132 Mbps).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>PCIe version</strong></td>
<td><strong>AGP</strong></td>
<td><strong>Bandwidth</strong></td>
</tr>
<tr class="even">
<td><p>PCIe x1</p></td>
<td><p>AGP 1X</p></td>
<td><p>264 Mbps</p></td>
</tr>
<tr class="odd">
<td><p>PCIe x4</p></td>
<td><p>AGP 4X</p></td>
<td><p>1 Gbps</p></td>
</tr>
<tr class="even">
<td><p>PCIe x8</p></td>
<td><p>AGP 8X</p></td>
<td><p>2 Gbps</p></td>
</tr>
<tr class="odd">
<td><p>PCIe x16</p></td>
<td><p>2 x AGP 8X</p></td>
<td><p>4 Gbps</p></td>
</tr>
</tbody>
</table>

 

Additionally, the AGP specification does not support "snooping." It implies that memory used by devices needs to be mapped uncached or write combined by the processor in order to prevent the processor from caching that memory, or else an expensive cache flush needs to be done between handoff of a surface between CPU and GPU. Thus, processor read access to that memory will be very slow.

PCIe will support snooping. It will now be possible to map such shared memory as cacheable and still be able to maintain coherency between the CPU and the GPU. Snooped transactions are slower than nonsnooped transactions, but since the CPU can read the shared memory at full speed and we do not need to flush any caches, the tradeoff might mean better performance in some scenarios.

**Is an n-lane PCIe slot compatible with a p-lane PCIe graphics card, where p &gt; n? Where n &gt; p?**

You cannot plug an x16 graphics card into an x8 slot. You can however, if you wish, plug an x8 card PCIe card into an x16 slot. A p-lane PCIe card will work at some speed in an n-lane PCIe slot, where n &gt; p. This is not true if n &lt; p.

## Related topics
[PCI-SIG](http://www.pcisig.com)  



