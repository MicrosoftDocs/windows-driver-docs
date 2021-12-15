---
title: Supporting 2D DirectSound Acceleration in WDM Audio
description: Supporting 2D DirectSound Acceleration in WDM Audio
keywords:
- hardware acceleration WDK DirectSound , 2D mixing
- 2D mixing WDK audio
ms.date: 04/20/2017
---

# Supporting 2D DirectSound Acceleration in WDM Audio


## <span id="supporting_2d_directsound_acceleration_in_wdm_audio"></span><span id="SUPPORTING_2D_DIRECTSOUND_ACCELERATION_IN_WDM_AUDIO"></span>


DirectSound exposes hardware-accelerated 2D mixing for WDM audio miniport drivers that meet the following requirements:

-   The miniport driver includes a pin factory that is an IRP sink (KSPIN\_COMMUNICATION\_SINK), has a [**KSPIN\_DATAFLOW**](/windows-hardware/drivers/ddi/ks/ne-ks-kspin_dataflow) direction of KSPIN\_DATAFLOW\_IN, and exposes a data range ([**KSDATARANGE\_AUDIO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdatarange_audio) structure) in which the specifier (**DataFormat**.**Specifier** member) is set to KSDATAFORMAT\_SPECIFIER\_DSOUND.

-   The pin factory's [**KSPROPERTY\_PIN\_CINSTANCES**](../stream/ksproperty-pin-cinstances.md) handler sets the **PossibleCount** member of the **KSPIN\_CINSTANCES** structure to a value of two or greater (the first pin is always reserved for KMixer). The **PossibleCount** value specifies the number of pin instances that can currently be instantiated from the pin factory.

-   The pin factory must support the [**KSPROPERTY\_AUDIO\_CPU\_RESOURCES**](./ksproperty-audio-cpu-resources.md) property and should report KSAUDIO\_CPU\_RESOURCES\_NOT\_HOST\_CPU for all nodes that are hardware accelerated.

-   The pin should meet the [DirectSound node-ordering requirements](directsound-node-ordering-requirements.md).

 

