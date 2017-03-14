---
title: Stream Output Stage
description: Stream Output Stage
ms.assetid: e3f4685f-a214-4934-a36f-92591ef99db8
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Stream%20Output%20Stage%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




