---
title: Reporting Support for Programmable Vertex Processing Hardware
description: Reporting Support for Programmable Vertex Processing Hardware
ms.assetid: c77dae52-ed7c-4385-b085-df3e16e53c5e
keywords:
- vertex shaders WDK DirectX 8.0 , programmable hardware
- programmable vertex processing hardware WDK DirectX 8.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Support for Programmable Vertex Processing Hardware


## <span id="ddk_reporting_support_for_programmable_vertex_processing_hardware_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_PROGRAMMABLE_VERTEX_PROCESSING_HARDWARE_GG"></span>


For a DirectX 8.0 level driver to report support for programmable vertex shader hardware it must set the **VertexShaderVersion** field of the D3DCAPS8 structure to a valid, nonzero vertex shader version number. The **VertexShaderVersion** is a DWORD where the most significant word must have the value 0xFFFE and the least significant word holds the actual version number. The least significant byte of this word holds the minor version number and the most significant byte holds the major version number. Because the format of this DWORD is complex, the driver must set the value of **VertexShaderVersion** using the macro D3DVS\_VERSION defined in *d3d8types.h*. For example, the following code fragment sets the **VertexShaderVersion** to indicate support for 1.0 level functionality.

```
myD3DCaps8.VertexShaderVersion = D3DVS_VERSION(1, 0);
```

To report no support for programmable vertex shaders, the following code fragment would be used:

```
myD3DCaps8.VertexShaderVersion = D3DVS_VERSION(0, 0);
```

Drivers that do not support programmable vertex processing should set **VertexShaderVersion** to zero.

In addition to setting the vertex shader version, the driver should report the number of constant registers it has for vertex shading. In order to support the 1.0 vertex shading specification, the device must have at least 96 constant registers. The driver reports the number of constant registers in the **MaxVertexShaderConst** field of the D3DCAPS8 structure. For example, the following code fragment reports the minimum number of constant registers required for version 1.0 vertex shaders.

```
myD3DCaps8.MaxVertexShaderConst = 96;
```

*d3d8types.h* defines a symbol for the minimum number of constant registers required by version 1.0 of the vertex shader specification. This symbol is D3DVS\_CONSTREG\_MAX\_V1\_0 and it is recommended that the driver use this symbol unless it supports more than 96 constant registers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Support%20for%20Programmable%20Vertex%20Processing%20Hardware%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




