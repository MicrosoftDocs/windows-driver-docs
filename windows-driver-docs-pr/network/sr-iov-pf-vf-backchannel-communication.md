---
title: SR-IOV PF/VF Backchannel Communication
description: SR-IOV PF/VF Backchannel Communication
ms.assetid: 66D40452-1286-449E-BD6B-AFAD466E03A1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SR-IOV PF/VF Backchannel Communication


The single root I/O virtualization (SR-IOV) interface provides a communication channel, or *backchannel*, between the miniport drivers of a PCI Express (PCIe) Virtual Function (VF) and the PCIe Physical Function (PF). Each VF miniport driver can issue requests over the backchannel to the PF miniport driver. The PF miniport driver can issue status notifications over the backchannel to individual VF miniport drivers.

Data exchanged between the PF and VF miniport drivers over the backchannel interface involves the use of a *VF configuration block*. Each VF configuration block is similar in concept to an interprocess communication (IPC) message, in which each block has a proprietary format, length, and block identifier. The independent hardware vendor (IHV) can define one or more VF configuration blocks for the PF and VF miniport drivers.

This section includes the following topics:

[Backchannel Communication from a VF Miniport Driver](backchannel-communication-from-a-vf-miniport-driver.md)

[Backchannel Communication from the PF Miniport Driver](backchannel-communication-from-the-pf-miniport-driver.md)

 

 





