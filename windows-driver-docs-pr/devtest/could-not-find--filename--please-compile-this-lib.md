---
title: Could not find filename please compile this lib
description: Could not find filename please compile this lib
ms.assetid: e572ed6d-a3f3-402a-aa99-66c503de8457
---

# Could not find &lt;filename&gt; please compile this lib


This warning appears when SDV detects that a driver requires a library, but it cannot find one or more of the files that it creates when processing a library with the **staticdv /lib** command. This situation can occur when the library has not been processed or because files have been deleted.

Because library processing is recommended, but not required, SDV continues with the verification after displaying this message.

To process or reprocess a library that the driver requires, use the **staticdv /lib** command. Do not delete any files in the driver's sources directory or the library's sources directory. You do not need to delete any files before reprocessing a library that has already been processed.

For more information about processing libraries, see [Library Processing in SDV](library-processing-in-static-driver-verifier.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Could%20not%20find%20<filename>%20please%20compile%20this%20lib%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




