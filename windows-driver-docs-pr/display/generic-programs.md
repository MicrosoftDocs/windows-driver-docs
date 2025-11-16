---
title: Generic Programs
description: Describes how a graphics driver can support generic programs starting in Windows 11, version 24H2 (WDDM 3.2).
keywords:
- WDDM, generic programs
- Direct3D 12, generic programs
- WDDM, state objects
- pipeline state objects, generic programs
ms.date: 11/14/2025
ms.topic: concept-article
ai.usage: ai-assisted
---

# Generic programs

Generic programs provide a way to define graphics and compute pipelines within state objects, using the same infrastructure as raytracing and [work graphs](work-graphs.md). Instead of creating separate pipeline state objects (PSOs), you can define multiple programs in a single state object by composing shared building blocks, such as shaders and blend state.

This article describes the DDIs for a user-mode graphics driver (UMD) to support generic programs, available starting in Windows 11, version 24H2 (WDDM 3.2). Generic programs require Shader Model 6.8 support. For details, see the [Generic Programs specification](https://microsoft.github.io/DirectX-Specs/d3d/WorkGraphs.html#generic-programs).

## Reporting generic programs support

Shader Model 6.8 support implies generic programs support. There's no separate capability reporting specific to generic programs.

## DDI function tables

Generic programs use the following DDI functions:

* [**D3D12DDI_DEVICE_FUNCS_CORE_0109**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_device_funcs_core_0109):
  * [**pfnGetProgramIdentifier**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_get_program_identifier_0108)

* [**D3D12DDI_COMMAND_LIST_FUNCS_3D_0108**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_command_list_funcs_3d_0108):
  * [**pfnSetProgram**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_set_program_0108)

## State objects

Define generic programs within state objects by using the **D3D12DDI_STATE_SUBOBJECT_TYPE_GENERIC_PROGRAM** subobject type (value 15) in [**D3D12DDI_STATE_SUBOBJECT_TYPE**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_state_subobject_type). See [**D3D12DDI_GENERIC_PROGRAM_DESC_0108**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_generic_program_desc_0108) for the subobject structure.

A generic program specifies a program name, shader exports (vertex shader, pixel shader, compute shader, and others), and references to other subobjects like blend state and rasterizer state. Graphics pipeline state subobjects include blend, rasterizer, depth/stencil, input layout, primitive topology, render target formats, and others as defined in the **D3D12DDI_STATE_SUBOBJECT_TYPE** enum.

Generic programs support the following Shader Model 6.8 shader targets: **vs_6_8**, **ps_6_8**, **cs_6_8**, **ms_6_8**, and **as_6_8**.

## Relationship to work graphs

Generic programs and [work graphs](work-graphs.md) are independent features that share state object infrastructure. Generic programs require only Shader Model 6.8, while work graphs require explicit WorkGraphsTier capability support.

## See also

* [Work graphs](work-graphs.md)
* [Generic Programs specification](https://microsoft.github.io/DirectX-Specs/d3d/WorkGraphs.html#generic-programs)
* [D3D12 Work Graphs specification](https://microsoft.github.io/DirectX-Specs/d3d/WorkGraphs.html)
