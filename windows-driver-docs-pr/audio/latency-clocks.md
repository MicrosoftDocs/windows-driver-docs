---
title: Latency Clocks
description: Latency Clocks
ms.assetid: 3cdd4c69-d99d-48bc-a1d9-9da2a2511e94
keywords:
- synthesizers WDK audio , latency clocks
- latency WDK audio , clocks
- clocks WDK audio , latency
- latency WDK audio
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Latency Clocks


## <span id="latency_clocks"></span><span id="LATENCY_CLOCKS"></span>


The synthesizer miniport driver model is designed to allow synchronization of audio output between multiple devices. As such, it contains a more complex timing model than that provided by a pure UART device.

Events are delivered to (and captured from) the miniport driver with an associated time stamp. This time stamp is relative to a [master clock](https://msdn.microsoft.com/library/windows/hardware/ff567717). The master clock is the same clock used by all sequencing in the entire system. Master-clock time is measured in units of 100-nanosecond ticks.

The miniport driver obtains the current time from the master clock by calling [**IMasterClock::GetTime**](https://msdn.microsoft.com/library/windows/hardware/ff536697). At pin creation time, the port driver passes the kernel-mode [IMasterClock](https://msdn.microsoft.com/library/windows/hardware/ff536696) interface to the miniport driver as one of the input parameters to the [**IMiniportDMus::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536701) method. Currently, the master clock wraps the system real-time clock. The master clock never changes when there are pins that require it to be in the *run* state. It is a constant-rate clock that never pauses.

All rendering devices have some amount of latency between the time they accept an event and the time the event can be heard. This latency can be constant or variable (as in the case of a software synthesizer, where the latency depends on the current playback position of the audio buffer). This latency is compensated for by:

-   Allowing the DMus miniport driver to receive events far enough in advance so that they can be played on time, despite the latency of the device. Events are sequenced for the miniport driver by a sequencer engine in the DMus port driver.

    At pin-creation time, the port driver queries the miniport driver for a delta time in 100-nanosecond units. This delta time is how far ahead of each event's presentation time the miniport driver wants to receive the event. The port driver makes its best effort to deliver events this far ahead. Specifying a very large value for this delta (specified by *SchedulePreFetch* parameter of [**IMiniportDMus::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536701)) makes the port driver pass the events to the miniport driver as soon as they are delivered to the port driver from user mode.

-   Informing applications how far ahead to schedule events. Using the maximum latency is not desirable in this case. Because events cannot be canceled once they are submitted, the closer that events can be submitted to their presentation time, the more responsively the application and synth can interact. To handle this requirement, DirectMusic has introduced the concept of a latency clock.

    The latency clock provides the nearest time in the future that an event can be scheduled to play and still play on time. In other words, if the application schedules an event to be played before the current time according to the latency clock, then the event is played late. Synthesizer miniport drivers provide a latency clock by responding to the [**KSPROPERTY\_SYNTH\_LATENCYCLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff537402) property item.

    The miniport driver is queried for [KSPROPSETID\_Synth](https://msdn.microsoft.com/library/windows/hardware/ff537486) and KSPROPERTY\_SYNTH\_LATENCYCLOCK. The miniport driver's property handler should return a latency clock that specifies, in terms of the master clock, the next time that data can be rendered on time. For example, if the master clock currently reads 50, and there are currently 25 units of latency, then the latency clock reads 75. The reason the clock is implemented in this way is that the latency does not need to be constant, and the returned value is of more use to applications than just the delta.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Latency%20Clocks%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


