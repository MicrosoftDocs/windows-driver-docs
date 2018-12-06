---
title: The Checked Build and Driver Verifier
description: The Checked Build and Driver Verifier
ms.assetid: 311a9588-5094-432c-b696-339ff3ff8c35
keywords:
- checked builds WDK , Driver Verifier
- Driver Verifier WDK checked builds
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The Checked Build and Driver Verifier


## <span id="ddk_the_checked_build_and_driver_verifier_tools"></span><span id="DDK_THE_CHECKED_BUILD_AND_DRIVER_VERIFIER_TOOLS"></span>


While the checked build and [Driver Verifier](driver-verifier.md) provide some checks that overlap, it is best to think of them as providing complementary levels of checking. Testing your driver with the checked build is not a substitute for testing with Driver Verifier. Similarly, testing with Driver Verifier does not provide precisely the same level of test coverage as using the checked build.

When Driver Verifier runs on the checked build, it often displays additional information in the debugger when a problem is detected. In addition, when a debugger is attached, in many cases Driver Verifier runs a breakpoint prior to halting the system with a bug check. This breakpoint gives you a chance to examine the state of the system, and debug your driver, prior to the Driver-Verifier-invoked system crash.

 

 





