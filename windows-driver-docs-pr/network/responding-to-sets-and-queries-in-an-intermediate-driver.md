---
title: Responding to Sets and Queries in an Intermediate Driver
description: Responding to Sets and Queries in an Intermediate Driver
keywords:
- query operations WDK NDIS intermediate
- set operations WDK NDIS intermediate
- canceling OID requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Responding to Sets and Queries in an Intermediate Driver





Because an NDIS intermediate driver is bound to an overlying NDIS driver, it can also receive queries and sets from its [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function. In some cases, the intermediate driver just passes such requests through to the underlying miniport driver. Otherwise, it can respond to these queries and sets as appropriate to the medium that it exports at its upper edge. Note that an intermediate driver must always pass through any OID\_PNP\_*Xxx* requests that it receives from an overlying NDIS driver to the underlying miniport driver. NDIS 6.0 intermediate drivers can also cancel OID requests.

To forward a request down to the underlying drivers, an NDIS intermediate driver calls [**NdisAllocateCloneOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatecloneoidrequest) to allocate a cloned [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure. The driver calls the [**NdisOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisoidrequest) function to send the request. When the request is complete, the driver must call the [**NdisFreeCloneOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreecloneoidrequest) function to free the NDIS\_OID\_REQUEST structure.

To cancel an OID request, call the [**NdisCancelOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscanceloidrequest) function.

Typically, the general OIDs that an intermediate driver receives are the same or similar to those that the intermediate driver sends to the underlying miniport driver. The medium-specific OIDs that an intermediate driver receives are the type of the medium that the overlying driver requires.

If an intermediate driver itself processes the setting of an OID rather than passing the set request to an underlying miniport, it should validate the value to be set. If the intermediate driver determines that the value to be set is out of bounds, it should fail the set request.

**Note**  If an intermediate driver modifies the contents of TCP network data that it forwards down to an underlying miniport driver such that TCP offload functions cannot be performed on the network data, the intermediate driver should respond to [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](./oid-tcp-offload-current-config.md) queries with a status of NDIS\_STATUS\_NOT\_SUPPORTED instead of passing the request down to the underlying miniport.

 

For additional information about responding to sets and queries in an intermediate driver, see [Obtaining and Setting Miniport Driver Information and NDIS Support for WMI](ndis-management-information-and-oids.md).

 

