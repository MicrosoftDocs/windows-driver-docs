---
title: Physical sensor model
author: windows-driver-content
description: Physical sensor model
ms.assetid: D3887E09-E0A4-4FBC-9D26-344016047235
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
---

# Physical sensor model


The typical configuration in a system is to have one NFP provider that implements NFC. However, there can be multiple NFP providers on a given system, each supporting a different or the same NFP technologies. For example, a given tablet form-factor system may have multiple NFC antennas placed around its edges, and the back of the tablet could have an additional combined NFC/TransferJet touch-point used to connect to a wireless dock. In the physical modeling of NFP on this example system, these additional antennas are not individually addressable within a single provider. To provide individually-addressable touchpoints, the system maker would need to implement a specific NFP provider instance for each of the antennas and NFP technologies. When any device becomes proximate across one of these providers, the published messages are transmitted to all subscribers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Physical%20sensor%20model%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




