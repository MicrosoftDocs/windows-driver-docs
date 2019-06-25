---
title: Enumerating Filters on a VMQ
description: Enumerating Filters on a VMQ
ms.assetid: 6d5d8cb6-7bdf-488b-8fcd-7c6e78c4fb24
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Filters on a VMQ





To obtain a list of all the filters that are set on a receive queue, overlying drivers and applications can use the [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-enum-filters) method object identifier (OID) request.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_oid_request) structure initially contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure. When it formats the **NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY** structure, the overlying driver or application must set the **QueueId** member to the identifier (ID) of the receive queue. The receive queue ID is obtained in the following ways:

-   The overlying driver obtained the receive queue ID value from earlier OID method requests of [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-allocate-queue) or [OID\_RECEIVE\_FILTER\_ENUM\_QUEUES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-enum-queues). The driver can also specify **NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID** for the default receive queue.

-   An application obtained the receive queue ID value from an earlier OID method request of [OID\_RECEIVE\_FILTER\_ENUM\_QUEUES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-enum-queues). The application can also specify **NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID** for the default receive queue.

After a successful return from the OID method request of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-enum-filters), the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an updated [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure that is followed by one or more [**NDIS\_RECEIVE\_FILTER\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_receive_filter_info) structures. Each **NDIS\_RECEIVE\_FILTER\_INFO** structure specifies the ID for a filter that is set on the specified receive queue.

Overlying drivers or applications can use the [OID\_RECEIVE\_FILTER\_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-parameters) OID method request to obtain the parameters of a specific filter on a receive queue.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_oid_request) structure initially contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) structure. The overlying driver or application formats the **NDIS\_RECEIVE\_FILTER\_PARAMETERS** structure by setting the **FilterId** member to the nonzero ID value of the filter whose parameters are to be returned.

**Note**  The overlying driver obtained the filter ID from an earlier OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-set-filter) or [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-enum-filters). The application can obtain the filter ID only from an earlier OID method request of OID\_RECEIVE\_FILTER\_ENUM\_FILTERS.

 

NDIS handles the [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-enum-filters) and [OID\_RECEIVE\_FILTER\_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-parameters) method OID requests for miniport drivers. NDIS obtained the information from an internal cache of the data that it received from the [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-set-filter) OID request.

 

 





