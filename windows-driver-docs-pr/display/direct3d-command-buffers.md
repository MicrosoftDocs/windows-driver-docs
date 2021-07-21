---
title: Direct3D Command Buffers
description: Direct3D Command Buffers
keywords:
- command buffers WDK Direct3D
- buffers WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D Command Buffers


## <span id="ddk_direct3d_command_buffers_gg"></span><span id="DDK_DIRECT3D_COMMAND_BUFFERS_GG"></span>


The following figure shows portions of a sample logical command buffer. The driver's [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) callback receives a pointer to a command buffer in the **lpDDCommands** member of the [**D3DHAL\_DRAWPRIMITIVES2DATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_drawprimitives2data) structure. The command buffer is always processed sequentially.

![diagram illustrating portions of a direct3d sample logical command buffer.](images/d3dcmbuf.png)

As shown in the preceding figure, a command buffer contains [**D3DHAL\_DP2COMMAND**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2command) structures, where the **bCommand** member of each structure identifies a command. The following lists possible commands:

-   D3DDP2OP\_RENDERSTATE indicates that there are **wStateCount**[**D3DHAL\_DP2RENDERSTATE**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2renderstate) structures that follow in the command buffer. The driver should parse the state from each of these structures and update its private driver state accordingly. The driver should also update the appropriate state in the array to which **lpdwRStates** points. If the driver does not support the state requested in the command buffer, the driver should override the requested value with one that it supports.

-   D3DDP2OP\_TEXTURESTAGESTATE indicates that there are **wStateCount**[**D3DHAL\_DP2TEXTURESTAGESTATE**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2texturestagestate) structures that follow in the command buffer. The driver should parse the state from each of these structures and update the driver's texture state associated with the specified texture stage accordingly. The driver does not report texture stage state back to the Direct3D runtime.

    A driver is required to properly parse up to eight texture coordinate sets regardless of how many coordinate sets it actually uses.

-   D3DDP2OP\_VIEWPORTINFO indicates that there is one [**D3DHAL\_DP2VIEWPORTINFO**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2viewportinfo) structure that follows in the command buffer. The driver should parse this structure and update the viewport information stored in the driver's internal rendering context.

-   D3DDP2OP\_WINFO indicates that there is one [**D3DHAL\_DP2WINFO**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2winfo) structure that follows in the command buffer. The driver should parse this structure and update the w-buffer information stored in the driver's internal rendering context.

-   Any of the remaining D3DDP2OP\_*Xxx* commands indicate that there is enough data following in the command buffer to render **wPrimitiveCount** (a member of the [**D3DHAL\_DP2COMMAND**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2command) structure) primitives. Depending on the primitive command, the driver should parse D3DHAL\_DP2*Xxx* structures from the command buffer and vertex-associated data from either or both the vertex buffer and command buffer. The driver must attempt to process all valid D3DDP2OP\_*Xxx* commands; that is, the driver cannot choose to ignore certain defined primitive types. For more information, see the individual D3DHAL\_DP2*Xxx* structure reference pages.

Depending on the current command, the following additional information is stored in the command buffer:

-   Index information for all D3DDP2OP\_INDEXED*Xxx* primitive commands.

-   Vertex data for the D3DDP2OP\_TRIANGLEFAN\_IMM and D3DDP2OP\_LINELIST\_IMM primitive commands.

-   Additional operations are also defined as D3DDP2OP\_*Xxx* opcodes in the [**D3DHAL\_DP2OPERATION**](/windows-hardware/drivers/ddi/d3dhal/ne-d3dhal-_d3dhal_dp2operation) structure. These are equivalent to D3DDP2OP\_*Xxx* commands with the same names.

The command buffer occasionally contains commands that are understood only by Direct3D. If the driver's [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) callback does not recognize the command, the driver should call Direct3D's **D3dParseUnknownCommand** callback to attempt to parse it. When **D3dParseUnknownCommand** returns successfully, the driver should continue parsing and processing the command buffer. If **D3dParseUnknownCommand** fails by returning D3DERR\_COMMAND\_UNPARSED, **D3dDrawPrimitives2** should set the following members of the [**D3DHAL\_DRAWPRIMITIVES2DATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_drawprimitives2data) structure and return:

-   In **dwErrorOffset**, write the offset of the first unhandled [**D3DHAL\_DP2COMMAND**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2command) structure that is part of the buffer to which **lpDDCommands** points.

-   Set **ddrval** to D3DERR\_COMMAND\_UNPARSED.

For information about how to initialize the **D3dParseUnknownCommand** callback, see [Direct3D Driver Initialization](direct3d-driver-initialization.md).

To simplify implementation of **D3dDrawPrimitives2**, driver writers can copy the parsing code from the *Perm3* sample code and write driver-specific rendering and state update code only.

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia3 sample display driver (*Perm3.h*). You can get this sample driver from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the DDK - Windows Driver Development Kit page of the WDHC website.

 

Direct3D is not always informed of the current render states. For example, execute buffers are not inspected by the runtime before they reach the driver. The driver can keep track of the render state array with the **lpdwRStates** member of the [**D3DHAL\_DRAWPRIMITIVES2DATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_drawprimitives2data) structure. This is a pointer to the internal render states array that the driver keeps up to date as state changes occur.

 

