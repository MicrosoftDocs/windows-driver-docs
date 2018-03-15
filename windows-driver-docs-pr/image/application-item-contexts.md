---
title: Application Item Contexts
author: windows-driver-content
description: Application Item Contexts
ms.assetid: d11b1750-999f-411c-9e83-6d2b20ce65db
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Application Item Contexts


## <a href="" id="ddk-application-item-contexts-si"></a>


An application item context, also known as a *WIA service context*, is a reference to a root or child item that the WIA service passes to the minidriver in a call to one of several [IWiaMiniDrv interface](https://msdn.microsoft.com/library/windows/hardware/ff545027) methods. The minidriver then uses this reference when it calls certain WIA service library functions. The application item context for the item indicates which item is to be processed in the method. The minidriver should not attempt to directly access the application item context. A minidriver can determine whether the item is a root item or a child item by calling the driver services library function, [**wiasGetItemType**](https://msdn.microsoft.com/library/windows/hardware/ff549255).

When an application requests a data transfer from the device to a WIA item it created, it calls on the WIA service to initiate the transfer. The WIA service passes the application item's context to a minidriver entry point such as the [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) method. Subsequently, when the minidriver uses a WIA service library function, such as [**wiasReadPropLong**](https://msdn.microsoft.com/library/windows/hardware/ff549330), and passes in the application item context, the WIA service reads the specified property from the property storage associated with that application item.

 

 




