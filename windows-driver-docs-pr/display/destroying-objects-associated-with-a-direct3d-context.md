---
title: Destroying Objects Associated with a Direct3D Context
description: Destroying Objects Associated with a Direct3D Context
keywords:
- memory leaks WDK DirectX 9.0
- context WDK Direct3D , DirectX 9.0
- destroying objects associated with context WDK DirectX 9.0
ms.date: 04/20/2017
---

# Destroying Objects Associated with a Direct3D Context


## <span id="ddk_destroying_objects_associated_with_a_direct3d_context_gg"></span><span id="DDK_DESTROYING_OBJECTS_ASSOCIATED_WITH_A_DIRECT3D_CONTEXT_GG"></span>


This topic applies to DirectX 7.0 and later.

To prevent memory leaks, a display driver must release all objects associated with a Direct3D context when the driver's [**D3dContextDestroy**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_contextdestroycb) function is called. These objects include, for example, vertex and pixel [shaders](direct3d-shaders.md), [declarations and code for vertex shaders](separating-declarations-and-code-for-vertex-shaders.md), resources for [asynchronous queries](supporting-asynchronous-query-operations.md), and texture resources.

 

