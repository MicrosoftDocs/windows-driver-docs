---
title: Filter Module Synchronous OID Requests
description: This topic describes Filter Module Synchronous OID requests
keywords: Filter Module Synchronous OID Requests Interface, Filter Module Synchronous OID call, WDK Filter Module Synchronous OIDs, Filter Module Synchronous OID request
ms.date: 04/03/2017
---

# Filter Module Synchronous OID Requests

To support the Synchronous OID request path, filter drivers provide a [*FilterSynchronousOidRequest*](/windows-hardware/drivers/ddi/ndis/nf-ndis-filter_synchronous_oid_request) function entry point in the [**NDIS\_FILTER\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics) structure when they call the [**NdisFRegisterFilterDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfregisterfilterdriver) function.

> [!NOTE]
> NDIS 6.81 supports specific OIDs for use with the Synchronous OID request interface. OIDs that existed before NDIS 6.80 and some NDIS 6.80 OIDs are not supported. To determine if an OID can be used in the Synchronous OID request interface, see the OID reference page.

To support the Synchronous OID request interface, use the documentation for the standard OID request interface. The following table shows the relationship between the functions in the Synchronous OID request interface and the standard OID request interface.

| Synchronous OID function | Standard OID function |
| --- | --- |
| [*FilterSynchronousOidRequest*](/windows-hardware/drivers/ddi/ndis/nf-ndis-filter_synchronous_oid_request) | [*FilterOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request) |
| [*FilterSynchronousOidRequestComplete*](/windows-hardware/drivers/ddi/ndis/nf-ndis-filter_synchronous_oid_request_complete) | [*FilterOidRequestComplete*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request_complete) |
