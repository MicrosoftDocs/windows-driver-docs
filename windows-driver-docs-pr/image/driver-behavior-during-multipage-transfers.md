---
title: Driver Behavior During Multipage Transfers
author: windows-driver-content
description: Driver Behavior During Multipage Transfers
ms.assetid: ecf0428b-c11c-49ff-9aa3-322e55dbca07
---

# Driver Behavior During Multipage Transfers


Drivers do not have to support folder acquisition directly. If drivers do not support it, the WIA service will recursively walk the item tree and call [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) on all items that have the **WiaItemTypeTransfer** bit set in the [**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585) property.

Drivers that support folder acquisition directly must expose the [**WIA\_IPS\_TRANSFER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff552657) property on the folder item. This property is a flag property and should have the WIA\_TRANSFER\_ACQUIRE\_CHILDREN\_CAPABLE bit set to indicate that it directly supports folder acquisition functionality. This support means that the driver itself will walk the tree to transfer the relevant items and the WIA service will simply call **IWiaMiniDrv::drvAcquireItemData** on the folder. The driver can differentiate between a normal transfer request and a folder acquisition request by testing the *lFlags* parameter for the WIA\_TRANSFER\_ACQUIRE\_CHILDREN bit.

One of the main reasons that a driver would support folder acquisition directly is efficiency. A driver might transfer multiple items far more efficiently than having the WIA service call a transfer on each of the items.

A good example of this situation is during a multiregion scan. When multiple regions (such as separate pictures) are detected on the flatbed of a scanner, they could be represented as children off the "Flatbed" item. An example of this situation is represented in the following figure.

![diagram illustrating an item tree for multiregion scanning](images/itemtree-multiregionscan.png)

If a separate transfer was called on each of the child items of "Flatbed", the driver would perform three separate scans, which could be time consuming. However, if a folder acquisition was requested on "Flatbed", the driver would perform one scan, decompose it, and hand back three separate regions (which is often faster).

**Note**  We recommend that only more sophisticated drivers directly support folder acquisition, because the driver is responsible for walking the item tree and taking the appropriate action.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Driver%20Behavior%20During%20Multipage%20Transfers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


