---
title: Basic Scanning for Flatbed Scanners
author: windows-driver-content
description: Basic Scanning for Flatbed Scanners
ms.assetid: a1100a8d-752a-4109-b1dc-cf7c4bf5a100
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Basic Scanning for Flatbed Scanners


## <a href="" id="ddk-basic-scanning-for-flatbed-scanners-si"></a>


A WIA application enumerates the root item and top-level child item in the scanner item tree to determine the supported features of the scanner. The application then uses this child item as the scanning source. For example, flatbed scanner items are used for scanning from the flatbed, while feeder items are used for scanning from the document feeder, and so on.

The programming and scanning behavior of the flatbed item in Windows Vista is identical to the overload system that is used by Windows XP and Windows Me. This overload system programs the first child item in the item tree by putting all of the WIA attribute flags on it.

An application will normally perform the following operations when it programs the scanner's flatbed, but not necessarily in this order:

-   Enumerate top-level WIA items and look for items that are marked with the **WiaItemTypeProgrammableDataSource** item flag and with the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property set to WIA\_CATEGORY\_FLATBED.

-   Read the valid values for the [**WIA\_IPA\_TYMED**](https://msdn.microsoft.com/library/windows/hardware/ff551656) and [**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553) properties.

-   Choose either a memory transfer or file transfer type by setting the WIA\_IPA\_TYMED property. For more information about the available types of transfers, see [Data Transfers](data-transfers.md). For **IStream**-based transfers, WIA\_IPA\_TYMED is set by default to TYMED\_FILE and should not be changed.

-   Choose the final format of the data by setting the WIA\_IPA\_FORMAT property.

-   Choose the image settings, such as [**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546) and [**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543).

-   Transfer the data using this WIA item.

The driver will normally perform the following operations when it uses the scanner's flatbed to scan:

1.  Call [**IWiaMiniDrv::drvValidateItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545017) and [**IWiaMiniDrv::drvReadItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545005). The WIA driver should validate any property settings during the application's property-setting phase.

2.  Call [**IWiaMiniDrv::drvWriteItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545020). The WIA item context that is passed in belongs to the flatbed scanner item so that the driver knows that the application intends to use the scanner's flatbed to scan.

3.  Call [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956). The WIA item context that is passed in belongs to the flatbed scanner item, so the driver can easily determine that the application intends to scan by using the flatbed platen.

4.  Program the device and scan from the flatbed, using the current flatbed item properties. If the WIA driver is not in flatbed scanning mode, it should attempt to switch to this mode for the scan. There is no special setting for the application to toggle to use the flatbed. Using the flatbed item to scan is a contract between the application and the driver; they agree that the flatbed is to be used for the data transfer.

The driver must use the WIA properties on the flatbed scanner item as settings to be applied to the flatbed part of the scanner before the scan. The WIA application is required to always trust the headers of the data that is returned by the WIA driver. For example, if a scanner determines that it cannot scan an image of a specified width and, as a result, rounds the value to a width that it can scan, the driver should update the image headers with the modified width information. This update ensures that correct information is available to the application. The WIA driver should attempt to update the WIA properties with the actual information that is returned from the device.

### Advanced Scanning for Flatbed Scanners

Multiregion scanning from the flatbed is possible either though manual configuration or by automatically using the [WIA Segmentation Filter](wia-segmentation-filter.md). Note that the segmentation filter is no different from an application in what it can and cannot do. The same procedures that are described for the segmentation filter can be run directly by the application to create child items for new scan regions.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Basic%20Scanning%20for%20Flatbed%20Scanners%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


