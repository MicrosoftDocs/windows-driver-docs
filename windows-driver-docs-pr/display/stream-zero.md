---
title: Stream Zero
description: Stream Zero
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multiple vertex streams
- multiple vertex streams WDK DirectX 8.0
- vertex multiple streams WDK DirectX 8.0
- stream zero WDK DirectX 8.0
- vertex stream zero WDK DirectX 8.0
ms.date: 04/20/2017
---

# Stream Zero


## <span id="ddk_stream_zero_gg"></span><span id="DDK_STREAM_ZERO_GG"></span>


Vertex stream zero is treated differently from the other streams because it is the only stream supported by earlier versions of Direct3D. Vertex buffers that have a flexible vertex format (FVF), where the FVF field is nonzero, can only be bound to stream zero. However, this does not imply that the vertex buffer bound to stream zero always has a flexible vertex format.

Stream zero is also the implied vertex source when one of the special, fixed-function vertex shaders is the current vertex shader handle.

 

 





