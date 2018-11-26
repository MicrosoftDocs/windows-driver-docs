---
title: Capturing Still Frames from a USB Camera
description: Capturing Still Frames from a USB Camera
ms.assetid: 762021ea-753c-4cd2-9eec-1403ee918d4e
keywords:
- Windows 2000 Kernel Streaming Model WDK , USBCAMD2 minidriver library
- Streaming Model WDK Windows 2000 Kernel , USBCAMD2 minidriver library
- Kernel Streaming Model WDK , USBCAMD2 minidriver library
- USBCAMD2 minidriver library WDK Windows 2000 Kernel Streaming
- USB-based streaming cameras WDK USBCAMD2
- cameras WDK USBCAMD2
- capturing still frames WDK USBCAMD2
- still frame captures WDK USBCAMD2
- bulk pipe WDK USBCAMD2
- push model WDK USBCAMD2
- pull model WDK USBCAMD2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Capturing Still Frames from a USB Camera





USBCAMD2 provides the capability for a separate [Still Image driver](https://msdn.microsoft.com/library/windows/hardware/ff548278) to retrieve still frames from the camera through the camera's bulk pipe.

***<em>To support still frame capture a USBCAMD2 minidriver must perform the following</em>***

-   Call [*USBCAMD\_BulkReadWrite*](https://msdn.microsoft.com/library/windows/hardware/ff568577) from the PROPSETID\_VIDCAP\_VIDEOCONTROL property handler and pass a pointer to a minidriver-allocated buffer into which the still image can be captured. The pointer must not be **NULL**.

-   USBCAMD2 then calls the minidriver's [*CamNewVideoFrameEx*](https://msdn.microsoft.com/library/windows/hardware/ff557620) callback function before starting the bulk transfer. The camera minidriver can reduce the requested size of the bulk transfer if it determines that the actual still frame is smaller than the maximum size allocated by DirectShow.

-   After the bulk transfer completes, USBCAMD2 calls the minidriver's [*CamProcessRawVideoFrameEx*](https://msdn.microsoft.com/library/windows/hardware/ff557625) callback function to allow the minidriver to perform additional processing.

Still frame data flow is intended for use with a *pull* model. A pull occurs when an application requests a still frame. Alternately, still frame data flow also works in a *push* model. A push occurs when the user pushes the button on the camera, triggering the device event.

*<strong>*To use the** *</strong>pull*** **model to retrieve still frames from an STI minidriver****

-   Open the WDM video capture source filter associated with the camera.

-   Open the still pin on the filter handle obtained in the previous step.

-   Call **ReadFile** on that pin with the maximum-sized buffer.

-   Set the stream state from Pause to Run.

-   Get an interface pointer to the USBCAMD2 camera minidriver's [PROPSETID\_VIDCAP\_VIDEOCONTROL](https://msdn.microsoft.com/library/windows/hardware/ff568120) property set.

-   Set the *KS\_VideoControlFlag\_Trigger* flag associated with [**KSPROPERTY\_VIDEOCONTROL\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff566042).

*<strong>*To support the** *</strong>push*** **model to retrieve still frames from a camera****

-   Pass the *USBCAMD\_CamControlFlag\_EnableDeviceEvents* flag when you call [**USBCAMD\_InitializeNewInterface**](https://msdn.microsoft.com/library/windows/hardware/ff568599) from within the minidriver's SRB\_INITIALIZE\_DEVICE handler. The minidriver handles SRB\_INITIALIZE\_DEVICE from within its [*AdapterReceivePacket*](https://msdn.microsoft.com/library/windows/hardware/ff554080) callback function.

-   USBCAMD2 sends a [**KSEVENT\_VIDCAPTOSTI\_EXT\_TRIGGER**](https://msdn.microsoft.com/library/windows/hardware/ff561912) event to the registered imaging application when the user pushes the trigger button on the camera.

To cancel a requested bulk read or write, an application should call **CancelIO** with a handle to the still pin. If tables need to be transferred to the camera (through a USB bulk-out pipe), an application should call **WriteFile** with a handle to the still pin.

 

 




