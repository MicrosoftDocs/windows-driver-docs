---
title: NDIS network interface OIDs
description: This section describes network interface OIDs for all NDIS drivers
keywords: ["NDIS network interface OIDs", "WDK NDIS network interface OIDs", "WDK network interface OIDs"]
ms.date: 03/02/2023
---

# NDIS network interface OIDs

NDIS network interface object identifiers (OIDs) provide information about network interfaces to support the MIB ([RFC 2863](overview-of-ndis-network-interfaces.md)).

NDIS interface providers must support these OIDs. Drivers that are not registered interface providers should not support the OIDs in this section.

NDIS calls the [ProviderQueryObject](/windows-hardware/drivers/ddi/ndis/nc-ndis-if_query_object) function to make a query request for information from the interface provider. The *ObjectId* parameter of this function contains the object identifier. The interface provider registered *ProviderQueryObject* when it called the [NdisIfRegisterProvider](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifregisterprovider) function to register as an interface provider.

The handle at the *ProviderIfContext* parameter of the *ProviderQueryObject* function identifies the network interface. This handle was provided to NDIS when the interface provider called the [NdisIfRegisterInterface](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifregisterinterface) function to register the interface. The *pOutputBuffer* parameter of the *ProviderQueryObject* function contains the result of the OID request.

For more information about NDIS network interface OIDs, see [NDIS 6.0 Network Interfaces](ndis-network-interfaces2.md).

This section describes the following NDIS network interface OIDs:

- [OID_GEN_ALIAS](./oid-gen-alias.md) 
- [OID_GEN_ADMIN_STATUS](./oid-gen-admin-status.md) 
- [OID_GEN_OPERATIONAL_STATUS](./oid-gen-operational-status.md) 
- [OID_GEN_PROMISCUOUS_MODE](./oid-gen-promiscuous-mode.md) 
- [OID_GEN_XMIT_LINK_SPEED](./oid-gen-xmit-link-speed.md) 
- [OID_GEN_RCV_LINK_SPEED](./oid-gen-rcv-link-speed.md) 
- [OID_GEN_UNKNOWN_PROTOS](./oid-gen-unknown-protos.md) 
- [OID_GEN_DISCONTINUITY_TIME](./oid-gen-discontinuity-time.md) 
- [OID_GEN_LAST_CHANGE](./oid-gen-last-change.md) 
- [OID_GEN_INTERFACE_INFO](./oid-gen-interface-info.md) 
- [OID_GEN_MEDIA_CONNECT_STATUS_EX](./oid-gen-media-connect-status-ex.md) 
- [OID_GEN_LINK_SPEED_EX](./oid-gen-link-speed-ex.md) 
- [OID_GEN_MEDIA_DUPLEX_STATE](./oid-gen-media-duplex-state.md) 
- [OID_TUNNEL_INTERFACE_RELEASE_OID](./oid-tunnel-interface-release-oid.md) 
- [OID_TUNNEL_INTERFACE_SET_OID](./oid-tunnel-interface-set-oid.md)
