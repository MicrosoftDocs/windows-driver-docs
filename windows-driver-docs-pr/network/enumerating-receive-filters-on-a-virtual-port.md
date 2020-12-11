---
title: Enumerating Receive Filters on a Virtual Port
description: Enumerating Receive Filters on a Virtual Port
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Receive Filters on a Virtual Port





After a virtual port (VPort) is created on the NIC switch of the network adapter, overlying drivers and user applications can do the following:

-   Enumerate the parameters for receive filters on a VPort.

    For more information, see [Enumerating Receive Filters](#enumerating-receive-filters).

-   Query the parameters for a specific receive filter.

    For more information, see [Querying a Specific Receive Filter](#querying-a-specific-receive-filter).

For more information on how to create a VPort, see [Creating a Virtual Port](creating-a-virtual-port.md).

## Enumerating Receive Filters


To obtain a list of all receive filters that are set on a virtual port (VPort) of a NIC switch, overlying drivers and applications can issue object identifier (OID) method requests of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure initially contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure.

Before the overlying driver or user application issues this OID method request, it must initialize an [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure and set the members of this structure in the following way:

-   The **QueueId** member must be set to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

-   The **VPortId** member must be set to the identifier associated with the VPort. The overlying driver obtains the VPort identifier through one of the following ways:

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md).

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_ENUM\_VPORTS](./oid-nic-switch-enum-vports.md).

    **Note**  This member is only valid if the driver or application sets the NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY\_VPORT\_ID\_SPECIFIED flag in the **Flags** member. If this flag is not set, receive filters are returned that were set on every VPort on the NIC switch.

     

After a successful return from the OID method request of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md), the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an updated [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure that is followed by one or more [**NDIS\_RECEIVE\_FILTER\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info) structures. Each **NDIS\_RECEIVE\_FILTER\_INFO** structure specifies the unique identifier for the receive filter that is set on the specified VPort.

## Querying a Specific Receive Filter


Overlying drivers or applications can issue an OID method request of [OID\_RECEIVE\_FILTER\_PARAMETERS](./oid-receive-filter-parameters.md) to obtain the parameters of a specific filter on a VPort.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure initially contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) structure.

Before the overlying driver or user application issues this OID method request, it must initialize an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) structure and set the members of this structure in the following way:

-   The **FilterId** member must be set to the nonzero identifier value of the filter whose parameters are to be returned.

    **Note**  The overlying driver obtained the filter identifier from an earlier OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) or [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md). The application can obtain the filter identifier only from an earlier OID method request of OID\_RECEIVE\_FILTER\_ENUM\_FILTERS.

     

-   The **QueueId** member must be set to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

-   The **VPortId** member must be set to the identifier associated with the VPort. The overlying driver obtains the VPort identifier through one of the following ways:

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md).

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_ENUM\_VPORTS](./oid-nic-switch-enum-vports.md).

NDIS handles the [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md) and [OID\_RECEIVE\_FILTER\_PARAMETERS](./oid-receive-filter-parameters.md) method OID requests for miniport drivers. NDIS obtained the information from an internal cache of the data that it received from the [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) OID request.

 

