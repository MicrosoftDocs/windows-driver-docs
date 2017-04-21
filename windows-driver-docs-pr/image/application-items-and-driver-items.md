---
title: Application Items and Driver Items
author: windows-driver-content
description: Application Items and Driver Items
ms.assetid: 33b602dc-4a0b-47e1-90e2-b77ecc05f66d
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Application Items and Driver Items


## <a href="" id="ddk-application-items-and-driver-items-si"></a>


WIA items represent device attributes and device data. Imaging applications see a WIA device as a hierarchical tree of items, with the root item representing the device itself, and any child items representing images or folders that contain images. The tree that an application sees, however, is separate from the tree that is created and maintained by a WIA minidriver. When a minidriver creates a tree of items, the WIA service automatically creates an identical copy of this tree that can be viewed by imaging applications. Items in the copied tree are called *application items*. Items in the tree created by a minidriver are called *driver items*.

More than one imaging application can use a single imaging device at the same time. Each application's view of an item object in a device tree must therefore be independent of another application's view. This is accomplished as follows:

1.  A minidriver creates an item tree of [IWiaDrvItem Interface](https://msdn.microsoft.com/library/windows/hardware/ff543896) objects using the [IWiaMiniDrv Interface](https://msdn.microsoft.com/library/windows/hardware/ff545027) and the [WIA Driver Services Library Functions](https://msdn.microsoft.com/library/windows/hardware/ff551473). The items in this driver item tree are global objects that the minidriver uses to represent the device's items.

2.  When an imaging application requests access to an item in the tree, the WIA service returns an item object that is a copy of the driver item. When an application acquires an application **IWiaItem** (described in the Microsoft Windows SDK documentation) item object (an application item), the WIA service links this object to the minidriver's corresponding **IWiaDrvItem** object in the *driver item tree*.

3.  WIA creates a separate *application item tree* for each application, each application item tree is a copy of the driver item tree.

Applications typically use the **IWiaItem** object to read, validate, and write item properties and to request item data.

The following diagram shows the relationship of application items to driver items.

![diagram illustrating the relationship between application items and driver items](images/art-5.png)

As the diagram illustrates, each imaging application has its own separate copy of the item tree. The root item in an application item tree contains a pointer back to the root item in the device item tree.

The remainder of this section contains the following topics:

[About Item Properties](about-item-properties.md)

[WIA Driver Item Tree](wia-driver-item-tree.md)

[WIA Camera Tree](wia-camera-tree.md)

[WIA Scanner Tree](wia-scanner-tree.md)

[Common, Camera, and Scanner Properties](common--camera--and-scanner-properties.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Application%20Items%20and%20Driver%20Items%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


