---
title: Managing NIC Switches
description: Managing NIC Switches
ms.assetid: EE198C8D-427B-4013-8D19-5323332A4D87
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing NIC Switches


This section describes the requirements and guidelines for managing the NIC switch of a network adapter that supports single root I/O virtualization (SR-IOV). The miniport driver for the PCI Express (PCIe) Physical Function (PF) of the SR-IOV network adapter manages the NIC switch on the adapter.

This section includes the following topics:

[Creating a NIC Switch](creating-a-nic-switch.md)

[Deleting a NIC Switch](deleting-a-nic-switch.md)

[Enumerating NIC Switches on a Network Adapter](enumerating-nic-switches-on-a-network-adapter.md)

[Querying the Parameters of a NIC Switch](querying-the-parameters-of-a-nic-switch.md)

[Setting the Parameters of a NIC Switch](setting-the-parameters-of-a-nic-switch.md)

For more information on NIC switches for SR-IOV network adapters, see [NIC Switches](nic-switches.md).

**Note**  Only the PF miniport driver can configure the network adapter's hardware resources, such as the NIC switch. The miniport driver for a PCIe Virtual Function (VF) on the SR-IOV network adapter cannot directly access most of the adapter's hardware resources. For more information, see [Writing SR-IOV VF Miniport Drivers](writing-sr-iov-vf-miniport-drivers.md).

 

 

 





