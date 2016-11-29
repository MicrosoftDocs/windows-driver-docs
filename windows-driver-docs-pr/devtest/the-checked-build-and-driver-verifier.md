---
title: The Checked Build and Driver Verifier
description: The Checked Build and Driver Verifier
ms.assetid: 311a9588-5094-432c-b696-339ff3ff8c35
keywords: ["checked builds WDK , Driver Verifier", "Driver Verifier WDK checked builds"]
---

# The Checked Build and Driver Verifier


## <span id="ddk_the_checked_build_and_driver_verifier_tools"></span><span id="DDK_THE_CHECKED_BUILD_AND_DRIVER_VERIFIER_TOOLS"></span>


While the checked build and [Driver Verifier](driver-verifier.md) provide some checks that overlap, it is best to think of them as providing complementary levels of checking. Testing your driver with the checked build is not a substitute for testing with Driver Verifier. Similarly, testing with Driver Verifier does not provide precisely the same level of test coverage as using the checked build.

When Driver Verifier runs on the checked build, it often displays additional information in the debugger when a problem is detected. In addition, when a debugger is attached, in many cases Driver Verifier runs a breakpoint prior to halting the system with a bug check. This breakpoint gives you a chance to examine the state of the system, and debug your driver, prior to the Driver-Verifier-invoked system crash.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20The%20Checked%20Build%20and%20Driver%20Verifier%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




