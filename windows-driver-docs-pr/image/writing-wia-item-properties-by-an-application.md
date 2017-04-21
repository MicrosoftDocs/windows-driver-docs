---
title: Writing WIA Item Properties by an Application
author: windows-driver-content
description: Writing WIA Item Properties by an Application
ms.assetid: 728f3f73-4815-4d79-ac02-227de7ae9bb7
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Writing WIA Item Properties by an Application


## <a href="" id="ddk-writing-wia-item-properties-by-an-application-si"></a>


When a WIA application writes to a WIA property (and updates the value stored in the property), the WIA service gives the WIA minidriver the opportunity to validate incoming values by calling the [**IWiaMiniDrv::drvValidateItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545017) method. The WIA minidriver compares the incoming values to any current values by reading the properties in its own driver item tree. The WIA service library provides functions for accessing these values.

The **IWiaMiniDrv::drvValidateItemProperties** method should perform the following tasks:

1.  Determine the item type.

2.  Determine whether any special validation should be performed on the incoming WIA properties. To determine which WIA properties are being written, the WIA minidriver can use an array of PROPSPEC structures (the PROPSPEC structure is described in the Microsoft Windows SDK documentation). It is recommended that the WIA minidriver determine the item type before it processes the PROPSPEC array to reduce the need to traverse the array on every **IWiaMiniDrv::drvValidateItemProperties** call. If there are no special validation requirements, or if you need to update dependent properties on the root item of the device, only write requests to child item properties will be processed.

3.  Create a WIA property context to access values that changed during WIA property validation, which is necessary to update the dependent properties for a WIA item. Use the [**wiasCreatePropContext**](https://msdn.microsoft.com/library/windows/hardware/ff549167) and **wiasGetChangedValue***Xxx* service functions.

4.  Update dependent properties using the WIA service functions, [**wiasWriteMultiple**](https://msdn.microsoft.com/library/windows/hardware/ff549475) or **wiasWriteProp***Xxx*, which includes updating any valid values that might have changed as a result of setting a property. For example, if your WIA minidriver supports setting the [**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546) property, you must update the valid list of bit depths when the application changes the [**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543) property.

    When the value of the [**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543) property changes from WIA\_DATA\_THRESHOLD to WIA\_DATA\_COLOR, the related WIA\_IPA\_DEPTH property changes from reporting one-bit color depth, to reporting 24 bits or 48 bits.

5.  Call the [**wiasValidateItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff549454) service function to let the WIA service validate all other property requests. This is a "catch-all" case; the WIA service has built-in property validation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Writing%20WIA%20Item%20Properties%20by%20an%20Application%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


