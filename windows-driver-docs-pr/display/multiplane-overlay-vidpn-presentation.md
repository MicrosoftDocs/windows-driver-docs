---
title: Multiplane overlay VidPN presentation
ms.assetid: BAD7FD48-905D-4547-8C69-133240B39FA3
description: Requirements that apply to functions used to present on multiple surfaces.
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Multiplane%20overlay%20VidPN%20presentation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




