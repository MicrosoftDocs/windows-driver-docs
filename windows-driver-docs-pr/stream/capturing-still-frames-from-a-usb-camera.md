---
title: Capturing Still Frames from a USB Camera
author: windows-driver-content
description: Capturing Still Frames from a USB Camera
MS-HAID:
- 'usbcmdds\_a176ff19-6bdd-4daf-840f-83d07d8ee6fd.xml'
- 'stream.capturing\_still\_frames\_from\_a\_usb\_camera'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 762021ea-753c-4cd2-9eec-1403ee918d4e
keywords: ["Windows 2000 Kernel Streaming Model WDK , USBCAMD2 minidriver library", "Streaming Model WDK Windows 2000 Kernel , USBCAMD2 minidriver library", "Kernel Streaming Model WDK , USBCAMD2 minidriver library", "USBCAMD2 minidriver library WDK Windows 2000 Kernel Streaming", "USB-based streaming cameras WDK USBCAMD2", "cameras WDK USBCAMD2", "capturing still frames WDK USBCAMD2", "still frame captures WDK USBCAMD2", "bulk pipe WDK USBCAMD2", "push model WDK USBCAMD2", "pull model WDK USBCAMD2"]
---

# Capturing Still Frames from a USB Camera


## <a href="" id="ddk-using-bulk-pipes-to-retrieve-still-frames-from-the-camera-ksg"></a>


USBCAMD2 provides the capability for a separate [Still Image driver](https://msdn.microsoft.com/library/windows/hardware/ff548278) to retrieve still frames from the camera through the camera's bulk pipe.

****To support still frame capture a USBCAMD2 minidriver must perform the following****

-   Call [*USBCAMD\_BulkReadWrite*](https://msdn.microsoft.com/library/windows/hardware/ff568577) from the PROPSETID\_VIDCAP\_VIDEOCONTROL property handler and pass a pointer to a minidriver-allocated buffer into which the still image can be captured. The pointer must not be **NULL**.

-   USBCAMD2 then calls the minidriver's [*CamNewVideoFrameEx*](https://msdn.microsoft.com/library/windows/hardware/ff557620) callback function before starting the bulk transfer. The camera minidriver can reduce the requested size of the bulk transfer if it determines that the actual still frame is smaller than the maximum size allocated by DirectShow.

-   After the bulk transfer completes, USBCAMD2 calls the minidriver's [*CamProcessRawVideoFrameEx*](https://msdn.microsoft.com/library/windows/hardware/ff557625) callback function to allow the minidriver to perform additional processing.

Still frame data flow is intended for use with a *pull* model. A pull occurs when an application requests a still frame. Alternately, still frame data flow also works in a *push* model. A push occurs when the user pushes the button on the camera, triggering the device event.

****To use the** ***pull*** **model to retrieve still frames from an STI minidriver****

-   Open the WDM video capture source filter associated with the camera.

-   Open the still pin on the filter handle obtained in the previous step.

-   Call **ReadFile** on that pin with the maximum-sized buffer.

-   Set the stream state from Pause to Run.

-   Get an interface pointer to the USBCAMD2 camera minidriver's [PROPSETID\_VIDCAP\_VIDEOCONTROL](https://msdn.microsoft.com/library/windows/hardware/ff568120) property set.

-   Set the *KS\_VideoControlFlag\_Trigger* flag associated with [**KSPROPERTY\_VIDEOCONTROL\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff566042).

****To support the** ***push*** **model to retrieve still frames from a camera****

-   Pass the *USBCAMD\_CamControlFlag\_EnableDeviceEvents* flag when you call [**USBCAMD\_InitializeNewInterface**](https://msdn.microsoft.com/library/windows/hardware/ff568599) from within the minidriver's SRB\_INITIALIZE\_DEVICE handler. The minidriver handles SRB\_INITIALIZE\_DEVICE from within its [*AdapterReceivePacket*](https://msdn.microsoft.com/library/windows/hardware/ff554080) callback function.

-   USBCAMD2 sends a [**KSEVENT\_VIDCAPTOSTI\_EXT\_TRIGGER**](https://msdn.microsoft.com/library/windows/hardware/ff561912) event to the registered imaging application when the user pushes the trigger button on the camera.

To cancel a requested bulk read or write, an application should call **CancelIO** with a handle to the still pin. If tables need to be transferred to the camera (through a USB bulk-out pipe), an application should call **WriteFile** with a handle to the still pin.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Capturing%20Still%20Frames%20from%20a%20USB%20Camera%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


