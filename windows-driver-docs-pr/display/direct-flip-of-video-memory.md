---
title: Direct flip of video memory
description: The direct flip feature allows for special optimizations to the composition model to reduce power consumption.
keywords:
- direct flip
- DirectFlip
ms.date: 04/20/2017
---

# Direct flip of video memory


The direct flip feature allows for special optimizations to the composition model to reduce power consumption. The optimizations benefit these scenarios:

-   To ensure optimal power consumption for video playback and other full screen scenarios, direct flip enables a minimum of memory bandwidth to display full-screen content and ensure smooth transitions between full-screen apps, other apps, and the desktop environment.
-   The user wants to view a video or run an app that covers the entire screen. When the user enters or exits the app, or notifications appear over the app, no mode change is required, and the experience is smooth. Furthermore, the user enjoys extended battery life on mobile devices because memory bandwidth requirements are reduced for full-screen apps such as video.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Minimum Windows Display Driver Model (WDDM) version</td>
<td align="left">1.2</td>
</tr>
<tr class="even">
<td align="left">Minimum Windows version</td>
<td align="left">8</td>
</tr>
<tr class="odd">
<td align="left">Driver implementation—Full graphics</td>
<td align="left">Mandatory</td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/test/hlk/windows-hardware-lab-kit" data-raw-source="[WHCK](/windows-hardware/test/hlk/windows-hardware-lab-kit)">WHCK</a> requirements and tests</td>
<td align="left"><p><strong>Device.Graphics ¦ DirectFlip</strong></p></td>
</tr>
</tbody>
</table>

 

## <span id="directflip"></span><span id="DIRECTFLIP"></span>


## <span id="DirectFlip_device_driver_interface__DDI_"></span><span id="directflip_device_driver_interface__ddi_"></span><span id="DIRECTFLIP_DEVICE_DRIVER_INTERFACE__DDI_"></span>DirectFlip device driver interface (DDI)


These functions and structures are new or updated for Windows 8:

-   [*CheckDirectFlipSupport*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_checkdirectflipsupport)
-   [*CheckDirectFlipSupport(D3D11\_1)*](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_checkdirectflipsupport)
-   [*DxgkDdiSetVidPnSourceAddress*](/previous-versions/windows/hardware/drivers/ff560767(v=vs.85))
-   [**D3D11\_1\_DDI\_CHECK\_DIRECT\_FLIP\_FLAGS**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3d11_1_ddi_check_direct_flip_flags)
-   [**D3DDDI\_CHECK\_DIRECT\_FLIP\_FLAGS**](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-d3dddi_check_direct_flip_flags)
-   [**D3DDDIARG\_CHECKDIRECTFLIPSUPPORT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_checkdirectflipsupport)
-   [**D3DKMT\_DIRECTFLIP\_SUPPORT**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_directflip_support)
-   [**D3DKMT\_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_queryadapterinfo)
-   [**D3DKMT\_WAITFORVERTICALBLANKEVENT2**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_waitforverticalblankevent2)
-   [**D3DKMTWaitForVerticalBlankEvent2**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtwaitforverticalblankevent2)
-   [**DXGK\_DRIVERCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps)
-   [**DXGK\_SEGMENTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentflags)
-   [**DXGK\_SETVIDPNSOURCEADDRESS\_FLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_setvidpnsourceaddress_flags)

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics ¦ DirectFlip**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

