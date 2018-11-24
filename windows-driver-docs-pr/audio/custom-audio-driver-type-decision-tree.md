---
title: Custom Audio Driver Type Decision Tree
description: Custom Audio Driver Type Decision Tree
ms.assetid: 7b055baa-1843-4e31-a98e-48b05de94e70
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Custom Audio Driver Type Decision Tree


Use this decision tree with Step 3 of [Roadmap for Developing WDM Audio Drivers](roadmap-for-developing-wdm-audio-drivers.md). The tree helps you determine the type of audio driver to learn about. The system-supplied port class driver (PortCls) provides a set of port drivers that implement most of the basic functionality. These port drivers simplify the development process for the driver developer. High definition (HD) audio and AC97 drivers are typically based on the PortCls class driver, whereas USB and 1394 drivers are usually based on the AVStream class.

![diagram of decision tree for choosing an audio driver type](images/roadmap-uaacomp.png)

If your audio device is based on the universal audio architecture (UAA) standard, it is UAA-compatible. A UAA-compatible audio device can use the system-supplied UAA class drivers and does not need a custom driver, but you can provide your own [Windows Audio Processing Objects](windows-audio-processing-objects.md).

If your audio device is not UAA-compatible or it is UAA-compatible but you want to implement customized features, you must decide whether you want to develop a driver with Bus Master DMA support. If you want to provide Bus Master DMA support, for example, you must develop a PortCls-based audio driver.

For information about how to develop custom audio drivers and how to choose a port driver, see the following topics:

<span id="Custom_Audio_Drivers"></span><span id="custom_audio_drivers"></span><span id="CUSTOM_AUDIO_DRIVERS"></span>[Custom Audio Drivers](custom-audio-drivers.md)  
Provides an overview of PortCls and AVStream audio drivers and discusses the pros and cons of each type.

<span id="AVStream_Overview"></span><span id="avstream_overview"></span><span id="AVSTREAM_OVERVIEW"></span>[AVStream Overview](https://msdn.microsoft.com/library/windows/hardware/ff554240)  
Provides an architectural overview of AVStream-based drivers and highlights the cases where this type of driver is the best choice.

You must also decide about the data format that your audio driver will use and the range of formats it will support. For more information about data formats and ranges, see [Audio Data Formats and Data Ranges](audio-data-formats-and-data-ranges.md).

To complete steps for audio driver development, see [Roadmap for Developing WDM Audio Drivers](roadmap-for-developing-wdm-audio-drivers.md).

 

 




