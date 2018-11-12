---
title: Summary of changes to port a miniport driver to NDIS 6.0
description: Summary of Changes Required to Port a Miniport Driver to NDIS 6.0
ms.assetid: 9357a84e-ab70-423d-9432-2245e1453069
keywords:
- porting miniport drivers WDK networking , required changes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Changes Required to Port a Miniport Driver to NDIS 6.0





This topic summarizes the changes that are required to port an NDIS 5.*x* miniport driver to NDIS 6.0. Porting earlier drivers is similar to porting NDIS 5.*x* drivers.

To run in the NDIS 6.0 environment, NDIS 5.*x* miniport drivers must be modified as follows:

<a href="" id="build-environment"></a>**Build Environment**  
Replace the preprocessor definition NDIS51\_MINIPORT\_DRIVER with NDIS60\_MINIPORT\_DRIVER.

<a href="" id="driver-initialization"></a>**Driver Initialization**  
-   Set the NDIS version to 6.0 in the **MajorNdisVersion** and **MinorNdisVersion** members of the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure that is passed to the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function.

-   Set the miniport driver version in the **MajorDriverVersion** and **MinorDriverVersion** members of the NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS structure to an appropriate driver-specific value.

-   Define new and replace obsolete entry points in the NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS structure. For example, the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function replaces the [**MiniportInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff550472) function.

