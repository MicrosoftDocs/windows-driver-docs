---
title: WIA Compatibility Layer Data Transfers Overview
author: windows-driver-content
description: WIA Compatibility Layer Data Transfers Overview
MS-HAID:
- 'WIA\_Fundamentals\_a75f5f69-8de0-40c7-b2d9-3689389fd003.xml'
- 'image.wia\_compatibility\_layer\_data\_transfers\_overview'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4c88474e-f776-4876-a15f-c9d6fb0d20e5
---

# WIA Compatibility Layer Data Transfers Overview


Without the transfer compatibility layer, a Windows Vista WIA driver would have had to implement both TYMED and stream-based data transfer styles in order to be able to perform data transfers from legacy and Windows Vista applications. Similarly, a Windows Vista WIA application would have had to implement both styles of transfers (with different callback implementations) in order to be able to perform data transfers from legacy and Windows Vista drivers. With the WIA compatibility layer, the type of driver is transparent to a WIA application and a Windows Vista WIA driver does not have to deal with any legacy transfer code.

There are two transfer cases where a compatibility layer is needed, each of which can be further broken down into two sub-categories:

1.  Legacy application transferring data from a Windows Vista driver:
    1.  File transfer: The application calls **IWiaDataTransfer::idtGetBandedData**.
    2.  Callback transfer: The application calls **IWiaDataTransfer::idtGetData**.

2.  A Windows Vista application transferring data from a legacy driver:
    1.  File Transfer: The compatibility layer initiates file transfer with legacy driver.
    2.  Callback transfer: The compatibility layer initiates a callback transfer with the legacy driver.

The first step in determining whether to use the compatibility layer is to determine if a WIA driver is a Windows Vista driver or a legacy driver. The WIA service will determine this by looking at the version number that a driver returns from [**IStiUSD::GetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543817). A legacy driver returns STI\_VERSION for the version number, whereas a Windows Vista driver must return STI\_VERSION\_3. This version number will be exposed to the WIA COM proxy (and a WIA application) in the Windows Vista property, WIA\_DIP\_STI\_DRIVER\_VERSION.

The next step in determining whether to use the compatibility layer is to determine if an application is a Windows Vista WIA application or a legacy WIA application is simple: if the application calls **IWiaDataTransfer::idtGetBandedData** or **IWiaDataTransfer::idtGetData** it is a legacy WIA application, if the application calls **IWiaTransfer::Download** it is a Windows Vista WIA application.

With the new stream-based data transfer model, the WIA service will no longer distinguish between TYMED\_CALLBACK and TYMED\_FILE (or TYMED\_MULTIPAGE\_CALLBACK and TYMED\_MULTIPAGE\_FILE). Instead there will only be TYMED\_FILE and TYMED\_MULTIPAGE\_FILE. TYMED\_MULTIPAGE\_FILE is needed to allow drivers to support multi-page TIFF (or PDF) scans. For more information on the TYMED constants please see [Understanding TYMED](understanding-tymed.md).

WIA will not support the memory bitmap format **WiaImgFmt\_MEMORYBMP** in Windows Vista drivers.

Windows Vista drivers can send update messages to transfer data in bands rather then having the driver cache the entire image during a transfer. This form of transfer is useful for transferring data during scans where it is not immediately possible to determine the size of the image being transferred, for example, a scan with a scroll-feed scanner. In order to transfer image data in bands, the driver must call **IStream::Seek** on the stream passed to it in [**IWiaTransferCallback::GetNextStream**](https://msdn.microsoft.com/library/windows/hardware/ff545039).

For additional information on TYMED and stream-based transfers see [Data Transfers](data-transfers.md).

The **IWiaDataTransfer**, **IWiaTransfer**, and **IStream** interfaces are discussed in the Microsoft Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Compatibility%20Layer%20Data%20Transfers%20Overview%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


