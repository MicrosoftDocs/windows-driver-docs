---
title: Audio Drivers Enumerations
description: This section describes the enumerations that are used by various audio properties and structures.
ms.date: 03/06/2023
ms.topic: reference
---


# Audio Drivers Enumerations


This section describes the enumerations that are used by various audio properties and structures.

## <span id="Windows_10_and_later_operating_systems"></span><span id="windows_10_and_later_operating_systems"></span><span id="WINDOWS_10_AND_LATER_OPERATING_SYSTEMS"></span>Windows 10 and later operating systems


The following enumerations are used in Windows 10 and later operating systems:

[**TELEPHONY\_CALLCONTROLOP**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-telephony_callcontrolop). Used by audio driver structures to specify an operation to perform on a phone call.

[**TELEPHONY\_CALLSTATE**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-telephony_callstate). Used by audio driver structures to specify the state of a phone call.

[**TELEPHONY\_CALLTYPE**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-telephony_calltype). Used by audio driver structures to specify the type a phone call.

[**TELEPHONY\_PROVIDERCHANGEOP**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-telephony_providerchangeop). Used by audio driver structures to specify the type of change operation requested by the provider.

## <span id="Windows_8_and_later_operating_systems"></span><span id="windows_8_and_later_operating_systems"></span><span id="WINDOWS_8_AND_LATER_OPERATING_SYSTEMS"></span>Windows 8 and later operating systems


The following enumerations are used in Windows 8 and later operating systems:

[**AUDIO\_CURVE\_TYPE**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-audio_curve_type). Used by audio driver structures to indicate the type of curve algorithm that should be applied to an audio data stream for volume level control.

[**EPcMiniportEngineEvent**](/windows-hardware/drivers/ddi/portcls/ne-portcls-epcminiportengineevent). Used by the audio engine to provide information related to a glitching error.

[**PC\_EXIT\_LATENCY**](/windows-hardware/drivers/ddi/portcls/ne-portcls-_pc_exit_latency). Used by the audio port class driver (PortCls) to indicate the maximum delay times for exiting sleep state and entering the fully functional state.

[**eEngineFormatType**](/windows-hardware/drivers/ddi/portcls/ne-portcls-eengineformattype). Used by miniport drivers to indicate the data format type supported by the audio engine.

[**eChannelTargetType**](/windows-hardware/drivers/ddi/portcls/ne-portcls-echanneltargettype). Used by miniport drivers to indicate the type of node (target) that is in the path of the audio data stream.

## <span id="Windows_7_and_earlier_operating_systems"></span><span id="windows_7_and_earlier_operating_systems"></span><span id="WINDOWS_7_AND_EARLIER_OPERATING_SYSTEMS"></span>Windows 7 and earlier operating systems


The following enumerations were introduced in Windows 7 and earlier operating systems:

[**KSPROPERTY\_AUDIOENGINE**](ksproperty-audioengine.md). Used by miniport drivers to specify attributes and setup parameters for the audio engine.

[**KSPROPERTY\_JACK**](ksproperty-jack.md). Used by miniport drivers to specify the attributes of an audio endpoint jack.

 

