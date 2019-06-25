---
title: NDIS network interface OIDs
description: This section describes network interface OIDs for all NDIS drivers
keywords: ["NDIS network interface OIDs", "WDK NDIS network interface OIDs", "WDK network interface OIDs"]
ms.assetid: A66B5AC6-9EAF-4234-8614-0EBF179B3DDE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS network interface OIDs

NDIS network interface object identifiers (OIDs) provide information about network interfaces to support the MIB ([RFC 2863](overview-of-ndis-network-interfaces.md)).

NDIS interface providers must support these OIDs. Drivers that are not registered interface providers should not support the OIDs in this section.

NDIS calls the [ProviderQueryObject](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-if_query_object) function to make a query request for information from the interface provider. The *ObjectId* parameter of this function contains the object identifier. The interface provider registered *ProviderQueryObject* when it called the [NdisIfRegisterProvider](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisifregisterprovider) function to register as an interface provider.

The handle at the *ProviderIfContext* parameter of the *ProviderQueryObject* function identifies the network interface. This handle was provided to NDIS when the interface provider called the [NdisIfRegisterInterface](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisifregisterinterface) function to register the interface. The *pOutputBuffer* parameter of the *ProviderQueryObject* function contains the result of the OID request.

For more information about NDIS network interface OIDs, see [NDIS 6.0 Network Interfaces](ndis-network-interfaces2.md).

This section describes the following NDIS network interface OIDs:

- [OID_GEN_ALIAS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-alias) 
- [OID_GEN_ADMIN_STATUS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-admin-status) 
- [OID_GEN_OPERATIONAL_STATUS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-operational-status) 
- [OID_GEN_PROMISCUOUS_MODE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-promiscuous-mode) 
- [OID_GEN_XMIT_LINK_SPEED](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-xmit-link-speed) 
- [OID_GEN_RCV_LINK_SPEED](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-link-speed) 
- [OID_GEN_UNKNOWN_PROTOS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-unknown-protos) 
- [OID_GEN_DISCONTINUITY_TIME](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-discontinuity-time) 
- [OID_GEN_LAST_CHANGE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-last-change) 
- [OID_GEN_INTERFACE_INFO](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-interface-info) 
- [OID_GEN_MEDIA_CONNECT_STATUS_EX](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-media-connect-status-ex) 
- [OID_GEN_LINK_SPEED_EX](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-link-speed-ex) 
- [OID_GEN_MEDIA_DUPLEX_STATE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-media-duplex-state) 
- [OID_TUNNEL_INTERFACE_RELEASE_OID](https://docs.microsoft.com/windows-hardware/drivers/network/oid-tunnel-interface-release-oid) 
- [OID_TUNNEL_INTERFACE_SET_OID](https://docs.microsoft.com/windows-hardware/drivers/network/oid-tunnel-interface-set-oid) 


