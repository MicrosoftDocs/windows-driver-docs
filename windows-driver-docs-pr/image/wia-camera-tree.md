---
title: WIA Camera Tree
author: windows-driver-content
description: WIA Camera Tree
ms.assetid: 8c932c91-b389-4b4c-b686-75ca6bf3de6a
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Camera Tree


## <a href="" id="ddk-wia-camera-tree-si"></a>


The following figure shows a camera that contains several images, two of which are in the same directory.

![diagram illustrating a camera with several images, two of which are in the same directory](images/art-camera.png)

In the following figure, WIA represents the camera shown in the previous figure, the pictures taken with the camera, and any folders as a tree of camera items.

![diagram illustrating how wia represents the camera shown in the previous figure, the pictures taken with the camera, and any folders as a tree of camera items](images/art-3.png)

The root item, which is the camera itself, consists of common device properties (properties that are common to both cameras and scanners), and camera-specific device properties. Similarly, each child item consists of properties common to both camera and scanner items, as well as properties that are specific to camera items.

Through the WIA service, an application can request the following from a camera item:

-   Query camera capabilities.

-   Set camera device properties.

-   Request a data transfer.

In the preceding diagram, the camera root item has three child items: two pictures and one folder. The folder has two child items that are both pictures. Camera items can also represent sound data or any other data on the camera that the device presents to the application.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Camera%20Tree%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


