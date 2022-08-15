---
title: Default NDIS Port
description: Default NDIS Port
keywords:
- ports WDK NDIS , default
- NDIS ports WDK , default NDIS ports
ms.date: 04/20/2017
---

# Default NDIS Port





Port zero is reserved as the default port for a miniport adapter. If the *PortNumber* parameter of any function or the **PortNumber** member of any structure is set to zero, either the miniport driver did not allocate any ports, or the current activity is not port-specific.

For a good example of the default NDIS port, consider a load balancing and failover (LBFO) MUX intermediate driver. The virtual miniport of such a driver can be port zero (the default port). The intermediate driver can assign ports to the underlying miniport adapters with the port numbers ranging from 1 through the number of ports (*N*). An overlying driver could send data to port zero to allow the LBFO driver to select one of the underlying ports, or the overlying driver could specify a port number from 1 through *N* to choose a specific port for the send operation.

Miniport drivers do not have to allocate any ports or support any port numbers other than the default port. Even if a miniport driver does not allocate ports, NDIS allocates the default port and activates it after the miniport driver calls the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function to set the registration attributes in the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_registration_attributes) structure. Miniport drivers can start operations on the default port when **NdisMSetMiniportAttributes** successfully returns. In this case, NDIS frees the default port when the miniport driver returns from the [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function.

 

