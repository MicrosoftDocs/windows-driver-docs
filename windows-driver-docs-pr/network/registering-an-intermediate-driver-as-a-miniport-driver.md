---
title: Registering an Intermediate Driver as a Miniport Driver
description: Registering an Intermediate Driver as a Miniport Driver
keywords:
- registering intermediate drivers
- intermediate drivers WDK networking , registering
- NDIS intermediate drivers WDK , registering
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering an Intermediate Driver as a Miniport Driver





An intermediate driver calls [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) to export its *MiniportXxx* functions. The *NdisMiniportDriverHandle* that is returned by **NdisMRegisterMiniportDriver** must be retained by the intermediate driver and input to NDIS when the driver calls [**NdisIMInitializeDeviceInstanceEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisiminitializedeviceinstanceex).

The intermediate driver must:

1.  Zero-initialize an [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure with [**NdisZeroMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiszeromemory).

2.  Store the addresses of the mandatory *MiniportXxx* functions, as well as any optional *MiniportXxx* functions that the driver exports.

An intermediate driver that supports NDIS 6.0 features must register as a version 6.0 miniport driver. For more information about specifying miniport driver version numbers, see [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics).

You must set the following entries in *MiniportCharacteristics* to a valid *MiniportXxx* function address unless the function is optional and is not exported. If the driver does not export the function, set the address to **NULL**.

<a href="" id="setoptionshandler"></a>**SetOptionsHandler**  
[*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) is an optional function. NDIS calls *MiniportSetOptions* so the intermediate driver can specify optional handlers.

<a href="" id="initializehandlerex"></a>**InitializeHandlerEx**  
NDIS calls [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) as a result of the intermediate driver calling **NdisIMInitializeDeviceInstanceEx** to initialize its miniport adapter operations for the virtual miniport being initialized.

<a href="" id="halthandlerex"></a>**HaltHandlerEx**  
[*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) is a required function. NDIS calls *MiniportHaltEx* if the virtual miniport device that the intermediate driver exposed is disabled or stopped, or if the intermediate driver called [**NdisIMDeInitializeDeviceInstance**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisimdeinitializedeviceinstance) to initiate its removal.

<a href="" id="unloadhandler"></a>**UnloadHandler**  
[*MiniportDriverUnload*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_unload) is a required function. NDIS calls *MiniportDriverUnload* to unload the intermediate driver.

<a href="" id="pausehandler"></a>**PauseHandler**  
[*MiniportPause*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pause) is a required function. NDIS calls *MiniportPause* to stop the flow of network data through a specified virtual miniport of the intermediate driver.

<a href="" id="restarthandler"></a>**RestartHandler**  
[**MiniportRestart**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_restart) is a required function. NDIS calls *MiniportRestart* to restart the flow of network data through a specified virtual miniport of the intermediate driver.

<a href="" id="oidrequesthandler"></a>**OidRequestHandler**  
[*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) receives OID\_*XXX* requests originating from an overlying driver that has called [**NdisOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisoidrequest) or from NDIS. The intermediate driver might handle a request or pass it on to the underlying miniport driver.

<a href="" id="sendnetbufferlistshandler"></a>**SendNetBufferListsHandler**  
[*MiniportSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists) receives an array of one or more pointers to [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures that specify network data for transmission over the network. Every intermediate driver should supply a *MiniportSendNetBufferLists* function. For more information, see [Transmitting Network Data Through an Intermediate Driver](transmitting-network-data-through-an-intermediate-driver.md).

<a href="" id="returnnetbufferlistshandler"></a>**ReturnNetBufferListsHandler**  
[*MiniportReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_return_net_buffer_lists) receives a returned [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure that it previously indicated to a higher-level driver by calling **NdisMIndicateReceiveNetBufferLists**. The call to **NdisMIndicateReceiveNetBufferLists** relinquishes control of the resources indicated to the higher-level driver. After the higher-level driver consumes each indication, the intermediate driver allocated NET\_BUFFER\_LIST structure and the resources it describes are returned to the *MiniportReturnNetBufferLists* function.

<a href="" id="cancelsendhandler"></a>**CancelSendHandler**  
[*MiniportCancelSend*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_send) is a required function. NDIS calls *MiniportCancelSend* to cancel a send request.

<a href="" id="checkforhanghandler"></a>**CheckForHangHandler**  
[*MiniportCheckForHangEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_check_for_hang) is not required for intermediate drivers, so they should set this entry point to **NULL**.

<a href="" id="resethandlerex"></a>**ResetHandlerEx**  
[*MiniportResetEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset) is not required for intermediate drivers, so they should set this entry point to **NULL**.

<a href="" id="devicepnpeventnotifyhandler"></a>**DevicePnPEventNotifyHandler**  
The entry point for the [*MiniportDevicePnPEventNotify*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_device_pnp_event_notify) function.

<a href="" id="shutdownhandlerex"></a>**ShutdownHandlerEx**  
[*MiniportShutdownEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_shutdown) is a required function. *MiniportShutdownEx* restores the virtual miniport to its initial state (before the intermediate driver's **DriverEntry** routine runs).

<a href="" id="canceloidrequesthandler"></a>**CancelOidRequestHandler**  
[*MiniportCancelOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_oid_request) is a required function. NDIS calls *MiniportCancelOidRequest* to cancel an OID request.

An intermediate driver might require other *MiniportXxx* functions that are implementation specific. For information about registering optional, see [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md).

Certain miniport driver handler functions are never supplied by an intermediate driver. Reasons for this include: such drivers do not manage interrupting devices, or such drivers do not allocate buffers at raised IRQL.

**Note**  Intermediate drivers must include pause and restart functionality. Include support for pause and restart of virtual miniports, if needed, when NDIS pauses an underlying driver stack. For more information about pause and restart, see [Driver Stack Management](driver-stack-management.md).

 

 

