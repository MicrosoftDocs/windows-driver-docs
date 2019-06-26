---
title: WIA Properties Supported by an Auto Item
description: WIA Properties Supported by an Auto Item
ms.assetid: 71b3a9ea-e402-4be8-9c62-9463e2a10f27
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Properties Supported by an Auto Item


An [auto item](auto-item.md) represents the [auto-configured scanning](auto-configured-scanning.md) function of a WIA device that can automatically configure most of its settings for a scanning job without intervention by a WIA application. For more information about auto items, see the discussion of the WIA\_CATEGORY\_AUTO category in [WIA Item Categories](wia-item-categories.md).

The WIA service manages the following WIA properties on an auto item:

[**WIA\_IPA\_ITEM\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-name)

[**WIA\_IPA\_FULL\_ITEM\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-full-item-name)

[**WIA\_IPA\_ITEM\_FLAGS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-flags)

[**WIA\_IPA\_ACCESS\_RIGHTS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-access-rights)

[**WIA\_IPA\_COLOR\_PROFILE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-color-profile)

The WIA service initializes the WIA\_IPA\_ITEM\_NAME property on behalf of the minidriver by setting the property value to the item name submitted by the minidriver. Similarly, the WIA service initializes the WIA\_IPA\_ITEM\_FLAGS property on behalf of the minidriver by setting the property to the flags value submitted by the minidriver.

The WIA minidriver can implement the following properties on an auto item:

[**WIA\_IPA\_ITEM\_CATEGORY**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-category)

[**WIA\_IPA\_COMPRESSION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-compression)

[**WIA\_IPA\_FILENAME\_EXTENSION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-filename-extension)

[**WIA\_IPA\_FORMAT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-format)

[**WIA\_IPA\_PREFERRED\_FORMAT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-preferred-format)

[**WIA\_IPA\_TYMED**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-tymed)

For an auto item, the WIA architecture requires the minidriver to support all of the properties in the preceding list, except WIA\_IPA\_FILENAME\_EXTENSION. Support for the WIA\_IPA\_FILENAME\_EXTENSION property is optional, but recommended.

The minidriver must set the WIA\_IPA\_ITEM\_CATEGORY property on an auto item to the value WIA\_CATEGORY\_AUTO. The last five properties in the preceding list enable a WIA application to negotiate the file format used to transfer image data that the device acquires during auto-configured scanning. The application should select a file format based on its internal requirements. Some applications might enable a user to select a file format from a list of formats that are supported by both the application and the driver.

 

 




