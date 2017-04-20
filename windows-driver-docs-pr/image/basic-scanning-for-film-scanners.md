---
title: Basic Scanning for Film Scanners
author: windows-driver-content
description: Basic Scanning for Film Scanners
ms.assetid: ca25c14d-120e-4e53-9d57-ba5663536bae
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Basic Scanning for Film Scanners


## <a href="" id="ddk-basic-scanning-for-film-scanners-si"></a>


A WIA application enumerates the top-level items in the scanner item tree to determine the supported features of the scanner. The application then uses the top level item as the scanning source. For example, flatbed scanner items are used for scanning from the flatbed, and feeder Items are used for scanning from the document feeder.

The programming and scanning behaviors of the film item are almost identical to those of the flatbed item.

An application will typically perform the following operations when it programs the scanner's film item, but not necessarily in this order:

-   Enumerate top-level WIA items, searching for WIA items that are marked with the **WiaItemTypeProgrammableDataSource** item flag and the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) setting of WIA\_CATEGORY\_FILM.

-   Read the valid values for [**WIA\_IPS\_FILM\_SCAN\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff552598) to check for the film scanning settings. This setting will indicate either positive image or negative image (that is, a photographic negative) scanning support.

-   Choose the positive or negative light source by setting the WIA\_IPS\_FILM\_SCAN\_MODE property.

-   Read the current settings for the scanner lamp and turn the lamp on, if needed by using the [**WIA\_IPS\_LAMP**](https://msdn.microsoft.com/library/windows/hardware/ff552603) property (if it is supported).

-   Read the valid values for [**WIA\_IPA\_TYMED**](https://msdn.microsoft.com/library/windows/hardware/ff551656) and [**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553).

-   Choose the final format of the data by setting the WIA\_IPA\_FORMAT property.

-   Choose the image settings, such as [**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546), [**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543), and [**WIA\_IPA\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551526).

-   Choose a single or multipage (if supported) file transfer by setting the WIA\_IPA\_TYMED property.

-   Enumerate child items to look for existing frames.

-   Read the [**WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION**](https://msdn.microsoft.com/library/windows/hardware/ff552653) item to determine whether the scanner supports creation of new frames.

-   Adjust existing film item frames or create new frames (depending on the frame creation support).

-   Read the WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION property to determine whether the film scanner item supports the special folder acquisition feature.

-   Perform one of the following operations:
    -   Transfer data by using the WIA film scanner item (not by using the folder acquisition feature). The full film scanning area will be returned as a single image.
    -   Transfer data by using the WIA film scanner item (by using the folder acquisition feature). Only the WIA film scanner child items (that is, frames) are transferred to the application.
    -   Navigate to each frame item and transfer that WIA item.

The driver normally performs the following operations when it uses the scanner's film scanning unit to scan:

1.  Call [**IWiaMiniDrv::drvValidateItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545017) and [**IWiaMiniDrv::drvReadItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545005). The WIA driver should validate any property settings during the application's property setting phase.

2.  Call [**IWiaMiniDrv::drvWriteItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545020). The WIA item context that is passed in belongs to the film scanner item or to a film scanning item frame so that the driver knows that the application intends to use the scanner's film scanning unit to scan. Some scanners use their flatbeds for film scanning. The scanner must be configured for proper lighting (based on the WIA\_IPS\_FILM\_SCAN\_MODE property) and extent changes for film scanning.

3.  Call [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956). The WIA item context that is passed in belongs to the film scanner item or to a film scanning item frame. The driver can easily determine that the application intends to scan by using the film scanning unit.

4.  Program the device and scan from the film scanning unit by using the current film item properties (including any child frame properties). If the WIA driver is not in film scanning mode, it attempts to switch to this mode for the scan. The application may toggle only between negative and positive light. Using a film scanner item to scan is a contract between the application and the driver; they agree that the film scanning feature of the scanner will be used for the data transfer.

The WIA properties that are located on the film scanner item should be used by the driver as settings to be applied to the film scanning part of the scanner before the scan. The WIA application is required to always trust the headers of the data that is returned by the WIA driver. For example, the scanner has determined that it cannot scan the specified image width and needs to round up the value. The driver should update the image headers with the updated width information so that the application has the proper data. The WIA driver should always update the WIA property set with the actual data information that is returned from the device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Basic%20Scanning%20for%20Film%20Scanners%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


