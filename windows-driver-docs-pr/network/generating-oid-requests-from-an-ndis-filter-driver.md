---
title: Generating OID Requests from an NDIS Filter Driver
description: Generating OID Requests from an NDIS Filter Driver
keywords:
- OIDs WDK networking , filter drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Generating OID Requests from an NDIS Filter Driver





A filter driver can originate OID query or set requests to underlying drivers by calling the [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) function.

The following figure illustrates an OID request that is originated by a filter driver.

![diagram illustrating an oid request originated by a filter driver.](images/filterrequest.png)

After a filter driver calls the [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) function, NDIS calls the request function of the next underlying driver. For more information about how a miniport driver handles OID requests, see [OID Requests for an Adapter](miniport-adapter-oid-requests.md).

To complete synchronously, [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) returns NDIS\_STATUS\_SUCCESS or an error status. To complete asynchronously, **NdisFOidRequest** returns NDIS\_STATUS\_PENDING.

To determine what information was successfully handled by an underlying driver, filter drivers that issue OID requests must check the value in the **SupportedRevision** member in the NDIS\_OID\_REQUEST structure after the OID request returns. For more information about NDIS version information, see [Specifying NDIS Version Information](specifying-ndis-version-information.md).

If [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) returns NDIS\_STATUS\_PENDING, NDIS calls the [*FilterOidRequestComplete*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request_complete) function after the underlying drivers complete the OID request. In this case, NDIS passes the results of the request at the *OidRequest* parameter of *FilterOidRequestComplete*. NDIS passes the final status of the request at the *Status* parameter of *FilterOidRequestComplete*.

If [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) returns NDIS\_STATUS\_SUCCESS, it returns the results of a query request in the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure at the *OidRequest* parameter. In this case, NDIS does not call the [*FilterOidRequestComplete*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request_complete) function.

A driver can call [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) when it is in the *Restarting*, *Running*, *Pausing*, or *Paused* state.

**Note**  A filter driver should keep track of OID requests that it originates and make sure that it does not call the [**NdisFOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequestcomplete) function when such requests are complete.

 

 

