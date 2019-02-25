---
title: Requirements for a Non-PCM Pin Factory
description: Requirements for a Non-PCM Pin Factory
ms.assetid: 3ba5da2e-f96f-4645-8a37-dd985287a9f2
keywords:
- non-PCM audio formats WDK , pin factories
- pin factories WDK audio
- data-intersection handlers WDK audio , non-PCM wave formats
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requirements for a Non-PCM Pin Factory


## <span id="requirements_for_a_non_pcm_pin_factory"></span><span id="REQUIREMENTS_FOR_A_NON_PCM_PIN_FACTORY"></span>


Under Windows XP and later, and Microsoft Windows Me, drivers that play non-PCM [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799) formats should expose their non-PCM pins according to the following guidelines.

First, define a pin factory for your non-PCM data format that is separate from any PCM pin factories. PCM and non-PCM cannot share the same single-instance pin factory because the sole pin instance automatically is allocated to KMixer. If the pin factory supports multiple instances, PCM and non-PCM can coexist on the same pin factory. In this case, however, you cannot guarantee that these pin instances are available to a non-PCM client at runtime - PCM clients might already have allocated them. The safest option is to provide a separate pin factory for your non-PCM format.

In order for the pin to be discovered and used by DirectSound 8, define this non-PCM pin factory on a filter that already supports PCM. Otherwise, DirectSound will not detect the non-PCM pin. This also means that a device that does not support PCM at all cannot support a non-PCM format.

Second, implement a [data-intersection handler](proprietary-data-intersection-handlers.md) on your non-PCM pin. PortCls provides a built-in handler, but this default handler always chooses PCM, so you should add your own handler for non-PCM formats. You should not support WAVE\_FORMAT\_PCM in the intersection handler for your non-PCM pin. Note that this handler can be called with an *OutputBufferLength* of 0, in which case the caller is asking only for the size of the preferred data range, not for the data itself. In this case, the handler should respond by copying the non-PCM data range's size into the *ResultantFormatLength* parameter and returning STATUS\_BUFFER\_OVERFLOW. The Msvad sample in the Windows Driver Kit (WDK) contains the code for a [**DataRangeIntersection**](https://msdn.microsoft.com/library/windows/hardware/ff536764) routine that you can use as an example handler. To test your **DataRangeIntersection** routine, use the [KsStudio utility](ksstudio-utility.md) to instantiate your pin--it first calls your intersection handler in order to determine an acceptable default format. To support a non-PCM format, your driver must properly handle it in the following locations:

-   [**IMiniport::DataRangeIntersection**](https://msdn.microsoft.com/library/windows/hardware/ff536764)

-   Miniport driver methods **Init** and **NewStream** (For example, see [**IMiniportWavePci::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536734) and [**IMiniportWavePci::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536735).)

-   Miniport-stream method **SetFormat** (For example, see [**IMiniportWavePciStream::SetFormat**](https://msdn.microsoft.com/library/windows/hardware/ff536732).)

 

 




