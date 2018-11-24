---
title: Media Extensibility in NDIS 6.20
description: Media Extensibility in NDIS 6.20
ms.assetid: abc240da-be6e-4a7a-a9d1-186633c5bfd3
keywords:
- NDIS 6.20 WDK , media extensibility
- media extensibility WDK NDIS 6.20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Media Extensibility in NDIS 6.20





NDIS 6.20 introduces additional media extensibility features. That is, the network layer of the driver stack is more media independent.

These features in NDIS 6.20 and later reduce the complexity of the code that is required to implement drivers that do not implement IEEE 802.3. In addition, these non-IEEE 802.3 implementations do not have to implement ARP and DHCP.

NDIS 6.20 and later provide *raw IP* frame support with a new media type for raw IP (NdisMediumIP). For example, NDIS WWAN support uses raw IP.

NDIS 6.20 introduces enhanced support for media specific out of band (OOB) data. The media specific information has a tag that Microsoft assigns. NDIS 6.20 and later support multiple media specific information tags.

For more information about media specific information, for more information about media extensibility, see [OID\_GEN\_PHYSICAL\_MEDIUM\_EX](https://msdn.microsoft.com/library/windows/hardware/ff569622) and [**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff566518).

 

 





