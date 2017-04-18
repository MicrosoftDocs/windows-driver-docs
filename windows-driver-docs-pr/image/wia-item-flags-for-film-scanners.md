---
title: WIA Item Flags for Film Scanners
author: windows-driver-content
description: WIA Item Flags for Film Scanners
ms.assetid: 50aad730-6897-488d-a9de-58ce24738c17
---

# WIA Item Flags for Film Scanners


## <a href="" id="ddk-wia-item-flags-for-film-scanners-si"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Item%20Flags%20for%20Film%20Scanners%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


