---
title: Hardware-Offloaded Audio Processing
description: Hardware-offloaded audio processing allows the main audio processing tasks to be performed outside the computer's main CPU.
ms.assetid: DB20A1D4-F253-4FC0-8445-A92DF5D14605
---

# <span id="audio.hardware-offloaded_audio_processing"></span>Hardware-Offloaded Audio Processing


Hardware-offloaded audio processing allows the main audio processing tasks to be performed outside the computer's main CPU.

Audio processing can be very computationally intensive. So in many scenarios, it may be beneficial to allow a dedicated processor to take care of processing tasks like, for example, mixing, and applying effects. But Windows 7 and earlier versions of Windows did not provide support for hardware-offloaded audio processing.

With Windows 8 and later operating systems, the audio driver model has been updated to provide support for hardware-offloaded audio processing, and the following sections provide information about how to develop an audio driver that can expose its ability to handle offloaded audio for processing.

[Architectural Overview](architectural-overview.md)

[Driver Implementation for Offloaded Audio](driver-implementation-for-offloaded-audio.md)

[PortCls Power Management Updates for SoC](portcls-power-management-updates-for-soc.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Hardware-Offloaded%20Audio%20Processing%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




