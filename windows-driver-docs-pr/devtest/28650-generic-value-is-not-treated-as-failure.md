---
title: C28650
description: warning C28650 The type for which 0 is being used does not treat it as failure case. Returning a status value such as TRUE is not the same as returning a status value that indicates failure.
ms.assetid: faa24e4b-327c-42c7-92ee-33cd7b6ce5cb
---

# C28650


warning C28650: The type for which !0 is being used does not treat it as failure case.

Returning a status value such as !TRUE is not the same as returning a status value that indicates failure.

Certain data types such as **NTSTATUS** and **HRESULT** have associated macros that classify values of these types into SUCCESS or FAILURE. These macros check the most significant bit of the returned value or values to determine this. Thus, 0 and 1 are both classified as SUCCESS values.

The proper way to fix this warning is to return a proper error code instead of a generic value such as –1.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28650%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




