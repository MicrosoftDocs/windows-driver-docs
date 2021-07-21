---
title: Activating an NDIS Port
description: Activating an NDIS Port
keywords:
- ports WDK NDIS , activating
- NDIS ports WDK , activating
- activating NDIS ports
- port states WDK NDIS
- activation PnP events WDK NDIS ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Activating an NDIS Port





After a miniport driver successfully allocates an NDIS port, and before using the port number in NDIS functions, the driver must activate the port. To activate the port, the miniport driver sends a port activation Plug and Play (PnP) event to NDIS. To send the port activation PnP event, miniport drivers use the **NetEventPortActivation** PnP event code in the call to the [**NdisMNetPnPEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismnetpnpevent) function.

To activate ports, the miniport driver must set the members of the [**NET\_PNP\_EVENT\_NOTIFICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_pnp_event_notification) structure that the *NetPnPEvent* parameter of **NdisMNetPnPEvent** points to as follows:

<a href="" id="portnumber"></a>**PortNumber**  
The source port of the event notification. Set this member to zero because the port numbers are provided in the **Buffer** member of the structure that the **NetPnPEvent** member specifies.

<a href="" id="netpnpevent"></a>**NetPnPEvent**  
A [**NET\_PNP\_EVENT**](/windows-hardware/drivers/ddi/netpnp/ns-netpnp-_net_pnp_event) structure that describes the port activation event. Set the members of this structure as follows:

<a href="" id="netevent"></a>**NetEvent**  
An event code that describes the event. Set this member to **NetEventPortActivation**.

<a href="" id="buffer"></a>**Buffer**  
A pointer to a linked list of [**NDIS\_PORT**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port) structures. The **Next** member of the NDIS\_PORT structures points to the next NDIS\_PORT structure in the list.

<a href="" id="bufferlength"></a>**BufferLength**  
The number of bytes that are specified in **Buffer** . Set **BufferLength** to the size of the NDIS\_PORT structures.

<a href="" id="other-members"></a>Other members  
Set the remaining members of NET\_PNP\_EVENT to **NULL**.

The miniport driver lists the ports that have changed states from inactive to active in a linked list of [**NDIS\_PORT**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port) structures. However, if the default port of a miniport adapter is the target of a **NetEventPortActivation** PnP event, the default port must be the only port in the list.

When the miniport driver notifies NDIS of the activation of a port (and possibly before this notification call returns), the miniport driver must be ready to handle send requests and OID requests that are associated with the port. Miniport drivers must not use the port number of a newly activated port in status or receive indications until after the call to [**NdisMNetPnPEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismnetpnpevent) returns.

NDIS does not notify overlying drivers about activated ports until after the default port is active. When NDIS calls the [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function of a protocol driver, NDIS provides a list of all currently active ports in the **ActivePorts** member of the [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) structure that the *BindParameters* parameter points to. When a miniport driver activates new ports, NDIS notifies all of the protocol drivers that are bound to the miniport driver with the **NetEventPortActivation** PnP event. For more information about handling these port activation events in a protocol driver, see [Handling the Port Activation PnP Event](handling-the-port-activation-pnp-event.md).

Before a miniport driver allocates an NDIS port, the driver must call the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function to set the registration attributes in the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_registration_attributes) structure. Miniport drivers can control the activation of the default port by setting the NDIS\_MINIPORT\_CONTROLS\_DEFAULT\_PORT attribute flag when they call **NdisMSetMiniportAttributes**. If a miniport driver assumes the responsibility for activating the default port, NDIS does not initiate the binding between the miniport adapter and the overlying drivers until the miniport driver activates the default port with the port activation PnP event.

All of the ports that are specified by the linked list of NDIS\_PORT structures must be in the allocated state. A miniport driver should not attempt to activate a port that is already active; if the driver does attempt to activate an active port, NDIS treates the situation as a port activation failure.

If NDIS fails to activate any ports on the list, it fails the call to [**NdisMNetPnPEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismnetpnpevent), and none of the ports on the list change state to the activated state. If NDIS fails to activate the ports because some of the ports do not exist, **NdisMNetPnPEvent** returns an NDIS\_STATUS\_INVALID\_PORT return value. If NDIS fails to activate the ports because some of the ports are not in the allocated state, **NdisMNetPnPEvent** returns an NDIS\_STATUS\_INVALID\_PORT\_STATE return value.

After a port has been successfully activated, the port is in the activated state. Miniport drivers can indicate received data and status for a port in the activated state.

NDIS passes the authentication state of the default port to the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function at the **DefaultPortAuthStates** member of the [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_init_parameters) structure. If a miniport driver controls the default port, when the miniport driver activates the default port, it can activate the default port by using the default authentication settings. To use the default authentication settings, set the NDIS\_PORT\_CHAR\_USE\_DEFAULT\_AUTH\_SETTINGS flag in the **Flags** member of [**NDIS\_PORT\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_characteristics) structure. Miniport drivers can use the NDIS\_PORT\_CHAR\_USE\_DEFAULT\_AUTH\_SETTINGS flag for the ports that they allocate and activate. For the activation case, NDIS assigns the default authentication states to the newly activated port and ignores the authentication states that are passed to [**NdisMNetPnPEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismnetpnpevent) for the **NetEventPortActivation** event.

For more information about controlling the default port and allocating ports, see [Allocating NDIS Ports](allocating-an-ndis-port.md).

 

