---
title: NDIS Ports PnP Event Notifications
description: NDIS Ports PnP Event Notifications
keywords:
- ports WDK NDIS , PnP event notifications
- NDIS ports WDK , PnP event notifications
- PnP event notifications WDK NDIS ports
- event notifications WDK networking
- notifications WDK networking
- notifications WDK PnP , NDIS ports
- events WDK networkin
ms.date: 04/20/2017
---

# NDIS Ports PnP Event Notifications

NDIS forwards PnP events to notify overlying drivers when ports are activated or deactivated. NDIS and miniport drivers do not generate a PnP event when a port is allocated. Miniport drivers notify NDIS that ports have been activated with the **NetEventPortActivation** PnP event and miniport drivers generate a **NetEventPortDeactivation** PnP event to notify NDIS that some ports have been deactivated.

When NDIS calls the [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function of a protocol driver, NDIS provides a list of all currently active ports in the **ActivePorts** member of the [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) structure at the *BindParameters* parameter.

The following topics describe how to handle port PnP events:

[Handling the Port Activation PnP Event](handling-the-port-activation-pnp-event.md)

[Handling the Port Deactivation PnP Event](handling-the-port-deactivation-pnp-event.md)

 

