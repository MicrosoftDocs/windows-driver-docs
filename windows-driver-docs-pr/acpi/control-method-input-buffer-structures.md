---
title: Control Method Input Buffer Structures
author: windows-driver-content
description: Control Method Input Buffer Structures
MS-HAID:
- 'acpi-meth-eval-dg\_4c8a9454-7235-414f-812d-77a0ae4fe0fa.xml'
- 'acpi.control\_method\_input\_buffer\_structures'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 41d4c53f-9dc7-4723-9707-ae48ff07f5f4
---

# Control Method Input Buffer Structures


Starting with Microsoft Windows 2000, the ACPI driver supports the [**IOCTL\_ACPI\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536148) request. A driver for a device can use this request to evaluate a control method that is an immediate child object in the ACPI namespace of the device to which the request is sent. The IOCTL\_ACPI\_EVAL\_METHOD request supports the following input structures:

<a href="" id="acpi-eval-input-buffer"></a>[**ACPI\_EVAL\_INPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536115)  
This structure supplies the signature of the buffer and the name of a control method that does not take an input argument.

<a href="" id="acpi-eval-input-buffer-simple-integer"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_INTEGER**](https://msdn.microsoft.com/library/windows/hardware/ff536119)  
This structure supplies the signature of the structure, the name of a control method, and a single input argument value of type ULONG.

<a href="" id="acpi-eval-input-buffer-simple-string"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff536121)  
This structure supplies the signature of the structure, the name of a control method, and an input argument that is a NULL-terminated ASCII string.

<a href="" id="acpi-eval-input-buffer-complex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_COMPLEX**](https://msdn.microsoft.com/library/windows/hardware/ff536116)  
This structure supplies the signature of the structure, the name of a control method, and an input array of [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structures. The array can contain a maximum number of seven such structures. An ACPI\_METHOD\_ARGUMENT structure can contain a ULONG integer, an ASCII string, an ACPI package description, or an array of custom data.

Windows Server 2008, Windows Vista and later versions of Windows also support the [**IOCTL\_ACPI\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536149) request. A driver for a device can use this request to evaluate a control method that is a descendant child object in the ACPI namespace of the device to which the request is sent. The IOCTL\_ACPI\_EVAL\_METHOD\_EX request supports the following input structures:

<a href="" id="acpi-eval-input-buffer-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536118)  
This structure supplies the signature of the structure and the path and name of a control method that does not take an input argument.

<a href="" id="acpi-eval-input-buffer-simple-integer-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_INTEGER\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536120)  
This structure supplies the signature of the structure and the path and name of a control method that takes a single integer of type ULONG64 as an input argument.

<a href="" id="acpi-eval-input-buffer-simple-string-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_STRING\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536122)  
This structure supplies the signature of the structure and the path and name of a control method that takes a single NULL-terminated ASCII string as an input argument.

<a href="" id="acpi-eval-input-buffer-complex-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_COMPLEX\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536117)  
This structure supplies the signature of the structure and the path and name of a control method that takes an array of ACPI\_METHOD\_ARGUMENT structures as input. The array can contain a maximum number of seven such structures. An ACPI\_METHOD\_ARGUMENT structure can contain a ULONG integer, an ASCII string, an ACPI package description, or an array of custom data.

To obtain the path and name of child objects in the ACPI namespace of a device, a driver for a device can use an [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) request, as described in [Enumerating Child Devices and Control Methods](enumerating-child-devices-and-control-methods.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Control%20Method%20Input%20Buffer%20Structures%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


