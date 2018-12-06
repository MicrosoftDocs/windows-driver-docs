---
title: Serialized NDIS Miniport Drivers
description: Serialized NDIS Miniport Drivers
ms.assetid: 6b9b94ad-5d5d-465a-90bc-47095f6e2b9c
keywords:
- miniport drivers WDK networking , types
- NDIS miniport drivers WDK , types
- serialized NDIS miniport drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Serialized NDIS Miniport Drivers





Serialized NDIS miniport drivers are obsolete for Windows Vista and later versions. Serialized miniport drivers are not supported for NDIS 6.0 drivers. Windows Vista supports serialized miniport drivers only for NDIS 5.1 and earlier drivers. Unlike deserialized miniport drivers, a serialized miniport driver relies on NDIS to serialize the operation of its own *MiniportXxx* functions and to manage the queue for sending network data packets.

If you are writing a new miniport driver, you should write a [deserialized driver](deserialized-ndis-miniport-drivers.md). If possible, you should also port older drivers to NDIS 6.0 or later. For more information about porting drivers to NDIS 6.0, see [Porting NDIS 5.x Drivers to NDIS 6.0](porting-ndis-5-x-drivers-to-ndis-6-0.md).

 

 





