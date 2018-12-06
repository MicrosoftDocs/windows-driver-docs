---
title: Stream Output Stage
description: Stream Output Stage
ms.assetid: e3f4685f-a214-4934-a36f-92591ef99db8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stream Output Stage


The stream output (SO) stage can stream out vertices to memory just before those vertices arrive at the rasterizer. The stream output operates like a tap in the pipeline. This tap can be turned on even as data continues to flow down to the rasterizer. Data that is sent out through the stream output is concatenated to buffers. These buffers can be recirculated on subsequent passes as pipeline inputs.

One constraint about the stream output is that it is tied to the geometry shader, in that they must be created together (though either can be "NULL"/"off"). Although, the particular memory buffers that are streamed out to are not tied to a particular geometry shader and stream output pair. Only the description of which parts of the vertex data to feed to a stream output is tied to the geometry shader.

The stream output might be useful for saving ordered pipeline data that will be reused. For example, a batch of vertices might be "skinned" by passing the vertices into the pipeline as if they are independent points (just to visit all of them once), applying "skinning" operations on each vertex, and streaming out the results to memory. The saved out "skinned" vertices are subsequently available for use as input.

Because the amount of output that is written through the stream output is dynamic, a new type of Draw, [**DrawAuto**](https://msdn.microsoft.com/library/windows/hardware/ff556123), is necessary to allow stream output buffers to be reused with the input assembler, without the CPU involvement to determine how much data was actually written. In addition, queries are necessary to mitigate stream output overflow, as well as retrieve how much data was written to the stream output buffers (D3D10DDI\_QUERY\_STREAMOVERFLOWPREDICATE and D3D10DDI\_QUERY\_STREAMOUTPUTSTATS of the [**D3D10DDI\_QUERY**](https://msdn.microsoft.com/library/windows/hardware/ff541850) enumeration).

The Direct3D runtime calls the following driver functions to create and set up the stream output:

[**CalcPrivateGeometryShaderWithStreamOutput**](https://msdn.microsoft.com/library/windows/hardware/ff538291)

[**CreateGeometryShaderWithStreamOutput**](https://msdn.microsoft.com/library/windows/hardware/ff540650)

[**SoSetTargets**](https://msdn.microsoft.com/library/windows/hardware/ff569714)

 

 





