---
title: About Network Wake-Up Events
description: About Network Wake-Up Events
keywords:
- wake-up capabilities WDK networking , types
- NICs WDK networking , wake-up events
- network interface cards WDK networking , wake-up events
- Magic Packet WDK networking
- wake-up capabilities WDK networking , about wake-up capabilities
- network wake-up events WDK networking
- power management WDK NDIS miniport , wake-up capabilities
- wake-up frames WDK networking
ms.date: 04/20/2017
---

# About Network Wake-Up Events





A *network wake-up event* is an external event that causes a network adapter to wake the system. A network adapter wakes the system by asserting a bus-specific wake-up signal that eventually results in the system making a transition from a sleeping state to the working state.

NDIS defines the following two network wake-up events:

-   Receipt of a network wake-up frame that contains a pattern that was specified by a bound protocol driver.

-   Receipt of a Magic Packet.

A network adapter can support any combination of network wake-up events, including none at all. NDIS treats the miniport driver as not power management-aware if the miniport driver sets the **PowerManagementCapabilities** member of [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) to **NULL**.

Depending on the capabilities of the network adapter, a network wake-up event can occur from any device power state, including the highest-powered state (D0).

### Network Wake-Up Frames

If, during initialization, a miniport driver indicates that a network adapter can signal a wake-up on the receipt of a packet that contains a specified pattern, a bound protocol can enable the pattern-based wake up method on the network adapter and specify wake-up patterns. To enable this type of wake-up, a protocol driver sets the NDIS\_PNP\_WAKE\_UP\_PATTERN\_MATCH flag in [OID\_PNP\_ENABLE\_WAKE\_UP](./oid-pnp-enable-wake-up.md).

A protocol driver uses [OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](./oid-pnp-add-wake-up-pattern.md) to specify a wake-up pattern, along with a mask that indicates which bytes of an incoming packet should be compared with the pattern. A protocol driver can remove a wake-up pattern with [OID\_PNP\_REMOVE\_WAKE\_UP\_PATTERN](./oid-pnp-remove-wake-up-pattern.md).

For more information about network wake-up frames, see [Power Management for Network Devices](https://go.microsoft.com/fwlink/p/?linkid=9945).

### Magic-Packet Wake-Up

A *Magic Packet* is a packet that contains 16 contiguous copies of the receiving network adapter's MAC address.

This section includes:

[Enabling Wake-Up Events](enabling-wake-up-events.md)

[Handling Wake-Up Events](handling-wake-up-events.md)

 

