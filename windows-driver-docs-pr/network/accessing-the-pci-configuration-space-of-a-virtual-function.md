---
title: Accessing the PCI Configuration Space of a Virtual Function
description: Accessing the PCI Configuration Space of a Virtual Function
ms.assetid: 727E6FC5-F61F-4CB0-B6EB-9B372F2C59E1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing the PCI Configuration Space of a Virtual Function


This section describes guidelines for accessing the data from the PCI configuration space of PCI Express (PCIe) Virtual Functions (VFs). VFs are a hardware function of a network adapter that supports single root I/O virtualization (SR-IOV).

This section includes the following topics:

[Querying the PCI Configuration Data of a Virtual Function](overview-of-virtual-function-initialization-and-teardown.md)

[Setting the PCI Configuration Data of a Virtual Function](allocating-resources-for-a-virtual-function.md)

For more information on VFs for SR-IOV network adapters, see [SR-IOV Virtual Functions (VFs)](sr-iov-virtual-functions--vfs-.md).

**Note**  Only the PF miniport driver can configure the PCI configuration space for a VF. The VF miniport driver cannot directly access most of the SR-IOV adapter's hardware resources, such as the PCI configuration space. For more information, see [Writing SR-IOV VF Miniport Drivers](writing-sr-iov-vf-miniport-drivers.md).

 

 

 





