---
title: Hardware-Offloaded Audio Processing
description: Hardware-offloaded audio processing allows the main audio processing tasks to be performed outside the computer's main CPU.
ms.assetid: DB20A1D4-F253-4FC0-8445-A92DF5D14605
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="audio.hardware-offloaded_audio_processing"></span>Hardware-Offloaded Audio Processing


Hardware-offloaded audio processing allows the main audio processing tasks to be performed outside the computer's main CPU.

Audio processing can be very computationally intensive. So in many scenarios, it may be beneficial to allow a dedicated processor to take care of processing tasks like, for example, mixing, and applying effects. But Windows 7 and earlier versions of Windows did not provide support for hardware-offloaded audio processing.

With Windows 8 and later operating systems, the audio driver model has been updated to provide support for hardware-offloaded audio processing, and the following sections provide information about how to develop an audio driver that can expose its ability to handle offloaded audio for processing.

[Architectural Overview](architectural-overview.md)

[Driver Implementation for Offloaded Audio](driver-implementation-for-offloaded-audio.md)

[PortCls Power Management Updates for SoC](portcls-power-management-updates-for-soc.md)

 

 




