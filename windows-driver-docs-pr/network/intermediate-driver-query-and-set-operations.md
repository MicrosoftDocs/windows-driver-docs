---
title: Intermediate Driver Query and Set Operations
description: Intermediate Driver Query and Set Operations
ms.assetid: 68576241-20c1-4df4-ab2e-20ab89e67763
keywords:
- intermediate drivers WDK networking , query operations
- NDIS intermediate drivers WDK , query operations
- intermediate drivers WDK networking , set operations
- NDIS intermediate drivers WDK , set operations
- query operations WDK NDIS intermediate
- set operations WDK NDIS intermediate
- OIDs WDK networking , intermediate driver queries and sets
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Intermediate Driver Query and Set Operations





After it has successfully bound to an underlying miniport adapter and initialized its virtual miniports, an intermediate driver queries the operating characteristics of the underlying miniport adapter and sets its own internal state. If appropriate, the intermediate driver also negotiates such parameters as lookahead buffer size for the binding with the underlying miniport adapter. Most of the attributes that are associated with an underlying miniport adapter are passed to the intermediate driver at the *BindParameters* parameter of the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function. Intermediate drivers should use the values that are passed to *ProtocolBindAdapterEx*, if possible, instead of issuing OID queries. However, an intermediate driver with a connectionless lower edge can issue OID queries by calling [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710). An intermediate driver with a connection-oriented lower edge can issue OID queries by calling [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711).

An intermediate driver can also receive query and set requests from higher level drivers through its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. The driver can either respond to those requests or pass them down to the underlying driver. How an intermediate driver responds to queries and sets depends on the implementation.

**Note**  The behavior of intermediate drivers can also be affected by the power state of the virtual miniport and the underlying miniport driver. To learn more about the effects of the power state on query and set operations, see [Handling a Set Power Request](handling-a-set-power-request.md).

 

The Network Reference section contains information about all of the general, connection-oriented, nonmedia-specific OIDs and about required media-specific OIDs of interest to intermediate driver developers.

The following topics provide additional information about issuing and responding to queries and sets in an intermediate driver:

[Issuing Set and Query Requests from an Intermediate Driver](issuing-set-and-query-requests-from-an-intermediate-driver.md)

[Responding to Sets and Queries in an Intermediate Driver](responding-to-sets-and-queries-in-an-intermediate-driver.md)

 

 





