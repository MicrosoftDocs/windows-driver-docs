---
title: Physical sensor model
description: Physical sensor model
ms.assetid: D3887E09-E0A4-4FBC-9D26-344016047235
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Physical sensor model


The typical configuration in a system is to have one NFP provider that implements NFC. However, there can be multiple NFP providers on a given system, each supporting a different or the same NFP technologies. For example, a given tablet form-factor system may have multiple NFC antennas placed around its edges, and the back of the tablet could have an additional combined NFC/TransferJet touch-point used to connect to a wireless dock. In the physical modeling of NFP on this example system, these additional antennas are not individually addressable within a single provider. To provide individually-addressable touchpoints, the system maker would need to implement a specific NFP provider instance for each of the antennas and NFP technologies. When any device becomes proximate across one of these providers, the published messages are transmitted to all subscribers.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

