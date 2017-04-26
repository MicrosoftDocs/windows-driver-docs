---
title: Modifying Vertex Stream Frequency
description: Modifying Vertex Stream Frequency
ms.assetid: 81bbced4-7331-4e54-9617-1ef29b02f162
keywords:
- vertex stream frequency division WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Modifying Vertex Stream Frequency


## <span id="ddk_modifying_vertex_stream_frequency_gg"></span><span id="DDK_MODIFYING_VERTEX_STREAM_FREQUENCY_GG"></span>


A DirectX 9.0 version driver for a device that supports vertex shader version 3.0 and later must implement vertex stream frequency division. For version 2.0 and earlier models of vertex shader (including fixed function), the vertex shader is called once per vertex; for each call, the input vertex registers are initialized with unique vertex elements from the vertex streams. However, using vertex stream frequency division, the vertex shader (3.0 and later) can be called to initialize applicable input registers at a less frequent rate.

When an application calls the **IDirect3DDevice9::SetStreamSourceFreq** method to set the frequency for a given stream, the DirectX 9.0 runtime in turn calls the driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function using the D3DDP2OP\_SETSTREAMSOURCEFREQ operation code.

After the stream's frequency divisor is set--for example, to 2, then the driver must fetch data from the stream and pass this data into applicable input vertex registers every 2 vertices. This divisor affects each element in the stream.

The driver uses this divisor to compute the vertex offset into the vertex buffer according to the following formula:

```
VertexOffset = VertexIndex / Divider * StreamStride + StreamOffset 
```

For each vertex stream used, if the driver receives a start-vertex value during a call to the driver's *D3dDrawPrimitives2* function using the D3DDP2OP\_DRAWPRIMITIVE operation code, the driver also divides this start-vertex value by the frequency divisor and factors the result in the formula. This start-vertex value is provided in the **VStart** member of the [**D3DHAL\_DP2DRAWPRIMITIVE**](https://msdn.microsoft.com/library/windows/hardware/ff545526) structure. The following formula factors in the start-vertex value:

```
VertexOffset = StartVertex / Divider + 
               VertexIndex / Divider * StreamStride + StreamOffset 
```

Note that the preceding formulas use integer division.

The application passes the D3DSBT\_VERTEXSTATE state type in a call to the **IDirect3DDevice9::CreateStateBlock** method to capture the current vertex state.

The driver ignores the setting of a stream's frequency divisor either for indexed primitives or if the driver only supports a vertex shader model that is earlier than version 3.0 (including fixed function).

For more information about **IDirect3DDevice*Xxx*::SetStreamSourceFreq** and **IDirect3DDevice*Xxx*::CreateStateBlock**, see the latest DirectX SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Modifying%20Vertex%20Stream%20Frequency%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




