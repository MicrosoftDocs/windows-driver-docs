---
title: Direct flip of video memory
description: The direct flip feature allows for special optimizations to the composition model to reduce power consumption.
ms.assetid: 00A8FCB1-966A-4176-9840-7EB5BA300C8B
keywords:
- direct flip
- DirectFlip
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><a href="https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit" data-raw-source="[WHCK](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit)">WHCK</a> requirements and tests</td>
<td align="left"><p><strong>Device.Graphics ¦ DirectFlip</strong></p></td>
</tr>
</tbody>
</table>

 

## <span id="directflip"></span><span id="DIRECTFLIP"></span>


## <span id="DirectFlip_device_driver_interface__DDI_"></span><span id="directflip_device_driver_interface__ddi_"></span><span id="DIRECTFLIP_DEVICE_DRIVER_INTERFACE__DDI_"></span>DirectFlip device driver interface (DDI)


These functions and structures are new or updated for Windows 8:

-   [*CheckDirectFlipSupport*](https://msdn.microsoft.com/library/windows/hardware/hh698234)
-   [*CheckDirectFlipSupport(D3D11\_1)*](https://msdn.microsoft.com/library/windows/hardware/hh406253)
-   [*DxgkDdiSetVidPnSourceAddress*](https://msdn.microsoft.com/library/windows/hardware/ff560767)
-   [**D3D11\_1\_DDI\_CHECK\_DIRECT\_FLIP\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/hh451044)
-   [**D3DDDI\_CHECK\_DIRECT\_FLIP\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/hh451172)
-   [**D3DDDIARG\_CHECKDIRECTFLIPSUPPORT**](https://msdn.microsoft.com/library/windows/hardware/hh451072)
-   [**D3DKMT\_DIRECTFLIP\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/hh406459)
-   [**D3DKMT\_QUERYADAPTERINFO**](https://msdn.microsoft.com/library/windows/hardware/ff548203)
-   [**D3DKMT\_WAITFORVERTICALBLANKEVENT2**](https://msdn.microsoft.com/library/windows/hardware/hh780272)
-   [**D3DKMTWaitForVerticalBlankEvent2**](https://msdn.microsoft.com/library/windows/hardware/hh780252)
-   [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062)
-   [**DXGK\_SEGMENTFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff562039)
-   [**DXGK\_SETVIDPNSOURCEADDRESS\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff562052)

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics ¦ DirectFlip**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 





