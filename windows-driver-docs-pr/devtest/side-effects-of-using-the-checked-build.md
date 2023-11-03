---
title: Side Effects of Using the Checked Build
description: Side Effects of Using the Checked Build
keywords:
- checked builds WDK , performance impact
ms.date: 05/08/2020
---

# Side Effects of Using the Checked Build

## <span id="ddk_side_effects_of_using_the_checked_build_tools"></span><span id="DDK_SIDE_EFFECTS_OF_USING_THE_CHECKED_BUILD_TOOLS"></span>

> [!NOTE]
> Checked builds were available on older versions of Windows, before Windows 10 version 1803.
> Use tools such as Driver Verifier and GFlags to check driver code in later versions of Windows.

The checked components of the operating system contain fewer optimizations and more debugging checks than otherwise identical free components. Therefore, checked components run substantially slower than free counterparts.

It is important for driver writers to remember that this slower execution can cause changes in the timing relationships among code paths. Therefore, the checked build can hide timing problems (such as race conditions or deadlocks) that might be revealed in the free build. Thus, you must test all of your drivers on both the free build and the checked build of the operating system before release.

