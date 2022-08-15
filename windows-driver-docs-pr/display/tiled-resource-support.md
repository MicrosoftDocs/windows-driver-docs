---
title: Tiled resource support
description: Tiled resources can be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability is new starting with Windows 8.1.
ms.date: 10/20/2018
---

# Tiled resource support


Tiled resources can be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability is new starting with Windows 8.1.

These reference topics describe how to implement this capability in your user-mode display driver:

* [**PFND3DWDDM1_3DDI_CHECKMULTISAMPLEQUALITYLEVELS**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_checkmultisamplequalitylevels)
* [**PFND3DWDDM1_3DDI_COPYTILEMAPPINGS**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_copytilemappings)
* [**PFND3DWDDM1_3DDI_COPYTILES**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_copytiles)
* [**PFND3DWDDM1_3DDI_GETMIPPACKING**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_getmippacking)
* [**PFND3DWDDM1_3DDI_RELOCATEDEVICEFUNCS**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_relocatedevicefuncs)
* [**PFND3DWDDM1_3DDI_RESIZETILEPOOL**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_resizetilepool)
* [**PFND3DWDDM1_3DDI_TILEDRESOURCEBARRIER**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_tiledresourcebarrier)
* [**PFND3DWDDM1_3DDI_UPDATETILEMAPPINGS**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_updatetilemappings)
* [**PFND3DWDDM1_3DDI_UPDATETILES**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_updatetiles)
* [**D3DWDDM1\_3DDI\_CHECK\_MULTISAMPLE\_QUALITY\_LEVELS\_FLAG**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3dwddm1_3ddi_check_multisample_quality_levels_flag)
* [**D3DWDDM1\_3DDI\_D3D11\_OPTIONS\_DATA1**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3dwddm1_3ddi_d3d11_options_data1)
* [**D3DWDDM1\_3DDI\_DEVICEFUNCS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3dwddm1_3ddi_devicefuncs)
* [**D3DWDDM1\_3DDI\_TILE\_COPY\_FLAG**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3dwddm1_3ddi_tile_copy_flag)
* [**D3DWDDM1\_3DDI\_TILE\_MAPPING\_FLAG**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3dwddm1_3ddi_tile_mapping_flag)
* [**D3DWDDM1\_3DDI\_TILE\_RANGE\_FLAG**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3dwddm1_3ddi_tile_range_flag)
* [**D3DWDDM1\_3DDI\_TILE\_REGION\_SIZE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3dwddm1_3ddi_tile_region_size)
* [**D3DWDDM1\_3DDI\_TILED\_RESOURCE\_COORDINATE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3dwddm1_3ddi_tiled_resource_coordinate)
* [**D3DWDDM1\_3DDI\_TILED\_RESOURCES\_SUPPORT\_FLAG**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3dwddm1_3ddi_tiled_resources_support_flag)
* [**D3D10\_2DDICAPS\_TYPE**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3d10_2ddicaps_type) (**D3DWDDM1\_3DDICAPS\_D3D11\_OPTIONS1** constant value)
* [**D3D10\_DDI\_FILTER**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3d10_ddi_filter) (**D3DWDDM1\_3DDI\_FILTER\_XXX** constant values)
* [**D3D10\_DDI\_RESOURCE\_MISC\_FLAG**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3d10_ddi_resource_misc_flag)
 (**D3DWDDM1\_3DDI\_RESOURCE\_MISC\_TILED** and **D3DWDDM1\_3DDI\_RESOURCE\_MISC\_TILE\_POOL** constant values)
* [**D3D10DDIARG\_CREATEDEVICE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_createdevice) (**pWDDM1\_3DeviceFuncs** member)
* [**D3D11DDIARG\_CREATEDEFERREDCONTEXT**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddiarg_createdeferredcontext) (**pWDDM1\_3ContextFuncs** member)

 

