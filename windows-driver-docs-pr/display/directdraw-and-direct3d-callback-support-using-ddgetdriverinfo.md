---
title: DirectDraw and D3D Callback Support Using DdGetDriverInfo
description: The display driver can implement the DdGetDriverInfo function to indicate various DirectDraw and Direct3D callback support.
keywords:
- DirectDraw driver initialization WDK Windows 2000 display , Windows 2000
- callback functions WDK DirectDraw
- DdGetDriverInfo
- Direct3D WDK Windows 2000 display , callbacks
- callback functions WDK Direct3D
- DirectDraw driver initialization WDK Windows 2000 display , callback functions
ms.date: 12/06/2018
ms.custom: seodec18
---

# DirectDraw and Direct3D Callback Support Using DdGetDriverInfo

The display driver can implement the [**DdGetDriverInfo**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo) function to indicate various DirectDraw and Direct3D callback support. Callback support is contingent on the following GUIDs that the driver receives in the **guidInfo** member of the [**DD\_GETDRIVERINFODATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_getdriverinfodata) structure, to which the *lpGetDriverInfo* parameter points. The driver returns a pointer to a structure in the **lpvData** member that specifies DirectDraw or Direct3D callback support.

- If the driver receives the GUID\_ColorControlCallbacks GUID, it returns a pointer to the [**DD\_COLORCONTROLCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_colorcontrolcallbacks) structure. If it supports [color control](color-control-initialization.md), the driver fills the **ColorControl** member of DD\_COLORCONTROLCALLBACKS to specify its [*DdControlColor*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_colorcb_colorcontrol) callback function.

- If the driver receives the GUID\_D3DCallbacks, GUID\_D3DCallbacks3, or GUID\_Miscellaneous2Callbacks GUID, it returns a pointer to the [**D3DHAL\_CALLBACKS**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_callbacks), [**D3DHAL\_CALLBACKS3**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_callbacks3), or [**DD\_MISCELLANEOUS2CALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_miscellaneous2callbacks) structure. The driver uses these structures to indicate its [Direct3D callback support](driver-functions-to-support-direct3d.md). For more information, see [Direct3D DDI](direct3d.md).

- If the driver receives the GUID\_KernelCallbacks GUID, it returns a pointer to the [**DD\_KERNELCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_kernelcallbacks) structure. The driver fills members of DD\_KERNELCALLBACKS to indicate that it supports the following callback functions.

  <table>
  <colgroup>
  <col width="50%" />
  <col width="50%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th align="left">Callback Function</th>
  <th align="left">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_kernelcb_syncsurface" data-raw-source="[&lt;em&gt;DdSyncSurfaceData&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_kernelcb_syncsurface)"><em>DdSyncSurfaceData</em></a></p></td>
  <td align="left"><p>Sets and modifies surface data.</p></td>
  </tr>
  <tr class="even">
  <td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_kernelcb_syncvideoport" data-raw-source="[&lt;em&gt;DdSyncVideoPortData&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_kernelcb_syncvideoport)"><em>DdSyncVideoPortData</em></a></p></td>
  <td align="left"><p>Sets and modifies video port extensions (VPE) object data.</p></td>
  </tr>
  </tbody>
  </table>

- If the driver receives the GUID\_MiscellaneousCallbacks GUID, it returns a pointer to the [**DD\_MISCELLANEOUSCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_miscellaneouscallbacks) structure. If it supports a [*DdGetAvailDriverMemory*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getavaildrivermemory) callback function, the driver fills the *DdGetAvailDriverMemory* member of DD\_MISCELLANEOUSCALLBACKS to specify *DdGetAvailDriverMemory*.

- If the driver receives the GUID\_MotionCompCallbacks GUID, it returns a pointer to the [**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure to indicate its support of [motion compensation callbacks](motion-compensation-callbacks.md). For more information, see [Compressed Video Decoding](compressed-video-decoding.md).

- If the driver receives the GUID\_NTCallbacks GUID, it returns a pointer to the [**DD\_NTCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_ntcallbacks) structure. The driver fills members of DD\_NTCALLBACKS to indicate that it supports the following callback functions.

  <table>
  <colgroup>
  <col width="50%" />
  <col width="50%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th align="left">Callback Function</th>
  <th align="left">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_fliptogdisurface" data-raw-source="[&lt;em&gt;DdFlipToGDISurface&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_fliptogdisurface)"><em>DdFlipToGDISurface</em></a></p></td>
  <td align="left"><p>Notifies the driver when DirectDraw is flipping to or from a GDI surface.</p></td>
  </tr>
  <tr class="even">
  <td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_freedrivermemory" data-raw-source="[&lt;em&gt;DdFreeDriverMemory&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_freedrivermemory)"><em>DdFreeDriverMemory</em></a></p></td>
  <td align="left"><p>Frees offscreen or nonlocal display memory to satisfy a new allocation request.</p></td>
  </tr>
  <tr class="odd">
  <td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_setexclusivemode" data-raw-source="[&lt;em&gt;DdSetExclusiveMode&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_setexclusivemode)"><em>DdSetExclusiveMode</em></a></p></td>
  <td align="left"><p>Notifies the driver when a DirectDraw application is switching to or from exclusive mode.</p></td>
  </tr>
  </tbody>
  </table>

     

<!-- -->

-   If the driver receives the GUID\_VideoPortCallbacks GUID, it returns a pointer to the [**DD\_VIDEOPORTCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_videoportcallbacks) structure to indicate its support of [VPE Callback Functions](vpe-callback-functions.md). For more information, see [Video Port Extensions to DirectX](video-port-extensions-to-directx.md).

