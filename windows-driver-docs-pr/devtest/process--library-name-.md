---
title: Process library name
description: Process library name
ms.assetid: 4c075256-1e2a-498f-b738-890580392156
---

# Process &lt;library name&gt;


SDV reports this error when it detects that a driver depends on a library that it has not processed.

As a best practice, this error message should be regarded as indicating an error. Because the libraries might include code that changes the verification result, the verification is not reliable until it is run with all dependent libraries.

However, because some libraries cannot be processed, either because the source code is not available, or because the library is not written in C, SDV does not terminate the verification. It continues the verification without the library code. The user must determine if the verification is still valid without the libraries.

To process a library, in the library's sources directory, type **staticdv /lib**.

For more information about library processing, see [Library Processing in Static Driver Verifier](library-processing-in-static-driver-verifier.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Process%20<library%20name>%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




