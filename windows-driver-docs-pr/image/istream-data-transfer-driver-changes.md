---
title: IStream Data Transfer Driver Changes
description: IStream Data Transfer Driver Changes
ms.assetid: 1c837e4f-8d53-40ed-8f5b-0d525c7dd758
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




