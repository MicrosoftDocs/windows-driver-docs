---
title: Registering an Intermediate Driver as a Miniport Driver
description: Registering an Intermediate Driver as a Miniport Driver
ms.assetid: a01bc0f4-4a03-4d44-88c0-7029042d6953
keywords:
- registering intermediate drivers
- intermediate drivers WDK networking , registering
- NDIS intermediate drivers WDK , registering
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering an Intermediate Driver as a Miniport Driver





An intermediate driver calls [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) to export its *MiniportXxx* functions. The *NdisMiniportDriverHandle* that is returned by **NdisMRegisterMiniportDriver** must be retained by the intermediate driver and input to NDIS when the driver calls [**NdisIMInitializeDeviceInstanceEx**](https://msdn.microsoft.com/library/windows/hardware/ff562727).

The intermediate driver must:

1.  Zero-initialize an [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure with [**NdisZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff564698).

2.  Store the addresses of the mandatory *MiniportXxx* functions, as well as any optional *MiniportXxx* functions that the driver exports.

An intermediate driver that supports NDIS 6.0 features must register as a version 6.0 miniport driver. For more information about specifying miniport driver version numbers, see [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958).

You must set the following entries in *MiniportCharacteristics* to a valid *MiniportXxx* function address unless the function is optional and is not exported. If the driver does not export the function, set the address to **NULL**.

<a href="" id="setoptionshandler"></a>**SetOptionsHandler**  
[*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) is an optional function. NDIS calls *MiniportSetOptions* so the intermediate driver can specify optional handlers.

<a href="" id="initializehandlerex"></a>**InitializeHandlerEx**  
NDIS calls [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) as a result of the intermediate driver calling **NdisIMInitializeDeviceInstanceEx** to initialize its miniport adapter operations for the virtual miniport being initialized.

<a href="" id="halthandlerex"></a>**HaltHandlerEx**  
[*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) is a required function. NDIS calls *MiniportHaltEx* if the virtual miniport device that the intermediate driver exposed is disabled or stopped, or if the intermediate driver called [**NdisIMDeInitializeDeviceInstance**](https://msdn.microsoft.com/library/windows/hardware/ff562721) to initiate its removal.

<a href="" id="unloadhandler"></a>**UnloadHandler**  
[*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) is a required function. NDIS calls *MiniportDriverUnload* to unload the intermediate driver.

<a href="" id="pausehandler"></a>**PauseHandler**  
[*MiniportPause*](https://msdn.microsoft.com/library/windows/hardware/ff559418) is a required function. NDIS calls *MiniportPause* to stop the flow of network data through a specified virtual miniport of the intermediate driver.

<a href="" id="restarthandler"></a>**RestartHandler**  
[**MiniportRestart**](https://msdn.microsoft.com/library/windows/hardware/ff559435) is a required function. NDIS calls *MiniportRestart* to restart the flow of network data through a specified virtual miniport of the intermediate driver.

<a href="" id="oidrequesthandler"></a>**OidRequestHandler**  
[*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) receives OID\_*XXX* requests originating from an overlying driver that has called [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) or from NDIS. The intermediate driver might handle a request or pass it on to the underlying miniport driver.

<a href="" id="sendnetbufferlistshandler"></a>**SendNetBufferListsHandler**  
[*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) receives an array of one or more pointers to [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures that specify network data for transmission over the network. Every intermediate driver should supply a *MiniportSendNetBufferLists* function. For more information, see [Transmitting Network Data Through an Intermediate Driver](transmitting-network-data-through-an-intermediate-driver.md).

<a href="" id="returnnetbufferlistshandler"></a>**ReturnNetBufferListsHandler**  
[*MiniportReturnNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559437) receives a returned [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure that it previously indicated to a higher-level driver by calling **NdisMIndicateReceiveNetBufferLists**. The call to **NdisMIndicateReceiveNetBufferLists** relinquishes control of the resources indicated to the higher-level driver. After the higher-level driver consumes each indication, the intermediate driver allocated NET\_BUFFER\_LIST structure and the resources it describes are returned to the *MiniportReturnNetBufferLists* function.

<a href="" id="cancelsendhandler"></a>**CancelSendHandler**  
[*MiniportCancelSend*](https://msdn.microsoft.com/library/windows/hardware/ff559342) is a required function. NDIS calls *MiniportCancelSend* to cancel a send request.

<a href="" id="checkforhanghandler"></a>**CheckForHangHandler**  
[*MiniportCheckForHangEx*](https://msdn.microsoft.com/library/windows/hardware/ff559346) is not required for intermediate drivers, so they should set this entry point to **NULL**.

<a href="" id="resethandlerex"></a>**ResetHandlerEx**  
[*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) is not required for intermediate drivers, so they should set this entry point to **NULL**.

<a href="" id="devicepnpeventnotifyhandler"></a>**DevicePnPEventNotifyHandler**  
The entry point for the [*MiniportDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff559369) function.

<a href="" id="shutdownhandlerex"></a>**ShutdownHandlerEx**  
[*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449) is a required function. *MiniportShutdownEx* restores the virtual miniport to its initial state (before the intermediate driver's **DriverEntry** routine runs).

<a href="" id="canceloidrequesthandler"></a>**CancelOidRequestHandler**  
[*MiniportCancelOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559339) is a required function. NDIS calls *MiniportCancelOidRequest* to cancel an OID request.

An intermediate driver might require other *MiniportXxx* functions that are implementation specific. For information about registering optional, see [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md).

Certain miniport driver handler functions are never supplied by an intermediate driver. Reasons for this include: such drivers do not manage interrupting devices, or such drivers do not allocate buffers at raised IRQL.

**Note**  Intermediate drivers must include pause and restart functionality. Include support for pause and restart of virtual miniports, if needed, when NDIS pauses an underlying driver stack. For more information about pause and restart, see [Driver Stack Management](driver-stack-management.md).

 

 

 





