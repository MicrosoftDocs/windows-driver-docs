---
title: Control Method Input Buffer Structures
description: Control Method Input Buffer Structures
ms.assetid: 41d4c53f-9dc7-4723-9707-ae48ff07f5f4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Control Method Input Buffer Structures


The ACPI driver supports the [**IOCTL\_ACPI\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536148) request. A driver for a device can use this request to evaluate a control method that is an immediate child object in the ACPI namespace of the device to which the request is sent. The IOCTL\_ACPI\_EVAL\_METHOD request supports the following input structures:

<a href="" id="acpi-eval-input-buffer"></a>[**ACPI\_EVAL\_INPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536115)  
This structure supplies the signature of the buffer and the name of a control method that does not take an input argument.

<a href="" id="acpi-eval-input-buffer-simple-integer"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_INTEGER**](https://msdn.microsoft.com/library/windows/hardware/ff536119)  
This structure supplies the signature of the structure, the name of a control method, and a single input argument value of type ULONG.

<a href="" id="acpi-eval-input-buffer-simple-string"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff536121)  
This structure supplies the signature of the structure, the name of a control method, and an input argument that is a NULL-terminated ASCII string.

<a href="" id="acpi-eval-input-buffer-complex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_COMPLEX**](https://msdn.microsoft.com/library/windows/hardware/ff536116)  
This structure supplies the signature of the structure, the name of a control method, and an input array of [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structures. The array can contain a maximum number of seven such structures. An ACPI\_METHOD\_ARGUMENT structure can contain a ULONG integer, an ASCII string, an ACPI package description, or an array of custom data.

Windows also supports the [**IOCTL\_ACPI\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536149) request. A driver for a device can use this request to evaluate a control method that is a descendant child object in the ACPI namespace of the device to which the request is sent. The IOCTL\_ACPI\_EVAL\_METHOD\_EX request supports the following input structures:

<a href="" id="acpi-eval-input-buffer-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536118)  
This structure supplies the signature of the structure and the path and name of a control method that does not take an input argument.

<a href="" id="acpi-eval-input-buffer-simple-integer-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_INTEGER\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536120)  
This structure supplies the signature of the structure and the path and name of a control method that takes a single integer of type ULONG64 as an input argument.

<a href="" id="acpi-eval-input-buffer-simple-string-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_STRING\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536122)  
This structure supplies the signature of the structure and the path and name of a control method that takes a single NULL-terminated ASCII string as an input argument.

<a href="" id="acpi-eval-input-buffer-complex-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_COMPLEX\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536117)  
This structure supplies the signature of the structure and the path and name of a control method that takes an array of ACPI\_METHOD\_ARGUMENT structures as input. The array can contain a maximum number of seven such structures. An ACPI\_METHOD\_ARGUMENT structure can contain a ULONG integer, an ASCII string, an ACPI package description, or an array of custom data.

To obtain the path and name of child objects in the ACPI namespace of a device, a driver for a device can use an [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) request, as described in [Enumerating Child Devices and Control Methods](enumerating-child-devices-and-control-methods.md).
