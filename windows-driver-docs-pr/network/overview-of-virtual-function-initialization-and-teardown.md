---
title: Overview of Virtual Function Initialization and Teardown
description: Overview of Virtual Function Initialization and Teardown
ms.assetid: 2684A93A-40C2-49DA-925D-2BAACA9F8CD9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Virtual Function Initialization and Teardown


This section provides an overview of the initialization and teardown sequence for PCI Express (PCIe) Virtual Functions (VFs). VFs are provided by a network adapter that supports single root I/O virtualization (SR-IOV).

This section includes the following topics:

[Virtual Function Initialization Sequence](virtual-function-initialization-sequence.md)

[Virtual Function Teardown Sequence](virtual-function-teardown-sequence.md)

For more information on VFs for SR-IOV network adapters, see [SR-IOV Virtual Functions (VFs)](sr-iov-virtual-functions--vfs-.md).

**Note**  Only the PF miniport driver can configure the network adapter's hardware resources, such as the VFs. The VF miniport driver cannot directly access most of the SR-IOV adapter's hardware resources. For more information, see [Writing SR-IOV VF Miniport Drivers](writing-sr-iov-vf-miniport-drivers.md).

 

 

 





