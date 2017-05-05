---
title: Adding WIA Properties to a WIA Item
author: windows-driver-content
description: Adding WIA Properties to a WIA Item
ms.assetid: 0cf4748f-c50a-4781-8b8d-3fb73e5d7242
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Adding WIA Properties to a WIA Item


## <a href="" id="ddk-adding-wia-properties-to-a-wia-item-si"></a>


Each WIA item contains WIA properties. An application reads and writes WIA item properties to configure the WIA minidriver. The WIA service calls the [**IWiaMiniDrv::drvInitItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff544989) method once for every item that the application accesses, to initialize that WIA minidriver item's properties. If an application does not read or write WIA properties on an item, this method is not called for that item. The item context that the *pWiasContext* parameter points to indicates which item will be initialized with WIA properties.

The **IWiaMiniDrv::drvInitItemProperties** method should perform the following tasks:

1.  Use the data received in the *pWiasContext* parameter to determine the item type. The WIA minidriver can obtain the [IWiaDrvItem COM interface](iwiadrvitem-com-interface.md) by calling [**wiasGetDrvItem**](https://msdn.microsoft.com/library/windows/hardware/ff549243). After obtaining this interface, the [**IWiaDrvItem::GetItemFlags**](https://msdn.microsoft.com/library/windows/hardware/ff543883) method can be called to determine the WIA item type.

2.  Create an array of property names and property IDs that describe the full property set needed on the current item. After creating these arrays, the WIA minidriver should call the [**wiasSetItemPropNames**](https://msdn.microsoft.com/library/windows/hardware/ff549369) service function. This function instructs the WIA service to build a WIA property set based on the created arrays. This function should always be called before [**wiasWriteMultiple**](https://msdn.microsoft.com/library/windows/hardware/ff549475) and [**wiasSetItemPropAttribs**](https://msdn.microsoft.com/library/windows/hardware/ff549358).

3.  Write the initial, or default, setting values to the newly created WIA property set. The WIA minidriver should call the **wiasWriteMultiple** service function to set the initial values. This function should always be called before **wiasSetItemPropAttribs**.

4.  Write the valid values and access rights for each property. The WIA minidriver should call the **wiasSetItemPropAttribs** service function to set the access rights and valid values.

**Note**   Applications are responsible for reading (and rereading) any properties that they depend on, thereby, allowing the application to catch any changes in the property values.
Scanners and cameras have a set of required properties. These properties are listed in [About WIA Properties](about-wia-properties.md).

Some properties have dependencies on other properties. For example, the [**format**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property is dependent on the [**tymed**](https://msdn.microsoft.com/library/windows/hardware/ff551656) property. These inter-property dependencies are covered in [WIA Properties](https://msdn.microsoft.com/library/windows/hardware/ff552739).

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Adding%20WIA%20Properties%20to%20a%20WIA%20Item%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


