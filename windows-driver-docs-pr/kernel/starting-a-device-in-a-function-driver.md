---
title: Starting a Device in a Function Driver
description: Starting a Device in a Function Driver
ms.assetid: 148a3128-9cb1-4a2c-a62e-45199476d968
keywords: ["function drivers WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Starting a Device in a Function Driver





A function driver sets an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine, passes an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request down the device stack, and postpones its start operations until all lower drivers have finished with the IRP. See [Postponing PnP IRP Processing Until Lower Drivers Finish](postponing-pnp-irp-processing-until-lower-drivers-finish.md) for detailed information about using a kernel event and an *IoCompletion* routine to postpone IRP processing.

When its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine regains control after all lower drivers have finished with the IRP, the function driver performs its tasks for starting the device. A function driver starts the device with a procedure like the following:

1.  If a lower driver failed the IRP ([**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) returned an error), do not continue processing the IRP. Do any necessary cleanup and return from the *DispatchPnP* routine (go to the last step in this list).

2.  If lower drivers processed the IRP successfully, start the device.

    The exact steps to start a device vary from device to device. Such steps might include mapping I/O space, initializing hardware registers, setting the device in the D0 power state, and connecting the interrupt with [**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371). If the driver is restarting a device after an [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) request, the driver might have device state to restore.

    The device must be powered on before any drivers can access it. See [Powering Up a Device](powering-up-a-device.md) for more information.

    If the device should be enabled for wake-up, its power policy owner (usually the function driver) should send a wait/wake IRP after it powers up the device and before it completes the **IRP\_MN\_START\_DEVICE** request. For details, see [Sending a Wait/Wake IRP](sending-a-wait-wake-irp.md).

3.  Start IRPs in the IRP-holding queue.

    Clear the driver-defined HOLD\_NEW\_REQUESTS flag and start the IRPs in the IRP-holding queue. Drivers should do this when starting a device for the first time and when restarting a device after a query-stop or stop IRP. See [Holding Incoming IRPs When A Device Is Paused](holding-incoming-irps-when-a-device-is-paused.md) for more information.

4.  \[Optional\] Enable interfaces for the device by calling [**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700).

    Enable the interfaces, if any, that the driver previously registered in its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine (or in an INF or by another component such as a co-installer).

    On Windows 2000 and later versions of Windows, the PnP manager does not send notification of device-interface arrivals until the **IRP\_MN\_START\_DEVICE** IRP completes, indicating that all the drivers for the device have completed their start operations. The PnP manager also fails any create requests that arrive before all the drivers for the device complete the start IRP.

5.  Complete the IRP.

    The function driver's *IoCompletion* routine returned STATUS\_MORE\_PROCESSING\_REQUIRED, as described in [Postponing PnP IRP Processing Until Lower Drivers Finish](postponing-pnp-irp-processing-until-lower-drivers-finish.md), so the function driver's *DispatchPnP* routine must call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to resume I/O completion processing.

    If the function driver's start operations were successful, the driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS, calls **IoCompleteRequest** with a priority boost of IO\_NO\_INCREMENT, and returns STATUS\_SUCCESS from its *DispatchPnP* routine.

    If the function driver encounters an error during its start operations, the driver sets an error status in the IRP, calls **IoCompleteRequest** with IO\_NO\_INCREMENT, and returns the error from its *DispatchPnP* routine.

    If a lower driver failed the IRP (**IoCallDriver** returned an error), the function driver calls **IoCompleteRequest** with IO\_NO\_INCREMENT and returns the **IoCallDriver** error from its *DispatchPnP* routine. The function driver does not set **Irp-&gt;IoStatus.Status** in this case because the status has already been set by the lower driver that failed the IRP.

When a function driver receives an **IRP\_MN\_START\_DEVICE** request, it should examine the structures at **IrpSp-&gt;Parameters.StartDevice.AllocatedResources** and **IrpSp-&gt;Parameters.StartDevice.AllocatedResourcesTranslated**, which describe the raw and translated resources, respectively, that the PnP manager has assigned to the device. Drivers should save a copy of each resource list in the device extension as a debugging aid.

The resource lists are paired [**CM\_RESOURCE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff541994) structures, in which each element of the raw list corresponds to the same element of the translated list. For example, if **AllocatedResources.List**\[0\] describes a raw I/O port range, then **AllocatedResourcesTranslated.List**\[0\] describes the same range after translation. Each translated resource includes a physical address and the type of the resource.

If a driver is assigned a translated memory resource (**CmResourceTypeMemory**), it must call [**MmMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff554618) to map the physical address into a virtual address through which it can access device registers. For a driver to operate in a platform independent manner, it should check each returned, translated resource and map it, if necessary.

A function driver should do the following in response to an **IRP\_MN\_START\_DEVICE** to ensure access to all device resources:

1.  Copy **IrpSp-&gt;Parameters.StartDevice.AllocatedResources** to the device extension.

2.  Copy **IrpSp-&gt;Parameters.StartDevice.AllocatedResourcesTranslated** to the device extension.

3.  In a loop, inspect each descriptor element in **AllocatedResourcesTranslated**. If the descriptor resource type is **CmResourceTypeMemory**, call **MmMapIoSpace**, passing the physical address and length of the translated resource.

When the driver receives an **IRP\_MN\_STOP\_DEVICE**, **IRP\_MN\_REMOVE\_DEVICE**, or **IRP\_MN\_SURPRISE\_REMOVAL** request, it must release the mappings by calling [**MmUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff556387) in a similar loop. The driver should also call **MmUnmapIoSpace** if it must fail the **IRP\_MN\_START\_DEVICE** request.

See [Mapping Bus-Relative Addresses to Virtual Addresses](mapping-bus-relative-addresses-to-virtual-addresses.md) for more information.

 

 




