---
title: WAN Packet Framing
description: WAN Packet Framing
ms.assetid: 11a6fbf5-c7a9-474b-811e-c77a36e834f3
keywords:
- WAN miniport drivers WDK networking , packets
- CoNDIS WAN drivers WDK networking , packets
- packet framing WDK WAN
- NDISWAN WDK networking
- WAN packet framing WDK networking
- packet framing WDK WAN , about WAN packet framing
- WAN packet framing WDK networking , about WAN packet framing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WAN Packet Framing





This section provides information about WAN packet framing.

The NDISWAN intermediate driver retrieves information about the WAN packet framing performed by a WAN miniport driver from the miniport driver's response to the [OID\_WAN\_MEDIUM\_SUBTYPE](https://msdn.microsoft.com/library/windows/hardware/ff561216) query information request.

NDISWAN converts an out-going packet from LAN to PPP format. NDISWAN uses simple HDLC framing. Most of the media-specific framing must be done by the miniport driver.

Before sending packets to the WAN miniport driver's send function, NDISWAN does simple PPP HDLC framing. Simple PPP HDLC framing is PPP's HDLC framing without the FCS, bit or byte stuffing, and any beginning or end flags.

The following topics provide additional information about WAN packet framing:

[Asynchronous Framing](asynchronous-framing.md)

[ISDN and Switched-56K Framing](isdn-and-switched-56k-framing.md)

 

 





