---
title: Introduction to NDIS Network Interfaces
description: Learn about NDIS network interfaces, which provide a consistent representation of the network interfaces that Microsoft Windows supports.
keywords:
- NDIS WDK , network interfaces
- NDIS network interfaces WDK
- network interfaces WDK
- NDISIF WDK networking
ms.date: 12/18/2024
---

# Introduction to NDIS network interfaces

To support the management information base (MIB), the Network Driver Interface Specification (NDIS) manages a collection of network interface information for the local computer. NDIS interface providers provide information about some network interfaces to NDIS. NDIS provides a proxy interface provider that registers interfaces and handles interface provider requests for miniport adapters and filter modules. Therefore, no NDIS drivers are required to be network interface providers.

However, all NDIS network driver types can register as interface providers. Such drivers register network interfaces and provide callback functions to respond to interface OID requests. NDIS interface providers typically provide information about interfaces that aren't directly accessible to NDIS and aren't supported by the NDIS proxy interface provider. For example, a MUX intermediate driver can have internal interfaces between its virtual miniports and underlying adapters.

## Related content

- [Overview of NDIS Network Interfaces](overview-of-ndis-network-interfaces.md)
- [Registering as an Interface Provider](registering-as-an-interface-provider.md)
- [Managing NDIS Network Interfaces](managing-ndis-network-interfaces.md)
- [Handling OID Query and Set Requests in an NDIS Interface Provider](handling-oid-query-and-set-requests-in-an-ndis-interface-provider.md)
- [Mapping of NDIS Network Interfaces to NDIS OIDs](mapping-of-ndis-network-interfaces-to-ndis-oids.md)
