---
title: Handling an IRP_MN_QUERY_REMOVE_DEVICE Request
description: Handling an IRP_MN_QUERY_REMOVE_DEVICE Request
ms.assetid: 30177e51-5312-4a24-972e-0c1c2d183d18
keywords: ["IRP_MN_QUERY_REMOVE_DEVICE"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling an IRP\_MN\_QUERY\_REMOVE\_DEVICE Request





The PnP manager sends this IRP to inform drivers that a device is about to be removed from the machine and to ask whether the device can be removed without disrupting the machine. It also sends this IRP when a user requests to update drivers for the device.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in the context of a system thread.

It does the following before sending this IRP to the drivers for a device:

-   Notifies all user-mode applications that registered for notification on the device (or a related device).

    This includes applications that registered for notification on the device, on one of the device's descendants (child device, child of child, and so forth), or on one of the device's removal relations. An application registers for such notification by calling **RegisterDeviceNotification**.

    In response to this notification, an application either prepares for device removal (closes handles to the device) or fails the query.

-   Notifies all kernel-mode drivers that registered for notification on the device (or a related device).

    This includes drivers that registered for notification on the device, on one of the device's descendants, or on one of the device's removal relations. A driver registers for this notification by calling [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526) with an event category of **EventCategoryTargetDeviceChange**.

    In response to this notification, a driver either prepares for device removal (closes handles to the device) or fails the query.

-   Sends [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705) IRPs to the drivers for the device's descendants.

-   (Windows 2000 and later systems) If a file system is mounted on the device, the PnP manager sends a query-remove request to the file system and any file system filters. If there are open handles to the device, the file system typically fails the query-remove request. If not, the file system typically locks the volume to prevent future creates from succeeding. If a mounted file system does not support a query-remove request, the PnP manager fails the query-remove request for the device.

If all of the above steps succeed, the PnP manager sends the **IRP\_MN\_QUERY\_REMOVE\_DEVICE** to the drivers for the device.

An **IRP\_MN\_QUERY\_REMOVE\_DEVICE** request is handled first by the top driver in the device stack and then by each next lower driver. A driver handles remove IRPs in its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine.

In response to an **IRP\_MN\_QUERY\_REMOVE\_DEVICE**, a driver must do the following:

1.  Determine whether the device can be removed from the machine without disrupting operation.

    A driver must fail a query-remove IRP if any of the following are true:

    -   If removing the device could result in losing data.

    -   If a component has an open handle to the device. (This is an issue on Windows 98/Me only. Windows 2000 and later versions of Windows track open handles and fail the query if there are open handles after the **IRP\_MN\_QUERY\_REMOVE\_DEVICE** completes.)

    -   If a driver has been notified (through an [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841) IRP) that the device is in the path for a paging, crash dump, or hibernation file.

    -   If the driver has an outstanding interface reference against the device. That is, the driver provided an interface in response to an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request and the interface has not been dereferenced.

2.  If the device cannot be removed, fail the query-remove IRP.

    Set **Irp-&gt;IoStatus.Status** to an appropriate error status (typically STATUS\_UNSUCCESSFUL), call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with IO\_NO\_INCREMENT, and return from the driver's *DispatchPnP* routine. Do not pass the IRP to the next lower driver.

3.  If the driver previously sent an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) request to enable the device for wake-up, cancel the wait-wake IRP.

4.  Record the previous PnP state of the device.

    A driver should record the PnP state that the device was in when the driver received the [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705) request because the driver must return the device to that state if the query is canceled ([**IRP\_MN\_CANCEL\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff550823)). The previous state is typically "started", which is the state that the device enters when the driver successfully completes an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request.

    However, other previous states are possible. For example, the user might have disabled the device through Device Manager. Or, in response to an **IRP\_MN\_QUERY\_CAPABILITIES** request, the parent bus driver (or a filter driver on the bus driver) might have reported that the device's hardware is disabled. In either case, the driver for the disabled device can receive an **IRP\_MN\_QUERY\_REMOVE\_DEVICE** request before it receives an **IRP\_MN\_START\_DEVICE** request.

5.  Finish the IRP:

    In a function or filter driver:

    -   Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

    -   Set up the next stack location with [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) and pass the IRP to the next lower driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

    -   Propagate the status from **IoCallDriver** as the return status from the *DispatchPnP* routine.

    -   Do not complete the IRP.

    In a bus driver:

    -   Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

    -   Complete the IRP ([**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)) with IO\_NO\_INCREMENT.

    -   Return from the *DispatchPnP* routine.

If any driver in the device stack fails an **IRP\_MN\_QUERY\_REMOVE\_DEVICE**, the PnP manager sends an **IRP\_MN\_CANCEL\_REMOVE\_DEVICE** to the device stack. This prevents drivers from requiring an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for a query-remove IRP to detect whether a lower driver failed the IRP.

Once a driver succeeds an **IRP\_MN\_QUERY\_REMOVE\_DEVICE** and it considers the device to be in the remove-pending state, the driver must fail any subsequent create requests for the device. The driver processes all other IRPs as usual, until the driver receives an **IRP\_MN\_CANCEL\_REMOVE\_DEVICE** or an **IRP\_MN\_REMOVE\_DEVICE**.

 

 




