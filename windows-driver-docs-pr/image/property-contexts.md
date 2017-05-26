---
title: Property Contexts
author: windows-driver-content
description: Property Contexts
ms.assetid: da33848c-a9bc-40c7-ab1b-0ca056f3e06d
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Property Contexts


## <a href="" id="ddk-property-contexts-si"></a>


A property context provides a convenient way for a minidriver to identify a number of properties it is interested in during the validation of those properties. Using a property context, a minidriver can quickly determine whether any of the identified properties are being changed. The minidriver then passes the property context to one of the WIA service library functions (for example, [**wiasGetChangedValueFloat**](https://msdn.microsoft.com/library/windows/hardware/ff549200)), which uses the context to determine whether an application is changing a property's value.

The WIA approach to validation is that when an application changes a property, any dependent properties should also be updated. If, however, the application is also changing dependent properties, you can simply check the top-level property to determine whether its new value is valid. The WIA service library functions that are concerned with property validation use this principle to decide when they should update dependent properties, and when they should just check for validity.

Context for a set of properties is maintained in a [**WIA\_PROPERTY\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff552749) structure, which contains three members: the number of properties in the property context, a pointer to an array of property identifiers (PROPIDs), and a pointer to an array of BOOL values. The arrays are maintained in parallel (that is, the property whose property identifier is at index *N* in the property identifier array is associated with the BOOL value at the same index in the BOOL array).

The minidriver calls the WIA service library function, [**wiasCreatePropContext**](https://msdn.microsoft.com/library/windows/hardware/ff549167), to allocate memory and fill in the values for a property context. Other WIA service library functions, such as [**wiasGetChangedValueFloat**](https://msdn.microsoft.com/library/windows/hardware/ff549200), use a property context to determine when a property's values should be updated.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Property%20Contexts%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


