---
title: Querying Packet Coalescing Receive Filters
description: Querying Packet Coalescing Receive Filters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying Packet Coalescing Receive Filters





Overlying drivers and applications can query packet coalescing receive filters that have been downloaded to a miniport driver by doing the following:

-   Request an enumerated list of the receive filters on the miniport driver by issuing an OID method request of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md). For more information, see [Enumerating the Receive Filters on a Miniport Driver](#enumerating-the-receive-filters-on-a-miniport-driver).

-   Request the test criterion parameters for a receive filter on the miniport driver by issuing an OID method request of [OID\_RECEIVE\_FILTER\_PARAMETERS](./oid-receive-filter-parameters.md). For more information, see [Querying the Receive Filters on a Miniport Driver](#querying-the-parameters-of-a-receive-filters-on-a-miniport-driver)

NDIS handles the [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md) and [OID\_RECEIVE\_FILTER\_PARAMETERS](./oid-receive-filter-parameters.md) method OID requests for miniport drivers. NDIS obtained the information from an internal cache of the data that it received from the [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) OID request.

## Enumerating the Receive Filters on a Miniport Driver


To obtain a list of all the packet coalescing receive filters that have been downloaded to a miniport driver, overlying drivers and applications issue an OID method request of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure.

**Note**  When the overlying driver or application initializes the [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure, it must set the **QueueId** member to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

 

After a successful return from the OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure that specifies a list of receive filters that are currently configured on a miniport driver.

-   An array of [**NDIS\_RECEIVE\_FILTER\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info) structures about a receive filter that is currently configured on a miniport driver.

## Querying the Parameters of a Receive Filters on a Miniport Driver


To obtain the parameters of a specific packet coalescing receive filter that was downloaded to the miniport driver, overlying drivers or applications issue an OID method request of [OID\_RECEIVE\_FILTER\_PARAMETERS](./oid-receive-filter-parameters.md). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) structure. The overlying driver or application initializes the **NDIS\_RECEIVE\_FILTER\_PARAMETERS** structure by setting the **FilterId** member to the nonzero ID value of the filter whose parameters are to be returned.

**Note**  The overlying driver obtained the filter ID from an earlier OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) or [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md). The application can only obtain the filter ID from an earlier OID method request of OID\_RECEIVE\_FILTER\_ENUM\_FILTERS.

 

After a successful return from the OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) structure that specifies the parameters for an NDIS receive filter.

-   An array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_field_parameters) structures that specifies the filter test criterion for one field in a network packet header.

 

