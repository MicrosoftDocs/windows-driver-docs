---
title: INF Requirements for VF Miniport Drivers
description: INF Requirements for VF Miniport Drivers
ms.assetid: D15B337F-EC63-4E9A-94DA-E7F0487D5D48
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF Requirements for VF Miniport Drivers


The INF file for the miniport driver of a PCI Express (PCIe) Virtual Function (VF) does not specify any standardized INF keywords for single root I/O virtualization (SR-IOV). Only the INF file of a PCIe Physical Function (PF) specifies standardized SR-IOV keywords. For more information about these keywords, see [INF Requirements for PF Miniport Drivers](inf-requirements-for-pf-miniport-drivers.md).

The INF for a VF miniport driver follows (with one exception) the same requirements as other INF files for network adapters. For more information, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

The only exception is that the INF file for the VF miniport driver must define the binding relationships to the services that manage the SR-IOV data paths. This is needed to ensure that network access can fail over to the synthetic data path if the VF data path is torn down for any reason. For more information about these data paths, see [SR-IOV Data Paths](sr-iov-data-paths.md).

To bind to the services that manage these data paths, the INF file for the VF miniport driver must specify the following settings for the **UpperRange** and **LowerRange** entries:

``` syntax
HKR, Ndi\Interfaces, UpperRange, 0, "ndisvf"
HKR, Ndi\Interfaces, LowerRange, 0, "iovvf"
```

 

 





