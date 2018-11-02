---
title: Managing Virtual Functions
description: Managing Virtual Functions
ms.assetid: 6B08B04D-C9A1-4159-9866-D179012191B2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Virtual Functions


This section describes the requirements and guidelines for managing the PCI Express (PCIe) Virtual Functions (VFs) on a network adapter that supports single root I/O virtualization (SR-IOV).

This section includes the following topics:

[Overview of Virtual Function Initialization and Teardown](overview-of-virtual-function-initialization-and-teardown.md)

[Allocating Resources for a Virtual Function](allocating-resources-for-a-virtual-function.md)

[Freeing Resources for a Virtual Function](freeing-resources-for-a-virtual-function.md)

[Enumerating Virtual Functions on a Network Adapter](enumerating-virtual-functions-on-a-network-adapter.md)

[Querying the Parameters of a Virtual Function](querying-the-parameters-of-a-virtual-function.md)

[Accessing the PCI Configuration Space of a Virtual Function](accessing-the-pci-configuration-space-of-a-virtual-function.md)

[Setting the Power State of a Virtual Function](setting-the-power-state-of-a-virtual-function.md)

[Resetting a Virtual Function](resetting-a-virtual-function.md)

For more information on VFs for SR-IOV network adapters, see [SR-IOV Virtual Functions (VFs)](sr-iov-virtual-functions--vfs-.md).

**Note**  Only the PF miniport driver can configure the network adapter's hardware resources, such as the VFs. The VF miniport driver cannot directly access most of the SR-IOV adapter's hardware resources. For more information, see [Writing SR-IOV VF Miniport Drivers](writing-sr-iov-vf-miniport-drivers.md).

 

 

 





