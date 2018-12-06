---
title: Audio Drivers Enumerations
description: This section describes the enumerations that are used by various audio properties and structures.
ms.assetid: 9C7530BE-C63F-438C-A853-9A7E47C240E9
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Audio Drivers Enumerations


This section describes the enumerations that are used by various audio properties and structures.

## <span id="Windows_10_and_later_operating_systems"></span><span id="windows_10_and_later_operating_systems"></span><span id="WINDOWS_10_AND_LATER_OPERATING_SYSTEMS"></span>Windows 10 and later operating systems


The following enumerations are used in Windows 10 and later operating systems:

[**TELEPHONY\_CALLCONTROLOP**](https://msdn.microsoft.com/library/windows/hardware/mt169895). Used by audio driver structures to specify an operation to perform on a phone call.

[**TELEPHONY\_CALLSTATE**](https://msdn.microsoft.com/library/windows/hardware/mt169896). Used by audio driver structures to specify the state of a phone call.

[**TELEPHONY\_CALLTYPE**](https://msdn.microsoft.com/library/windows/hardware/mt169897). Used by audio driver structures to specify the type a phone call.

[**TELEPHONY\_PROVIDERCHANGEOP**](https://msdn.microsoft.com/library/windows/hardware/mt169898). Used by audio driver structures to specify the type of change operation requested by the provider.

## <span id="Windows_8_and_later_operating_systems"></span><span id="windows_8_and_later_operating_systems"></span><span id="WINDOWS_8_AND_LATER_OPERATING_SYSTEMS"></span>Windows 8 and later operating systems


The following enumerations are used in Windows 8 and later operating systems:

[**AUDIO\_CURVE\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh831852). Used by audio driver structures to indicate the type of curve algorithm that should be applied to an audio data stream for volume level control.

[**EPcMiniportEngineEvent**](https://msdn.microsoft.com/library/windows/hardware/dn302036). Used by the audio engine to provide information related to a glitching error.

[**PC\_EXIT\_LATENCY**](https://msdn.microsoft.com/library/windows/hardware/dn265130). Used by the audio port class driver (PortCls) to indicate the maximum delay times for exiting sleep state and entering the fully functional state.

[**eEngineFormatType**](https://msdn.microsoft.com/library/windows/hardware/dn302035). Used by miniport drivers to indicate the data format type supported by the audio engine.

[**eChannelTargetType**](https://msdn.microsoft.com/library/windows/hardware/dn302034). Used by miniport drivers to indicate the type of node (target) that is in the path of the audio data stream.

## <span id="Windows_7_and_earlier_operating_systems"></span><span id="windows_7_and_earlier_operating_systems"></span><span id="WINDOWS_7_AND_EARLIER_OPERATING_SYSTEMS"></span>Windows 7 and earlier operating systems


The following enumerations were introduced in Windows 7 and earlier operating systems:

[**KSPROPERTY\_AUDIOENGINE**](ksproperty-audioengine.md). Used by miniport drivers to specify attributes and setup parameters for the audio engine.

[**KSPROPERTY\_JACK**](ksproperty-jack.md). Used by miniport drivers to specify the attributes of an audio endpoint jack.

 

 





