---
title: WIA Item Flags for Film Scanners
description: WIA Item Flags for Film Scanners
ms.assetid: 50aad730-6897-488d-a9de-58ce24738c17
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Item Flags for Film Scanners





This topic lists the required WIA item flags for a scanner film item and scanner film child items (that is, frames). For a complete list of the WIA item flags and their definitions, see [**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585).

### Required WIA Item Flags for Film Scanners

The WIA film scanner item is required to support the following WIA item flags:

<a href="" id="wiaitemtypeprogrammabledatasource"></a>**WiaItemTypeProgrammableDataSource**  
The WIA item is configurable and follows a set of predefined configuration rules that are based on the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property. This flag is required because the film scanning part of the scanner is programmable.

<a href="" id="wiaitemtypetransfer"></a>**WiaItemTypeTransfer**  
The WIA item can be used to transfer data. This flag is required because the scanner's film item can be used to transfer data.

<a href="" id="wiaitemtypefile"></a>**WiaItemTypeFile**  
The item is a file. This flag is required by the **WiaItemTypeImage** flag.

<a href="" id="wiaitemtypeimage"></a>**WiaItemTypeImage**  
The item is an image. This flag is required because the film scanner reports image formats for the [**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property values. (WIA requires that all film scanner items support at least one image format.) WIA currently requires that the WiaImgFmt\_BMP and WiaImgFmt\_MEMORYBMP image formats be supported.

<a href="" id="wiaitemtypefolder"></a>**WiaItemTypeFolder**  
The item is a folder. This flag is required for the root film item to allow enumeration of the individual frame child items. (Frames represent multiple selected regions on a single film scanning surface.) The scanner film child items (frames) *cannot* have this flag.

 

 




