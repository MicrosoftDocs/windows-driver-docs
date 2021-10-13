---
title: CoNDIS MCM OID Requests
description: CoNDIS MCM OID Requests
keywords:
- miniport call managers WDK networking , OID requests
- MCMs WDK networking , OID requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS MCM OID Requests





Like other CoNDIS call managers, miniport call managers (MCMs) can query or set the operating parameters of CoNDIS client drivers. CoNDIS client drivers can query or set the call manager parameters or the miniport driver parameters of an MCM.

To originate an OID request to a CoNDIS client driver, an MCM calls the [**NdisMCmOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmoidrequest) function.

The following figure illustrates an OID request that an MCM originated.

![diagram illustrating an oid request that an mcm originated.](images/mcmcorequest.png)

After an MCM driver calls the [**NdisMCmOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmoidrequest) function, NDIS calls the [**ProtocolCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_oid_request) function of the client driver.

To complete synchronously, **NdisMCmOidRequest** returns NDIS\_STATUS\_SUCCESS or an error status. To complete asynchronously, **NdisMCmOidRequest** returns NDIS\_STATUS\_PENDING.

If [**NdisMCmOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmoidrequest) returns NDIS\_STATUS\_PENDING, NDIS calls the [**ProtocolCoOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_oid_request_complete) function of the MCM after the client drivers complete the OID request by calling the [**NdisCoOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequestcomplete) function. In this case, NDIS passes the results of the request at the *OidRequest* parameter of *ProtocolCoOidRequestComplete*. NDIS passes the final status of the request at the *Status* parameter of *ProtocolCoOidRequestComplete*.

If **NdisMCmOidRequest** returns NDIS\_STATUS\_SUCCESS, it returns the results of a query request in the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure at the *OidRequest* parameter. In this case, NDIS does not call the *ProtocolCoOidRequestComplete* function of the MCM.

CoNDIS client drivers can query or set the call manager operating parameters or miniport operating parameters of MCMs. To originate an OID request for MCM call manager parameters, a client calls the [**NdisCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequest) function and provides a valid address family (AF) handle at the *NdisAfHandle* parameter. To originate an OID request for MCM miniport parameters, a client calls the **NdisCoOidRequest** function and sets the AF handle to **NULL**.

After a client calls the **NdisCoOidRequest** function, NDIS calls either the [**MiniportCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function or the [**ProtocolCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_oid_request) function of the MCM driver.

The following figure illustrates an OID request for the miniport parameters of the MCM.

![diagram illustrating an oid request for the miniport parameters of the mcm.](images/protocol2mcmcorequest.png)

The following figure illustrates an OID request for the call manager parameters of the MCM.

![diagram illustrating an oid request for the call manager parameters of the mcm.](images/client2mcmcorequest.png)

To complete synchronously, [**NdisCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequest) returns NDIS\_STATUS\_SUCCESS or an error status. To complete asynchronously, [**ProtocolCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_oid_request) or [**MiniportCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) returns NDIS\_STATUS\_PENDING.

If *ProtocolCoOidRequest* or **MininportCoOidRequest** returns NDIS\_STATUS\_PENDING, NDIS calls the [**ProtocolCoOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_oid_request_complete) function of the client after the MCM completes the OID request by calling the [**NdisMCoOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcooidrequestcomplete) or [**NdisMCmOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmoidrequestcomplete) function. In this case, NDIS passes the results of the request at the *OidRequest* parameter of *ProtocolCoOidRequestComplete*. NDIS passes the final status of the request at the *Status* parameter of *ProtocolCoOidRequestComplete*.

If [**NdisCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequest) returns NDIS\_STATUS\_SUCCESS, it returns the results of a query request in the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure at the *OidRequest* parameter. In this case, NDIS does not call the client's *ProtocolCoOidRequestComplete* function.

 

