---
title: WIA Driver Item Tree
author: windows-driver-content
description: WIA Driver Item Tree
ms.assetid: 67232179-4b9b-49a0-b8b0-5ed0914d4156
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Driver Item Tree


## <a href="" id="ddk-wia-driver-item-tree-si"></a>


In WIA, an imaging device is represented logically as a hierarchical tree of WIA items, as shown in the following diagram of a camera tree.

![diagram illustrating a wia driver item tree](images/art-2.png)

The root item represents the actual device, and the child items represent images or folders. Folders can contain images or other folders. Items have properties that the minidriver can set or query.

Going through the WIA service, an application uses an item to perform such tasks as getting and setting device information, controlling the device, and starting driver item enumeration.

Applications can call the [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) method to acquire data from an item by requesting a data transfer from the item.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Driver%20Item%20Tree%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


