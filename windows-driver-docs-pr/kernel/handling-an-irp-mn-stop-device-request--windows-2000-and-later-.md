---
title: Handling an IRP\_MN\_STOP\_DEVICE Request (Windows 2000 and later)
author: windows-driver-content
description: Handling an IRP\_MN\_STOP\_DEVICE Request (Windows 2000 and later)
MS-HAID:
- 'PlugPlay\_4edcea93-bfbd-45a6-84a8-f399811209d7.xml'
- 'kernel.handling\_an\_irp\_mn\_stop\_device\_request\_\_windows\_2000\_and\_later\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5e91748c-d03a-48f7-a9cc-df2801d8a555
keywords: ["IRP_MN_STOP_DEVICE"]
---

# Handling an IRP\_MN\_STOP\_DEVICE Request (Windows 2000 and later)


## <a href="" id="ddk-handling-an-irp-mn-stop-device-request-windows-2000-and-later-kg"></a>


An [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) request is handled first by the top driver in the device stack and then by each next lower driver. A driver handles stop IRPs in its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine.

A driver handles an **IRP\_MN\_STOP\_DEVICE** request with a procedure such as the following:

1.  Ensure that the device is paused.

    If a driver did not completely pause the device in response to the [**IRP\_MN\_QUERY\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551725) request, it must do so now. Set a HOLD\_NEW\_REQUESTS flag in the device extension and perform any other necessary operations to pause the device.

    The device might lose power during the resource-rebalance operation and thus might lose device state. Drivers for the device should save any device state information and restore it when they receive the subsequent [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request.

2.  Release the hardware resources for the device.

    In a function driver, the exact operations depend on the device and the driver but can include disconnecting an interrupt with [**IoDisconnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff549089), freeing physical address ranges with [**MmUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff556387), and freeing I/O ports.

    If a filter or bus driver acquired any hardware resources for the device, that driver must release the resources in response to an **IRP\_MN\_STOP\_DEVICE** request.

3.  Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

4.  Pass the IRP to the next lower driver or complete the IRP.

    -   In a function or filter driver, set up the next stack location with [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355), pass the IRP to the next lower driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336), and return the status from **IoCallDriver** as the return status from the *DispatchPnP* routine. Do not complete the IRP.

    -   In a bus driver, complete the IRP using [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with IO\_NO\_INCREMENT and return from the *DispatchPnP* routine.

While the device is stopped to rebalance resources, a driver cannot start any IRPs that access the device. A driver must queue such IRPs, as described in [Holding Incoming IRPs When A Device Is Paused](holding-incoming-irps-when-a-device-is-paused.md), or fail them if the driver does not implement an IRP-holding queue and must not drop I/O requests.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20an%20IRP_MN_STOP_DEVICE%20Request%20%28Windows%202000%20and%20later%29%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


