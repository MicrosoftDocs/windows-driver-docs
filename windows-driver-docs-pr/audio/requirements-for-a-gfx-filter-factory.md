---
title: Requirements for a GFX Filter Factory
description: Requirements for a GFX Filter Factory
ms.assetid: 06212686-24d3-4169-ad93-1cd685e22dde
keywords:
- GFX filters WDK audio , filter factory
- filter factories WDK audio
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Requirements for a GFX Filter Factory


## <span id="requirements_for_a_gfx_filter_factory"></span><span id="REQUIREMENTS_FOR_A_GFX_FILTER_FACTORY"></span>


For the operating system to treat an [AVStream](https://msdn.microsoft.com/library/windows/hardware/ff554240) filter factory as a factory for GFX filters, the [filter factories](filter-factories.md) should do the following:

-   Register its device interface in both the KSCATEGORY\_AUDIO and KSCATEGORY\_DATATRANSFORM device classes.

-   Have only one input pin and one output pin.

-   Add a **Gfx** subkey to the filter's KSCATEGORY\_AUDIO device interface registry key. The device setup information file for the filter factory typically uses an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) to add the **Gfx** subkey to the registry path during driver installation.

 

 




