---
title: Setting a Packet Coalescing Receive Filter
description: Setting a Packet Coalescing Receive Filter
ms.assetid: 59BD092F-A530-446F-93E7-02E1F254E9A0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting a Packet Coalescing Receive Filter


To download and set a receive filter on a miniport driver that supports packet coalescing, an overlying driver issues an OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for the OID request contains a pointer to a caller-allocated buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure that specifies the parameters for an NDIS receive filter.

-   An array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures that specifies the filter test criterion for a field in a network packet header.

For more information about how an overlying driver specifies the parameters for a packet coalescing receive filter, see [Specifying a Packet Coalescing Receive Filter](specifying-a-packet-coalescing-receive-filter.md).

When NDIS receives an OID request to set a receive filter on the underlying network adapter, it verifies the receive filter parameters. If the overlying driver is specifying a new receive filter, NDIS will also generate a unique filter identifier (ID) for the receive filter.

After NDIS allocates the necessary resources and the filter ID, it forwards the OID request to the miniport driver. If the miniport driver can successfully allocate the necessary software and hardware resources for the receive filter, the miniport driver completes the OID request with a status of NDIS\_STATUS\_SUCCESS.

After a successful return from the OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795), the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure. This structure is updated by NDIS with the new filter ID.

 

 





