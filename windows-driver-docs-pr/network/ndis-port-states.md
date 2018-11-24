---
title: NDIS Port States
description: NDIS Port States
ms.assetid: bb13edd2-815b-488a-b36c-21a48809a143
keywords:
- ports WDK NDIS , states
- NDIS ports WDK , states
- states WDK NDIS ports
- authentication states WDK NDIS ports
- link states WDK NDIS ports
- initialization states WDK NDIS ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Port States





NDIS ports have operating states that include initialization states and states that are specified in the [**NDIS\_PORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff566800) structure. Port states fit into the following categories:

<a href="" id="initialization-states"></a>Initialization states  
NDIS port initialization states are associated with startup initialization and Plug and Play (PnP) events. When NDIS or a miniport driver first allocates a port, the port is in the *allocated state*. After NDIS or the miniport driver activates a port, the port is in the *activated state*. Inactive ports cannot send or receive data, make status indications, receive OID requests, or initiate PnP events.

<a href="" id="link-states"></a>Link states  
NDIS port link states are similar to link states that are associated with a miniport adapter and that are specified in an [**NDIS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh205390) structure. The port link states indicate the media link connection state and link speeds. The link state of a port can be different from the link state of the associated miniport adapter.

<a href="" id="authentication-states"></a>Authentication states  
NDIS port authentication states indicate if a port is controlled (requires authorization), the direction of data transmission (send, receive, or both), and the authorization state of a port (authorized, or not authorized). If a port is not controlled, the authenticated and not authenticated states are ignored.

A miniport driver can activate a port or deactivate a port with a PnP event. For more information about activating and deactivating ports, see [Activating NDIS Ports](activating-an-ndis-port.md) and [Deactivating NDIS Ports](deactivating-an-ndis-port.md).

Overlying drivers use the [OID\_GEN\_PORT\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569624) OID to get the current state of the port that is specified in the **PortNumber** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure. NDIS handles this OID, and miniport drivers do not receive this OID query.

Miniport drivers that support NDIS ports must use the [**NDIS\_STATUS\_PORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567415) status indication to indicate changes in the state of an NDIS port. Miniport drivers must set the port number in the **PortNumber** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure.

NDIS and overlying drivers use the [OID\_GEN\_PORT\_AUTHENTICATION\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569623) OID to set the current authentication states of an NDIS port. Miniport drivers that support NDIS ports must support this OID.

 

 





