---
title: Direct flip of video memory
description: The direct flip feature allows for special optimizations to the composition model to reduce power consumption.
ms.assetid: 00A8FCB1-966A-4176-9840-7EB5BA300C8B
keywords:
- direct flip
- DirectFlip
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left">[WHCK]( http://go.microsoft.com/fwlink/p/?linkid=258342) requirements and tests</td>
<td align="left"><p><strong>Device.Graphicsâ€¦DirectFlip</strong></p></td>
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


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation]( http://go.microsoft.com/fwlink/p/?linkid=258342) on **Device.Graphicsâ€¦DirectFlip**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Direct%20flip%20of%20video%20memory%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




