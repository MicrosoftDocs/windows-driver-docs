---
title: Reading WIA Item Properties by a Driver
author: windows-driver-content
description: Reading WIA Item Properties by a Driver
ms.assetid: 4e592c62-e8bf-4b25-9c65-5a0079d3a857
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reading WIA Item Properties by a Driver


## <a href="" id="ddk-reading-wia-item-properties-by-a-driver-si"></a>


A WIA minidriver should always use the properties in its own driver item tree as a basis for the current settings. Because the application is reading from and writing to the minidriver's item tree, it will never be out of date. A WIA minidriver should use the following WIA service functions to read from the properties in its driver item tree.

<a href="" id="wiasreadmultiple"></a>[**wiasReadMultiple**](https://msdn.microsoft.com/library/windows/hardware/ff549300)  
Read all WIA property types. This is a general function that allows a WIA driver to read any property existing on a WIA item, including custom properties. It can be used to read multiple properties per call.

<a href="" id="wiasreadpropstr"></a>[**wiasReadPropStr**](https://msdn.microsoft.com/library/windows/hardware/ff549341)  
Read WIA properties that are strings (type VT\_BSTR).

<a href="" id="wiasreadproplong"></a>[**wiasReadPropLong**](https://msdn.microsoft.com/library/windows/hardware/ff549330)  
Read WIA properties that are four-byte integers (type VT\_I4).

<a href="" id="wiasreadpropfloat"></a>[**wiasReadPropFloat**](https://msdn.microsoft.com/library/windows/hardware/ff549320)  
Read WIA properties that are four-byte real numbers (type VT\_R4).

<a href="" id="wiasreadpropguid"></a>[**wiasReadPropGuid**](https://msdn.microsoft.com/library/windows/hardware/ff549325)  
Read WIA properties that are GUIDs (type VT\_CLSID).

<a href="" id="wiasreadpropbin"></a>[**wiasReadPropBin**](https://msdn.microsoft.com/library/windows/hardware/ff549308)  
Read WIA properties that are strings of unsigned bytes (type VT\_VECTOR | VT\_UI1).

### Reading Legal Values

A WIA item property contains attributes that define the type of container and access rights. (For further information, see [Adding WIA Properties to a WIA Item](adding-wia-properties-to-a-wia-item.md).) The container types are WIA\_PROP\_NONE, WIA\_PROP\_LIST, and WIA\_PROP\_RANGE. The access rights are WIA\_PROP\_READ and WIA\_PROP\_RW. During validation of an existing property, a WIA minidriver should check the internal update setting to determine if it should read the valid values. A WIA minidriver should use the [**wiasGetPropertyAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff549257) service function to read the current valid values for its WIA properties.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Reading%20WIA%20Item%20Properties%20by%20a%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


