---
title: DirectDraw and Direct3D Callback Support Using DdGetDriverInfo
description: DirectDraw and Direct3D Callback Support Using DdGetDriverInfo
ms.assetid: 7054564e-4520-4900-946a-95c92908667c
keywords:
- DirectDraw driver initialization WDK Windows 2000 display , Windows 2000
- callback functions WDK DirectDraw
- DdGetDriverInfo
- Direct3D WDK Windows 2000 display , callbacks
- callback functions WDK Direct3D
- DirectDraw driver initialization WDK Windows 2000 display , callback functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectDraw and Direct3D Callback Support Using DdGetDriverInfo


## <span id="ddk_directdraw_and_direct3d_callback_support_using_ddgetdriverinfo_gg"></span><span id="DDK_DIRECTDRAW_AND_DIRECT3D_CALLBACK_SUPPORT_USING_DDGETDRIVERINFO_GG"></span>


The display driver can implement the [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) function to indicate various DirectDraw and Direct3D callback support. Callback support is contingent on the following GUIDs that the driver receives in the **guidInfo** member of the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) structure, to which the *lpGetDriverInfo* parameter points. The driver returns a pointer to a structure in the **lpvData** member that specifies DirectDraw or Direct3D callback support.

- If the driver receives the GUID\_ColorControlCallbacks GUID, it returns a pointer to the [**DD\_COLORCONTROLCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff550521) structure. If it supports [color control](color-control-initialization.md), the driver fills the **ColorControl** member of DD\_COLORCONTROLCALLBACKS to specify its [*DdControlColor*](https://msdn.microsoft.com/library/windows/hardware/ff549244) callback function.

- If the driver receives the GUID\_D3DCallbacks, GUID\_D3DCallbacks3, or GUID\_Miscellaneous2Callbacks GUID, it returns a pointer to the [**D3DHAL\_CALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff544716), [**D3DHAL\_CALLBACKS3**](https://msdn.microsoft.com/library/windows/hardware/ff544723), or [**DD\_MISCELLANEOUS2CALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551645) structure. The driver uses these structures to indicate its [Direct3D callback support](driver-functions-to-support-direct3d.md). For more information, see [Direct3D DDI](direct3d.md).

- If the driver receives the GUID\_KernelCallbacks GUID, it returns a pointer to the [**DD\_KERNELCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551633) structure. The driver fills members of DD\_KERNELCALLBACKS to indicate that it supports the following callback functions.

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
  <td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550345" data-raw-source="[&lt;em&gt;DdSyncSurfaceData&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550345)"><em>DdSyncSurfaceData</em></a></p></td>
  <td align="left"><p>Sets and modifies surface data.</p></td>
  </tr>
  <tr class="even">
  <td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550350" data-raw-source="[&lt;em&gt;DdSyncVideoPortData&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550350)"><em>DdSyncVideoPortData</em></a></p></td>
  <td align="left"><p>Sets and modifies video port extensions (VPE) object data.</p></td>
  </tr>
  </tbody>
  </table>

     

<!-- -->

- If the driver receives the GUID\_MiscellaneousCallbacks GUID, it returns a pointer to the [**DD\_MISCELLANEOUSCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551657) structure. If it supports a [*DdGetAvailDriverMemory*](https://msdn.microsoft.com/library/windows/hardware/ff549377) callback function, the driver fills the *DdGetAvailDriverMemory* member of DD\_MISCELLANEOUSCALLBACKS to specify *DdGetAvailDriverMemory*.

- If the driver receives the GUID\_MotionCompCallbacks GUID, it returns a pointer to the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure to indicate its support of [motion compensation callbacks](motion-compensation-callbacks.md). For more information, see [Compressed Video Decoding](compressed-video-decoding.md).

- If the driver receives the GUID\_NTCallbacks GUID, it returns a pointer to the [**DD\_NTCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551673) structure. The driver fills members of DD\_NTCALLBACKS to indicate that it supports the following callback functions.

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
  <td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549335" data-raw-source="[&lt;em&gt;DdFlipToGDISurface&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549335)"><em>DdFlipToGDISurface</em></a></p></td>
  <td align="left"><p>Notifies the driver when DirectDraw is flipping to or from a GDI surface.</p></td>
  </tr>
  <tr class="even">
  <td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549360" data-raw-source="[&lt;em&gt;DdFreeDriverMemory&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549360)"><em>DdFreeDriverMemory</em></a></p></td>
  <td align="left"><p>Frees offscreen or nonlocal display memory to satisfy a new allocation request.</p></td>
  </tr>
  <tr class="odd">
  <td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550305" data-raw-source="[&lt;em&gt;DdSetExclusiveMode&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550305)"><em>DdSetExclusiveMode</em></a></p></td>
  <td align="left"><p>Notifies the driver when a DirectDraw application is switching to or from exclusive mode.</p></td>
  </tr>
  </tbody>
  </table>

     

<!-- -->

-   If the driver receives the GUID\_VideoPortCallbacks GUID, it returns a pointer to the [**DD\_VIDEOPORTCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551758) structure to indicate its support of [VPE Callback Functions](vpe-callback-functions.md). For more information, see [Video Port Extensions to DirectX](video-port-extensions-to-directx.md).

 

 





