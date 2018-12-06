---
title: Command Stream
description: Command Stream
ms.assetid: 125e2072-42d6-4d4b-aec9-94b40a9d493c
keywords:
- Direct3D WDK Windows 2000 display , operation codes
- operation codes WDK Direct3D
- command stream WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Command Stream


## <span id="ddk_command_stream_gg"></span><span id="DDK_COMMAND_STREAM_GG"></span>


At the driver level, instructions come in the form of calls to [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704). The input structure [**D3DHAL\_DRAWPRIMITIVES2DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545957) contains a pointer into a command buffer. This is a sequence of [**D3DHAL\_DP2COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff545454) structures. Each of these structures contains a **bCommand** member that specifies what type of data follows it in the buffer. This specification comes in the form of a [**D3DHAL\_DP2OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff545678) enumerated type, such as D3DDP2OP\_INDEXEDTRIANGLESTRIP or, in the case of setting up texture states, D3DDP2OP\_TEXTURESTAGESTATE.

In other words, the D3DHAL\_DP2OPERATION operation code specifies what type of structures follow it in the command buffer. The number of structures to follow is specified by either **wPrimitiveCount** or **wStateCount**, members of a union that is in turn a member of the D3DHAL\_DP2COMMAND structure. The **wPrimitiveCount** member keeps track of the number of graphics primitives to render, while the **wStateCount** member keeps track of the number of state changes to process.

For an example of how a driver process operation codes, see [Processing Texture Stages](processing-texture-stages.md).

 

 





