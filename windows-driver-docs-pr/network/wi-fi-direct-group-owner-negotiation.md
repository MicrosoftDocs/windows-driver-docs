---
title: Wi-Fi Direct Group Owner Negotiation
description: The figure below shows the typical OID/Indications and message sequences when performing Group Owner Negotiation between two PCs. This flow assumes that the information for Group Owner Negotiation is already available on the responding PC.
ms.assetid: 111F8D6F-DEA7-459E-8BAF-F67A6873A87F
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Wi-Fi Direct Group Owner Negotiation


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The figure below shows the typical OID/Indications and message sequences when performing Group Owner Negotiation between two PCs. This flow assumes that the information for Group Owner Negotiation is already available on the responding PC.

![sequence diagram showing typical oid/indications and message sequences when performing group owner negotiation between two pcs](images/wfd-group-owner-negotiation.png)

The miniport driver must follow the guidelines for Wi-Fi Direct Action Frames to support this exchange. The miniport driver is not required to maintain GO Negotiation state between the various packets. It can treat each Receive Request/Indication Status/Process Direct Oid/Send Response as a distinct action without attempting to correlate to previously exchanged packets.

**See Also**

[**DOT11\_WFD\_GO\_INTENT**](https://msdn.microsoft.com/library/windows/hardware/hh464150)

[OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451804)

[**NDIS\_STATUS\_DOT11\_WFD\_GO\_NEGOTIATION\_REQUEST\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh439774)

[**NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_GO\_NEGOTIATION\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh439789)

[OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_RESPONSE](https://msdn.microsoft.com/library/windows/hardware/hh451805)

[**NDIS\_STATUS\_DOT11\_WFD\_GO\_NEGOTIATION\_RESPONSE\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh439776)

[**NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_GO\_NEGOTIATION\_RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/hh439791)

[OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_CONFIRMATION](https://msdn.microsoft.com/library/windows/hardware/hh451803)

[**NDIS\_STATUS\_DOT11\_WFD\_GO\_NEGOTIATION\_CONFIRMATION\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh451706)

[**NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_GO\_NEGOTIATION\_CONFIRMATION**](https://msdn.microsoft.com/library/windows/hardware/hh439787)

 

 





