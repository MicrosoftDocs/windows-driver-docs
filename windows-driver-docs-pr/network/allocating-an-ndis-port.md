---
title: Allocating an NDIS Port
description: Allocating an NDIS Port
keywords:
- ports WDK NDIS , allocating
- NDIS ports WDK , allocating
- allocating NDIS ports
- ports WDK NDIS , maximum number
- NDIS ports WDK , maximum number
- maximum number of ports WDK NDIS
- port states WDK NDIS
- allocated port state WDK NDIS
- port numbers
ms.date: 03/02/2023
---

# Allocating an NDIS Port





To allocate an NDIS port for a miniport adapter, a miniport driver calls the [**NdisMAllocatePort**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismallocateport) function. **NdisMAllocatePort** is synchronous and returns after NDIS has successfully allocated the resources that are required for the port.

Before the miniport driver calls **NdisMAllocatePort**, the driver must call the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function to set the attributes in the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_registration_attributes) structure. Miniport drivers can call **NdisMAllocatePort** for a miniport adapter after the call to **NdisMSetMiniportAttributes** returns successfully and before NDIS calls the [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function for that miniport adapter.

NDIS always allocates the default port (port zero) so miniport drivers should not allocate a default port. NDIS frees the default port after the miniport driver returns form [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt).

NDIS assigns a port number to a port when the miniport driver calls [**NdisMAllocatePort**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismallocateport). The driver specifies port characteristics in the [**NDIS\_PORT\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_characteristics) structure before the driver calls **NdisMAllocatePort**. When **NdisMAllocatePort** successfully returns, the **PortNumber** member of NDIS\_PORT\_CHARACTERISTICS that the *PortCharacteristics* parameter specifies is set to the port number that NDIS assigned to the port.

Before returning from [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt), a miniport driver must call the [**NdisMFreePort**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreeport) function to free all of the ports that are associated with a miniport adapter. If a miniport adapter fails initialization, the driver must call **NdisMFreePort** to free all of the ports that the driver allocated before it returns from the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. For more information about freeing NDIS ports, see [Freeing NDIS Ports](freeing-an-ndis-port.md).

The maximum number of ports that a miniport driver can allocate is 0xffffff. However, in practice, drivers will set a maximum number that is based on the port type and the requirements of the driver application. For example, for a bridge application, the number of ports is unlikely to exceed 16. The number of ports would be higher for access points that use 802.1x supplicant ports and significantly higher for WAN drivers that use virtual private network (VPN) ports.

After a miniport driver allocates a port, the port is in the allocated state, and the port is not active. A port cannot be used to send and receive data, initiate a status indication, issue an OID request, or initiate a Plug and Play (PnP) event, until the port is activated. NDIS activates the default port automatically after the miniport driver sets the registration attributes in an [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_registration_attributes) structure. To request that NDIS not activate the default port, a miniport driver can set NDIS\_MINIPORT\_ATTRIBUTES\_CONTROLS\_DEFAULT\_PORT in the **AttributeFlags** member of NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES.

NDIS passes the authentication state of the default port to the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function at the **DefaultPortAuthStates** member of the [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_init_parameters) structure. If a miniport driver controls the default port, when the miniport driver activates the default port, it can activate the default port by using the default authentication settings. For more information about activating the default port, see [Activating NDIS Ports](activating-an-ndis-port.md).

Miniport drivers can use the NDIS\_PORT\_CHAR\_USE\_DEFAULT\_AUTH\_SETTINGS flag in the **Flags** member of the [**NDIS\_PORT\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_characteristics) structure for the ports that the drivers allocate and activate. For the allocation case, NDIS assigns the default authentication states to the new ports and ignores the authentication states that are passed to the [**NdisMAllocatePort**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismallocateport) function.

For more information about NDIS port states, see [NDIS Port States](ndis-port-states.md). For more information about activating ports, see [Activating NDIS Ports](activating-an-ndis-port.md).

 

