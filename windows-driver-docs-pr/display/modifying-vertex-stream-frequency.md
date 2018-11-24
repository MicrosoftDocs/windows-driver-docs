---
title: Modifying Vertex Stream Frequency
description: Modifying Vertex Stream Frequency
ms.assetid: 81bbced4-7331-4e54-9617-1ef29b02f162
keywords:
- vertex stream frequency division WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying Vertex Stream Frequency


## <span id="ddk_modifying_vertex_stream_frequency_gg"></span><span id="DDK_MODIFYING_VERTEX_STREAM_FREQUENCY_GG"></span>


A DirectX 9.0 version driver for a device that supports vertex shader version 3.0 and later must implement vertex stream frequency division. For version 2.0 and earlier models of vertex shader (including fixed function), the vertex shader is called once per vertex; for each call, the input vertex registers are initialized with unique vertex elements from the vertex streams. However, using vertex stream frequency division, the vertex shader (3.0 and later) can be called to initialize applicable input registers at a less frequent rate.

When an application calls the **IDirect3DDevice9::SetStreamSourceFreq** method to set the frequency for a given stream, the DirectX 9.0 runtime in turn calls the driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function using the D3DDP2OP\_SETSTREAMSOURCEFREQ operation code.

After the stream's frequency divisor is set--for example, to 2, then the driver must fetch data from the stream and pass this data into applicable input vertex registers every 2 vertices. This divisor affects each element in the stream.

The driver uses this divisor to compute the vertex offset into the vertex buffer according to the following formula:

```cpp
VertexOffset = VertexIndex / Divider * StreamStride + StreamOffset 
```

For each vertex stream used, if the driver receives a start-vertex value during a call to the driver's *D3dDrawPrimitives2* function using the D3DDP2OP\_DRAWPRIMITIVE operation code, the driver also divides this start-vertex value by the frequency divisor and factors the result in the formula. This start-vertex value is provided in the **VStart** member of the [**D3DHAL\_DP2DRAWPRIMITIVE**](https://msdn.microsoft.com/library/windows/hardware/ff545526) structure. The following formula factors in the start-vertex value:

```cpp
VertexOffset = StartVertex / Divider + 
               VertexIndex / Divider * StreamStride + StreamOffset 
```

Note that the preceding formulas use integer division.

The application passes the D3DSBT\_VERTEXSTATE state type in a call to the **IDirect3DDevice9::CreateStateBlock** method to capture the current vertex state.

The driver ignores the setting of a stream's frequency divisor either for indexed primitives or if the driver only supports a vertex shader model that is earlier than version 3.0 (including fixed function).

For more information about **IDirect3DDevice*Xxx*::SetStreamSourceFreq** and **IDirect3DDevice*Xxx*::CreateStateBlock**, see the latest DirectX SDK documentation.

 

 





