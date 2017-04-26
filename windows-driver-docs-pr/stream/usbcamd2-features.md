---
title: USBCAMD2 Features
author: windows-driver-content
description: USBCAMD2 Features
ms.assetid: e800948a-6903-496e-9561-697ff5ccd1d7
keywords:
- Windows 2000 Kernel Streaming Model WDK , USBCAMD2 minidriver library
- Streaming Model WDK Windows 2000 Kernel , USBCAMD2 minidriver library
- Kernel Streaming Model WDK , USBCAMD2 minidriver library
- USBCAMD2 features WDK Windows 2000 Kernel Streaming
- USB-based streaming cameras WDK USBCAMD2
- cameras WDK USBCAMD2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# USBCAMD2 Features


The following features are present in USBCAMD2 (the original USBCAMD minidriver library does not support these features):

-   **Automatic Completion of SRBs**

    USBCAMD2 can automatically complete SRBs. The original USBCAMD required camera minidrivers to complete SRBs. To specify that USBCAMD2 automatically complete SRBs, pass **TRUE** in the *NeedsCompletion* parameter when you call [**USBCAMD\_AdapterReceivePacket**](https://msdn.microsoft.com/library/windows/hardware/ff568574).

-   **Support for Hardware-Triggered Events Through an Interrupt Pipe**

    USBCAMD2 camera minidrivers can register an external trigger event that is signaled through an interrupt pipe. The interrupt can be handled by USBCAMD2. For example, the interrupt pipe can signal the camera minidriver when the snapshot button is pressed. The Still Image (STI) architecture event monitor can be notified of the device event. By pressing the snapshot button, the STI monitor would be notified and a previously registered STI application, associated with the still pin on the camera, can be launched using the STI push model. To configure USBCAMD2 to send the external trigger event, pass the *USBCAMD\_CamControlFlag\_EnableDeviceEvents* flag in the *CamControlFlag* parameter when you call [**USBCAMD\_InitializeNewInterface**](https://msdn.microsoft.com/library/windows/hardware/ff568599).

-   **Versatile USB Pipe-Configuration Support**

    USBCAMD2 supports cameras that use bulk or isochronous pipes to transfer video and still image data. USBCAMD2 queries the minidriver and dynamically builds pipe-configuration information during initialization. The original USBCAMD library assumed preset pipe-configuration information about the number or type of pipes used. You specify pipe-configuration in a [**USBCAMD\_Pipe\_Config\_Descriptor**](https://msdn.microsoft.com/library/windows/hardware/ff568623) array that you pass to [*CamConfigureEx*](https://msdn.microsoft.com/library/windows/hardware/ff557605).

-   **Still Pin and Capture Pin Support**

    USBCAMD2 can expose a still pin to the *stream.sys* class in addition to the capture pin that the original USBCAMD exposed. The still pin can be exposed for imaging devices that have either dedicated pipes for still pins or that use the same pipe to multiplex both still and video pins. To expose a still pin, you specify the pipe that contains the still image data in the USBCAMD\_Pipe\_Config\_Descriptor array before you pass the array to **CamConfigureEx**.

-   **Improved Support for Plug and Play and Power Management**

    USBCAMD2 provides support for Plug and Play in Windows 2000 and later versions, such as surprise device removal. USBCAMD2 also supports system hibernation in Windows XP and later (hibernation support is not present in Windows 98 with no service packs installed, Windows 98 SE, or Windows 2000) and Windows Millennium Edition and later.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20USBCAMD2%20Features%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


