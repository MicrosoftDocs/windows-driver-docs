---
title: USB Video Class Implementation
description: Provides implementation details for the Microsoft-provided USB Video Class (UVC) driver (usbvideo.sys).
keywords:
- USB Video Class drivers WDK AVStream , implementing
- Video Class drivers WDK USB , implementing
- UVC drivers WDK AVStream , implementing
ms.date: 05/16/2022
---

# USB Video Class implementation

The Microsoft-provided USB Video Class (UVC) driver (usbvideo.sys) is a pin-centric AVStream minidriver. It creates a filter factory for each USB Video Class?compliant device instance enumerated by the operating system. The driver also creates a pin factory for each input or output terminal on the device, with the **DataFlow** member of the [**KSPIN\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor) structure set to the relevant value.

The USB Video Class driver uses the internal device topology reported by the device descriptors to construct a kernel streaming (KS) topology graph comprised of filters, nodes, and connections.

Based on the number and types of controls supported by the device, USB Video Class dynamically reports filter, pin, and node property sets through the KS automation tables in the AVStream filter and pin descriptors.

Based on the data formats supported by each video or still image data endpoint on the device, USB Video Class reports the corresponding list of KS data ranges supported and a data intersection handler in the respective AVStream pin descriptor. The USB Video Class driver exports the information through the [Kernel Streaming Proxy](/windows-hardware/drivers/ddi/_stream/index) module.

The USB Video Class driver also supports audio/video stream synchronization; usbvideo.sys can serve as a KS master clock and add time stamps to video samples. The USB Video Class specification includes details about how the hardware should provide timing information to the class driver.

To communicate with USB Video Class, user-mode clients call DirectShow or Media Foundation interfaces. These interfaces are COM interface wrappers defined by the kernel streaming proxy as plug-ins. See the Microsoft Windows SDK documentation for more information about [Media Foundation](/windows/win32/medfound/microsoft-media-foundation-sdk).
