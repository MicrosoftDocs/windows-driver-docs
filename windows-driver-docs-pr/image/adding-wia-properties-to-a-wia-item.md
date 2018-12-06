---
title: Adding WIA Properties to a WIA Item
description: Adding WIA Properties to a WIA Item
ms.assetid: 0cf4748f-c50a-4781-8b8d-3fb73e5d7242
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding WIA Properties to a WIA Item





Each WIA item contains WIA properties. An application reads and writes WIA item properties to configure the WIA minidriver. The WIA service calls the [**IWiaMiniDrv::drvInitItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff544989) method once for every item that the application accesses, to initialize that WIA minidriver item's properties. If an application does not read or write WIA properties on an item, this method is not called for that item. The item context that the *pWiasContext* parameter points to indicates which item will be initialized with WIA properties.

The **IWiaMiniDrv::drvInitItemProperties** method should perform the following tasks:

1.  Use the data received in the *pWiasContext* parameter to determine the item type. The WIA minidriver can obtain the [IWiaDrvItem COM interface](iwiadrvitem-com-interface.md) by calling [**wiasGetDrvItem**](https://msdn.microsoft.com/library/windows/hardware/ff549243). After obtaining this interface, the [**IWiaDrvItem::GetItemFlags**](https://msdn.microsoft.com/library/windows/hardware/ff543883) method can be called to determine the WIA item type.

2.  Create an array of property names and property IDs that describe the full property set needed on the current item. After creating these arrays, the WIA minidriver should call the [**wiasSetItemPropNames**](https://msdn.microsoft.com/library/windows/hardware/ff549369) service function. This function instructs the WIA service to build a WIA property set based on the created arrays. This function should always be called before [**wiasWriteMultiple**](https://msdn.microsoft.com/library/windows/hardware/ff549475) and [**wiasSetItemPropAttribs**](https://msdn.microsoft.com/library/windows/hardware/ff549358).

3.  Write the initial, or default, setting values to the newly created WIA property set. The WIA minidriver should call the **wiasWriteMultiple** service function to set the initial values. This function should always be called before **wiasSetItemPropAttribs**.

4.  Write the valid values and access rights for each property. The WIA minidriver should call the **wiasSetItemPropAttribs** service function to set the access rights and valid values.

**Note**   Applications are responsible for reading (and rereading) any properties that they depend on, thereby, allowing the application to catch any changes in the property values.
Scanners and cameras have a set of required properties. These properties are listed in [About WIA Properties](about-wia-properties.md).

Some properties have dependencies on other properties. For example, the [**format**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property is dependent on the [**tymed**](https://msdn.microsoft.com/library/windows/hardware/ff551656) property. These inter-property dependencies are covered in [WIA Properties](https://msdn.microsoft.com/library/windows/hardware/ff552739).

 

 

 




