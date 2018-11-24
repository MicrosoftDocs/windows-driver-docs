---
title: WIA Item Flags for Feeder Scanners
description: WIA Item Flags for Feeder Scanners
ms.assetid: b1256646-be6c-436c-86da-9dff43ef9867
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Item Flags for Feeder Scanners





This topic lists the required and optional WIA item flags for a scanner feeder item and scanner feeder child items (front and back page items). For a complete list of the WIA item flags and their definitions, see [**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585).

### Required WIA Item Flags for Feeder Scanners

A WIA feeder scanner item is required to support the following WIA item flags:

<a href="" id="wiaitemtypeprogrammabledatasource"></a>**WiaItemTypeProgrammableDataSource**  
The WIA item is configurable and follows a set of predefined configuration rules that are based on the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property. This flag is required because the scanner's document feeder is programmable.

<a href="" id="wiaitemtypetransfer-"></a>**WiaItemTypeTransfer**   
The WIA item can be used to transfer data. This flag is required because the scanner's feeder item, in the item tree, can be used to transfer data.

<a href="" id="wiaitemtypefile"></a>**WiaItemTypeFile**  
The item is a file. This flag is required by the **WiaItemTypeImage** flag.

<a href="" id="wiaitemtypeimage"></a>**WiaItemTypeImage**  
The item is an image. This flag is valid only for items that also have the **WiaItemTypeFile** flag set. The scanner's document feeder reports image formats for the [**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property values. (WIA requires that *all* feeder scanner items support at least one image format.) WIA currently requires WiaImgFmt\_BMP and WiaImgFmt\_MEMORYBMP as supported image formats.

### Optional WIA Item Flags for Feeder Scanners

The WIA feeder scanner item can optionally support the following WIA item flag:

<a href="" id="wiaitemtypefolder"></a>**WiaItemTypeFolder**  
The item is a folder. This flag is required for the root item if the automatic document feeder supports front and back items. This flag allows enumeration of the front and back of a page as child items. Child items *cannot* have this flag.

 

 




