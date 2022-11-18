---
title: Audio Processing Objects Utility Functions (Windows Drivers)
description: Learn more about the Audio Processing Objects Utility Functions.
ms.date: 10/27/2022
---

# Audio Processing Objects Utility Functions

Audio processing objects must have real-time compatibility. This means that all buffers set aside for use by the audio processing interfaces and methods must be nonpageable. The real-time compatibility requirement also means that all code and data in the process path must also be nonpageable.

The following utility functions allocate or release locked memory for use by the interfaces and methods that perform audio processing.

[**AERT\_Allocate**](/windows/win32/api/baseaudioprocessingobject/nf-baseaudioprocessingobject-aert_allocate)

[**AERT\_Free**](/windows/win32/api/baseaudioprocessingobject/nf-baseaudioprocessingobject-aert_free)

The following utility functions are used to create media types for audio data processing.

[**CreateAudioMediaType**](/windows/win32/api/audiomediatype/nf-audiomediatype-createaudiomediatype)

[**CreateAudioMediaTypeFromUncompressedAudioFormat**](/windows/win32/api/audiomediatype/nf-audiomediatype-createaudiomediatypefromuncompressedaudioformat)

For more information about the general requirements to help you develop audio processing objects, see [Design Considerations for sAPO Development](./exploring-the-windows-vista-audio-engine.md).