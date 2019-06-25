---
title: Handling an IRP_MN_STOP_DEVICE Request (Windows 2000 and later)
description: Handling an IRP_MN_STOP_DEVICE Request (Windows 2000 and later)
ms.assetid: 5e91748c-d03a-48f7-a9cc-df2801d8a555
keywords: ["IRP_MN_STOP_DEVICE"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling an IRP\_MN\_STOP\_DEVICE Request (Windows 2000 and later)





An [**IRP\_MN\_STOP\_DEVICE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-stop-device) request is handled first by the top driver in the device stack and then by each next lower driver. A driver handles stop IRPs in its [*DispatchPnP*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) routine.

A driver handles an **IRP\_MN\_STOP\_DEVICE** request with a procedure such as the following:

1.  Ensure that the device is paused.

    If a driver did not completely pause the device in response to the [**IRP\_MN\_QUERY\_STOP\_DEVICE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-stop-device) request, it must do so now. Set a HOLD\_NEW\_REQUESTS flag in the device extension and perform any other necessary operations to pause the device.

    The device might lose power during the resource-rebalance operation and thus might lose device state. Drivers for the device should save any device state information and restore it when they receive the subsequent [**IRP\_MN\_START\_DEVICE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-start-device) request.

2.  Release the hardware resources for the device.

    In a function driver, the exact operations depend on the device and the driver but can include disconnecting an interrupt with [**IoDisconnectInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iodisconnectinterrupt), freeing physical address ranges with [**MmUnmapIoSpace**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-mmunmapiospace), and freeing I/O ports.

    If a filter or bus driver acquired any hardware resources for the device, that driver must release the resources in response to an **IRP\_MN\_STOP\_DEVICE** request.

3.  Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

4.  Pass the IRP to the next lower driver or complete the IRP.

    -   In a function or filter driver, set up the next stack location with [**IoSkipCurrentIrpStackLocation**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer), pass the IRP to the next lower driver with [**IoCallDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocalldriver), and return the status from **IoCallDriver** as the return status from the *DispatchPnP* routine. Do not complete the IRP.

    -   In a bus driver, complete the IRP using [**IoCompleteRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocompleterequest) with IO\_NO\_INCREMENT and return from the *DispatchPnP* routine.

While the device is stopped to rebalance resources, a driver cannot start any IRPs that access the device. A driver must queue such IRPs, as described in [Holding Incoming IRPs When A Device Is Paused](holding-incoming-irps-when-a-device-is-paused.md), or fail them if the driver does not implement an IRP-holding queue and must not drop I/O requests.

 

 




