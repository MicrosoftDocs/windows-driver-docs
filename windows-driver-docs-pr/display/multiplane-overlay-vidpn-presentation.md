---
title: Multiplane overlay VidPN presentation
ms.assetid: BAD7FD48-905D-4547-8C69-133240B39FA3
description: Requirements that apply to functions used to present on multiple surfaces.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multiplane overlay VidPN presentation


When multiplane overlays are used, these requirements apply to functions used to present on multiple surfaces in video present networks (VidPNs):

<span id="DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay"></span><span id="dxgkddisetvidpnsourceaddresswithmultiplaneoverlay"></span><span id="DXGKDDISETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY"></span>[*DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay*](https://msdn.microsoft.com/library/windows/hardware/hh780298)  
-   If [**DXGK\_MULTIPLANE\_OVERLAY\_PLANE**](https://msdn.microsoft.com/library/windows/hardware/hh780305).**Enabled** is false, the display miniport driver should disable the specified plane.
-   If a plane was enabled in a previous call to [*DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay*](https://msdn.microsoft.com/library/windows/hardware/hh780298) but is not present in the current call, the driver should continue to display the plane without flipping it.
-   It's possible that the driver will receive multiple calls to [*DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay*](https://msdn.microsoft.com/library/windows/hardware/hh780298) during the same VSync (one call to flip one plane, and another call to flip a different plane). In this case, the driver should process both calls.
-   The data passed should have been validated in user mode by a trusted source. However, the display miniport driver should still check the data to ensure that it doesn't cause problems. If the data is incorrect, the driver can fail the call with a **STATUS\_INVALID\_PARAMETER** error code, but such failures might not be handled gracefully and imply either a bug in the operating system or in the user mode driver.

<span id="DxgkDdiSetVidPnSourceVisibility"></span><span id="dxgkddisetvidpnsourcevisibility"></span><span id="DXGKDDISETVIDPNSOURCEVISIBILITY"></span>[*DxgkDdiSetVidPnSourceVisibility*](https://msdn.microsoft.com/library/windows/hardware/ff560771)  
When [**DXGKARG\_SETVIDPNSOURCEVISIBILITY**](https://msdn.microsoft.com/library/windows/hardware/ff559486).**Visible** is set to **FALSE** on a given source in a call to this function, all hardware planes must be disabled, including the layer used for the primary surface. When **Visible** is set to **TRUE**, only the plane used for the primary surface must be enabled, and all other planes must remain disabled.

<span id="DxgkDdiSetVidPnSourceAddress"></span><span id="dxgkddisetvidpnsourceaddress"></span><span id="DXGKDDISETVIDPNSOURCEADDRESS"></span>[*DxgkDdiSetVidPnSourceAddress*](https://msdn.microsoft.com/library/windows/hardware/ff560767)  
When this function is called, the driver should disable all non-primary overlay planes. The primary surface is flipped using [*DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay*](https://msdn.microsoft.com/library/windows/hardware/hh780298) when in multiplane overlay mode.

 

 





