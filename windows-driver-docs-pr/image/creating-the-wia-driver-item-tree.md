---
title: Creating the WIA Driver Item Tree
author: windows-driver-content
description: Creating the WIA Driver Item Tree
ms.assetid: 3ae489b9-175e-4b1e-a6c8-a72a3a3c212a
---

# Creating the WIA Driver Item Tree


## <a href="" id="ddk-creating-the-wia-driver-item-tree-si"></a>


After the minidriver is initialized, it must create the driver item tree in the [**IWiaMiniDrv::drvInitializeWia**](https://msdn.microsoft.com/library/windows/hardware/ff544986) method by:

1.  Creating the driver item tree if it does not already exist. The minidriver sets the root item flags and creates the root item by calling the driver services library function [**wiasCreateDrvItem**](https://msdn.microsoft.com/library/windows/hardware/ff549160). The minidriver stores the returned pointer to the root item in a private member variable.

2.  Creating child items for each item on the device using the [**wiasCreateDrvItem**](https://msdn.microsoft.com/library/windows/hardware/ff549160) function. This function creates a device-specific context where the minidriver can store information about the item.

3.  Calling the [**IWiaDrvItem::AddItemToFolder**](https://msdn.microsoft.com/library/windows/hardware/ff543856) method on each child item to add the item to the driver item tree.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Creating%20the%20WIA%20Driver%20Item%20Tree%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


