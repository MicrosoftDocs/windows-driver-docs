---
title: WIA Item Flags for Flatbed Scanners
description: WIA Item Flags for Flatbed Scanners
ms.assetid: bd070e41-47e9-4165-a250-e759b8a214aa
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Item Flags for Flatbed Scanners





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

 

 




