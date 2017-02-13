---
title: Presentation with Multiple Heads
description: Presentation with Multiple Heads
ms.assetid: 60405ea7-91d5-4deb-9161-8890faa7e897
keywords: ["multiple-head hardware WDK DirectX 9.0 , presentation", "presentation WDK DirectX 9.0"]
---

# Presentation with Multiple Heads


## <span id="ddk_presentation_with_multiple_heads_gg"></span><span id="DDK_PRESENTATION_WITH_MULTIPLE_HEADS_GG"></span>


Applications can call the **Present** method either to present contents of back buffers for all heads at once or to present the back buffer for an individual head. For more information about **Present**, see the latest DirectX SDK documentation.

The runtime in turn makes independent sequential calls to the driver's [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306) or [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function. Because the display mode and refresh rate of each head might be different, these calls are always independent at the DDI level.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Presentation%20with%20Multiple%20Heads%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




