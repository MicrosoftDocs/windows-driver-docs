---
title: Intel's HD Audio Architecture
description: Intel's HD Audio Architecture
ms.assetid: 86cba795-847c-4f54-93f8-e34ae73dc708
keywords: ["HD Audio, architecture", "High Definition Audio (HD Audio), architecture", "architecture WDK audio", "Intel High Definition Audio Specification", "UAA WDK", "Universal Audio Architecture WDK"]
---

# Intel's HD Audio Architecture


The Intel High Definition Audio Specification (see the [Intel HD Audio](http://go.microsoft.com/fwlink/p/?linkid=42508) website) describes an audio hardware architecture that is being developed as the successor to the Intel AC'97 codec and controller specification. The operating system's UAA driver components can service an audio solution that exposes the HD Audio register set and connects to the system's internal bus without requiring a solution-specific driver from the hardware vendor.

The HD Audio architecture provides a uniform programming interface for digital audio controllers. Typically, today's audio codecs conform to the AC'97 industry standard, and digital controllers connect to one or more AC'97 codecs through another industry standard, AC-Link. Although these standards help to ensure that codecs and links are implemented consistently, no standard currently exists that defines the interface to the digital audio controller. Vendors tend to have very similar solutions for their system-integrated AC'97 digital audio controllers, but each AC'97 solution is likely to be different enough to require a separate driver. The HD Audio architecture is intended to eliminate the requirement for solution-specific drivers by specifying a base register set that is uniform across all implementations.

A bus controller that conforms to the HD Audio architecture:

-   Provides controller hardware version information.

-   Provides hardware configuration information, including the number of serial data-out (SDO) lines and DMA engines.

-   Manages the amount of bus bandwidth available on the HD Audio Link.

-   Accepts unsolicited responses and wake-up events from codecs.

-   Queues codec commands and codec responses in separate ring buffers.

-   Provides a collection of input, output, and bidirectional DMA engines that perform scatter/gather transfers and can stream data between codecs and cyclic buffers in memory without intervention by the host processor.

The following figure shows a diagram of the UAA driver architecture for HD Audio devices in Windows Vista. In the figure, the software components that are labeled UAA HD Audio Class Driver and HD Audio Bus Driver are provided by Microsoft. The component labeled Modem Driver is provided by an independent hardware vendor.

![diagram illustrating the uaa driver architecture for intel hd audio devices](images/hdaudio.png)

The UAA HD Audio class driver provides the streaming interface to the operating system audio stack above the driver (not shown in the preceding figure).

The HD Audio bus driver directly accesses the hardware registers in the HD Audio controller and provides the DDI that the UAA HD Audio class driver or modem driver uses to manage the DMA engines and to send commands to the codecs. The HD Audio bus driver handles all interrupts, Plug and Play notifications, and power management events on behalf of audio devices on the HD Audio Link.

The HD Audio controller provides the DMA engines and command buffers that are used to transfer commands and data to codecs on the HD Audio Link. The boxes labeled Codec in the preceding figure can be either audio or modem codecs, and they can be connected either to removable peripherals through external jacks or to fixed internal peripherals, such as mobile PC speakers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Intel's%20HD%20Audio%20Architecture%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


