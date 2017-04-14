---
title: Describing a WIA Device Using WIA Items
author: windows-driver-content
description: Describing a WIA Device Using WIA Items
ms.assetid: d8149f78-e095-48f9-be79-ff115b25f14e
---

# Describing a WIA Device Using WIA Items


## <a href="" id="ddk-describing-a-wia-device-using-wia-items-si"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Describing%20a%20WIA%20Device%20Using%20WIA%20Items%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


