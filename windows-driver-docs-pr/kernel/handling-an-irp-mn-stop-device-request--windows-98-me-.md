---
title: Handling an IRP_MN_STOP_DEVICE Request (Windows 98/Me)
description: Handling an IRP_MN_STOP_DEVICE Request (Windows 98/Me)
ms.assetid: 8e44561a-f494-48ce-ab61-aa47cd4e1c64
keywords: ["IRP_MN_STOP_DEVICE"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling an IRP\_MN\_STOP\_DEVICE Request (Windows 98/Me)





On Windows 98/Me, the PnP manager usually sends an [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) request after a successful query-stop. However, if the device stack previously failed an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request, the PnP manager sends an **IRP\_MN\_STOP\_DEVICE** request without a preceding query.

An **IRP\_MN\_STOP\_DEVICE** request is handled first by the top driver in the device stack and then by each next lower driver. A driver handles stop IRPs in its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine.

A driver handles an **IRP\_MN\_STOP\_DEVICE** request with a procedure such as the following:

1.  Ensure that the device is paused.

    If a driver did not completely pause the device in response to an [**IRP\_MN\_QUERY\_STOP**](https://msdn.microsoft.com/library/windows/hardware/ff551725) request, it must do so now.

    The device might lose power while it is stopped and thus might lose device state. Drivers for the device should save any device state information and restore it when they receive the subsequent **IRP\_MN\_START\_DEVICE** request.

2.  Release the hardware resources for the device.

    In a function driver, the exact operations depend on the device and the driver but can include disconnecting an interrupt with [**IoDisconnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff549089), freeing physical address ranges with [**MmUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff556387), and freeing I/O ports.

    If a filter or bus driver acquired any hardware resources for the device, that driver must release the resources in response to an **IRP\_MN\_STOP\_DEVICE** request.

3.  Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

4.  Pass the IRP to the next lower driver or complete the IRP.

    -   In a function or filter driver, set up the next stack location with [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355), pass the IRP to the next lower driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336), and return the status from **IoCallDriver** as the return status from the *DispatchPnP* routine. Do not complete the IRP.

    -   In a bus driver, complete the IRP using [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with IO\_NO\_INCREMENT and return from the *DispatchPnP* routine.

A driver cannot start any IRPs that access the device while the device is stopped. A driver must fail such IRPs.

 

 




