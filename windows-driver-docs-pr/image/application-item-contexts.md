---
title: Application Item Contexts
description: Application Item Contexts
MS-HAID:
- 'WIA\_arch\_aa3ad280-5f22-4062-a0e4-46c6abc4970b.xml'
- 'image.application\_item\_contexts'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d11b1750-999f-411c-9e83-6d2b20ce65db
---

# Application Item Contexts


## <a href="" id="ddk-application-item-contexts-si"></a>


An application item context, also known as a *WIA service context*, is a reference to a root or child item that the WIA service passes to the minidriver in a call to one of several [IWiaMiniDrv interface](https://msdn.microsoft.com/library/windows/hardware/ff545027) methods. The minidriver then uses this reference when it calls certain WIA service library functions. The application item context for the item indicates which item is to be processed in the method. The minidriver should not attempt to directly access the application item context. A minidriver can determine whether the item is a root item or a child item by calling the driver services library function, [**wiasGetItemType**](https://msdn.microsoft.com/library/windows/hardware/ff549255).

When an application requests a data transfer from the device to a WIA item it created, it calls on the WIA service to initiate the transfer. The WIA service passes the application item's context to a minidriver entry point such as the [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) method. Subsequently, when the minidriver uses a WIA service library function, such as [**wiasReadPropLong**](https://msdn.microsoft.com/library/windows/hardware/ff549330), and passes in the application item context, the WIA service reads the specified property from the property storage associated with that application item.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Application%20Item%20Contexts%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




