---
title: Data Transfer Between Legacy Application and Windows Vista Driver
author: windows-driver-content
description: Data Transfer Between Legacy Application and Windows Vista Driver
ms.assetid: 83817277-3526-4f64-8e7c-7e02c8cd77bd
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Data Transfer Between Legacy Application and Windows Vista Driver


The compatibility layer must ensure that the driver's image processing filter is always invoked, and that a legacy application that does not explicitly support the **LocalService** account will still be able to perform a data transfer. The **LocalService** account is available on Microsoft Windows XP and later operating systems.

At a minimum, a legacy driver must expose both TYMED\_FILE and TYMED\_CALLBACK; however, a Windows Vista driver will never expose TYMED\_CALLBACK (or TYMED\_MULTIPAGE\_CALLBACK). The transfer portion of the compatibility layer will make sure that a legacy application will see TYMED\_CALLBACK although the Windows Vista driver does not implement it. TYMED\_MULTIPAGE\_CALLBACK will never be exposed from a Windows Vista driver.

A legacy application will see the formats supported for TYMED\_FILE and TYMED\_MULTIPAGE\_FILE that the Windows Vista driver exposes. For TYMED\_CALLBACK, a legacy application will see the same formats as the driver exposes for TYMED\_FILE, with one exception: instead of exposing **WiaImgFmt\_BMP**, the compatibility layer will expose **WiaImgFmt\_MEMORYBMP** to the legacy application. The way this is done is by having the compatibility layer "intercept" calls to [**IWiaMiniDrv::drvGetWiaFormatInfo**](https://msdn.microsoft.com/library/windows/hardware/ff543986), and add all the Windows Vista driver's TYMED\_FILE formats (with the exception of **WiaImgFmt\_BMP** /**WiaImgFmt\_MEMORYBMP**) for TYMED\_CALLBACK. Most importantly the compatibility layer creates its own legacy callback object during data transfers, which converts Windows Vista transfer messages and data written into its stream into legacy transfer messages.

For more information on the TYMED constants, please see [Understanding TYMED](understanding-tymed.md).

The compatibility layer creates two callback objects in the WIA COM proxy: one for callback transfers and one for file transfers. The WIA COM proxy implements the [IWiaTransferCallback interface](https://msdn.microsoft.com/library/windows/hardware/ff545043). This callback object takes care of the conversion between stream-based transfer and "old-style" transfer. The WIA compatibility layer also initiates the driver's image processing filter to which we pass the compatibility layer's callback object. Thus, the image processing filter will always run in the application's context just as with Windows Vista transfers.

The following diagram illustrates how the compatibility layer would work with a Windows Vista driver and a legacy application.

![diagram illustrating data transfer between a legacy application and a windows vista driver](images/vistaapp-legacydrv.png)

The legacy callback object within the WIA COM proxy converts Windows Vista transfer messages and data written into stream into legacy transfer messages, and writes data to file or banded data callback.

When the driver calls any of the methods exposed by the **IStream** interface that it receives from the [**IWiaMiniDrvTransferCallback::GetNextStream**](https://msdn.microsoft.com/library/windows/hardware/jj151551) method (note a driver should only call **IStream::Write**, **IStream::Seek**, and **IStream::SetSize**). Thus, the compatibility layer creates a custom **IStream** implementation that simply wraps the **IStream** interface that the WIA COM proxy provides.

Legacy file transfers are straightforward. An example of such transfer is when a legacy application calls **IWiaDataTransfer::idtGetData**. The compatibility layer creates a data stream on the file that the application specifies in the STGMEDIUM structure. This stream is passed to the driver or image processing filter when it calls [**IWiaTransferCallback::GetNextStream**](https://msdn.microsoft.com/library/windows/hardware/ff545039) and all the transfer messages are easily mapped to legacy transfer messages. For a more detailed description of how the messages are mapped, see [WIA Compatibility Layer Data Transfer Implementation](wia-compatibility-layer-message-mapping.md).

When calling into the **IWiaDataTransfer::dtGetData method**, the compatibility layer does some stricter parameter checking. For example, the compatibility layer does not allow calling the **IWiaDataTrasnfer::idtGetData** method with [TYMED\_FILE](understanding-tymed.md) and a page count higher then one In data transfers that do not utilize the compatibility layer it was possible to call the **IWiaDataTrasnfer::idtGetData** method with TYMED\_FILE and have a page count larger then one.

Legacy callback transfers are a little bit trickier. Because a Windows Vista driver does not support **WiaImgFmt\_MEMORYBMP**, which is required for legacy drivers, the compatibility layer's callback object must handle the conversion from **WiaImgFmt\_BMP** to **WiaImgFmt\_MEMORYBMP**. The mapping between transfer messages is also not quite straightforward. The compatibility layer creates its own stream implementation. The compatibility layer sends IT\_MSG\_DATA messages to the application's callback upon calls to the **IStream::Write** method by the application.

A change had to be made to the **IWiaTransfer** interface as part of implementing the compatibility layer; The function **IWiaTransfer::EnumWIA\_FORMAT\_INFO** is added to **IWiaTransfer** to allow TYMED\_MULTIPAGE\_FILE transfers. This addition is not a consequence of the compatibility layer, but is necessary because it is not possible to get to the **IWiaDataTransfer** interface from **IWiaTransfer** interface or from the **IWiaItem2** interface to the **IWiaItem** interface.

The **IWiaDataTransfer**, **IWiaTransfer**, **IWiaItem**, **IWiaItem2**, and **IStream** interfaces and the STGMEDIUM structure are discussed in the Microsoft Windows SDK documentation.

## Related topics
[**IWiaMiniDrvTransferCallback**](https://msdn.microsoft.com/library/windows/hardware/jj151550)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Data%20Transfer%20Between%20Legacy%20Application%20and%20Windows%20Vista%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


