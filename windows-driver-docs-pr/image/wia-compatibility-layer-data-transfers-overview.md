---
title: WIA Compatibility Layer Data Transfers Overview
description: WIA Compatibility Layer Data Transfers Overview
ms.assetid: 4c88474e-f776-4876-a15f-c9d6fb0d20e5
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




