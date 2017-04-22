---
title: INF DDInstall.HW Section for PF Miniport Drivers
description: INF DDInstall.HW Section for PF Miniport Drivers
ms.assetid: 65399462-4AF1-401C-87CB-BF387CA0B053
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF DDInstall.HW Section for PF Miniport Drivers


INF *DDInstall***.HW** sections are typically used for setting up any device-specific information in the registry, whether with explicit **AddReg** directives or with **Include** and **Needs** entries.

The INF file for the miniport driver of the PCI Express (PCIe) Physical Function (PF) network adapter must have a *DDInstall***.HW** section that contains the following INF entries:

-   An **Include** entry that specifies the pci.inf file that is included with the Windows operating system.

-   A **Needs** entry that specifies the **PciSriovSupported.HW** section to include from the pci.inf file. This section defines standard INF settings that apply to all PF miniport drivers for network adapters that support the single root I/O virtualization (SR-IOV) interface.

The following is an example of a *DDInstall***.HW** section for a PF miniport driver:

``` syntax
[Device_Inst.NT.HW]

Include=pci.inf
Needs=PciSriovSupported.HW
```

For more information about the *DDInstall* section, see [DDInstall Section in a Network INF File](ddinstall-section-in-a-network-inf-file.md).

For more information about the *DDInstall*.HW section, see [**INF DDInstall.HW Section**](https://msdn.microsoft.com/library/windows/hardware/ff547330).

 

 





