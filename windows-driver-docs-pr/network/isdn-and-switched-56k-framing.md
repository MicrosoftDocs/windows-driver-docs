---
title: ISDN and Switched 56K Framing
description: ISDN and Switched 56K Framing
ms.assetid: e0532ded-c429-4f3a-b3c9-fd8ccc6b1b65
keywords:
- packet framing WDK WAN , ISDN framing
- ISDN framing WDK WAN
- packet framing WDK WAN , Switched 56K framing
- Switched 56K framing WDK WAN
- WAN packet framing WDK networking , ISDN framing
- WAN packet framing WDK networking , Switched 56K framing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ISDN and Switched 56K Framing





Initially, ISDN B channels (not D channels) should be used. Multiple B channel support is done through NDISWAN's multilink support. Initially, bit-synchronous HDLC framing with NRZ encoding should be used. Transparency should be provided by the driver or ISDN hardware. It is also the responsibility of the ISDN driver or hardware to provide for NRZ encoding, to calculate the FCS to add the PPP end flag (0x7E), and to insert any inter-frame time fill. Switched 56K drivers should frame in the same manner as ISDN.

 

 





