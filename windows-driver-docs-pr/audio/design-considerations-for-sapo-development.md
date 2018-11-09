---
title: Design Considerations for sAPO Development
description: Design Considerations for sAPO Development
ms.assetid: ebcef929-af7b-4fce-a3a0-890c13bbd41f
ms.date: 04/20/2017
ms.localizationpriority: medium
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

-  An sAPO reports this latency through the [**IAudioProcessingObject::GetLatency**](https://msdn.microsoft.com/library/windows/hardware/ff536509) API.

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

 

 




