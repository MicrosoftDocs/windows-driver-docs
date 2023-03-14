---
title: Managing NDIS Network Interfaces
description: Managing NDIS Network Interfaces
keywords:
- NDIS network interfaces WDK , managing
- network interfaces WDK , managing
ms.date: 03/02/2023
---

# Managing NDIS Network Interfaces





NDIS network interface providers register network interfaces with NDIS. Before registering an interface, an interface provider obtains a [**NET\_LUID**](/windows/win32/api/ifdef/ns-ifdef-net_luid_lh) value for that interface. NDIS assigns an interface index ( *IfIndex* in RFC 2863) to an interface when it is registered.

NDIS also provides services that drivers can use to manage entries in the interface stack table (*ifStackTable* in RFC 2863).

This section includes:

[NET\_LUID Value](net-luid-value.md)

[Using a NET\_LUID Index](using-a-net-luid-index.md)

[Registering a Network Interface](registering-a-network-interface.md)

[Deregistering a Network Interface](deregistering-a-network-interface.md)

[Mapping a NET\_LUID Value to an Interface Index](mapping-a-net-luid-value-to-an-interface-index.md)

[NET\_LUID Values for Miniport Adapters and Filter Modules](net-luid-values-for-miniport-adapters-and-filter-modules.md)

[Maintaining a Network Interface Stack](maintaining-a-network-interface-stack.md)

 

