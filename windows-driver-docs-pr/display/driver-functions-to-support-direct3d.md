---
title: Driver Functions to Support Direct3D
description: Driver Functions to Support Direct3D
ms.assetid: 949551c3-2172-454c-b398-eba468b90705
keywords: ["Direct3D WDK Windows 2000 display , functions", "functions WDK Direct3D", "callback functions WDK Direct3D", "LPD3DHAL_MYFUNCTIONDATA", "D3DHAL_MYFUNCTIONDATA"]
---

# Driver Functions to Support Direct3D


## <span id="ddk_driver_functions_to_support_direct3d_gg"></span><span id="DDK_DRIVER_FUNCTIONS_TO_SUPPORT_DIRECT3D_GG"></span>


A driver that supports Direct3D provides both Direct3D callback functions and DirectDraw DDI functions. The Direct3D DDI callbacks are prototyped as follows:

```
typedef DWORD (APIENTRY *LPD3DHAL_MYFUNCTIONCB) (LPD3DHAL_MYFUNCTIONDATA);
```

In the preceding syntax:

-   LPD3DHAL\_MYFUNCTIONCB points to a driver-implemented callback that can be called *MyFunction*. All callback names are pseudonames decided upon by the display driver writer.

-   LPD3DHAL\_MYFUNCTIONDATA is a pointer to a D3DHAL\_MYFUNCTIONDATA structure being passed to the callback. Callback parameter structures are characterized as follows:
    -   The first member of every structure, **dwhContext**, is the context handle that describes the 3D context in which the callback should operate. The only exception to this rule is the D3DHAL\_CONTEXTCREATEDATA structure.
    -   The last member of every structure is **ddrval**. This member is used to pass the callback's return value back to Direct3D so it can be returned to the calling application.

To determine how to initialize Direct3D callback functions, see [Direct3D Driver Initialization](direct3d-driver-initialization.md).

The following table lists the Direct3D callback functions that are implemented in a Direct3D driver. All callback functions are required except for [**D3dValidateTextureStageState**](https://msdn.microsoft.com/library/windows/hardware/ff549064), which is optional depending on the hardware capabilities.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>D3dContextCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542178)</p></td>
<td align="left"><p>Creates a context.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>D3dContextDestroy</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542180)</p></td>
<td align="left"><p>Destroys a context.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>D3dCreateSurfaceEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542840)</p></td>
<td align="left"><p>Creates an association between a texture handle and a surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>D3dDestroyDDLocal</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544685)</p></td>
<td align="left"><p>Destroys all the Direct3D surfaces previously created by [<strong>D3dCreateSurfaceEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542840) that belong to the same given local DirectDraw object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>D3dDrawPrimitives2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544704)</p></td>
<td align="left"><p>Renders primitives and returns updated state to Direct3D.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>D3dGetDriverState</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544708)</p></td>
<td align="left"><p>Returns state information about the driver to DirectDraw and Direct3D runtimes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>D3dValidateTextureStageState</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549064)</p></td>
<td align="left"><p>Performs texture stage state validation, which is required for all drivers that support texturing.</p></td>
</tr>
</tbody>
</table>

 

In order to support Direct3D, a driver must minimally support Microsoft DirectDraw and must also implement certain DirectDraw DDI functions. The functions pertinent to Direct3D support are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DrvGetDirectDrawInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556229)</p></td>
<td align="left"><p>This function retrieves the capabilities of the graphics hardware. In this initialization function the driver indicates that it supports Direct3D.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DdGetDriverInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549404)</p></td>
<td align="left"><p>The runtime queries this callback function with GUIDs for additional information about the driver. Several GUIDs pertain specifically to the driver's Direct3D support.</p></td>
</tr>
</tbody>
</table>

 

DirectDraw function and callback implementation details are discussed in [DirectDraw](directdraw.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Driver%20Functions%20to%20Support%20Direct3D%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




