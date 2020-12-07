---
title: Reading WIA Item Properties by a Driver
description: Reading WIA Item Properties by a Driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reading WIA Item Properties by a Driver





A WIA minidriver should always use the properties in its own driver item tree as a basis for the current settings. Because the application is reading from and writing to the minidriver's item tree, it will never be out of date. A WIA minidriver should use the following WIA service functions to read from the properties in its driver item tree.

<a href="" id="wiasreadmultiple"></a>[**wiasReadMultiple**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadmultiple)  
Read all WIA property types. This is a general function that allows a WIA driver to read any property existing on a WIA item, including custom properties. It can be used to read multiple properties per call.

<a href="" id="wiasreadpropstr"></a>[**wiasReadPropStr**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropstr)  
Read WIA properties that are strings (type VT\_BSTR).

<a href="" id="wiasreadproplong"></a>[**wiasReadPropLong**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadproplong)  
Read WIA properties that are four-byte integers (type VT\_I4).

<a href="" id="wiasreadpropfloat"></a>[**wiasReadPropFloat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropfloat)  
Read WIA properties that are four-byte real numbers (type VT\_R4).

<a href="" id="wiasreadpropguid"></a>[**wiasReadPropGuid**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropguid)  
Read WIA properties that are GUIDs (type VT\_CLSID).

<a href="" id="wiasreadpropbin"></a>[**wiasReadPropBin**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropbin)  
Read WIA properties that are strings of unsigned bytes (type VT\_VECTOR | VT\_UI1).

### Reading Legal Values

A WIA item property contains attributes that define the type of container and access rights. (For further information, see [Adding WIA Properties to a WIA Item](adding-wia-properties-to-a-wia-item.md).) The container types are WIA\_PROP\_NONE, WIA\_PROP\_LIST, and WIA\_PROP\_RANGE. The access rights are WIA\_PROP\_READ and WIA\_PROP\_RW. During validation of an existing property, a WIA minidriver should check the internal update setting to determine if it should read the valid values. A WIA minidriver should use the [**wiasGetPropertyAttributes**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetpropertyattributes) service function to read the current valid values for its WIA properties.

 

