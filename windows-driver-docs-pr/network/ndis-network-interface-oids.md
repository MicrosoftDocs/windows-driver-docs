---
title: NDIS network interface OIDs
description: This section describes network interface OIDs for all NDIS drivers
keywords: ["NDIS network interface OIDs", "WDK NDIS network interface OIDs", "WDK network interface OIDs"]
ms.assetid: A66B5AC6-9EAF-4234-8614-0EBF179B3DDE
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# NDIS network interface OIDs

NDIS network interface object identifiers (OIDs) provide information about network interfaces to support the MIB ([RFC 2863](overview-of-ndis-network-interfaces.md)).

NDIS interface providers must support these OIDs. Drivers that are not registered interface providers should not support the OIDs in this section.

NDIS calls the [ProviderQueryObject](https://msdn.microsoft.com/library/windows/hardware/ff570399) function to make a query request for information from the interface provider. The *ObjectId* parameter of this function contains the object identifier. The interface provider registered *ProviderQueryObject* when it called the [NdisIfRegisterProvider](https://msdn.microsoft.com/library/windows/hardware/ff562716) function to register as an interface provider.

The handle at the *ProviderIfContext* parameter of the *ProviderQueryObject* function identifies the network interface. This handle was provided to NDIS when the interface provider called the [NdisIfRegisterInterface](https://msdn.microsoft.com/library/windows/hardware/ff562715) function to register the interface. The *pOutputBuffer* parameter of the *ProviderQueryObject* function contains the result of the OID request.

For more information about NDIS network interface OIDs, see [NDIS 6.0 Network Interfaces](ndis-network-interfaces2.md).

This section describes the following NDIS network interface OIDs:

- [OID_GEN_ALIAS](https://msdn.microsoft.com/library/windows/hardware/ff569438) 
- [OID_GEN_ADMIN_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569437) 
- [OID_GEN_OPERATIONAL_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569619) 
- [OID_GEN_PROMISCUOUS_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569625) 
- [OID_GEN_XMIT_LINK_SPEED](https://msdn.microsoft.com/library/windows/hardware/ff569655) 
- [OID_GEN_RCV_LINK_SPEED](https://msdn.microsoft.com/library/windows/hardware/ff569630) 
- [OID_GEN_UNKNOWN_PROTOS](https://msdn.microsoft.com/library/windows/hardware/ff569648) 
- [OID_GEN_DISCONTINUITY_TIME](https://msdn.microsoft.com/library/windows/hardware/ff569581) 
- [OID_GEN_LAST_CHANGE](https://msdn.microsoft.com/library/windows/hardware/ff569591) 
- [OID_GEN_INTERFACE_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569589) 
- [OID_GEN_MEDIA_CONNECT_STATUS_EX](https://msdn.microsoft.com/library/windows/hardware/ff569605) 
- [OID_GEN_LINK_SPEED_EX](https://msdn.microsoft.com/library/windows/hardware/ff569594) 
- [OID_GEN_MEDIA_DUPLEX_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569606) 
- [OID_TUNNEL_INTERFACE_RELEASE_OID](https://msdn.microsoft.com/library/windows/hardware/dn155803) 
- [OID_TUNNEL_INTERFACE_SET_OID](https://msdn.microsoft.com/library/windows/hardware/dn155804) 


