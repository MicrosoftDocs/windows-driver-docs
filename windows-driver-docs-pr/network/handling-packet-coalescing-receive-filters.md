---
title: Handling Packet Coalescing Receive Filters
description: Handling Packet Coalescing Receive Filters
ms.assetid: 83FF780F-6B8F-4222-90F0-42037FFF7653
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Packet Coalescing Receive Filters


Multiple receive filters are downloaded to a miniport driver through OID method requests of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795). Each filter can specify one or more tests (*header field tests*) that the network adapter uses to determine whether a received packet should be coalesced in a hardware coalescing buffer on the adapter.

Before the miniport driver configures the network adapter with the receive filters, the driver should optimize the receive filters based on the hardware capabilities of the adapter. For example, all receive filters require a header field test for the MAC header. Therefore, the driver could optimize filter rules based on the results of this test. This allows the adapter to determine which Open Systems Interconnection (OSI) layer 3 (L3) and layer 4 (L4) header field tests to perform next.

As soon as the network adapter has been configured with receive filters, it must do the following:

-   All the header field test parameters for a particular filter must match on the received packet in order to coalesce the packet in the coalescing buffer.

    The network adapter combines the results from all header field tests of a receive filter with a logical AND operation. That is, if any header field test that is included in the array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures for a receive filter fails, the received packet does not meet the specified filter criterion and must not be coalesced.

-   The network adapter only inspects packet data based on the specified header field test parameters. The adapter must ignore all header fields in the packet for which header field tests are not specified.

-   If a received packet matches all the header field tests for any of the receive filters, the network adapter must coalesce the packet within the hardware coalescing buffer. As soon as the first packet is coalesced, the network adapter must start a hardware timer and must set the expiration time to the value of the **MaxCoalescingDelay** member of the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure for the matching receive filter.

-   As more packets are received that match a packet coalescing receive filter, the network adapter puts them into the coalescing buffer.

    If the hardware timer is already running, the adapter must not stop or restart the timer for the matching receive filter. However, the adapter can configure the hardware timer with the smallest expiration value from matching receive filters. For example, when the driver receives a packet that matches receive filter *X*, the adapter starts the timer with the specified expiration value for that receive filter. If the adapter then receives a packet that matches receive filter *Y*, the adapter can reconfigure the hardware timer with the specified expiration value for that receive filter.

    **Note**  The network adapter must not reconfigure the hardware timer if the time that is remaining on the timer is less than a receive filter's expiration time.

     

-   As soon as received packets are coalesced, the network adapter generates an interrupt if any of the following events occur:

    -   If the available space within the hardware coalescing buffer reaches a hardware-specific low-water mark, the network adapter must generate a receive interrupt so that the miniport driver can process the coalesced receive packets.

    -   If the hardware timer used for the hardware coalescing buffer expires, the network adapter must generate a receive interrupt so that the miniport driver can process the coalesced receive packets.

    -   If a receive filter is cleared and packets have been coalesced that match that filter, the network adapter must generate a receive interrupt so that the miniport driver can process the coalesced receive packets.

    -   If a received packet does not match any of the receive filters, the network adapter must generate a receive interrupt so that the miniport driver can process the received packet. If any packets have been coalesced, the miniport driver must also process those packets.

    -   If the network adapter generates an interrupt for any other interrupt status other than a receive interrupt, the network adapter must also signal a receive interrupt status so that the miniport driver can process the coalesced received packets.

    As soon as the interrupt is generated, the network adapter must stop the hardware timer if it hasn't expired and must clear the hardware coalescing buffer.

The miniport driver must maintain a coalesced packet counter, which contains a value for the number of received packets that have matched a packet coalescing filter. NDIS queries this counter through an OID query request of [OID\_PACKET\_COALESCING\_FILTER\_MATCH\_COUNT](https://msdn.microsoft.com/library/windows/hardware/hh451826).

The network adapter only performs packet coalescing while the hardware is operating in a full-power state. While the hardware is in a low-power state, the adapter must only filter received packets based on wake-up patterns that have been offloaded to the adapter through OID set requests of [OID\_PNP\_ENABLE\_WAKE\_UP](https://msdn.microsoft.com/library/windows/hardware/ff569775).

When the network adapter transitions to a full-power state, the miniport driver must follow these steps:

-   The miniport driver must configure the network adapter to discard any coalesced packets within the hardware coalescing buffer. The network adapter may have coalesced these packets when it was transitioned to a low-power state.

-   The miniport driver must configure the network adapter with the set of packet coalescing receive filters that were downloaded to the driver before the low-power transition.

-   The miniport driver must clear the coalesced packet counter.

 

 





