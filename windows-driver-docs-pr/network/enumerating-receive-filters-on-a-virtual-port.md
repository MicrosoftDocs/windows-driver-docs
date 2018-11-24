---
title: Enumerating Receive Filters on a Virtual Port
description: Enumerating Receive Filters on a Virtual Port
ms.assetid: E809B7A3-256B-4351-8A60-D80D4A86EFDB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Receive Filters on a Virtual Port





After a virtual port (VPort) is created on the NIC switch of the network adapter, overlying drivers and user applications can do the following:

-   Enumerate the parameters for receive filters on a VPort.

    For more information, see [Enumerating Receive Filters](#enumerate).

-   Query the parameters for a specific receive filter.

    For more information, see [Querying a Specific Receive Filter](#query).

For more information on how to create a VPort, see [Creating a Virtual Port](creating-a-virtual-port.md).

## Enumerating Receive Filters


To obtain a list of all receive filters that are set on a virtual port (VPort) of a NIC switch, overlying drivers and applications can issue object identifier (OID) method requests of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569787).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure initially contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff567179) structure.

Before the overlying driver or user application issues this OID method request, it must initialize an [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff567179) structure and set the members of this structure in the following way:

-   The **QueueId** member must be set to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

-   The **VPortId** member must be set to the identifier associated with the VPort. The overlying driver obtains the VPort identifier through one of the following ways:

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816).

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_ENUM\_VPORTS](https://msdn.microsoft.com/library/windows/hardware/hh451821).

    **Note**  This member is only valid if the driver or application sets the NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY\_VPORT\_ID\_SPECIFIED flag in the **Flags** member. If this flag is not set, receive filters are returned that were set on every VPort on the NIC switch.

     

After a successful return from the OID method request of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569787), the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an updated [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff567179) structure that is followed by one or more [**NDIS\_RECEIVE\_FILTER\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567176) structures. Each **NDIS\_RECEIVE\_FILTER\_INFO** structure specifies the unique identifier for the receive filter that is set on the specified VPort.

## Querying a Specific Receive Filter


Overlying drivers or applications can issue an OID method request of [OID\_RECEIVE\_FILTER\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569792) to obtain the parameters of a specific filter on a VPort.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure initially contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure.

Before the overlying driver or user application issues this OID method request, it must initialize an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure and set the members of this structure in the following way:

-   The **FilterId** member must be set to the nonzero identifier value of the filter whose parameters are to be returned.

    **Note**  The overlying driver obtained the filter identifier from an earlier OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) or [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569787). The application can obtain the filter identifier only from an earlier OID method request of OID\_RECEIVE\_FILTER\_ENUM\_FILTERS.

     

-   The **QueueId** member must be set to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

-   The **VPortId** member must be set to the identifier associated with the VPort. The overlying driver obtains the VPort identifier through one of the following ways:

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816).

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_ENUM\_VPORTS](https://msdn.microsoft.com/library/windows/hardware/hh451821).

NDIS handles the [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569787) and [OID\_RECEIVE\_FILTER\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569792) method OID requests for miniport drivers. NDIS obtained the information from an internal cache of the data that it received from the [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) OID request.

 

 





