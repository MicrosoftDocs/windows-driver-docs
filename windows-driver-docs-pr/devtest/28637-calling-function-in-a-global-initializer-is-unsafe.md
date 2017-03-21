---
title: C28637
description: Warning C28637 Calling the function in a global initializer is unsafe.
ms.assetid: 9b392995-9583-4847-aded-f32e1daf28ed
---

# C28637


warning C28637: Calling the function in a global initializer is unsafe

When you use a DLL, it is frequently the case that any static constructors are called from DllMain. There are a number of constraints that apply to call other functions from DllMain. In particular, it is possible to create memory leaks if the DLL is loaded and unloaded dynamically. For more information, see the [DllMain Callback Function](http://go.microsoft.com/fwlink/p/?linkid=133876).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28637%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




