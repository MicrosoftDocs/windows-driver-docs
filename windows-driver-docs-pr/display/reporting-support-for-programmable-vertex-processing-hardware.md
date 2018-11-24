---
title: Reporting Support for Programmable Vertex Processing Hardware
description: Reporting Support for Programmable Vertex Processing Hardware
ms.assetid: c77dae52-ed7c-4385-b085-df3e16e53c5e
keywords:
- vertex shaders WDK DirectX 8.0 , programmable hardware
- programmable vertex processing hardware WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Support for Programmable Vertex Processing Hardware


## <span id="ddk_reporting_support_for_programmable_vertex_processing_hardware_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_PROGRAMMABLE_VERTEX_PROCESSING_HARDWARE_GG"></span>


For a DirectX 8.0 level driver to report support for programmable vertex shader hardware it must set the **VertexShaderVersion** field of the D3DCAPS8 structure to a valid, nonzero vertex shader version number. The **VertexShaderVersion** is a DWORD where the most significant word must have the value 0xFFFE and the least significant word holds the actual version number. The least significant byte of this word holds the minor version number and the most significant byte holds the major version number. Because the format of this DWORD is complex, the driver must set the value of **VertexShaderVersion** using the macro D3DVS\_VERSION defined in *d3d8types.h*. For example, the following code fragment sets the **VertexShaderVersion** to indicate support for 1.0 level functionality.

```cpp
myD3DCaps8.VertexShaderVersion = D3DVS_VERSION(1, 0);
```

To report no support for programmable vertex shaders, the following code fragment would be used:

```cpp
myD3DCaps8.VertexShaderVersion = D3DVS_VERSION(0, 0);
```

Drivers that do not support programmable vertex processing should set **VertexShaderVersion** to zero.

In addition to setting the vertex shader version, the driver should report the number of constant registers it has for vertex shading. In order to support the 1.0 vertex shading specification, the device must have at least 96 constant registers. The driver reports the number of constant registers in the **MaxVertexShaderConst** field of the D3DCAPS8 structure. For example, the following code fragment reports the minimum number of constant registers required for version 1.0 vertex shaders.

```cpp
myD3DCaps8.MaxVertexShaderConst = 96;
```

*d3d8types.h* defines a symbol for the minimum number of constant registers required by version 1.0 of the vertex shader specification. This symbol is D3DVS\_CONSTREG\_MAX\_V1\_0 and it is recommended that the driver use this symbol unless it supports more than 96 constant registers.

 

 





