---
title: Removing a Device in a Function Driver
description: Removing a Device in a Function Driver
ms.assetid: 46a75647-e72a-4194-be9d-070e3ac95650
keywords: ["function drivers WDK PnP", "DispatchPnP routine"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Removing a Device in a Function Driver





When removing a device, a function driver must undo any operations it performed to add and start the device. This discussion includes function drivers for peripheral devices and function drivers for bus devices.

A function driver removes a device using a procedure such as the following in its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine:

1. Is this a function driver for a bus device?

   If so, possibly delete any outstanding child PDOs for devices on the bus.

   If the bus driver handled a previous [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request for the child device, but the driver has not yet received the subsequent [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request, the bus driver leaves the child PDO intact. At some later time, when all handles to the child device are closed, the PnP manager will send the remove IRP for the child device and the bus driver deletes the child PDO at that time.

   If the bus driver handled a previous **IRP\_MN\_REMOVE\_DEVICE** request for the device, and there has been no subsequent **IRP\_MN\_SURPRISE\_REMOVAL** request, then the bus driver deletes the child PDO. In this case, the PnP manager ensures that any function and filter drivers have been removed from the child device (FDO and filter DOs have been deleted) before it sends a remove IRP to the parent bus device. The child PDO might still be present, so the bus driver must delete the child PDO before it removes the bus device.

2. Has the driver already handled a previous **IRP\_MN\_SURPRISE\_REMOVAL** request for this FDO?

   If so, perform any remaining clean-up and skip to step 8, [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

   A driver typically maintains a flag in the device extension that indicates whether the driver has handled an **IRP\_MN\_SURPRISE\_REMOVAL** request for the device.

3. If the driver previously enabled the device for wake-up, cancel the [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) request.

4. Ensure that the device is inactive.

   If the device is not already inactive in response to a prior **IRP\_MN\_QUERY\_REMOVE\_DEVICE**, the driver must mark the device as not accepting new requests and must complete any requests queued in this driver. The driver must fail any outstanding requests that require access to the device.

   A driver can use the **Io*Xxx*RemoveLock*Xxx*** routines to count outstanding I/O and to set an event indicating that remove processing can continue.

5. Perform any power-down operations.

   Each driver for the device performs its power-down operations, if any, when it receives the **IRP\_MN\_REMOVE\_DEVICE** request. The power policy owner for the device, typically the function driver, does not send a separate [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request to set the device power state to D3. The parent bus driver typically powers down the slot and notifies the power manager with [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) when the bus driver gets the remove IRP. For additional information, see [Power Management](implementing-power-management.md).

6. Disable any device interfaces by calling [**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700).

7. Free any hardware resources for the device in use by the driver.

   The exact operations depend on the device and the driver but can include disconnecting an interrupt with [**IoDisconnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff549089), freeing physical address ranges with [**MmUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff556387), and freeing I/O ports.

8. Pass the **IRP\_MN\_REMOVE\_DEVICE** request down to the next driver.

   Set up the IRP stack location for the next lower driver with [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) and pass the IRP to the next driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

   A driver is not required to wait for underlying drivers to finish their remove operations before continuing with its remove activities.

9. Remove the device object from the device stack with [**IoDetachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549087).

   Specify a pointer to the next lower device object as the *TargetDevice* parameter. The driver receives such a pointer from the call to [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) in the driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine.

10. Clean up any device-specific allocations, memory, events, and so forth.

11. Free the FDO with [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083).

12. Return from the [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine, propagating the return status from **IoCallDriver**.

A function driver does not specify an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for a remove IRP, nor does it complete the IRP. Remove IRPs are completed by the parent bus driver.

 

 




