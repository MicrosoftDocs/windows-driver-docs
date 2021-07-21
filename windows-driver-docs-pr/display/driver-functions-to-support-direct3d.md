---
title: Driver Functions to Support Direct3D
description: Driver Functions to Support Direct3D
keywords:
- Direct3D WDK Windows 2000 display , functions
- functions WDK Direct3D
- callback functions WDK Direct3D
- LPD3DHAL_MYFUNCTIONDATA
- D3DHAL_MYFUNCTIONDATA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Functions to Support Direct3D


## <span id="ddk_driver_functions_to_support_direct3d_gg"></span><span id="DDK_DRIVER_FUNCTIONS_TO_SUPPORT_DIRECT3D_GG"></span>


A driver that supports Direct3D provides both Direct3D callback functions and DirectDraw DDI functions. The Direct3D DDI callbacks are prototyped as follows:

```cpp
typedef DWORD (APIENTRY *LPD3DHAL_MYFUNCTIONCB) (LPD3DHAL_MYFUNCTIONDATA);
```

In the preceding syntax:

-   LPD3DHAL\_MYFUNCTIONCB points to a driver-implemented callback that can be called *MyFunction*. All callback names are pseudonames decided upon by the display driver writer.

-   LPD3DHAL\_MYFUNCTIONDATA is a pointer to a D3DHAL\_MYFUNCTIONDATA structure being passed to the callback. Callback parameter structures are characterized as follows:
    -   The first member of every structure, **dwhContext**, is the context handle that describes the 3D context in which the callback should operate. The only exception to this rule is the D3DHAL\_CONTEXTCREATEDATA structure.
    -   The last member of every structure is **ddrval**. This member is used to pass the callback's return value back to Direct3D so it can be returned to the calling application.

To determine how to initialize Direct3D callback functions, see [Direct3D Driver Initialization](direct3d-driver-initialization.md).

The following table lists the Direct3D callback functions that are implemented in a Direct3D driver. All callback functions are required except for [**D3dValidateTextureStageState**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_validatetexturestagestatecb), which is optional depending on the hardware capabilities.

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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_contextcreatecb" data-raw-source="[&lt;strong&gt;D3dContextCreate&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_contextcreatecb)"><strong>D3dContextCreate</strong></a></p></td>
<td align="left"><p>Creates a context.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_contextdestroycb" data-raw-source="[&lt;strong&gt;D3dContextDestroy&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_contextdestroycb)"><strong>D3dContextDestroy</strong></a></p></td>
<td align="left"><p>Destroys a context.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex" data-raw-source="[&lt;strong&gt;D3dCreateSurfaceEx&lt;/strong&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex)"><strong>D3dCreateSurfaceEx</strong></a></p></td>
<td align="left"><p>Creates an association between a texture handle and a surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_destroyddlocal" data-raw-source="[&lt;strong&gt;D3dDestroyDDLocal&lt;/strong&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_destroyddlocal)"><strong>D3dDestroyDDLocal</strong></a></p></td>
<td align="left"><p>Destroys all the Direct3D surfaces previously created by <a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex" data-raw-source="[&lt;strong&gt;D3dCreateSurfaceEx&lt;/strong&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex)"><strong>D3dCreateSurfaceEx</strong></a> that belong to the same given local DirectDraw object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb" data-raw-source="[&lt;strong&gt;D3dDrawPrimitives2&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb)"><strong>D3dDrawPrimitives2</strong></a></p></td>
<td align="left"><p>Renders primitives and returns updated state to Direct3D.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverstate" data-raw-source="[&lt;strong&gt;D3dGetDriverState&lt;/strong&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverstate)"><strong>D3dGetDriverState</strong></a></p></td>
<td align="left"><p>Returns state information about the driver to DirectDraw and Direct3D runtimes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_validatetexturestagestatecb" data-raw-source="[&lt;strong&gt;D3dValidateTextureStageState&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_validatetexturestagestatecb)"><strong>D3dValidateTextureStageState</strong></a></p></td>
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvgetdirectdrawinfo" data-raw-source="[&lt;strong&gt;DrvGetDirectDrawInfo&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvgetdirectdrawinfo)"><strong>DrvGetDirectDrawInfo</strong></a></p></td>
<td align="left"><p>This function retrieves the capabilities of the graphics hardware. In this initialization function the driver indicates that it supports Direct3D.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo" data-raw-source="[&lt;strong&gt;DdGetDriverInfo&lt;/strong&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo)"><strong>DdGetDriverInfo</strong></a></p></td>
<td align="left"><p>The runtime queries this callback function with GUIDs for additional information about the driver. Several GUIDs pertain specifically to the driver's Direct3D support.</p></td>
</tr>
</tbody>
</table>

 

DirectDraw function and callback implementation details are discussed in [DirectDraw](directdraw.md).

