---
title: Creating a WIA Camera Item Tree Layout
description: Creating a WIA Camera Item Tree Layout
MS-HAID:
- 'WIA\_drv\_cam\_9a4c9c0a-7f88-49b3-b4d6-355e8eb5074c.xml'
- 'image.creating\_\_a\_wia\_camera\_item\_tree\_layout'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 83b496dc-8c47-46fb-b703-837eb536cb66
---

# Creating a WIA Camera Item Tree Layout


## <a href="" id="ddk-creating-a-wia-camera-item-tree-layout-si"></a>


A WIA camera item tree for Microsoft Windows Me and Windows XP consists of a root item, and child items that represent images and folders stored on the camera device. See [Initializing the WIA Minidriver](initializing-the-wia-minidriver.md) for an example on how to create an item tree. The following illustration shows the item tree for Windows Me and Windows XP.

![diagram illustrating a wia camera item tree for windows me and windows xp](images/camera-tree.png)

For a diagram of a camera tree in Windows Vista and later operating systems, see [Example Usage of WIA Item Flags and Categories](example-usage-of-wia-item-flags-and-categories.md).

The root item of a camera item tree contains all the standard WIA minidriver information and camera-specific properties. The camera-specific properties include the number of pictures taken and other camera control properties.

The child items of a camera item tree represent the images or folders stored on the device. It is recommended that the minidriver eliminate any unnecessary levels of folders to allow easier access to transferable items. This makes access to the WIA items by the application easier and prevents the user from having to navigate deep into a folder structure to get to the actual images.

The minidriver writer can give files and folder items whatever names he or she desires. However, each item in the WIA item tree represents a physical data item on the camera, and should be given a name that suggests the actual data items in the camera.

When a data item is added to or deleted from the camera, it is the responsibility of the WIA minidriver to synchronize its WIA item tree with the contents of the camera. For an example of how this is done, see [Changing the WIA Item Tree Structure](changing-the-wia-item-tree-structure.md).

Through the WIA service, an application can perform the following actions:

-   Query camera capabilities.

-   Set camera device properties.

-   Request a data transfer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Creating%20%20a%20WIA%20Camera%20Item%20Tree%20Layout%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




