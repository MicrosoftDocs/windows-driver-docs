---
title: Handling NDIS Ports PnP Event Notifications
description: Handling NDIS Ports PnP Event Notifications
ms.assetid: 2f542b62-43a0-42fa-b72d-f789e029d3f0
keywords:
- ports WDK NDIS , PnP event notifications
- NDIS ports WDK , PnP event notifications
- PnP event notifications WDK NDIS ports
- event notifications WDK networking
- notifications WDK networking
- notifications WDK PnP , NDIS ports
- events WDK networkin
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling NDIS Ports PnP Event Notifications





NDIS forwards PnP events to notify overlying drivers when ports are activated or deactivated. NDIS and miniport drivers do not generate a PnP event when a port is allocated. Miniport drivers notify NDIS that ports have been activated with the **NetEventPortActivation** PnP event and miniport drivers generate a **NetEventPortDeactivation** PnP event to notify NDIS that some ports have been deactivated.

When NDIS calls the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function of a protocol driver, NDIS provides a list of all currently active ports in the **ActivePorts** member of the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure at the *BindParameters* parameter.

The following topics describe how to handle port PnP events:

[Handling the Port Activation PnP Event](handling-the-port-activation-pnp-event.md)

[Handling the Port Deactivation PnP Event](handling-the-port-deactivation-pnp-event.md)

 

 





