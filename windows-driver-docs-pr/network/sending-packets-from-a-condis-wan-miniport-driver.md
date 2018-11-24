---
title: Sending Packets from a CoNDIS WAN Miniport Driver
description: Sending Packets from a CoNDIS WAN Miniport Driver
ms.assetid: 66c42e90-e0d9-47d1-9e6d-cadb511bcb7a
keywords:
- CoNDIS WAN drivers WDK networking , packet sending
- loopbacks WDK networking
- software loopbacks WDK networking
- promiscuous-mode loopbacks WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending Packets from a CoNDIS WAN Miniport Driver





An upper-layer driver calls [**NdisCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561728) to send network data packets to an underlying CoNDIS WAN miniport driver in a list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures. The NDISWAN intermediate driver forwards those NET\_BUFFER\_LIST structures from the upper-layer driver. NDISWAN repackages the structures before sending them. NDISWAN forwards packets in new NET\_BUFFER\_LIST structures.

The NDISWAN intermediate driver calls NDIS to forward the new NET\_BUFFER\_LIST structures, NDIS calls the WAN miniport driver's [**MiniportCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff559365) function.

The CoNDIS WAN miniport driver owns both the NET\_BUFFER\_LIST structures and associated data until the send completes. The miniport driver must later call [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668) to complete the send request.

A completion call does not necessarily indicate that the network datahas been transmitted; however with the exception of intelligent NICs, the network data usually has been transmitted. A completion call does however, indicate that the miniport driver is ready to release ownership of the NET\_BUFFER\_LIST structures.

After the CoNDIS WAN miniport driver receives NET\_BUFFER\_LIST structure that contains a network data packet, it should send the packet out on an active virtual connection (VC).

A CoNDIS WAN miniport driver specifies the number of outstanding packets that it can have per VC in the **MaxSendWindow** member of the NDIS\_WAN\_CO\_INFO structure. The miniport driver provides this structure when the miniport driver responds to the [OID\_WAN\_CO\_GET\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569818) request from the protocol driver. However, the miniport driver can adjust this number dynamically and on a per-VC basis by using the **SendWindow** member in the [**WAN\_CO\_LINKPARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff565819) structure. The miniport driver passes this structure to the [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562) function. NDISWAN uses the current **SendWindow** value as its limit on outstanding sends. The miniport driver can set the value of the **SendWindow** member to zero to specify that it cannot handle any outstanding packets. That is, if the **SendWindow** member is set to zero, the send window is shut down and NDISWAN stops sending packets for the particular VC.

Packets that a WAN miniport driver sends contain simple HDLC PPP framing if PPP framing is set. For SLIP or RAS framing, packets contain only the data portion with no framing whatsoever. For more information about WAN packet framing, see [WAN Packet Framing](wan-packet-framing.md).

A WAN miniport driver must not attempt to provide software loopback or promiscuous-mode loopback. Both of these loopback types are fully supported by the NDISWAN driver.

 

 





