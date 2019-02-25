---
title: WIA Item Flags
description: WIA Item Flags
ms.assetid: 2b96bc23-705b-47f0-811c-1cb4a8be8b34
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Item Flags





This topic applies to Windows Vista and later.

WIA item flags are used to help classify the content or supported behavior of a particular WIA item. The WIA item flags fall into two basic groups:

<a href="" id="item-status-flags"></a>Item status flags  
Flags that report the current state of the WIA item.

For example: **WiaItemTypeDisconnected**, **WiaItemTypeDeleted**, etc.

<a href="" id="item-data-representation-usage-flags"></a>Item data representation/usage flags  
Flags that report the data that the WIA item represents or can produce if transferred.

For example: **WiaItemTypeImage** is a data representation flag that tells the application the data associated with the current WIA item is image data and should have image data properties. **WiaItemTypeProgrammableDataSource** is an item usage flag that tells the application that the WIA item is configurable, follows a set of predefined configuration rules base on the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581), and the configuration can possibly change the result for each data transfer. See [WIA Item Categories](wia-item-categories.md) for more information about category definitions.

For a complete list of the WIA item flags and their definitions see [**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585).

 

 




