---
title: Specifying Bundle Membership
description: Specifying Bundle Membership
ms.assetid: aa73c7fd-a5c8-4ef5-99fd-229fbcc6b4df
keywords:
- add-registry-sections WDK networking , bundle membership
- bundle membership WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Bundle Membership




> [!NOTE]
> Bundle membership has been deprecated in Windows Vista and later. 


An INF file that installs **Net** components (physical or virtual network adapters) can specify that those network adapters belong to the same bundle of adapters. Note that NDIS intermediate drivers and filter drivers, which export virtual network adapters, are included in the Net class. An NDIS driver can use adapters that it installed to balance its workload by distributing the workload over the bundle of adapters. For more information about load balancing, see [Load Balancing and Failover](https://msdn.microsoft.com/library/windows/hardware/ff549197).

To specify that an adapter belongs to a particular bundle of adapters, the INF file for the driver that installs the adapter must contain the **BundleId** keyword and a case-insensitive string value (REG\_SZ). This string value identifies the driver's bundle of adapters. The registry is configured using the bundle-identifier information.

The following is an example of an *add-registry-section* in a driver's INF file that adds the **BundleId** subkey to the **Ndi\\params** key and gives the **ParamDesc** (parameter description) for **BundleId** a string value of "Bundle1".

```INF
[a1.params.reg]
HKR, Ndi\params\BundleId, ParamDesc, 0, "Bundle1"
```

 

 





