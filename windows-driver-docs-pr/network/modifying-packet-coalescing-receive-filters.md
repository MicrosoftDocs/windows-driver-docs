---
title: Modifying Packet Coalescing Receive Filters
description: Modifying Packet Coalescing Receive Filters
ms.assetid: 082A969F-2977-482A-B060-ED8D353EC2E9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying Packet Coalescing Receive Filters


To modify a receive filter on a miniport driver that supports packet coalescing, an overlying protocol or filter driver performs the following steps:

1.  To obtain a list of all the packet coalescing receive filters that have been downloaded to a miniport driver, the overlying driver issues an OID method request of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569787). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff567179) structure.

    **Note**  When the overlying driver or application initializes the [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff567179) structure, it must set the **QueueId** member to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

    After a successful return from the OID method request of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569787), the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an updated [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff567179) structure that is followed by one or more [**NDIS\_RECEIVE\_FILTER\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567176) structures. Each **NDIS\_RECEIVE\_FILTER\_INFO** structure specifies the identifier (ID) for a filter that is set on the network adapter.

2.  To obtain the parameters of a specific packet coalescing receive filter that was downloaded to the miniport driver, the overlying driver issues OID method request of [OID\_RECEIVE\_FILTER\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569792). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure. The overlying driver or application initializes the **NDIS\_RECEIVE\_FILTER\_PARAMETERS** structure by setting the **FilterId** member to the nonzero ID value of the filter whose parameters are to be returned.

    After a successful return from the OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer is formatted to contain the following:

    -   An [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure that specifies the parameters for the NDIS receive filter.

    -   An array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures that specifies the filter test criterion for one field in a network packet header.

3.  The overlying driver modifies the receive filter to add, delete, or change the filter's set of test criterion. The driver does this by adding, deleting, or modifying individual [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures from the field parameter array specified by the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure.

    When the overlying driver has completed the modifications to the test criterion, it must update the members of the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure to reflect the changes that were made to the receive filter. For example, the overlying driver must update the **FieldParametersArrayNumElements** member to contain the new number of elements in the array.

    For more information, see [Specifying a Packet Coalescing Receive Filter](specifying-a-packet-coalescing-receive-filter.md).

4.  The overlying driver issues an OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) to download the modified receive filter to the miniport driver.

    For more information, see [Setting a Packet Coalescing Receive Filter](setting-a-packet-coalescing-receive-filter.md).









