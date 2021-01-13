---
title: One-to-One ID Mapping
description: One-to-One ID Mapping
keywords:
- mapping network component IDs
- ID mapping WDK netmap.inf
- one-to-one ID mapping WDK networking
- preupgrade IDs WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# One-to-One ID Mapping





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

An entry in an **Oem<em>Xxx</em>** section of a netmap.inf file that specifies one-to-one ID mapping has the following format:

*preupgrade-ID* = *postupgrade-ID*

For example:

```cpp
netservice=netservice_2000
```

A one-to-one ID mapping must be used for network protocols, services, and clients. Either one-to-one ID mapping or one-to-many ID mapping can be used for network adapters.

 

 





