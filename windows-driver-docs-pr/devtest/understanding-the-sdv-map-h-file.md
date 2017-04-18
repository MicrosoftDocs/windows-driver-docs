---
title: Understanding the Sdv-map.h File
description: Understanding the Sdv-map.h File
ms.assetid: 2ad3d94d-3991-414b-ae1c-27a07c10839f
keywords: ["Sdv-map.h WDK Static Driver Verifier , about Sdv-map.h"]
---

# Understanding the Sdv-map.h File


Before verifying a driver, SDV scans the driver's source code and creates an Sdv-map.h file in the driver's sources directory. You should examine and approve this header file before verifying your driver.

You can also use a **staticdv /scan** command to direct SDV to scan the driver's code and creates the file. For instructions, see [Scanning the driver](scanning-the-driver.md).

If the Sdv-map.h file is incomplete or incorrect, that is, if any of the entry points are missing, or the entry points are associated with the wrong function role type, the verification is not reliable.

For a list of the functions that SDV uses for the WDM, KMDF, and NDIS drivers, see [Using Function Role Type Declarations](using-function-role-type-declarations.md).

The function role types that appear in the Sdv-map.h file are the ones that SDV uses in its rule verification. SDV uses the function role type declarations that you added to your header files to produce the Sdv-map.h file in the driver's source code directory. In the Sdv-map.h file, SDV maps the declared driver functions to function identifiers that are used by SDV during verification. For example, for a KMDF driver, a callback function called *MyDpc* might be mapped to fun\_WDF\_DPC\_1. SDV does not require that the driver declare function role types for all of the callback functions that it uses. It requires only that if the driver has declared the function role type that SDV knows about and interprets it correctly. If a driver does not have a function role type that SDV requires to verify a particular rule, SDV concludes that the rule does not apply to the driver. This is not considered to be an error or a defect. For a list of the functions that SDV uses for the WDM, KMDF, and NDIS drivers, see [Using Function Role Type Declarations](using-function-role-type-declarations.md).

It is important that you correct any errors in the Sdv-map.h file before verifying the driver. If the file is wrong, the verification might not be reliable.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Understanding%20the%20Sdv-map.h%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




