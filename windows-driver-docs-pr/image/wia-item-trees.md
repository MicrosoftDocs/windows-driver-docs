---
title: WIA Item Trees
author: windows-driver-content
description: WIA Item Trees
ms.assetid: 98c43595-8547-4916-8671-86652212ac92
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Item Trees


## <a href="" id="ddk-wia-item-trees-si"></a>


WIA items represent device data and device attributes. Imaging applications see a WIA device as a hierarchical tree of items, with the root item representing the device itself, and any child items representing programmable data sources, images, or folders that contain images. If the device data or device attributes represented by the items in an item tree are changed or configured without using WIA (for example, when a TWAIN driver deletes an image), the WIA item tree must be refreshed. For more information, see [WIA-TWAIN Compatibility](wia-twain-compatibility.md).

This section contains more information in the following sections:

[WIA Item Tree Architecture](wia-item-tree-architecture.md)

[Changing the WIA Item Tree Structure](changing-the-wia-item-tree-structure.md)

[WIA Scanner Item Tree for Windows Me and Windows XP](wia-scanner-item-tree-for-windows-me-and-windows-xp.md)

[WIA Scanner Item Tree for Windows Vista](wia-scanner-item-tree-for-windows-vista.md)

[WIA Scanner Item Tree for Windows 7](wia-scanner-item-tree-for-windows-7.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Item%20Trees%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


