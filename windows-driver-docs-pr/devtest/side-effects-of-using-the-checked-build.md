---
title: Side Effects of Using the Checked Build
description: Side Effects of Using the Checked Build
ms.assetid: 8c08d4f3-1221-4858-afd4-249d966c14a7
keywords: ["checked builds WDK , performance impact"]
---

# Side Effects of Using the Checked Build


## <span id="ddk_side_effects_of_using_the_checked_build_tools"></span><span id="DDK_SIDE_EFFECTS_OF_USING_THE_CHECKED_BUILD_TOOLS"></span>


The checked components of the operating system contain fewer optimizations and more debugging checks than otherwise identical free components. Therefore, checked components run substantially slower than free counterparts.

It is important for driver writers to remember that this slower execution can cause changes in the timing relationships among code paths. Therefore, the checked build can hide timing problems (such as race conditions or deadlocks) that might be revealed in the free build. Thus, you must test all of your drivers on both the free build and the checked build of the operating system before release.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Side%20Effects%20of%20Using%20the%20Checked%20Build%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




