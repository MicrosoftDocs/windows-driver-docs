---
title: Enumerating Child Devices and Control Methods
description: Enumerating Child Devices and Control Methods
ms.assetid: fe0553df-a5b9-46c4-8e1d-8b89a7d4ad67
keywords:
- ACPI devices WDK , enumerating child devices
- ACPI devices WDK , enumerating control methods
- ACPI namespaces WDK
- ACPI control methods WDK , enumerating
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Enumerating Child Devices and Control Methods


In an ACPI namespace, an object that is a device--for example, a device named 'ABCD'--can have child objects that are child devices of the device or that are control methods that are supported by the device. Any child object that is a child device of a parent device can, in turn, recursively have child objects that are child devices or control methods. For example, in the following simplified ACPI namespace, the root of the ACPI namespace is designated by '\\' and the object 'ABCD' is a device that is an immediate child of the root of the ACPI namespace. In addition, device 'ABCD' has two immediate child devices named 'CHL1' and 'CHL2' and a child object that is a control method named '\_FOO.' In addition, the child device 'CHL2' has a child device named 'CHL3' and device "CHL3" has a child object that is a control method named '\_FOO.'

```syntax
\     root of ACPI namespace
 ABCD            parent device 
    CHL1         child device of ABCD
    CHL2         child device of ABCD
       CHL3      child device of CHL2
          _FOO   control method
 _FOO            control method
```

To use [**IOCTL\_ACPI\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536149) or [**IOCTL\_ACPI\_ASYNC\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536146), a driver for a device supplies the path and name of the control method in an ACPI namespace. To help obtain the path and name of a device and child objects of a device, Windows supports the [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) request. Referring to the simplified ACPI namespace provided in this section as an example, a driver in the device stack of device 'ABCD' can use this request to do the following:

-   Enumerate device 'ABCD' and the immediate child devices of 'ABCD.' For example, the request can be used to return '\\ABCD,' '\\ABCD.CHL1,' and '\\ABCD.CHL2.'

-   Recursively enumerate all the devices in the namespace of 'ABCD.' For example, the request can be used to return '\\ABCD,' '\\ABCD.CHL1,' '\\ABCD.CHL2,' and '\\ABCD.CHL2.CHL3.'

-   Recursively enumerate all descendant child objects of 'ABCD' of a supplied name. The supplied name acts as a filter so that only those child objects that have the same name are enumerated. For example, for a supplied name '\_FOO,' the request can be used to return '\\ABCD.\_FOO' and '\\ABCD.CHL2.CHL3.\_FOO.'

After a driver obtains the path and name of a control method, it can supply the path and name as input to IOCTL\_ACPI\_EVAL\_METHOD\_EX or IOCTL\_ACPI\_ASYNC\_EVAL\_METHOD\_EX, as described in [Evaluating ACPI Control Methods Synchronously](evaluating-acpi-control-methods-synchronously.md).

An [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) request takes as input a driver-allocated variable-length [**ACPI\_ENUM\_CHILDREN\_INPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536110) structure that contains the following members:

<a href="" id="signature"></a>**Signature**  
The signature of the input buffer, which must be set to ACPI\_ENUM\_CHILDREN\_INPUT\_BUFFER\_SIGNATURE.

<a href="" id="flags"></a>**Flags**  
A flag that determines which objects in the ACPI namespace of a device that the ACPI driver enumerates. The ACPI driver returns the full path and name of the enumerated object beginning with the root of the ACPI namespace. The flag must be set to one of the following values:

<a href="" id="enum-children-immediate-only"></a>ENUM\_CHILDREN\_IMMEDIATE\_ONLY  
Enumerates the device and enumerates the immediate child devices of the device.

<a href="" id="enum-children-multilevel"></a>ENUM\_CHILDREN\_MULTILEVEL  
Enumerates the device and recursively enumerates all child devices of the device.

<a href="" id="enum-children-multilevel----enum-children-name-is-filter-"></a>ENUM\_CHILDREN\_MULTILEVEL || ENUM\_CHILDREN\_NAME\_IS\_FILTER   
A bitwise OR of ENUM\_CHILDREN and ENUM\_CHILDREN\_NAME\_IS\_FILTER enumerates the device's child objects whose name is identical to that supplied by the **Name** member.

<a href="" id="namelength"></a>**NameLength**  
The number of ASCII characters that the **Name** array contains.

<a href="" id="name"></a>**Name**  
A NULL-terminated four-character ASCII array that contains the name of a child object that the ACPI driver uses to restrict the enumeration of child objects to those objects that have the same name.

The IOCTL\_ACPI\_ENUM\_CHILDREN request returns the path and name of child objects in a driver-allocated variable-length ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER that contains the following members:

<a href="" id="signature"></a>**Signature**  
The signature of the output buffer, which must be set to ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER\_SIGNATURE.

<a href="" id="numberofchildren"></a>**NumberOfChildren**  
The number of elements of type ACPI\_ENUM\_CHILD in the **Children** array.

<a href="" id="children"></a>**Children**  
An array of elements of type ACPI\_ENUM\_CHILD. The **Name** member of an ACPI\_ENUM\_CHILD structure contains the path and name of the child object, and the **Flags** member indicates whether the child object has child objects.

If the output buffer that the driver allocates is not large enough to return all the enumerated child names, the ACPI driver returns no child names and sets the **Status** member of the IO\_STATUS\_BLOCK for the request to STATUS\_BUFFER\_OVERFLOW. In this case, if the size, in bytes, of the output buffer is at least **sizeof**(ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER\_SIGNATURE), the ACPI driver also sets **NumberOfChildren** to the size, in bytes, that is required to retrieve the requested paths and names.

For more information about how to enumerate child devices, see [Sending an IOCTL\_ACPI\_ENUM\_CHILDREN Request](sending-an-ioctl-acpi-enum-children-request.md).
