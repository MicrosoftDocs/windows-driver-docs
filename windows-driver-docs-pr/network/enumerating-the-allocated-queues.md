---
title: Enumerating the Allocated Queues
description: Enumerating the Allocated Queues
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating the Allocated Queues





To get a list of all the receive queues that are allocated on a network adapter, an overlying driver issues an [OID\_RECEIVE\_FILTER\_ENUM\_QUEUES](./oid-receive-filter-enum-queues.md) query OID request. After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_QUEUE\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_info_array) structure that is followed by an [**NDIS\_RECEIVE\_QUEUE\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_info) structure for each queue.

NDIS handles the OID\_RECEIVE\_FILTER\_ENUM\_QUEUES query OID request for miniport drivers. NDIS obtained the information from an internal cache of the data that it received from the [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](./oid-receive-filter-allocate-queue.md) and [OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](./oid-receive-filter-queue-parameters.md) OID requests.

Overlying drivers and user-mode applications can use the OID\_RECEIVE\_FILTER\_ENUM\_QUEUES OID query request to enumerate the receive queues on a network adapter.

If a protocol driver issues the request, the request type in the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure is set to **NdisRequestQueryInformation** and this OID returns an array of all the receive queues that the protocol driver allocated on the network adapter. If a user-mode application issued the request, the request type in the NDIS\_OID\_REQUEST is set to **NdisRequestQueryStatistics**, and this OID returns an array of information for all the receive queues on the miniport adapter.

 

