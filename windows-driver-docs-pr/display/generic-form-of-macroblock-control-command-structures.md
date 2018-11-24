---
title: Generic Form of Macroblock Control Command Structures
description: Generic Form of Macroblock Control Command Structures
ms.assetid: 44009238-0a8e-4018-9b50-06729640f5e4
keywords:
- macroblocks WDK DirectX VA , generic command structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Generic Form of Macroblock Control Command Structures


## <span id="ddk_generic_form_of_macroblock_control_command_structures_gg"></span><span id="DDK_GENERIC_FORM_OF_MACROBLOCK_CONTROL_COMMAND_STRUCTURES_GG"></span>


The following macroblock control structures explicitly defined in *dxva.h* are special cases of a generic design used for macroblock control commands in DirectX VA:

[**DXVA\_MBctrl\_I\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563983)

[**DXVA\_MBctrl\_I\_OffHostIDCT\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563989)

[**DXVA\_MBctrl\_P\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563993)

[**DXVA\_MBctrl\_P\_OffHostIDCT\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563997)

These structures represent only the most commonly used forms of macroblock control commands. Additional macroblock control commands can be created, based upon the design of these existing structures, to allow a driver to support other video decoding elements and to handle different configurations for the decoding process.

This section describes the members of a generic macroblock control command structure that are used as the basis for creating additional macroblock control commands. The macroblock control command structure definition in this section is divided into four parts.

**Note**   Macroblock control commands are aligned with 16-byte memory boundaries and constructed as packed data structures with single-byte alignment packing.

 

 

 





