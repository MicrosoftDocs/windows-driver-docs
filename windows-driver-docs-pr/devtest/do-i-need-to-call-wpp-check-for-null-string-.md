---
title: Do I need to call WPP\_CHECK\_FOR\_NULL\_STRING
description: Do I need to call WPP\_CHECK\_FOR\_NULL\_STRING
ms.assetid: 4a4dfe91-a70b-4297-9f11-fcc4b0e5a900
---

# Do I need to call WPP\_CHECK\_FOR\_NULL\_STRING?


Starting with the Windows 7 version of the Windows Driver Kit (WDK), the tracing components automatically check for **NULL** strings in the arguments that you pass in to the tracing functions. As a result, you do not have to call WPP\_CHECK\_FOR\_NULL\_STRING to verify each argument in order to prevent **NULL** strings from causing an exception.

If you build your [trace provider](trace-provider.md) (such as a driver or application) with the Windows 7 and later versions of the WDK, you can remove the WPP\_CHECK\_FOR\_NULL\_STRING macro from your source code.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Do%20I%20need%20to%20call%20WPP_CHECK_FOR_NULL_STRING?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




