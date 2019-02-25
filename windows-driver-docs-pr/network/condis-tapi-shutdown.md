---
title: CoNDIS TAPI Shutdown
description: CoNDIS TAPI Shutdown
ms.assetid: 97baf489-9a9b-48c8-b0f8-79beea33bc38
keywords:
- CoNDIS WAN drivers WDK networking , TAPI services
- telephonic services WDK WAN , shutdown
- CoNDIS TAPI WDK networking , shutdown
- CoNDIS TAPI WDK networking , closing operations
- shutdown WDK networking
- closing CoNDIS TAPI operations calls WDK CoNDIS WAN
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS TAPI Shutdown





A TAPI session begins after a CoNDIS WAN miniport driver has enumerated its TAPI capabilities to an application. Within a session, one or more lines can be opened and one or more calls can be established. During the time a line is open, many calls can be established and then closed or dropped. During a session, one or more lines can go through transitions from open to closed many times. How a miniport driver handles such transitions is described in this section.

### Closing a Call

An in-process call can be closed either by the local node or by the remote node. The call can be closed on the local node, either because the last application with a handle to the call has closed the handle, or perhaps because the miniport driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) or [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) has been called. If the remote node hangs up an in-process call, the miniport driver must inform upper layers to tear down the call.

If an application on the local node closes the call, it must disconnect the call. A call is disconnected as a result of an application calling the TAPI **lineDrop** function. This TAPI-function call causes the NDPROXY driver to call the [**NdisClCloseCall**](https://msdn.microsoft.com/library/windows/hardware/ff561627) function and to pass a handle that represents the VC for the call. NDIS in turn calls the CoNDIS WAN miniport driver's [**ProtocolCmCloseCall**](https://msdn.microsoft.com/library/windows/hardware/ff570241) function. The miniport driver should return NDIS\_STATUS\_PENDING to NDPROXY so the miniport driver can complete **NdisClCloseCall** asynchronously.

The miniport driver's *ProtocolCmCloseCall* must communicate with network control devices to terminate a connection between the local node and a remote node. The miniport driver must then call the [**NdisMCmDeactivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562818) function to initiate deactivation of the VC used for the call.

After the miniport driver terminates the connection, its *ProtocolCmCloseCall* can call the [**NdisMCmCloseCallComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562803) function to complete the call closure.

If the remote node hangs up an in-process call, the miniport driver calls the [**NdisCmDispatchIncomingCloseCall**](https://msdn.microsoft.com/library/windows/hardware/ff561670) function to inform NDISWAN and NDPROXY to tear down the incoming call.

### Closing a Line

A line is closed when the last application with an open handle to the line has closed the handle. A line is closed as a result of an application calling the TAPI **lineClose** function. This TAPI-function call causes the NDPROXY driver to initiate the closure of all calls on that line as described in the preceding section. The miniport driver should drop those calls and clean up their state.

### Closing a Session

Session termination can be initiated by either the upper layers or a CoNDIS WAN miniport driver. After the last client process has detached from the higher-level Telephony module, the NDPROXY driver will be informed that it must terminate its session with each of the registered adapters. To do so, the NDPROXY driver calls the [**NdisClCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff561626) function and passes the handle to the TAPI address family. NDIS in turn calls the miniport driver's [**ProtocolCmCloseAf**](https://msdn.microsoft.com/library/windows/hardware/ff570240) function. The miniport driver should terminate any related activities it has in progress on the specified adapter and release any relevant resources. After calling **NdisClCloseAddressFamily**, the client should consider the handle to the TAPI address family invalid.

Driver-initiated session termination can occur if the miniport driver is being unloaded in its *MiniportHaltEx* function. Typically, the miniport driver would complete any outstanding NDPROXY requests and notify NDISWAN that all calls are closing. If the miniport driver were reloaded again later, it would go through the same initialization process described previously.

The CoNDIS WAN miniport driver might also initiate session termination if it underwent some dynamic reconfiguration that necessitated a complete reinitialization of all clients and drivers. For example, if an adapter's line-device modeling (for example, the number of line devices supported) was changed on the fly.

 

 





