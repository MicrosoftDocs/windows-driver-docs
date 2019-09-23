---
title: Clearing a Receive Filter on a Virtual Port
description: Clearing a Receive Filter on a Virtual Port
ms.assetid: 8431322B-2BF0-4F82-AAAE-0E0396BBC857
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Clearing a Receive Filter on a Virtual Port


To clear a receive filter from a virtual port (VPort) on the NIC switch, an overlying driver issues an object identifier (OID) set request of [OID\_RECEIVE\_FILTER\_CLEAR\_FILTER](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-clear-filter). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_CLEAR\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_receive_filter_clear_parameters) structure.

Before the overlying driver issues the [OID\_RECEIVE\_FILTER\_CLEAR\_FILTER](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-clear-filter) request, it must initialize the [**NDIS\_RECEIVE\_FILTER\_CLEAR\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_receive_filter_clear_parameters) structure and set the members in the following way:

-   The **QueueId** member must be set to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

-   The **FilterId** member must be set to the filter identifier value that the driver obtained from an earlier [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-set-filter) method OID request. For more information about how to set receive filters, see [Setting a Receive Filter on a Virtual Port](setting-a-receive-filter-on-a-virtual-port.md).

An overlying driver must clear all of the filters that it set on a VPort before it frees the VPort. An overlying driver must also clear all of the filters that it set on the default VPort before it closes its binding to or detached from the network adapter.

 

 





