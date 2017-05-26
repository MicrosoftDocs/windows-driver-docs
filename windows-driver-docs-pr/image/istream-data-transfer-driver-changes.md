---
title: IStream Data Transfer Driver Changes
author: windows-driver-content
description: IStream Data Transfer Driver Changes
ms.assetid: 1c837e4f-8d53-40ed-8f5b-0d525c7dd758
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IStream Data Transfer Driver Changes


To minimize changes to drivers that were developed before Windows Vista, the drivers do not have to implement any new interfaces to support **IStream** data transfer. Instead, a new interface was exposed through the [IWiaMiniDrvCallBack interface](https://msdn.microsoft.com/library/windows/hardware/ff543943). Drivers can call **IWiaMiniDrvCallBack::QueryInterface** for the new **IWiaTransfer** callback function, which will give them access to the data streams and status notifications. The **IWiaTransfer** interface is described in the Microsoft Windows SDK documentation.

The data transfer code inside the driver is now more simple because all transfers are handled the same way, with no file or memory transfer branch logic.

Drivers that do not support the **IStream** transfer model typically perform the following steps:

1.  Check the flags to determine if the request is for an upload or a download.

2.  Acquire the [IWiaMiniDrvCallBack](https://msdn.microsoft.com/library/windows/hardware/ff543943) interface.

3.  Receive a destination stream from the callback function.

4.  Perform a data transfer loop:
    1.  Receive data from the device.
    2.  Write data to the stream.

However, for drivers that implement the new **IStream** transfer model, the WIA service will not call [**IWiaMiniDrv::drvWriteItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545020) because *folder acquisition* is supported.

In folder acquisition, a single transfer request is on the parent item, but the actual item properties are on each of the child items that is being transferred. The **IWiaMiniDrv::drvWriteItemProperties** method is not called for each child item, so this method cannot be used to program the device settings. For drivers that support **IStream** data transfers, the WIA service calls [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) instead.

**Note**  This change affects only drivers that support the new data transfers. Legacy drivers, which do not support **IStream** data transfers, are not affected; the WIA service will continue to call the **IWiaMiniDrv::drvWriteItemProperties** method for them.

 

In folder acquisitions where the driver makes multiple calls to **IWiaTransferCallback::GetNextStream** (which is described in the Microsoft Windows SDK documentation), the driver can have only one active stream at a time.

The driver must call only the stream's **IStream::Write**, **IStream::Seek**, and **IStream::SetSize** methods (which are described in the Windows SDK documentation) during a download operation. This restriction makes it easier for you to write the filter. The driver should not expect that the destination stream will implement any other methods.

When the [**WIA\_DPS\_PAGE\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551417) property is set to WIA\_PAGE\_AUTO (that is, automatic page size detection is enabled), the driver should provide accurate dimension information about the image only after it completes the transfer of the image data. For stream-based transfers, the driver should update the image dimensions in the image header at the end of the transfer. At the beginning of a new session, the value for WIA\_DPS\_PAGE\_SIZE property should always be set to a value other than WIA\_PAGE\_AUTO.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20IStream%20Data%20Transfer%20Driver%20Changes%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


