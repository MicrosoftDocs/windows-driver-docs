---
title: Driver Behavior on Upload
author: windows-driver-content
description: Driver Behavior on Upload
MS-HAID:
- 'WIA\_arch\_a9b7e481-3d56-4062-a6bd-37b34067481d.xml'
- 'image.driver\_behavior\_on\_upload'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a8edfd88-89b9-4759-b9b3-6f1ff2ae7fc9
---

# Driver Behavior on Upload


The behavior of the driver depends on what kind of item the upload is being called on.

For example, if **IWiaTransfer::Upload** is being called on a "Flatbed" item (that is, an item whose [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property is set to WIA\_CATEGORY\_FLATBED), the exact meaning of uploading data is undefined because a "Flatbed" item is not a data storage item. Typically, a vendor will use **IWiaTransfer::Upload** to enable its extensions or applications to communicate with the device in some proprietary way.

However, if **IWiaTransfer::Upload** is being called on an application item that was recently created by the application's call to **IWiaItem2::CreateChildItem**, the upload should represent some new data item for the device, such as a file, that needs to be saved to the device's storage.

The **IWiaTransfer** and **IWiaItem2** interfaces are described in the Microsoft Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Driver%20Behavior%20on%20Upload%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


