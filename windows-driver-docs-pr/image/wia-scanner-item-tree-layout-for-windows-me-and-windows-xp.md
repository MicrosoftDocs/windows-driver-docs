---
title: WIA Scanner Item Tree Layout for Windows Me and Windows XP
author: windows-driver-content
description: WIA Scanner Item Tree Layout for Windows Me and Windows XP
ms.assetid: e4824d3a-6439-4ebb-903e-2b592108ddbe
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Scanner Item Tree Layout for Windows Me and Windows XP


## <a href="" id="ddk-wia-scanner-item-tree-layout-for-windows-me-and-windows-xp-si"></a>


A WIA scanner item tree for Windows Me and Windows XP consists of a root item and a single child item. The following diagram illustrates the WIA scanner item tree.

![diagram illustrating the wia scanner item tree](images/scanner-tree.png)

See [How the Application Creates the WIA Device](how-the-application-creates-the-wia-device.md) for an example on how to create an item tree. For additional information, see [Initializing the WIA Minidriver](initializing-the-wia-minidriver.md), [Building and Maintaining an Item Tree](wia-driver-services-library.md#ddk-building-and-maintaining-an-item-tree-si), and [**IWiaMiniDrv::drvInitializeWia**](https://msdn.microsoft.com/library/windows/hardware/ff544986). The root item in a scanner item tree contains information that is present in all WIA minidrivers, as well as scanner-specific properties. The scanner-specific properties include device optics information and document feeder support.

The child item represents the data-collecting functionality of the device and is used for transferring data. The child item for a scanner should be named to reflect the operations it can perform.

Microsoft requires the following names for Windows XP:

<a href="" id="root"></a>**Root**  
The item that represents the first element in a WIA item tree.

<a href="" id="flatbed"></a>**Flatbed**  
The item that represents a flatbed scanner, with or without a document feeder.

<a href="" id="feeder"></a>**Feeder**  
The item that represents a scanner that has only a document feeder.

For Windows Me and Windows XP, an application must read WIA properties on the root item and on the first child item so that it can determine the functionality of the scanner device.

An application can use the WIA service to perform the following operations:

-   Query scanner capabilities.

-   Set scanner device properties.

-   Request a data transfer.

Applications typically expect flatbed scanners, including those with automatic document feeders (ADFs), to be represented by two items: a root item and a single child item. All data transfers are performed from the child item.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Scanner%20Item%20Tree%20Layout%20for%20Windows%20Me%20and%20Windows%20XP%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


