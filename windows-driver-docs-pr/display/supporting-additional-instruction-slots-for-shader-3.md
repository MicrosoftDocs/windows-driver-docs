---
title: Supporting Additional Instruction Slots for Shader 3
description: Supporting Additional Instruction Slots for Shader 3
ms.assetid: 8ff00178-cd08-42ce-8dea-127fc0d04733
keywords:
- instruction slots WDK DirectX 9.0
- shaders WDK DirectX 9.0
- pixel shaders WDK DirectX 9.0
- vertex shaders WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Additional Instruction Slots for Shader 3


## <span id="ddk_supporting_additional_instruction_slots_for_shader_3_gg"></span><span id="DDK_SUPPORTING_ADDITIONAL_INSTRUCTION_SLOTS_FOR_SHADER_3_GG"></span>


A display device that supports either pixel or vertex shader version 3.0 and later must support at least 512 instruction slots for either shader type. However, this display device can support up to 32768 instruction slots for either shader type.

To indicate the maximum number of instruction slots for the vertex shader 3.0 that the device supports, the DirectX 9.0 driver for the device sets the **MaxVertexShader30InstructionSlots** member of the D3DCAPS9 structure to the maximum number.

To indicate the maximum number of instruction slots for the pixel shader 3.0 that the device supports, the DirectX 9.0 driver for the device sets the **MaxPixelShader30InstructionSlots** member of the D3DCAPS9 structure to the maximum number.

Because the maximum number of instruction slots for pixel and vertex 3.0 shaders can be different, the DirectX 9.0 driver can set **MaxVertexShader30InstructionSlots** and **MaxPixelShader30InstructionSlots** to different values. The driver can set the maximum number of instruction slots from 512 to 32768. If the driver sets either **MaxVertexShader30InstructionSlots** or **MaxPixelShader30InstructionSlots** to a value that is outside the allowable range, the driver fails to load.

The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

 

 





