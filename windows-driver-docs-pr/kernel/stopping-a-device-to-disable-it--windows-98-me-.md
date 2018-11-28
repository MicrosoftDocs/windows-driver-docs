---
title: Stopping a Device to Disable It (Windows 98/Me)
description: Stopping a Device to Disable It (Windows 98/Me)
ms.assetid: 2fc42fe4-ad29-4a51-9560-74b568bcd129
keywords: ["disabling PnP devices"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Stopping a Device to Disable It (Windows 98/Me)





On Windows 98/Me, the PnP manager issues stop IRPs when Device Manager disables the device. (Windows 2000 and later versions of Windows issue [remove IRPs](removing-a-device.md) in this situation).

The PnP manager sends the stop IRPs in the following sequence:

1.  The PnP manager issues an [**IRP\_MN\_QUERY\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551725) to ask whether the drivers for a device can stop the device.

    If all the drivers in the device stack return STATUS\_SUCCESS, the drivers have put the device into a state (stop-pending) from which the device can be quickly stopped.

    The PnP manager queries as many device stacks as necessary to disable the device.

2.  If the **IRP\_MN\_QUERY\_STOP\_DEVICE** succeeds, the PnP manager issues an [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) to stop the device.

    The PnP manager sends the stop IRP only if the previous query-stop IRP for the device completed successfully. In response to the stop IRP, drivers release the device's hardware resources (such as its I/O ports) and fail any IRPs that require access to the device.

3.  If the **IRP\_MN\_QUERY\_STOP\_DEVICE** fails, the PnP manager sends an [**IRP\_MN\_CANCEL\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff550826) to cancel the query.

    In response to an **IRP\_MN\_CANCEL\_STOP\_DEVICE**, the drivers for a device return the device to the started state and resume processing I/O requests for the device.

    The PnP manager cancels the query-stop for a device stack if one driver in the stack failed the request. When the PnP manager cancels the query-stop on just one device stack, it sends the **IRP\_MN\_CANCEL\_STOP\_DEVICE** request because any drivers attached above the driver that failed the query have the device in the stop-pending state. When the **IRP\_MN\_CANCEL\_STOP\_DEVICE** succeeds, drivers have returned the device to the started state.

When a device is being disabled, its drivers cannot queue incoming IRPs because there is no guarantee when the device might be reenabled. Consequently, data might be lost.

 

 




