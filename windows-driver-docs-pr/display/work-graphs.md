---
title: Work Graphs
description: Describes how a graphics driver can support work graphs starting in Windows 11, version 24H2 (WDDM 3.2).
keywords:
- WDDM, work graphs
- Direct3D 12, work graphs
- WDDM, GPU-driven rendering with work graphs
ms.date: 05/03/2024
---

# Work graphs

This article describes the DDIs that are added for a user-mode graphics driver (UMD) to support D3D12 work graphs. The work graph feature is available starting in Windows 11, version 24H2 (WDDM 3.2). A detailed explanation of work graphs can be found in the [D3D12 Work Graphs](https://microsoft.github.io/DirectX-Specs/d3d/WorkGraphs.html) specification.

## Reporting work graphs support

The following interfaces are updated or introduced for a UMD to report its support for work graphs:

* The **D3D12DDICAPS_TYPE_OPTIONS_0109** capability-reporting entry is added to the[**D3D12DDICAPS_TYPE**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddicaps_type) enum used by [**PFND3D12DDI_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_getcaps).

* This caps entry corresponds to the [**D3D12DDI_OPTIONS_DATA_0103**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_options_data_0103) caps structure, whose [**WorkGraphsTier**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_work_graphs_tier) member indicates the level of work graph support that the driver supports.

## DDI function tables

To support work graphs, UMD must implement the following functions and provide pointers to them in the following DDI function tables:

* [**D3D12DDI_DEVICE_FUNCS_CORE_0109**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_device_funcs_core_0109):
  * [**pfnGetProgramIdentifier**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_get_program_identifier_0108)
  * [**pfnGetWorkGraphMemoryRequirements**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_get_work_graph_memory_requirements_0108)

* [**D3D12DDI_COMMAND_LIST_FUNCS_3D_0108**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_command_list_funcs_3d_0108):
  * [**pfnSetProgram**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_set_program_0108)
  * [**pfnDispatchGraph**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_dispatch_graph_0108)

Reference pages for the dozens of work graph structures and enums associated with these added DDIs can be discovered by following the links from the DDI reference pages.

## DDI state object creation related structures and enums

The following [**D3D12DDI_STATE_SUBOBJECT_TYPE**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_state_subobject_type) subobject types (and their related state object creation structures) are relevant to work graphs.

| Definition | Enum Value | Related Structure |
| ---------- | ---------- | ----------------- |
| D3D12DDI_STATE_SUBOBJECT_TYPE_STATE_OBJECT_CONFIG   | 0 | D3D12DDI_STATE_OBJECT_CONFIG_0054 |
| D3D12DDI_STATE_SUBOBJECT_TYPE_GLOBAL_ROOT_SIGNATURE | 1 | D3D12DDI_GLOBAL_ROOT_SIGNATURE_0054 |
| D3D12DDI_STATE_SUBOBJECT_TYPE_LOCAL_ROOT_SIGNATURE  | 2 | D3D12DDI_LOCAL_ROOT_SIGNATURE_0054 |
| D3D12DDI_STATE_SUBOBJECT_TYPE_NODE_MASK             | 3 | D3D12_NODE_MASK_0054 |
| D3D12DDI_STATE_SUBOBJECT_TYPE_DXIL_LIBRARY          | 5 | D3D12DDI_DXIL_LIBRARY_DESC_0054 |
| D3D12DDI_STATE_SUBOBJECT_TYPE_EXISTING_COLLECTION   | 6 |  D3D12DDI_EXISTING_COLLECTION_DESC_0054 |
| D3D12DDI_STATE_SUBOBJECT_TYPE_WORK_GRAPH            | 13| D3D12DDI_WORK_GRAPH_DESC_0108 |
| D3D12DDI_STATE_SUBOBJECT_TYPE_SHADER_EXPORT_SUMMARY | 0x100000 | D3D12DDI_FUNCTION_SUMMARY_005 |

In a state object definition at the DDI, work graphs are a subobject of type **D3D12DDI_STATE_SUBOBJECT_TYPE_WORK_GRAPH**. See the [**D3D12DDI_WORK_GRAPH_DESC_0108**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_work_graph_desc_0108) structure for the subobject layout. Related structures and enums are linked from this structure's refpage.

The other subobject types are inherited as-is from the [DXR specification](https://microsoft.github.io/DirectX-Specs/d3d/Raytracing.html).
