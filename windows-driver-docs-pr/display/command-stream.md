---
title: Command Stream
description: Command Stream
ms.assetid: 125e2072-42d6-4d4b-aec9-94b40a9d493c
keywords:
- Direct3D WDK Windows 2000 display , operation codes
- operation codes WDK Direct3D
- command stream WDK Direct3D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Command Stream


## <span id="ddk_command_stream_gg"></span><span id="DDK_COMMAND_STREAM_GG"></span>


At the driver level, instructions come in the form of calls to [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704). The input structure [**D3DHAL\_DRAWPRIMITIVES2DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545957) contains a pointer into a command buffer. This is a sequence of [**D3DHAL\_DP2COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff545454) structures. Each of these structures contains a **bCommand** member that specifies what type of data follows it in the buffer. This specification comes in the form of a [**D3DHAL\_DP2OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff545678) enumerated type, such as D3DDP2OP\_INDEXEDTRIANGLESTRIP or, in the case of setting up texture states, D3DDP2OP\_TEXTURESTAGESTATE.

In other words, the D3DHAL\_DP2OPERATION operation code specifies what type of structures follow it in the command buffer. The number of structures to follow is specified by either **wPrimitiveCount** or **wStateCount**, members of a union that is in turn a member of the D3DHAL\_DP2COMMAND structure. The **wPrimitiveCount** member keeps track of the number of graphics primitives to render, while the **wStateCount** member keeps track of the number of state changes to process.

For an example of how a driver process operation codes, see [Processing Texture Stages](processing-texture-stages.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Command%20Stream%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




