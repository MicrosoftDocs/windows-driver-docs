---
title: Property Keys
description: Property Keys
ms.assetid: 767dbe79-72c6-4445-8d4a-8be53a080825
keywords:
- device properties WDK device installations , property keys
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Property Keys


Programmatically, all device properties in the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) are represented by property keys. The property keys are coded as [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544) structures. The property keys are defined in *Devpkey.h*.

A DEVPROPKEY structure has the following members:

<a href="" id="fmtid"></a>**fmtid**  
A DEVPROPGUID-typed variable that identifies the property category.

<a href="" id="pid"></a>**pid**  
A DEVPROPID-typed variable that is the property identifier. For internal system reasons, a property identifier must be greater than or equal to two.

To create a custom device property key, use the [**DEFINE_DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff541072) macro.

The following is an example of how to use the DEFINE_DEVPROPKEY macro to create a DEVPROPKEY structure. The name of the structure is "DEVPROPKEYStructureName", the sequence of values 0xde5c254e through 0xe0 supply the GUID value, and the value "2" is the property identifier.

```cpp
DEFINE_DEVPROPKEY(DEVPROPKEYStuctureName, 0xde5c254e, 0xab1c, 0xeffd, 0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0, 2)
```

**Note**   The system-defined property key categories are reserved for system use only.

 

 

 





