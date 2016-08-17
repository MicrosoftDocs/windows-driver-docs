---
title: WIA Item Tree Architecture
description: WIA Item Tree Architecture
MS-HAID:
- 'WIA\_tree\_ecd274ff-586a-430b-bd62-6c19d5508a20.xml'
- 'image.wia\_item\_tree\_architecture'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7e0f2b65-7150-4f8a-9780-abdaf93e44d6
---

# WIA Item Tree Architecture


## <a href="" id="ddk-wia-item-tree-architecture-si"></a>


The WIA item tree that an application can see is separate from the tree that is created and maintained by a WIA minidriver. When a minidriver creates a tree of items, the WIA service uses this WIA item tree as a guide to create identical copies that can be viewed by imaging applications. Items in the copied tree are called application items. Items in the tree created by a minidriver are called driver items.

More information is available in the following sections:

[Application Items and Driver Items](application-items-and-driver-items.md)

[Describing a WIA Device Using WIA Items](describing-a-wia-device-using-wia-items.md)

[Changing the WIA Item Tree Structure](changing-the-wia-item-tree-structure.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Item%20Tree%20Architecture%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




