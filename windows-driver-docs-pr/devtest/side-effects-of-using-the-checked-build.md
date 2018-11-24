---
title: Side Effects of Using the Checked Build
description: Side Effects of Using the Checked Build
ms.assetid: 8c08d4f3-1221-4858-afd4-249d966c14a7
keywords:
- checked builds WDK , performance impact
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Side Effects of Using the Checked Build


## <span id="ddk_side_effects_of_using_the_checked_build_tools"></span><span id="DDK_SIDE_EFFECTS_OF_USING_THE_CHECKED_BUILD_TOOLS"></span>


The checked components of the operating system contain fewer optimizations and more debugging checks than otherwise identical free components. Therefore, checked components run substantially slower than free counterparts.

It is important for driver writers to remember that this slower execution can cause changes in the timing relationships among code paths. Therefore, the checked build can hide timing problems (such as race conditions or deadlocks) that might be revealed in the free build. Thus, you must test all of your drivers on both the free build and the checked build of the operating system before release.

 

 





