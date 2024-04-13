---
title: Miniport Adapter Synchronous OID Requests
description: Learn about miniport adapter Synchronous OID requests. See a table that shows the relationship between the Synchronous OID and standard OID request interfaces.
keywords: Miniport Adapter Synchronous OID Requests Interface, Miniport Adapter Synchronous OID call, WDK Miniport Adapter Synchronous OIDs, Miniport Adapter Synchronous OID request
ms.date: 09/28/2017
---

# Miniport Adapter Synchronous OID Requests

To support the Synchronous OID request path, miniport drivers provide a [*MiniportSynchronousOidRequest*](/windows-hardware/drivers/ddi/ndis/nf-ndis-miniport_synchronous_oid_request) function entry point in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure when they call the [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) function.

For miniport drivers, the *Synchronous OID request interface* differs from the Regular and Direct OID request interfaces in that miniport drivers do not have to register an asynchronous *complete* callback function. This is because of the synchronous nature of the path. For more info about the differences between Regular, Direct, and Synchronous OIDs in general, see [Synchronous OID Request Interface in NDIS 6.80](synchronous-oid-request-interface-in-ndis-6-80.md).

> [!NOTE]
> NDIS 6.80 supports specific OIDs for use with the Synchronous OID request interface. OIDs that existed before NDIS 6.80 and some NDIS 6.80 OIDs are not supported. To determine if an OID can be used in the Synchronous OID request interface, see the OID reference page.

To support the Synchronous OID request interface, use the documentation for the standard OID request interface. The following table shows the relationship between the functions in the Synchronous OID request interface and the standard OID request interface.

| Synchronous OID function | Standard OID function |
| --- | --- |
| [*MiniportSynchronousOidRequest*](/windows-hardware/drivers/ddi/ndis/nf-ndis-miniport_synchronous_oid_request) | [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) |
