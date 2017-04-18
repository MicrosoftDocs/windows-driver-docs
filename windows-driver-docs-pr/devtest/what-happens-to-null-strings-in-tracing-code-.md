---
title: What happens to NULL strings in tracing code
description: What happens to NULL strings in tracing code
ms.assetid: a2226cbd-28cf-48eb-b129-5c4d12eb2564
---

# What happens to NULL strings in tracing code?


By default, the tracing components in this version of the Windows Driver Kit (WDK) search for **NULL** strings in the arguments that you pass in functions. As a result, you do not have to verify each argument to prevent **NULL** strings from causing an exception.

In earlier versions of the WDK, the WPP\_CHECK\_FOR\_NULL\_STRING macro performed this function. If you build your kernel-mode driver or user-mode application by using this version of the WDK, you can remove the macro from your source code.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20What%20happens%20to%20NULL%20strings%20in%20tracing%20code?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




