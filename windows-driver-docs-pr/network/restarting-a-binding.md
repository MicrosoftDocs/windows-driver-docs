---
title: Restarting a Binding
description: Restarting a Binding
ms.assetid: 5abec927-cb73-4b02-b977-c4f45bd37c42
keywords:
- protocol drivers WDK networking , binding restarts
- NDIS protocol drivers WDK , binding restarts
- binding restarts WDK networking
- binding states WDK networking
- restarting binding for protocol driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Restarting a Binding





To restart a binding that is paused, NDIS sends the protocol driver a network Plug and Play (PnP) restart event notification. After the protocol driver receives the restart notification, the affected binding enters the Restarting state.

To send a restart notification, NDIS calls a protocol driver's [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function. The [**NET\_PNP\_EVENT\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff568752) structure that NDIS passes to *ProtocolNetPnPEvent* specifies **NetEventRestart** in the **NetEvent** member and the **Buffer** member contains a pointer to the [**NDIS\_PROTOCOL\_RESTART\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566844) structure. NDIS provides a pointer to an [**NDIS\_RESTART\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff567255) structure in the **RestartAttributes** member of the NDIS\_PROTOCOL\_RESTART\_PARAMETERS structure.

**Note**  While the binding was paused, NDIS could have reconfigured the driver stack. The new stack configuration can support a different set of capabilities for the underlying adapter. These new capabilities can affect how the protocol driver communicates on a binding.

 

The protocol driver should use the information in the [**NDIS\_PROTOCOL\_RESTART\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566844) structure to avoid unnecessary OID requests.

In the Restarting state, the protocol driver can:

-   Use OID requests to query the driver stack. For example, the driver can find out about support for receive side scaling by using [OID\_GEN\_RECEIVE\_SCALE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569636).

-   Reallocate [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) and [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) pools, if necessary.

-   Enumerate the list of the underlying filter modules.

-   Use OID requests to reveal new adapter capabilities.

After the driver is ready to resume send and receive operations for the binding, the binding enters the Running state.

 

 





