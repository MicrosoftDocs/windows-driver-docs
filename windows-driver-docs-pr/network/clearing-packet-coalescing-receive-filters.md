---
title: Clearing Packet Coalescing Receive Filters
description: Clearing Packet Coalescing Receive Filters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Clearing Packet Coalescing Receive Filters


To free, or *clear*, a receive filter on a miniport driver that supports packet coalescing, an overlying driver issues an OID set request of [OID\_RECEIVE\_FILTER\_CLEAR\_FILTER](./oid-receive-filter-clear-filter.md). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_CLEAR\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_clear_parameters) structure.

The overlying driver, such as a protocol or filter driver, initializes the [**NDIS\_RECEIVE\_FILTER\_CLEAR\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_clear_parameters) structure in the following way:

-   The **QueueId** member must be set to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

    **Note**  Starting with NDIS 6.30, packet coalescing receive filters are only supported on the default receive queue of the network adapter. This receive queue has an identifier of NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

     

-   The **FilterId** member must be set to the nonzero identifier (ID) value of the filter to be cleared on the miniport driver. The overlying driver obtained the filter ID from an earlier OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) or [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md).

    **Note**  Only the overlying driver that set the packet coalescing receive filter can clear it.

     

**Note**  Before it completes the unbind or detach operation, the overlying protocol or filter driver must clear all the packet coalescing receive filters that it set on the underlying miniport driver.

 

 

