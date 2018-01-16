---
title: Query Implemented Functions (Function Index 0)
description: This function returns the functions supported by this interface version.
ms.assetid: AFF735D7-BB3F-4532-8BF4-F616C081921C
---

# Query Implemented Functions (Function Index 0)


This function returns the functions supported by this interface version. Function 0 of every \_DSM is a query function that returns the set of supported function indexes, and is always required. For the definition of Function 0, see section 9.14.1, "\_DSM (Device Specific Method)" in the [ACPI 6.0 specification](http://www.acpi.info).

## <span id="Arguments__ARG_3_"></span><span id="arguments__arg_3_"></span><span id="ARGUMENTS__ARG_3_"></span>Arguments (ARG 3)


None.

## <span id="Returns"></span><span id="returns"></span><span id="RETURNS"></span>Returns


This function returns an ACPI Buffer containing the following byte values in order: 0xFF, 0xFF, 0xFF, & 0xFF.

## <span id="related_topics"></span>Related topics


[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Query%20Implemented%20Functions%20%28Function%20Index%200%29%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





