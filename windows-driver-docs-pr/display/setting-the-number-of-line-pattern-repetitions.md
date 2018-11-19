---
title: Setting the Number of Line Pattern Repetitions
description: Setting the Number of Line Pattern Repetitions
ms.assetid: 090b823a-59d0-40e1-8feb-0b03b7f08fee
keywords:
- line pattern repetitions WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Number of Line Pattern Repetitions


## <span id="ddk_setting_the_number_of_line_pattern_repetitions_gg"></span><span id="DDK_SETTING_THE_NUMBER_OF_LINE_PATTERN_REPETITIONS_GG"></span>


Applications can direct a Direct3D device to render primitives using solid or patterned lines. Applications can also stretch a particular line pattern if the device supports repeating the pattern. The device's driver must set the D3DPMISCCAPS\_LINEPATTERNREP flag to indicate that the device supports repeating a particular line pattern. How this flag is set depends on the DirectX version:

-   For DirectX 7.0 and earlier, set this flag in the **dwMiscCaps** member of the [**D3DPRIMCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549034) structure.

-   For DirectX 8.0 and later, set this flag in the **PrimitiveMiscCaps** member of the D3DCAPS*Xx* structure, where *Xx* indicates the DirectX version (for example, D3DCAPS8 for version 8 and D3DCAPS9 for version 9). D3DCAPS8 and D3DCAPS9 are described in their respective versions of the DirectX SDK documentation.

When applications set the render-state value for the D3DRENDERSTATE\_LINEPATTERN (or D3DRS\_LINEPATTERN) render state, they can specify the number of times to repeat the line pattern by setting the **wRepeatFactor** member of the D3DLINEPATTERN structure. Applications can set this member to a maximum value of 65535 (16-bit value). However, hardware only supports a maximum of 255 (8-bit value). Therefore, a display driver must fail a request that attempts to set the line-pattern-repetition number to a value greater than 255 as an invalid request. D3DLINEPATTERN is described in the DirectX SDK documentation.

 

 





