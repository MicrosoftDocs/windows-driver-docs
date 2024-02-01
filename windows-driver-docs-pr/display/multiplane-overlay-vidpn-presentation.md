---
title: Multiplane Overlay VidPN Presentation
description: Requirements that apply to functions used to present on multiple surfaces.
ms.date: 04/20/2017
---

# Multiplane overlay VidPN presentation


When multiplane overlays are used, these requirements apply to functions used to present on multiple surfaces in video present networks (VidPNs):

<span id="DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay"></span><span id="dxgkddisetvidpnsourceaddresswithmultiplaneoverlay"></span><span id="DXGKDDISETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY"></span>[*DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay)  
-   If [**DXGK\_MULTIPLANE\_OVERLAY\_PLANE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_plane).**Enabled** is false, the display miniport driver should disable the specified plane.
-   If a plane was enabled in a previous call to [*DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay) but is not present in the current call, the driver should continue to display the plane without flipping it.
-   It's possible that the driver will receive multiple calls to [*DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay) during the same VSync (one call to flip one plane, and another call to flip a different plane). In this case, the driver should process both calls.
-   The data passed should have been validated in user mode by a trusted source. However, the display miniport driver should still check the data to ensure that it doesn't cause problems. If the data is incorrect, the driver can fail the call with a **STATUS\_INVALID\_PARAMETER** error code, but such failures might not be handled gracefully and imply either a bug in the operating system or in the user mode driver.

<span id="DxgkDdiSetVidPnSourceVisibility"></span><span id="dxgkddisetvidpnsourcevisibility"></span><span id="DXGKDDISETVIDPNSOURCEVISIBILITY"></span>[*DxgkDdiSetVidPnSourceVisibility*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourcevisibility)  
When [**DXGKARG\_SETVIDPNSOURCEVISIBILITY**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_setvidpnsourcevisibility).**Visible** is set to **FALSE** on a given source in a call to this function, all hardware planes must be disabled, including the layer used for the primary surface. When **Visible** is set to **TRUE**, only the plane used for the primary surface must be enabled, and all other planes must remain disabled.

<span id="DxgkDdiSetVidPnSourceAddress"></span><span id="dxgkddisetvidpnsourceaddress"></span><span id="DXGKDDISETVIDPNSOURCEADDRESS"></span>[*DxgkDdiSetVidPnSourceAddress*](/previous-versions/windows/hardware/drivers/ff560767(v=vs.85))  
When this function is called, the driver should disable all non-primary overlay planes. The primary surface is flipped using [*DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay) when in multiplane overlay mode.

 

