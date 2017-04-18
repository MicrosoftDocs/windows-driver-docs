---
title: Present and GetBltStatus
description: Present and GetBltStatus
ms.assetid: 76fd88df-18a9-4f00-834d-6683788fc2f6
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , presentation", "presentation WDK DirectX 8.0", "rendering results visible WDK DirectX 8.0", "visible results WDK DirectX 8.0", "DdGetBltStatus"]
---

# Present and GetBltStatus


## <span id="ddk_present_and_getbltstatus_gg"></span><span id="DDK_PRESENT_AND_GETBLTSTATUS_GG"></span>


For DX8 the runtime no longer calls [*DdGetBltStatus*](https://msdn.microsoft.com/library/windows/hardware/ff549385) on blts involving system memory surfaces. This was always the behavior on Windows 2000. The result is that asynchronous DMA to or from system memory surfaces is no longer possible. DX8 drivers should not page lock system memory surfaces by themselves, and system memory to video memory transfers should be synchronous.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Present%20and%20GetBltStatus%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




