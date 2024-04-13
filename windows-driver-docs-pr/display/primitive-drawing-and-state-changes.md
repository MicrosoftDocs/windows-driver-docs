---
title: Primitive Drawing and State Changes
description: Primitive Drawing and State Changes
keywords:
- Direct3D WDK Windows 2000 display , primitive drawing
- Direct3D WDK Windows 2000 display , state changes
- states WDK Direct3D
- primitive drawing WDK Direct3D
- D3dDrawPrimitives2
ms.date: 04/20/2017
---

# Primitive Drawing and State Changes


## <span id="ddk_primitive_drawing_and_state_changes_gg"></span><span id="DDK_PRIMITIVE_DRAWING_AND_STATE_CHANGES_GG"></span>


All Microsoft Direct3D graphics primitives and state changes are passed to the [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) callback in command and vertex buffers. The driver must parse these buffers and process all drawing and state change requests.

The following sections discuss the layout of command and vertex buffers and describe how the driver should process them:

[Command and Vertex Buffers](command-and-vertex-buffers.md)

[Direct3D Command Buffers](direct3d-command-buffers.md)

[Direct3D Vertex Buffers](direct3d-vertex-buffers.md)

[Accelerated State Management](accelerated-state-management.md)

 

