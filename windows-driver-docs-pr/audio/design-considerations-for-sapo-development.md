---
title: Design Considerations for sAPO Development
description: Design Considerations for sAPO Development
ms.assetid: ebcef929-af7b-4fce-a3a0-890c13bbd41f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Design Considerations for sAPO Development


If you want to develop your own sAPOs, be aware that all sAPOs must have similar characteristics to work with Windows Vista.

### <span id="general_characteristics_and_requirements"></span><span id="GENERAL_CHARACTERISTICS_AND_REQUIREMENTS"></span> General Characteristics and Requirements

All system-supplied and custom sAPOs must have the following general characteristics:

-   An sAPO must have one input and one output connection. These connections are audio buffers and can have multiple channels.

-   An sAPO must have real-time compatibility. This means the following:

    All buffers that are processed by the sAPO must be nonpageable.

    All code and data in the process path must be nonpageable.

    All methods that are members of real-time interfaces must be implemented as nonblocking members. They must not block, use paged memory, or call any blocking system routines.

    **Note**  Real-time interfaces are identified by an "RT" at the end of their name, such as [IAudioProcessingObjectRT](https://msdn.microsoft.com/library/windows/hardware/ff536505).

     

    Real-time compatible sAPOs can be used in contexts that do not require real-time processing.

-   An sAPO can modify only the audio data that is passed to it through its [**IAudioProcessingObjectRT::APOProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536506) routine. The sAPO cannot change the settings of the underlying logical device, including its KS topology.

-   GFX sAPOs must process data by using a format with a fixed frame size. The frame size is specified by the audio engine. The format is static for both input and output.

-   GFX sAPOs should not introduce more than 10 ms of latency into the audio processing chain. An sAPO reports this latency through the [**IAudioProcessingObject::GetLatency**](https://msdn.microsoft.com/library/windows/hardware/ff536509) API.

In addition to **IUnknown**, sAPOs must expose the following interfaces:

-   [IAudioProcessingObject.](https://msdn.microsoft.com/library/windows/hardware/ff536501) An interface that handles setup tasks such as initialization and format negotiation.

-   [IAudioProcessingObjectConfiguration](https://msdn.microsoft.com/library/windows/hardware/ff536502). The configuration interface.

-   **IAudioProcessingObjectRT**. A real-time interface that handles audio processing. It can be called from a real-time processing thread.

-   [IAudioSystemEffects](https://msdn.microsoft.com/library/windows/hardware/ff536514). The interface that makes the audio engine recognize a DLL as an sAPO.

**Important**   Custom sAPOs must not expose the **IAudioProcessingObjectVBR** interface.

 

For detailed information about the required interfaces, see the Audioenginebaseapo.h and Audioenginebaseapo.idl files in the WinDDK\\&lt;build number&gt;\\inc\\API folder.

### <span id="design_tasks_and_development_options"></span><span id="DESIGN_TASKS_AND_DEVELOPMENT_OPTIONS"></span> Design Tasks and Development Options

The following topics provide details about the two main tasks required for wrapping one or more system-supplied sAPOs and replacing the rest with custom sAPOs.

[Wrapping system-supplied sAPOs](wrapping-system-supplied-sapos.md)

[Replacing System-supplied sAPOs](replacing-system-supplied-sapos.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Design%20Considerations%20for%20sAPO%20Development%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


