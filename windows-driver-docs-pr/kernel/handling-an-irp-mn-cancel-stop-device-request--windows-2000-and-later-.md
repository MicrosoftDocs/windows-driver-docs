---
title: Handling an IRP_MN_CANCEL_STOP_DEVICE Request (Windows 2000 and Later)
description: Handling an IRP_MN_CANCEL_STOP_DEVICE Request (Windows 2000 and later)
keywords: ["IRP_MN_CANCEL_STOP_DEVICE"]
ms.date: 06/16/2017
---

# Handling an IRP\_MN\_CANCEL\_STOP\_DEVICE Request (Windows 2000 and later)





An [**IRP\_MN\_CANCEL\_STOP\_DEVICE**](./irp-mn-cancel-stop-device.md) request must be handled first by the parent bus driver for a device and then by each next higher driver in the device stack. A driver handles stop IRPs in its [*DispatchPnP*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

In response to an **IRP\_MN\_CANCEL\_STOP\_DEVICE** request, a driver must return the device to its started state and resume normal operation. Drivers must succeed a cancel-stop IRP.

A driver handles an **IRP\_MN\_CANCEL\_STOP\_DEVICE** request with a procedure such as the following:

1.  Postpone restarting the device until lower drivers have completed their restart operations. (See [Postponing PnP IRP Processing Until Lower Drivers Finish](postponing-pnp-irp-processing-until-lower-drivers-finish.md).)

2.  After lower drivers finish, return the device to its started state.

    Exact operations depend on the device and the driver.

3.  Start IRPs in the IRP-holding queue.

    If the driver was holding requests while the device was in the stop-pending state, clear the HOLD\_NEW\_REQUESTS flag and start the IRPs in the IRP-holding queue. See [Holding Incoming IRPs When A Device Is Paused](holding-incoming-irps-when-a-device-is-paused.md) for more information.

4.  Complete the IRP with [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest).

    -   In a function or filter driver:

        The driver's [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine returned STATUS\_MORE\_PROCESSING\_REQUIRED, as described in [Postponing PnP IRP Processing Until Lower Drivers Finish](postponing-pnp-irp-processing-until-lower-drivers-finish.md), so the driver's *DispatchPnP* routine must call **IoCompleteRequest** to resume I/O completion processing.

        The driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS, calls **IoCompleteRequest** with a priority boost of IO\_NO\_INCREMENT, and returns STATUS\_SUCCESS from its *DispatchPnP* routine.

        Drivers must not fail this operation. If a driver fails the restart IRP, the device is in an inconsistent state and will not operate properly.

    -   In a parent bus driver:

        The driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS and calls **IoCompleteRequest** specifying a priority boost of IO\_NO\_INCREMENT. The bus driver returns STATUS\_SUCCESS from its *DispatchPnP* routine.

        A bus driver must not fail this operation. If a driver fails the restart IRP, the device is in an inconsistent state and will not operate properly.

A driver might receive a spurious cancel-stop request when the device is started and active. This can occur, for example, if the driver (or a driver higher in the device stack) failed an [**IRP\_MN\_QUERY\_STOP\_DEVICE**](./irp-mn-query-stop-device.md) request. When a device is started and active, drivers can safely succeed spurious cancel-stop requests for the device.

 

