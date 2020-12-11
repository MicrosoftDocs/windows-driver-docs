---
title: Handling an IRP_MN_QUERY_STOP_DEVICE Request (Windows 2000 and later)
description: Handling an IRP_MN_QUERY_STOP_DEVICE Request (Windows 2000 and later)
keywords: ["IRP_MN_QUERY_STOP_DEVICE"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling an IRP\_MN\_QUERY\_STOP\_DEVICE Request (Windows 2000 and later)





An [**IRP\_MN\_QUERY\_STOP\_DEVICE**](./irp-mn-query-stop-device.md) request is handled first by the top driver in the device stack and then by each next lower driver. A driver handles stop IRPs in its [*DispatchPnP*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

In response to an **IRP\_MN\_QUERY\_STOP\_DEVICE**, a driver must do the following:

1.  Determine whether the device can be stopped, and its hardware resources released, without adverse affects.

    A driver must fail a query-stop IRP if any of the following are true:

    -   A driver has been notified (through [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](./irp-mn-device-usage-notification.md)) that the device is in the path of a paging, hibernation, or crash dump file.

    -   The device's hardware resources cannot be released.

    A driver might fail a query-stop IRP if the following is true:

    -   The driver must not drop I/O requests and does not have a mechanism for queuing IRPs.

        While the device is in the stopped state, a driver must hold IRPs that require access to the device. If a driver does not queue IRPs, it must not allow the device to be stopped and thus must fail a query-stop IRP.

        The exception to this rule is a device that is allowed to drop I/O. The drivers for such a device can succeed query-stop and stop requests without queuing IRPs.

2.  If the device cannot be stopped, fail the query-stop IRP.

    Set **Irp-&gt;IoStatus.Status** to an appropriate error status, call **IoCompleteRequest** with IO\_NO\_INCREMENT, and return from the driver's *DispatchPnP* routine. Do not pass the IRP to the next lower driver.

3.  If the device can be stopped and the driver queues IRPs, set the HOLD\_NEW\_REQUESTS flag in the device extension so subsequent IRPs will be queued (see [Holding Incoming IRPs When A Device Is Paused](holding-incoming-irps-when-a-device-is-paused.md)).

    Alternatively, the drivers for a device can defer completely pausing the device until the drivers receive the subsequent [**IRP\_MN\_STOP\_DEVICE**](./irp-mn-stop-device.md) request. Such drivers, however, must queue any requests that would prevent them from immediately succeeding the stop IRP when it arrives. Until the device is restarted, such drivers must queue requests such as the following:

    -   [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](./irp-mn-device-usage-notification.md) requests (for example, to put a paging file on the device).

    -   Requests for isochronous transfers.

    -   Create requests that would prevent the drivers from succeeding a stop IRP.

4.  If the device cannot have an IRP in progress fail, ensure that any outstanding requests that were passed to other driver routines and to lower drivers have completed.

    One way that a driver can achieve this is to use a reference count and an event to ensure that all requests have been completed:

    -   In its [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine, the driver defines an I/O reference count in the device extension and initializes the count to one.

    -   Also in its *AddDevice* routine, the driver creates an event with [**KeInitializeEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializeevent) and initializes the event to the Not-Signaled state with [**KeClearEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keclearevent).
    -   Each time it processes an IRP, the driver increments the reference count with [**InterlockedIncrement**](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedincrement).

    -   Each time it completes a request, the driver decrements the reference count with [**InterlockedDecrement**](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockeddecrement).

        The driver decrements the reference count in the [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine, if the request has one, or right after the call to [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) if the driver uses no *IoCompletion* routine for the request.

    -   When the driver receives an **IRP\_MN\_QUERY\_STOP\_DEVICE**, it decrements the reference count with **InterlockedDecrement**. If there are no outstanding requests, this reduces the reference count to zero.

    -   When the reference count reaches zero, the driver sets the event with [**KeSetEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetevent) signaling that the query-stop code can continue.

    As an alternative to the above procedure, a driver can serialize the **IRP\_MN\_QUERY\_STOP\_DEVICE** IRP behind any IRPs in progress.

5.  Perform any other steps required to put the device in the stop-pending state.

    After a driver succeeds a query-stop IRP, it must be ready to succeed an **IRP\_MN\_STOP\_DEVICE**.

6.  Finish the IRP.

    In a function or filter driver:

    -   Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

    -   Set up the next stack location with [**IoSkipCurrentIrpStackLocation**](./mm-bad-pointer.md) and pass the IRP to the next lower driver with [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver).

    -   Propagate the status from **IoCallDriver** as the return status from the *DispatchPnP* routine.

    -   Do not complete the IRP.

    In a bus driver:

    -   Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

        If, however, the devices on the bus use hardware resources, reevaluate the resource requirements of the bus and the child devices. If any of the requirements have changed, return STATUS\_RESOURCE\_REQUIREMENTS\_CHANGED instead of STATUS\_SUCCESS. This status indicates success but requests that the PnP manager requery your resources before sending the stop IRP.

    -   Complete the IRP ([**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest)) with IO\_NO\_INCREMENT.

    -   Return from the *DispatchPnP* routine.

If any driver in the device stack fails the **IRP\_MN\_QUERY\_STOP\_DEVICE**, the PnP manager sends an [**IRP\_MN\_CANCEL\_STOP\_DEVICE**](./irp-mn-cancel-stop-device.md) to the device stack. This prevents drivers from requiring an *IoCompletion* routine for a query-stop IRP to detect whether a lower driver failed the IRP.

 

