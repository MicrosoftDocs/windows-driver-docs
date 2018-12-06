---
title: Deactivating an NDIS Port
description: Deactivating an NDIS Port
ms.assetid: 2a5d288f-b6ea-4b63-91a3-44155aae8064
keywords:
- ports WDK NDIS , deactivating
- NDIS ports WDK , deactivating
- deactivating NDIS ports WDK NDIS
- deactivation PnP events WDK NDIS ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deactivating an NDIS Port





To deactivate NDIS ports, a miniport driver sends a port deactivation Plug and Play (PnP) event to NDIS. After a miniport driver successfully activates a port, the driver must deactivate the port before it can free the port. Also, the driver might deactivate a port for application-specific reasons. A port can be reactivated after it is deactivated, but a port cannot be reactivated if it is freed.

To send a port deactivation PnP event, miniport drivers use the **NetEventPortDeactivation** PnP event code in the call to the [**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616) function. To deactivate ports, the miniport driver must set the members of the [**NET\_PNP\_EVENT\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff568752) structure that the *NetPnPEvent* parameter of **NdisMNetPnPEvent** points to as follows:

<a href="" id="portnumber"></a>**PortNumber**  
The source port of the event notification. Set this member to zero because the port numbers are provided in the **Buffer** member of the structure that the **NetPnPEvent** member specifies.

<a href="" id="netpnpevent"></a>**NetPnPEvent**  
A [**NET\_PNP\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff568751) structure that describes the port deactivation event. Set the members of this structure as follows:

<a href="" id="netevent"></a>**NetEvent**  
An event code that describes the event. Set this member to **NetEventPortDeactivation**.

<a href="" id="buffer"></a>**Buffer**  
A pointer to an array of NDIS\_PORT\_NUMBER-typed elements. The array contains the port numbers of all of the ports that the miniport driver is deactivating.

<a href="" id="bufferlength"></a>**BufferLength**  
The number of bytes that are specified in **Buffer** . Set **BufferLength** to the size of the array that **Buffer** points to. To obtain the number of elements in the array, divide the value in **BufferLength** by the size of the NDIS\_PORT\_NUMBER data type.

<a href="" id="other-members"></a>Other members  
Set the remaining members of NET\_PNP\_EVENT to **NULL**.

A miniport driver can provide an array with a list of ports to deactivate. However, if the default port of a miniport adapter is the target of a **NetEventPortDeactivation** PnP event, the default port must be the only port that is specified in the array.

Miniport drivers can deactivate active ports at any time. However, before a miniport driver deactivates a port, it must ensure that there are no outstanding status indications or receive indications that are associated with that port. After the miniport driver sends the port deactivation PnP event, it must not initiate any status or receive indications that are associated with the deactivated ports.

A miniport driver can also reactivate a port. For more information about activating NDIS ports, see [Activating NDIS Ports](activating-an-ndis-port.md).

When a miniport driver deactivates ports, NDIS notifies all of the protocol drivers that are bound to the miniport driver with the **NetEventPortDeactivation** PnP event. This PnP event lists those ports that have changed to the allocated state and does not include any ports that are already deactivated. For more information about handling port deactivation events in a protocol driver, see [Handling the Port Deactivation PnP Event](handling-the-port-deactivation-pnp-event.md).

Before a miniport driver allocates an NDIS port, the driver must call the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function to set the registration attributes in the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565934) structure. Miniport drivers can control the activation of the default port by setting the NDIS\_MINIPORT\_CONTROLS\_DEFAULT\_PORT attribute flag when they call **NdisMSetMiniportAttributes**. If a miniport driver assumes the responsibility for activating the default port and the miniport driver activated the default port, it must deactivate the default port before returning from the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function.

All of the ports that are specified by the array of NDIS\_PORT\_NUMBER elements must be in the activated state. A miniport driver should not attempt to deactivate a port that has already deactivated.

If NDIS fails to deactivate any ports in the port array, none of the ports in the port array will change state. If the deactivation fails because some of the specified ports do not exist, the [**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616) function returns the NDIS\_STATUS\_INVALID\_PORT return value. If the deactivation fails because some of the ports are not in the activated state, **NdisMNetPnPEvent** returns the NDIS\_STATUS\_INVALID\_PORT\_STATE return value.

Until the call to **NdisMNetPnPEvent** returns, a port is not deactivated, and miniport drivers must be able to handle OID requests and send requests that are associated with that port.

When a miniport driver deactivates the default port, NDIS closes all of the bindings between the overlying protocol drivers and the miniport adapter. If a miniport driver tries to deactivate the default port and default port is already deactivated, [**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616) fails and returns the NDIS\_STATUS\_INVALID\_PORT\_STATE return value. If a miniport driver tries to deactivates the default port and the default port is not the only port that is specified in the array of NDIS\_PORT\_NUMBER elements, **NdisMNetPnPEvent** fails and returns the NDIS\_STATUS\_INVALID\_PORT return value. If a miniport driver sets the **Buffer** member to **NULL** or **BufferLength** member to zero, NDIS fails the **NdisMNetPnPEvent** call and returns the NDIS\_STATUS\_INVALID\_PARAMETER return value.

After a port is successfully deactivated, the port is in the allocated state. Miniport drivers cannot indicate received data or status for the port in the allocated state.

 

 





