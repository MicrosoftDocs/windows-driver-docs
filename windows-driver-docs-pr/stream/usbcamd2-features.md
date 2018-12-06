---
title: USBCAMD2 Features
description: USBCAMD2 Features
ms.assetid: e800948a-6903-496e-9561-697ff5ccd1d7
keywords:
- Windows 2000 Kernel Streaming Model WDK , USBCAMD2 minidriver library
- Streaming Model WDK Windows 2000 Kernel , USBCAMD2 minidriver library
- Kernel Streaming Model WDK , USBCAMD2 minidriver library
- USBCAMD2 features WDK Windows 2000 Kernel Streaming
- USB-based streaming cameras WDK USBCAMD2
- cameras WDK USBCAMD2
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




