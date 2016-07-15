---
Description: 'Requirements for a Non-PCM Pin Factory'
MS-HAID: 'audio.requirements\_for\_a\_non\_pcm\_pin\_factory'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Requirements for a Non-PCM Pin Factory'
---

# Requirements for a Non-PCM Pin Factory


## <span id="requirements_for_a_non_pcm_pin_factory"></span><span id="REQUIREMENTS_FOR_A_NON_PCM_PIN_FACTORY"></span>


Under Windows XP and later, and Microsoft Windows Me, drivers that play non-PCM [**WAVEFORMATEX**](audio.waveformatex) formats should expose their non-PCM pins according to the following guidelines.

First, define a pin factory for your non-PCM data format that is separate from any PCM pin factories. PCM and non-PCM cannot share the same single-instance pin factory because the sole pin instance automatically is allocated to KMixer. If the pin factory supports multiple instances, PCM and non-PCM can coexist on the same pin factory. In this case, however, you cannot guarantee that these pin instances are available to a non-PCM client at runtime - PCM clients might already have allocated them. The safest option is to provide a separate pin factory for your non-PCM format.

In order for the pin to be discovered and used by DirectSound 8, define this non-PCM pin factory on a filter that already supports PCM. Otherwise, DirectSound will not detect the non-PCM pin. This also means that a device that does not support PCM at all cannot support a non-PCM format.

Second, implement a [data-intersection handler](proprietary-data-intersection-handlers.md) on your non-PCM pin. PortCls provides a built-in handler, but this default handler always chooses PCM, so you should add your own handler for non-PCM formats. You should not support WAVE\_FORMAT\_PCM in the intersection handler for your non-PCM pin. Note that this handler can be called with an *OutputBufferLength* of 0, in which case the caller is asking only for the size of the preferred data range, not for the data itself. In this case, the handler should respond by copying the non-PCM data range's size into the *ResultantFormatLength* parameter and returning STATUS\_BUFFER\_OVERFLOW. The Msvad sample in the Windows Driver Kit (WDK) contains the code for a [**DataRangeIntersection**](audio.iminiport_datarangeintersection) routine that you can use as an example handler. To test your **DataRangeIntersection** routine, use the [KsStudio utility](ksstudio-utility.md) to instantiate your pin--it first calls your intersection handler in order to determine an acceptable default format. To support a non-PCM format, your driver must properly handle it in the following locations:

-   [**IMiniport::DataRangeIntersection**](audio.iminiport_datarangeintersection)

-   Miniport driver methods **Init** and **NewStream** (For example, see [**IMiniportWavePci::Init**](audio.iminiportwavepci_init) and [**IMiniportWavePci::NewStream**](audio.iminiportwavepci_newstream).)

-   Miniport-stream method **SetFormat** (For example, see [**IMiniportWavePciStream::SetFormat**](audio.iminiportwavepcistream_setformat).)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Requirements%20for%20a%20Non-PCM%20Pin%20Factory%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


