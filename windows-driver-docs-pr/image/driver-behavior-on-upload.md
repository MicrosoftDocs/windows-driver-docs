---
title: Driver Behavior on Upload
description: Driver Behavior on Upload
ms.date: 04/20/2017
---

# Driver Behavior on Upload


The behavior of the driver depends on what kind of item the upload is being called on.

For example, if **IWiaTransfer::Upload** is being called on a "Flatbed" item (that is, an item whose [**WIA\_IPA\_ITEM\_CATEGORY**](./wia-ipa-item-category.md) property is set to WIA\_CATEGORY\_FLATBED), the exact meaning of uploading data is undefined because a "Flatbed" item is not a data storage item. Typically, a vendor will use **IWiaTransfer::Upload** to enable its extensions or applications to communicate with the device in some proprietary way.

However, if **IWiaTransfer::Upload** is being called on an application item that was recently created by the application's call to **IWiaItem2::CreateChildItem**, the upload should represent some new data item for the device, such as a file, that needs to be saved to the device's storage.

The **IWiaTransfer** and **IWiaItem2** interfaces are described in the Microsoft Windows SDK documentation.

 

