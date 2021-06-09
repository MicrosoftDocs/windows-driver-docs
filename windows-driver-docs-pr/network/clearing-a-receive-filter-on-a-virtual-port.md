---
title: Clearing a Receive Filter on a Virtual Port
description: Clearing a Receive Filter on a Virtual Port
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Clearing a Receive Filter on a Virtual Port


To clear a receive filter from a virtual port (VPort) on the NIC switch, an overlying driver issues an object identifier (OID) set request of [OID\_RECEIVE\_FILTER\_CLEAR\_FILTER](./oid-receive-filter-clear-filter.md). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_CLEAR\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_clear_parameters) structure.

Before the overlying driver issues the [OID\_RECEIVE\_FILTER\_CLEAR\_FILTER](./oid-receive-filter-clear-filter.md) request, it must initialize the [**NDIS\_RECEIVE\_FILTER\_CLEAR\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_clear_parameters) structure and set the members in the following way:

-   The **QueueId** member must be set to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

-   The **FilterId** member must be set to the filter identifier value that the driver obtained from an earlier [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) method OID request. For more information about how to set receive filters, see [Setting a Receive Filter on a Virtual Port](setting-a-receive-filter-on-a-virtual-port.md).

An overlying driver must clear all of the filters that it set on a VPort before it frees the VPort. An overlying driver must also clear all of the filters that it set on the default VPort before it closes its binding to or detached from the network adapter.

 

