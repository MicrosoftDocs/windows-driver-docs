---
title: MAC/PHY Reset
description: MAC/PHY Reset
ms.assetid: 91f6b669-16bd-452d-ad89-1b0c18c7a6ab
keywords:
- Native 802.11 miniport drivers WDK networking , reset operations
- miniport drivers WDK Native 802.11 , reset operations
- OID_DOT11_RESET_REQUEST
- MAC/PHY reset WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MAC/PHY Reset


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The media access control (MAC) and PHY layers on the 802.11 station can be reset through a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409). When the method request of this OID is made, the miniport driver invokes the following 802.11 MAC layer management entity (MLME) and PHY-layer management entity (PLME) service primitives:

-   MLME-RESET.request, as defined in Clause 6.3.10.2 of the IEEE 802.11-2012 standard. Through this primitive, the miniport driver resets the MAC sublayer.

-   PLME-RESET.request, as defined in Clause 6.5.2 of the IEEE 802.11-2012 standard. Through this primitive, the miniport driver resets the PHY layer.

The following topics describe the actions performed by the miniport driver when a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) is made:

-   [MAC/PHY Reset Request](mac-phy-reset-request.md)
-   [MAC/PHY Reset Operation](mac-phy-reset-operation.md)
-   [MAC/PHY Reset Confirmation](mac-phy-reset-confirmation.md)

 

 





