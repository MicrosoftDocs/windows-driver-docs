---
title: WIA Item Flags
description: WIA Item Flags
MS-HAID:
- 'WIA\_tree\_5cc18bfb-06b9-4c92-a57e-69986b427aaa.xml'
- 'image.wia\_item\_flags'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2b96bc23-705b-47f0-811c-1cb4a8be8b34
---

# WIA Item Flags


## <a href="" id="ddk-wia-item-flags-si"></a>


This topic applies to Windows Vista and later.

WIA item flags are used to help classify the content or supported behavior of a particular WIA item. The WIA item flags fall into two basic groups:

<a href="" id="item-status-flags"></a>Item status flags  
Flags that report the current state of the WIA item.

For example: **WiaItemTypeDisconnected**, **WiaItemTypeDeleted**, etc.

<a href="" id="item-data-representation-usage-flags"></a>Item data representation/usage flags  
Flags that report the data that the WIA item represents or can produce if transferred.

For example: **WiaItemTypeImage** is a data representation flag that tells the application the data associated with the current WIA item is image data and should have image data properties. **WiaItemTypeProgrammableDataSource** is an item usage flag that tells the application that the WIA item is configurable, follows a set of predefined configuration rules base on the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581), and the configuration can possibly change the result for each data transfer. See [WIA Item Categories](wia-item-categories.md) for more information about category definitions.

For a complete list of the WIA item flags and their definitions see [**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Item%20Flags%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




