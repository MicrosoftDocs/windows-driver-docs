---
title: Stopping a Device to Disable It (Windows 98/Me)
author: windows-driver-content
description: Stopping a Device to Disable It (Windows 98/Me)
ms.assetid: 2fc42fe4-ad29-4a51-9560-74b568bcd129
keywords: ["disabling PnP devices"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Stopping a Device to Disable It (Windows 98/Me)


## <a href="" id="ddk-stopping-a-device-to-disable-it-windows-98-me-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Stopping%20a%20Device%20to%20Disable%20It%20%28Windows%2098/Me%29%20%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


