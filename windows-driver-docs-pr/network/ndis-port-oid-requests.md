---
title: NDIS Port OID Requests
description: NDIS Port OID Requests
keywords:
- ports WDK NDIS , OID requests
- NDIS ports WDK , OID requests
- OID requests WDK NDIS ports
- associating OID requests WDK NDIS ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Port OID Requests





NDIS drivers can associate OID requests with NDIS ports. In such an OID request, the **PortNumber** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure is set to the target port number. The port number is zero if the OID request is for the default port. The overlying driver must ensure that a port is active before making any OID requests that specify a specific port number.

When NDIS calls the [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function of a protocol driver, NDIS provides a list of all currently active ports in the **ActivePorts** member of the [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) structure that the *BindParameters* parameter points to. NDIS also informs protocol drivers with a PnP event when ports are activated and deactivated. For more information about PnP port activation and deactivation notifications, see [Handling NDIS Ports PnP Notifications](handling-ndis-ports-pnp-event-notifications.md).

The following OIDs are specific to the NDIS ports interface:

<a href="" id="oid-gen-enumerate-ports"></a>[OID\_GEN\_ENUMERATE\_PORTS](./oid-gen-enumerate-ports.md)  
Enumerates the active ports that are associated with a miniport adapter.

<a href="" id="oid-gen-port-state"></a>[OID\_GEN\_PORT\_STATE](./oid-gen-port-state.md)  
Retrieves the current link and authentication port states.

<a href="" id="--------oid-gen-port-authentication-parameters"></a>[OID\_GEN\_PORT\_AUTHENTICATION\_PARAMETERS](./oid-gen-port-authentication-parameters.md)  
Sets the current authentication states of an NDIS port.

This section includes:

-   [Enumerating Ports](enumerating-ports.md)
-   [Querying the Port State](querying-the-port-state.md)
-   [Setting Port Authentication Parameters](setting-port-authentication-parameters.md)

 

