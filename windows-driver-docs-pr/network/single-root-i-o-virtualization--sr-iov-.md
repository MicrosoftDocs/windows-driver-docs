---
title: Single Root I/O Virtualization (SR-IOV)
description: Single Root I/O Virtualization (SR-IOV)
ms.assetid: E64DD4F0-D5F8-4FFF-931B-C04C5C42D000
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Single Root I/O Virtualization (SR-IOV)


This section describes the NDIS single root I/O virtualization (SR-IOV) interface. Starting with NDIS 6.30, the SR-IOV interface supports Microsoft Hyper-V performance improvements for virtualized networks on Windows Server 2012 and later versions of Windows Server.

The SR-IOV specification from PCI-SIG defines the extensions to the PCI Express (PCIe) specification suite that enable multiple virtual machines (VMs) to share the same PCIe physical hardware resources. This section describes the NDIS SR-IOV interface and describes the techniques for writing an NDIS miniport driver for an SR-IOV capable network adapter that implements the PCIe SR-IOV specification.

This section includes the following topics:

[Overview of Single Root I/O Virtualization (SR-IOV)](overview-of-single-root-i-o-virtualization--sr-iov-.md)

[Writing SR-IOV PF Miniport Drivers](writing-sr-iov-pf-miniport-drivers.md)

[Writing SR-IOV VF Miniport Drivers](writing-sr-iov-vf-miniport-drivers.md)

[SR-IOV PF/VF Backchannel Communication](sr-iov-pf-vf-backchannel-communication.md)

[SR-IOV OIDs](sr-iov-oids.md)

For more information on SR-IOV, refer to the PCI-SIG [Single Root I/O Virtualization and Sharing 1.1](http://go.microsoft.com/fwlink/p/?linkid=221742) specification.

 

 





