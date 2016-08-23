---
title: WIA Item Flags for Flatbed Scanners
author: windows-driver-content
description: WIA Item Flags for Flatbed Scanners
MS-HAID:
- 'WIA\_scanner\_tree\_765b0be6-8df1-4562-a179-d91766913dbc.xml'
- 'image.wia\_item\_flags\_for\_flatbed\_scanners'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: bd070e41-47e9-4165-a250-e759b8a214aa
---

# WIA Item Flags for Flatbed Scanners


## <a href="" id="ddk-wia-item-flags-for-flatbed-scanners-si"></a>


This topic lists the required and optional WIA item flags for the root item and child items of a flatbed scanner item tree. For a complete list of the WIA item flags and their definitions, see [**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585).

### Required WIA Item Flags for Flatbed Scanners

A WIA flatbed scanner item is required to support the following WIA item flags:

<a href="" id="wiaitemtypeprogrammabledatasource"></a>**WiaItemTypeProgrammableDataSource**  
The WIA item is configurable and follows a set of predefined configuration rules that are based on the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property. This flag is required because the flatbed part of the scanner is programmable.

<a href="" id="wiaitemtypetransfer"></a>**WiaItemTypeTransfer**  
The WIA item can be used to transfer data. This flag is required because the flatbed scanner item can be used to transfer data.

<a href="" id="wiaitemtypefile"></a>**WiaItemTypeFile**  
The item is a file. This flag is required by the **WiaItemTypeImage** flag.

<a href="" id="wiaitemtypeimage"></a>**WiaItemTypeImage**  
The item is an image. This flag is valid only for items that also have the **WiaItemTypeFile** flag set. This flag is required because the flatbed scanner reports image formats for the [**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property values. All WIA flatbed scanner items are required to support at least one image format. WIA currently requires WiaImgFmt\_BMP and WiaImgFmt\_MEMORYBMP as supported image formats.

### Optional WIA Item Flags for Flatbed Scanners

The WIA flatbed scanner item can optionally support the following WIA item flag:

<a href="" id="wiaitemtypefolder"></a>**WiaItemTypeFolder**  
The item is a folder. Add this flag if the flatbed scanner item contains child items. (These items may include multiple selected regions on a single flatbed platen.)You should use this flag only on the base item. Child items *cannot* have this flag.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Item%20Flags%20for%20Flatbed%20Scanners%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


