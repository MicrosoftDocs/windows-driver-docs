---
title: Describing a WIA Device Using WIA Items
description: Describing a WIA Device Using WIA Items
ms.assetid: d8149f78-e095-48f9-be79-ff115b25f14e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Describing a WIA Device Using WIA Items





This topic applies to Windows Vista and later.

A WIA item can represent a programmable data source of a WIA device (for example, a scanner's automatic document feeder) or data stored on that device (for example, pictures on a camera). A WIA device should be broken into individual items to properly describe different data produced by that device. Here are two examples:

<a href="" id="scanner-example"></a>**Scanner example**  
A WIA scanner device that supports both flatbed scanning and document feeder scanning has two major child items. One child item represents the flatbed scanning functionality, and the other represents the document feeder scanning functionality.

<a href="" id="camera-example"></a>**Camera example**  
A WIA camera device that stores pictures has child items that represent subfolders and pictures.

The remainder of this section contains the following topics:

[WIA Item Flags](wia-item-flags.md)

[WIA Item Categories](wia-item-categories.md)

[Example Usage of WIA Item Flags and Categories](example-usage-of-wia-item-flags-and-categories.md)

[WIA Root Item](wia-root-item.md)

[WIA Data Item](wia-data-item.md)

 

 




