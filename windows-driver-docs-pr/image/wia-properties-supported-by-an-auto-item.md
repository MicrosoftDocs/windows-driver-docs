---
title: WIA Properties Supported by an Auto Item
author: windows-driver-content
description: WIA Properties Supported by an Auto Item
MS-HAID:
- 'WIA\_scanner\_tree\_7a59eefd-076d-4689-aa9c-67683e07ad8f.xml'
- 'image.wia\_properties\_supported\_by\_an\_auto\_item'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 71b3a9ea-e402-4be8-9c62-9463e2a10f27
---

# WIA Properties Supported by an Auto Item


An [auto item](auto-item.md) represents the [auto-configured scanning](auto-configured-scanning.md) function of a WIA device that can automatically configure most of its settings for a scanning job without intervention by a WIA application. For more information about auto items, see the discussion of the WIA\_CATEGORY\_AUTO category in [WIA Item Categories](wia-item-categories.md).

The WIA service manages the following WIA properties on an auto item:

[**WIA\_IPA\_ITEM\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551590)

[**WIA\_IPA\_FULL\_ITEM\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551561)

[**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585)

[**WIA\_IPA\_ACCESS\_RIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff551518)

[**WIA\_IPA\_COLOR\_PROFILE**](https://msdn.microsoft.com/library/windows/hardware/ff551536)

The WIA service initializes the WIA\_IPA\_ITEM\_NAME property on behalf of the minidriver by setting the property value to the item name submitted by the minidriver. Similarly, the WIA service initializes the WIA\_IPA\_ITEM\_FLAGS property on behalf of the minidriver by setting the property to the flags value submitted by the minidriver.

The WIA minidriver can implement the following properties on an auto item:

[**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581)

[**WIA\_IPA\_COMPRESSION**](https://msdn.microsoft.com/library/windows/hardware/ff551540)

[**WIA\_IPA\_FILENAME\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff551549)

[**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553)

[**WIA\_IPA\_PREFERRED\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551623)

[**WIA\_IPA\_TYMED**](https://msdn.microsoft.com/library/windows/hardware/ff551656)

For an auto item, the WIA architecture requires the minidriver to support all of the properties in the preceding list, except WIA\_IPA\_FILENAME\_EXTENSION. Support for the WIA\_IPA\_FILENAME\_EXTENSION property is optional, but recommended.

The minidriver must set the WIA\_IPA\_ITEM\_CATEGORY property on an auto item to the value WIA\_CATEGORY\_AUTO. The last five properties in the preceding list enable a WIA application to negotiate the file format used to transfer image data that the device acquires during auto-configured scanning. The application should select a file format based on its internal requirements. Some applications might enable a user to select a file format from a list of formats that are supported by both the application and the driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Properties%20Supported%20by%20an%20Auto%20Item%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


