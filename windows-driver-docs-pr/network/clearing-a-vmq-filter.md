---
title: Clearing a VMQ Filter
description: Clearing a VMQ Filter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Clearing a VMQ Filter





To free a filter on a receive queue, an overlying driver issues an [OID\_RECEIVE\_FILTER\_CLEAR\_FILTER](./oid-receive-filter-clear-filter.md) set OID request. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_CLEAR\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_clear_parameters) structure.

The protocol driver obtained the filter identifier from an earlier [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) method OID request. For more information about setting filters, see [Setting a VMQ Filter](setting-a-vmq-filter.md).

A protocol driver must clear all the filters that it set on a queue before it frees the queue. A protocol driver must also clear all the filters that it set on the default queue before it closes its binding to the network adapter.

A miniport driver must not indicate packets on a nondefault queue if it has completed the OID\_RECEIVE\_FILTER\_CLEAR\_FILTER OID request to clear the last filter on the queue or if it has completed an [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](./oid-receive-filter-free-queue.md) OID request to free the queue.

 

