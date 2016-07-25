---
title: Property Keys
description: Property Keys
ms.assetid: 767dbe79-72c6-4445-8d4a-8be53a080825
keywords: ["device properties WDK device installations , property keys"]
---

# Property Keys


Programmatically, all device properties in the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) are represented by property keys. The property keys are coded as [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544) structures. The property keys are defined in *Devpkey.h*.

A DEVPROPKEY structure has the following members:

<a href="" id="fmtid"></a>**fmtid**  
A DEVPROPGUID-typed variable that identifies the property category.

<a href="" id="pid"></a>**pid**  
A DEVPROPID-typed variable that is the property identifier. For internal system reasons, a property identifier must be greater than or equal to two.

To create a custom device property key, use the [**DEFINE\_DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff541072) macro.

The following is an example of how to use the DEFINE\_DEVPROPKEY macro to create a DEVPROPKEY structure. The name of the structure is "DEVPROPKEYStructureName", the sequence of values 0xde5c254e through 0xe0 supply the GUID value, and the value "2" is the property identifier.

```
DEFINE_DEVPROPKEY(DEVPROPKEYStuctureName, 0xde5c254e, 0xab1c, 0xeffd, 0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0, 2)
```

**Note**   The system-defined property key categories are reserved for system use only.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Property%20Keys%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




