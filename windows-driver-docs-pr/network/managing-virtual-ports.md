---
title: Managing Virtual Ports
description: Managing Virtual Ports
ms.assetid: BF3DFE01-6583-4FBB-AFFA-2C017A3D9A05
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Virtual Ports


This section describes the requirements and guidelines for managing the virtual ports (VPorts) on a NIC switch. This switch is provided by a network adapter that supports single root I/O virtualization (SR-IOV).

This section includes the following topics:

[Creating a Virtual Port](creating-a-virtual-port.md)

[Deleting a Virtual Port](deleting-a-virtual-port.md)

[Enumerating Virtual Ports on a Network Adapter](enumerating-virtual-ports-on-a-network-adapter.md)

[Querying the Parameters of a Virtual Port](querying-the-parameters-of-a-virtual-port.md)

[Setting the Parameters of a Virtual Port](setting-the-parameters-of-a-virtual-port.md)

[Managing the Receive Filters for a Virtual Port](managing-receive-filters-for-a-virtual-port.md)

[Symmetric and Asymmetric Assignment of Queue Pairs](symmetric-and-asymmetric-assignment-of-queue-pairs.md)

[Packet Flow over a Virtual Port](packet-flow-over-a-virtual-port.md)

[Nondefault Virtual Ports and VMQ](nondefault-virtual-ports-and-vmq.md)

For more information on VPorts, see [Virtual Ports (VPorts)](virtual-ports--vports-.md).

For more information on NIC switches, see [NIC Switches](nic-switches.md).

**Note**  Only the miniport driver for the PCI Express (PCIe) Physical Function (PF) can configure the network adapter's hardware resources, such as the VPorts. The miniport driver for the PCIe Virtual Function (VF) cannot directly access most of the SR-IOV adapter's hardware resources. For more information, see [Writing SR-IOV VF Miniport Drivers](writing-sr-iov-vf-miniport-drivers.md).

 

 

 





