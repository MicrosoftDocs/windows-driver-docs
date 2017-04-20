---
title: Basic Functions of a WDM Audio Driver
description: Basic Functions of a WDM Audio Driver
ms.assetid: 88013d17-c28c-4c99-9c43-17532f03bfdd
keywords:
- WDM audio drivers WDK , about WDM audio drivers
- audio drivers WDK , about audio drivers
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Basic Functions of a WDM Audio Driver


## <span id="basic_functions_of_a_wdm_audio_driver"></span><span id="BASIC_FUNCTIONS_OF_A_WDM_AUDIO_DRIVER"></span>


A Microsoft Windows Driver Model (WDM) audio driver provides the following functionality:

-   The driver exposes all the types of input and output streams, and the number of instances of each stream type that it can support. The driver provides this information in the form of a set of pin factories and the number of pins that each factory can instantiate. For example, a simple audio device might input a single PCM audio stream and output a single PCM audio stream. The filter for this device contains two pin factories--one for the input stream an one for the output stream--and each pin factory supports only a single pin instance. If the adapter card contains only one of these devices, the adapter driver provides a filter factory containing only a single instance of a filter with these capabilities.

-   The driver supports one or more property sets. For example, all audio drivers should support [KSPROPSETID\_Audio](https://msdn.microsoft.com/library/windows/hardware/ff537440), but some audio drivers might support additional property sets as well. Clients of the driver use property requests both to discover a filter's capabilities and to change the filter's configurable settings.

-   The driver optionally supports a hardware clock. This clock should be readable and writable so that streams can synchronize with other streams on the same or different hardware. For additional information, see [KSPROPSETID\_Clock](https://msdn.microsoft.com/library/windows/hardware/ff566564).

-   The driver optionally supports other media interfaces, such as [**KSINTERFACE\_STANDARD\_STREAMING**](https://msdn.microsoft.com/library/windows/hardware/ff563384), [**KSINTERFACE\_MEDIA\_WAVE\_QUEUED**](https://msdn.microsoft.com/library/windows/hardware/ff563377), or [**KSINTERFACE\_STANDARD\_LOOPED\_STREAMING**](https://msdn.microsoft.com/library/windows/hardware/ff563381).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Basic%20Functions%20of%20a%20WDM%20Audio%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


