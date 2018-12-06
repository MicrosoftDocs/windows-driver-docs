---
title: Removing a Device in a Bus Driver
description: Removing a Device in a Bus Driver
ms.assetid: f3961c29-02e1-41f0-bb7f-784bcdb57eb0
keywords: ["bus drivers WDK PnP", "DispatchPnP routine"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Removing a Device in a Bus Driver





When removing a child device (child PDO), the parent bus driver must undo any operations it performed to add and start the device.

A bus driver removes a child device with a procedure such as the following in its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine:

1.  Has the driver handled a previous [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request for this PDO?

    If so, perform any remaining clean-up and skip to step 4.

    A driver typically maintains a flag in the device extension that indicates whether the driver has handled an **IRP\_MN\_SURPRISE\_REMOVAL** request for the device.

2.  Complete any requests queued in the driver.

3.  Remove power from the device, if the bus driver is capable of doing so, and notify the power manager by calling [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765).

    The bus driver powers down the child device, if possible, and notifies the power manager of the device's change in power state. The bus driver does this in response to the [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request; the device's power policy owner does not send an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request when the device is being removed. For additional information, see [Power Management](implementing-power-management.md).

4.  If the bus driver reported this device in its most recent response to an [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670) request for **BusRelations**, the device is still physically present on the machine. In this case, the bus driver:

    -   Retains the PDO for the device until the device has been physically removed.

    -   Sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

    -   Completes the IRP with [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343).

    -   Returns from the [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine.

    The bus driver must continue to report this device in subsequent enumerations (**IRP\_MN\_QUERY\_DEVICE\_RELATIONS** for **BusRelations**) until the device is physically removed. The PnP manager keeps track of whether an enumerated device has been added and started.

5.  If the device was not included in the bus driver's most recent response to an **IRP\_MN\_QUERY\_DEVICE\_RELATIONS** request for **BusRelations**, the bus driver considers the device to be physically removed from the machine. In this case, the bus driver does the following:

    -   Cleans up device-specific allocations, memory, events, and so forth.

    -   Sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

    -   Completes the IRP with [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343).

    -   Frees the PDO with [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083).

        The bus driver must delete the PDO if the driver omitted the device from its most recent **BusRelations** list. If a user plugs the device into the machine again, the bus driver must create a new PDO in response to the next **BusRelations** query. If a bus driver reuses the same PDO for a new instance of a device, the machine will not operate properly.

    -   Returns from the *DispatchPnP* routine.

If the device is still present when the PnP manager sends the **IRP\_MN\_REMOVE\_DEVICE** request, the bus driver retains the PDO. If, at some later time, the device is physically removed from the bus, the PnP manager sends another **IRP\_MN\_REMOVE\_DEVICE**. Upon receipt of the subsequent remove IRP, the bus driver deletes the PDO for the device.

A bus driver must be able to handle an **IRP\_MN\_REMOVE\_DEVICE** for a device it has already removed and whose PDO is marked for deletion. In response to such an IRP, the bus driver can succeed the IRP or return STATUS\_NO\_SUCH\_DEVICE. The PDO for the device has not yet been deleted in this case, despite the bus driver's previous call to **IoDeleteDevice**, because some component still has a reference to the object. Therefore, the bus driver can access the PDO while handling the second remove IRP. The bus driver must not call **IoDeleteDevice** a second time for the PDO; the I/O system deletes the PDO when its reference count reaches zero.

A bus driver does not remove its data structures for a child device until it receives an **IRP\_MN\_REMOVE\_DEVICE** request for the device. A bus driver might detect that a device has been removed and call [**IoInvalidateDeviceRelations**](https://msdn.microsoft.com/library/windows/hardware/ff549353), but it must not delete the device's PDO until the PnP manager sends an **IRP\_MN\_REMOVE\_DEVICE** request.

 

 




