---
title: Command Stream
description: Command Stream
keywords:
- Direct3D WDK Windows 2000 display , operation codes
- operation codes WDK Direct3D
- command stream WDK Direct3D
ms.date: 04/20/2017
---

# Command Stream


## <span id="ddk_command_stream_gg"></span><span id="DDK_COMMAND_STREAM_GG"></span>


At the driver level, instructions come in the form of calls to [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb). The input structure [**D3DHAL\_DRAWPRIMITIVES2DATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_drawprimitives2data) contains a pointer into a command buffer. This is a sequence of [**D3DHAL\_DP2COMMAND**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2command) structures. Each of these structures contains a **bCommand** member that specifies what type of data follows it in the buffer. This specification comes in the form of a [**D3DHAL\_DP2OPERATION**](/windows-hardware/drivers/ddi/d3dhal/ne-d3dhal-_d3dhal_dp2operation) enumerated type, such as D3DDP2OP\_INDEXEDTRIANGLESTRIP or, in the case of setting up texture states, D3DDP2OP\_TEXTURESTAGESTATE.

In other words, the D3DHAL\_DP2OPERATION operation code specifies what type of structures follow it in the command buffer. The number of structures to follow is specified by either **wPrimitiveCount** or **wStateCount**, members of a union that is in turn a member of the D3DHAL\_DP2COMMAND structure. The **wPrimitiveCount** member keeps track of the number of graphics primitives to render, while the **wStateCount** member keeps track of the number of state changes to process.

For an example of how a driver process operation codes, see [Processing Texture Stages](processing-texture-stages.md).

 

