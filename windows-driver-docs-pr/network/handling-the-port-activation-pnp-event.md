---
title: Handling the Port Activation PnP Event
description: Handling the Port Activation PnP Event
keywords:
- ports WDK NDIS , PnP event notifications
- NDIS ports WDK , PnP event notifications
- PnP event notifications WDK NDIS ports
- activation PnP events WDK NDIS ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Port Activation PnP Event





Overlying drivers must handle the **NetEventPortActivation** PnP event when a miniport driver activates an NDIS port. NDIS does not initiate the binding between a protocol driver and miniport adapter until the default port has been activated. Therefore, protocol drivers should treat the call to their [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function as a notification that the default port is active.

Protocol drivers must not use a port number in any NDIS requests unless the driver received notification that the port is active, either through the bind parameters or through the **NetEventPortActivation** PnP event.

NDIS generates a port activation PnP event after the miniport driver activates some ports. (Miniport drivers specify the **NetEventPortActivation** PnP event code in the [**NET\_PNP\_EVENT\_NOTIFICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_pnp_event_notification) structure that the *NetPnPEvent* parameter points to in the call to [**NdisMNetPnPEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismnetpnpevent) to activate NDIS ports.)

Miniport drivers can indicate the activation of multiple ports in one PnP notification by using the **Next** member in an [**NDIS\_PORT**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port) structure to link multiple NDIS\_PORT structures. For more information about the linked list of NDIS\_PORT structures, see [Activating NDIS Ports](activating-an-ndis-port.md).

NDIS generates a **NetEventPortDeactivation** PnP event to the bound protocol drivers when a miniport deactivates some ports. For more information about the **NetEventPortDeactivation** PnP event, see [Handling the Port Deactivation PnP Event](handling-the-port-deactivation-pnp-event.md).

 

