---
title: Physical sensor model
description: Physical sensor model
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
---

# Physical sensor model


The typical configuration in a system is to have one NFP provider that implements NFC. However, there can be multiple NFP providers on a given system, each supporting a different or the same NFP technologies. For example, a given tablet form-factor system may have multiple NFC antennas placed around its edges, and the back of the tablet could have an additional combined NFC/TransferJet touch-point used to connect to a wireless dock. In the physical modeling of NFP on this example system, these additional antennas are not individually addressable within a single provider. To provide individually-addressable touchpoints, the system maker would need to implement a specific NFP provider instance for each of the antennas and NFP technologies. When any device becomes proximate across one of these providers, the published messages are transmitted to all subscribers.

 

 
## Related topics
[Near field communications (NFC) API reference](/windows-hardware/drivers/ddi/_nfpdrivers/)