-   If the miniport driver uses optional handlers, add the entry point for the [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function to the NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS structure. To register optional handlers, *MiniportSetOptions* calls the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function.

-   In the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, replace calls to the [**NdisMInitializeWrapper**](https://msdn.microsoft.com/library/windows/hardware/ff553547), [**NdisMRegisterUnloadHandler**](https://msdn.microsoft.com/library/windows/hardware/ff553606), and [**NdisMRegisterMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff553602) functions with a call to the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function. If an error occurs after a successful call to **NdisMRegisterMiniportDriver**, the driver must call [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) before **DriverEntry** returns. NDIS 6.0 miniport drivers do not call the [**NdisTerminateWrapper**](https://msdn.microsoft.com/library/windows/hardware/ff554814) function.

<a href="" id="driver-unload"></a>**Driver Unload**  
-   Create the miniport driver's [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function or, if it exists, update it. For NDIS 6.0, the *MiniportDriverUnload* entry point is in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure. NDIS 6.0 drivers do not call the [**NdisMRegisterUnloadHandler**](https://msdn.microsoft.com/library/windows/hardware/ff553606) function.

-   To deregister the miniport driver, *MiniportDriverUnload* must call the [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) function.

<a href="" id="miniport-adapter-initialization"></a>**Miniport Adapter Initialization**  
-   Rewrite the *MiniportInitialize* function (renamed *MiniportInitializeEx*) to support the [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565972) structure.

-   Replace calls to the [**NdisMSetAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff553619) and [**NdisMSetAttributesEx**](https://msdn.microsoft.com/library/windows/hardware/ff553623) functions with calls to the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function.

<a href="" id="miniport-adapter-halt-and-shutdown"></a>**Miniport Adapter Halt and Shutdown**  
-   To support the new *HaltAction* parameter, modify the miniport driver's [**MiniportHalt**](https://msdn.microsoft.com/library/windows/hardware/ff549451) function (renamed [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388)).

-   To support the new *ShutdownAction* parameter, modify the miniport driver's [**MiniportShutdown**](https://msdn.microsoft.com/library/windows/hardware/ff550533) function (renamed [*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449)).

<a href="" id="send-and-receive-code-paths"></a>**Send and Receive Code Paths**  
-   All NDIS 6.0 miniport drivers are deserialized.

-   Rewrite the send and receive code paths to use [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures and [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures instead of [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures.

-   If the driver uses scatter gather DMA (SGDMA) for send operations, add calls to the SGDMA functions as described in the following DMA change summary.

<a href="" id="dma"></a>**DMA**  
-   Bus master miniport drivers should call the [**NdisMRegisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563659) function from the *MiniportInitializeEx* function to allocate, initialize, and obtain the necessary information for scatter gather DMA (SGDMA) run-time operations. To release the SGDMA resources obtained with **NdisMRegisterScatterGatherDma**, call the [**NdisMDeregisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563581) function from *MiniportHaltEx*.

-   Define the [*MiniportSharedMemoryAllocateComplete*](https://msdn.microsoft.com/library/windows/hardware/ff559446) function (formerly [**MiniportAllocateComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549352)) for miniport drivers that call the [**NdisMAllocateSharedMemoryAsyncEx**](https://msdn.microsoft.com/library/windows/hardware/ff562784) function (formerly [**NdisMAllocateSharedMemoryAsync**](https://msdn.microsoft.com/library/windows/hardware/ff552304)). The entry point for *MiniportSharedMemoryAllocateComplete* is in the NDIS\_SG\_DMA\_DESCRIPTION structure that the driver passed to **NdisMRegisterScatterGatherDma**.

-   Define the [*MiniportProcessSGList*](https://msdn.microsoft.com/library/windows/hardware/ff559420) function The entry point for *MiniportProcessSGList* is in the NDIS\_SG\_DMA\_DESCRIPTION structure that the driver passed to **NdisMRegisterScatterGatherDma**.

-   When handling send requests, drivers call the [**NdisMAllocateNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff562776) function to allocate a scatter gather list (SGL). The driver uses the SGL, obtained from *MiniportProcessSGList*, to send data to a NIC. After the driver is done with the SGL, free the SGL by calling the [**NdisMFreeNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff563586) function.

<a href="" id="interrupts"></a>**Interrupts**  
-   Define the interrupt parameters in the [**NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566465) structure. Also, define the entry points for the interrupt functions in this structure..

-   Update the interrupt function entry points. For example, replace the [**MiniportISR**](https://msdn.microsoft.com/library/windows/hardware/ff550478) function with the [*MiniportInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559395) function.

-   Add optional entry points for message signaled interrupts (MSI). For example, define a [*MiniportMessageInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559407) function.

-   Replace the [**NdisMRegisterInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff553596) function with the [**NdisMRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563649) function.

-   Replace the [**NdisMDeregisterInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff553501) function with the [**NdisMDeregisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563575) function.

<a href="" id="oid-requests"></a>**OID Requests**  
-   Replace the miniport driver's [**MiniportQueryInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550490) function and [**MiniportSetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550530) function with the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. The *MiniportOidRequest* function uses [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structures instead of [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) structures.

-   Create the miniport driver's [*MiniportCancelOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559339) function. To cancel OID requests, NDIS calls *MiniportCancelOidRequest*. NDIS does not reset the miniport adapter.

<a href="" id="status-indications"></a>**Status Indications**  
-   Replace calls to the [**NdisMIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553538) function with calls to the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function and remove calls to the [**NdisMIndicateStatusComplete**](https://msdn.microsoft.com/library/windows/hardware/ff553540) function. To make status indications, pass the **NdisMIndicateStatusEx** function an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure.

<a href="" id="plug-and-play-events"></a>**Plug and Play Events**  
-   Replace the [**MiniportPnPEventNotify**](https://msdn.microsoft.com/library/windows/hardware/ff550487) function with the [*MiniportDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff559369) function.

<a href="" id="check-for-hang-and-reset"></a>**Check for Hang and Reset**  
-   Replace the [**MiniportCheckForHang**](https://msdn.microsoft.com/library/windows/hardware/ff549367) function with the [*MiniportCheckForHangEx*](https://msdn.microsoft.com/library/windows/hardware/ff559346) function.

-   Replace the [*MiniportReset*](https://msdn.microsoft.com/library/windows/hardware/ff550502) function with the [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function.

<a href="" id="new-adapter-states"></a>**New Adapter States**  
-   Include new miniport adapter pause and restart functionality. For more information about adapter states, see [Adapter States of a Miniport Driver](adapter-states-of-a-miniport-driver.md).

 

 





