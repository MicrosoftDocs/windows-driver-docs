---
title: Supporting 2D DirectSound Acceleration in WDM Audio
description: Supporting 2D DirectSound Acceleration in WDM Audio
ms.assetid: dbbb2416-8928-41ee-90d5-b3b77d23c251
keywords:
- hardware acceleration WDK DirectSound , 2D mixing
- 2D mixing WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting 2D DirectSound Acceleration in WDM Audio


## <span id="supporting_2d_directsound_acceleration_in_wdm_audio"></span><span id="SUPPORTING_2D_DIRECTSOUND_ACCELERATION_IN_WDM_AUDIO"></span>


DirectSound exposes hardware-accelerated 2D mixing for WDM audio miniport drivers that meet the following requirements:

-   The miniport driver includes a pin factory that is an IRP sink (KSPIN\_COMMUNICATION\_SINK), has a [**KSPIN\_DATAFLOW**](https://msdn.microsoft.com/library/windows/hardware/ff563532) direction of KSPIN\_DATAFLOW\_IN, and exposes a data range ([**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure) in which the specifier (**DataFormat**.**Specifier** member) is set to KSDATAFORMAT\_SPECIFIER\_DSOUND.

-   The pin factory's [**KSPROPERTY\_PIN\_CINSTANCES**](https://msdn.microsoft.com/library/windows/hardware/ff565193) handler sets the **PossibleCount** member of the **KSPIN\_CINSTANCES** structure to a value of two or greater (the first pin is always reserved for KMixer). The **PossibleCount** value specifies the number of pin instances that can currently be instantiated from the pin factory.

-   The pin factory must support the [**KSPROPERTY\_AUDIO\_CPU\_RESOURCES**](https://msdn.microsoft.com/library/windows/hardware/ff537255) property and should report KSAUDIO\_CPU\_RESOURCES\_NOT\_HOST\_CPU for all nodes that are hardware accelerated.

-   The pin should meet the [DirectSound node-ordering requirements](directsound-node-ordering-requirements.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Supporting%202D%20DirectSound%20Acceleration%20in%20WDM%20Audio%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


