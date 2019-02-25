---
title: MSI-X Pre-Registration
description: MSI-X Pre-Registration
ms.assetid: 93a09ebd-8a50-4c96-a926-54bb4686a618
keywords:
- MSI-X WDK networking , resource-requirements filter function
- message-signaled interrupts WDK networking , resource-requirements filter function
- MSIs WDK networking , resource-requirements filter function
- resource-requirements filter function WDK net
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MSI-X Pre-Registration





To support changing interrupt affinities for MSI-X or to remove message interrupt resources, a miniport driver must establish a resource-requirements filter function. This pre-registration step occurs before NDIS calls the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function.

To establish a resource-requirements filter function, the miniport driver must provide a [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function. When the miniport driver calls the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function from the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, the driver passes the entry point for *MiniportSetOptions* in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure. NDIS calls the *MiniportSetOptions* function in the context of **NdisMRegisterMiniportDriver**.

From *MiniportSetOptions*, the miniport driver calls the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function and specifies an [**NDIS\_MINIPORT\_PNP\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566475) structure. This structure defines the entry points for the [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332), [*MiniportRemoveDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559427), [*MiniportStartDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559452), and [*MiniportFilterResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff559384) functions.

When NDIS receives an add-device request from the Plug and Play (PnP) manager, NDIS calls the miniport driver's *MiniportAddDevice* function. The handle that NDIS passes to *MiniportAddDevice* in the *MiniportAdapterHandle* parameter is the handle that NDIS later passes to the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function.

In [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332), the driver initializes an [**NDIS\_MINIPORT\_ADD\_DEVICE\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565945) structure and passes this structure to the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function. The NDIS\_MINIPORT\_ADD\_DEVICE\_REGISTRATION\_ATTRIBUTES structure contains the **MiniportAddDeviceContext** member that is a handle to a miniport driver-allocated context area for the device. NDIS later provides this context handle to the [*MiniportRemoveDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559427), [*MiniportFilterResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff559384), [*MiniportStartDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559452), and [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) functions. For *MiniportInitializeEx*, the context handle is passed in the **MiniportAddDeviceContext** member of the [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565972) structure that the *MiniportInitParameters* parameter points to.

After NDIS calls [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332) and *MiniportAddDevice* returns NDIS\_STATUS\_SUCCESS, NDIS calls the *MiniportFilterResourceRequirements* function every time that it receives the [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550874) I/O request packet (IRP). *MiniportFilterResourceRequirements* can change the interrupt affinity for each MSI-X message, add message interrupt resources, or remove message interrupt resources if the driver will register for line-based interrupts in the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function. For more information about establishing an interrupt affinity policy, see [MSI-X Resource Filtering](msi-x-resource-filtering.md).

When NDIS receives a remove-device request from the PnP manager, NDIS calls the miniport driver's [*MiniportRemoveDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559427) function. The *MiniportRemoveDevice* function should undo the operations that the [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332) function performed.

 

 





