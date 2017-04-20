---
title: Other Benefits of CoNDIS WAN
description: Other Benefits of CoNDIS WAN
ms.assetid: 5b937ae4-1486-4563-a863-5c02ba57c7df
keywords:
- CoNDIS WAN drivers WDK networking , benefits
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Other Benefits of CoNDIS WAN


## <a href="" id="ddk-other-benefits-of-condis-wan-ng"></a>


In addition to flexibility and simplicity, the CoNDIS WAN model provides the following benefits:

-   CoNDIS WAN miniport drivers support multipacket [send and receive operations](sending-and-receiving-data.md).

-   When a CoNDIS miniport driver indicates a receive packet, a bound protocol can defer processing of the packet. When an NDIS WAN miniport driver indicates a receive packet, a bound protocol must copy the data immediately.

-   CoNDIS WAN supports multipoint calls. For more information about making multipoint calls, see [Making a Call](making-a-call.md).

-   CoNDIS WAN supports quality of service (QoS). CoNDIS WAN drivers use the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure. For more information about CoNDIS QoS, see [Client-Initiated Request to Change Call Parameters](client-initiated-request-to-change-call-parameters.md).

-   Only CoNDIS WAN will support future NDIS enhancements that apply to WAN drivers.

 

 





