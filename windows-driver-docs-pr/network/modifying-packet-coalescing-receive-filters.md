---
title: Modifying Packet Coalescing Receive Filters
description: Modifying Packet Coalescing Receive Filters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying Packet Coalescing Receive Filters


To modify a receive filter on a miniport driver that supports packet coalescing, an overlying protocol or filter driver performs the following steps:

1.  To obtain a list of all the packet coalescing receive filters that have been downloaded to a miniport driver, the overlying driver issues an OID method request of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure.

    **Note**  When the overlying driver or application initializes the [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure, it must set the **QueueId** member to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

    After a successful return from the OID method request of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md), the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an updated [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure that is followed by one or more [**NDIS\_RECEIVE\_FILTER\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info) structures. Each **NDIS\_RECEIVE\_FILTER\_INFO** structure specifies the identifier (ID) for a filter that is set on the network adapter.

2.  To obtain the parameters of a specific packet coalescing receive filter that was downloaded to the miniport driver, the overlying driver issues OID method request of [OID\_RECEIVE\_FILTER\_PARAMETERS](./oid-receive-filter-parameters.md). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) structure. The overlying driver or application initializes the **NDIS\_RECEIVE\_FILTER\_PARAMETERS** structure by setting the **FilterId** member to the nonzero ID value of the filter whose parameters are to be returned.

    After a successful return from the OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a buffer. This buffer is formatted to contain the following:

    -   An [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) structure that specifies the parameters for the NDIS receive filter.

    -   An array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_field_parameters) structures that specifies the filter test criterion for one field in a network packet header.

3.  The overlying driver modifies the receive filter to add, delete, or change the filter's set of test criterion. The driver does this by adding, deleting, or modifying individual [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_field_parameters) structures from the field parameter array specified by the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) structure.

    When the overlying driver has completed the modifications to the test criterion, it must update the members of the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) structure to reflect the changes that were made to the receive filter. For example, the overlying driver must update the **FieldParametersArrayNumElements** member to contain the new number of elements in the array.

    For more information, see [Specifying a Packet Coalescing Receive Filter](specifying-a-packet-coalescing-receive-filter.md).

4.  The overlying driver issues an OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) to download the modified receive filter to the miniport driver.

    For more information, see [Setting a Packet Coalescing Receive Filter](setting-a-packet-coalescing-receive-filter.md).
