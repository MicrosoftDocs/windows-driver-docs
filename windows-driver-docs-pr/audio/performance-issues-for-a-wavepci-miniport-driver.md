---
title: Performance Issues for a WavePci Miniport Driver
description: Performance Issues for a WavePci Miniport Driver
ms.assetid: 785fd743-0c78-44cd-95bf-1f961aa414b5
keywords:
- WavePci performance issues WDK audio
- stream servicing mechanisms WDK audio
- hardware interrupts WDK audio
- interrupt service routines WDK audio
- ISRs WDK audio
- timer DPCs WDK audio
- PAUSE/ACQUIRE optimizations WDK audio
- IPreFetchOffset
- synchronization primitives WDK audio
- IPinCount
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performance Issues for a WavePci Miniport Driver


## <span id="performance_issues_for_a_wavepci_miniport_driver"></span><span id="PERFORMANCE_ISSUES_FOR_A_WAVEPCI_MINIPORT_DRIVER"></span>


An audio driver's performance impact on the system can be significantly reduced by following these general principles:

-   Minimize the code that is run during normal operation.

-   Run code only when necessary.

-   Consider the total system resource consumption (not just CPU loading).

-   Optimize code for speed and size.

In addition, WavePci miniport drivers must address several performance issues that are specific to audio devices. The following discussion deals primarily with audio-rendering issues, although some of the suggested techniques apply to audio capture as well.

### <span id="Stream_Servicing_Mechanisms"></span><span id="stream_servicing_mechanisms"></span><span id="STREAM_SERVICING_MECHANISMS"></span>Stream Servicing Mechanisms

Before discussing performance optimizations, some background is necessary to understand the WavePci mechanisms for servicing streams.

When processing a wave render or capture stream, an audio device requires servicing at regular intervals by the miniport driver. When new mappings are available for a stream, the driver adds those mappings to the stream's DMA queue. The driver also removes from the queue any mappings that have already been processed. For information about mappings, see [WavePci Latency](wavepci-latency.md).

To perform the servicing, the miniport driver provides either a [*deferred procedure call (DPC)*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss_deferred_procedure_call__dpc_) or interrupt service routine (ISR), depending on whether the interval is set by a system timer or by DMA-driven interrupts. In the latter case, the DMA hardware typically triggers an interrupt each time if finishes transferring some amount of stream data.

Each time the DPC or ISR executes, it determines which streams require servicing. The DPC or ISR services a stream by calling the [**IPortWavePci::Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536918) method. This method takes as a call parameter the stream's service group, which is an object of type [IServiceGroup](https://msdn.microsoft.com/library/windows/hardware/ff536994). The **Notify** method calls the service group's [**RequestService**](https://msdn.microsoft.com/library/windows/hardware/ff537009) method (see **IServiceSink::RequestService**).

A service-group object contains a group of service sinks, which are objects of type [IServiceSink](https://msdn.microsoft.com/library/windows/hardware/ff537006). [IServiceGroup](https://msdn.microsoft.com/library/windows/hardware/ff536994) is derived from IServiceSink, and both interfaces have [**RequestService**](https://msdn.microsoft.com/library/windows/hardware/ff537009) methods. When the [**Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536918) method calls the service group's **RequestService** method, the service group responds by calling the **RequestService** method on each service sink in the group.

A stream's service group contains at least one service sink, which the port driver adds to the service group immediately following creation of the stream. The port driver calls the miniport driver's [**IMiniportWavePci::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536735) method to obtain a pointer to the service group. The service sink's [**RequestService**](https://msdn.microsoft.com/library/windows/hardware/ff537009) method is the port driver's stream-specific service routine. This routine does the following:

-   Calls the miniport driver's [**IMiniportWavePciStream::Service**](https://msdn.microsoft.com/library/windows/hardware/ff536731) method.

-   Triggers any newly pending position or clock events on the stream since the last time the service routine executed.

As discussed in [KS Events](https://msdn.microsoft.com/library/windows/hardware/ff567643), clients can register to be notified when a stream reaches a particular position or when a clock reaches a particular time stamp. The [**NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536735) method has the option of not supplying a service group, in which case the port driver sets up its own timer to mark off the intervals between calls to its service routine.

Like the [**NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536735) method, the miniport driver's [**IMiniportWavePci::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536734) method also outputs a pointer to a service group. Following the **Init** call, the port driver adds its service sink to the service group. This particular service sink contains the service routine for the filter as a whole. (The preceding paragraph describes the service sink for the stream associated with a pin on the filter.) This service routine calls the miniport driver's [**IMiniportWavePci::Service**](https://msdn.microsoft.com/library/windows/hardware/ff536736) method. The service routine executes each time the DPC or ISR calls [**Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536918) with the service group for the filter. The **Init** method has the option of not supplying a service group, in which case the port driver never calls its filter service routine.

### <span id="Hardware_Interrupts"></span><span id="hardware_interrupts"></span><span id="HARDWARE_INTERRUPTS"></span>Hardware Interrupts

Some miniport drivers generate either too many or not enough hardware interrupts. In some WavePci rendering devices with DirectSound hardware acceleration, a hardware interrupt occurs only when the supply of mappings is nearly exhausted and the rendering engine is at risk of starvation. In other hardware-accelerated WavePci devices, a hardware interrupt occurs on every single mapping completion or some other relatively small interval. In this case, the ISR frequently finds that it has little to do, but each interrupt still consumes system resources with register swaps and cache reloads. The first step in improving driver performance is to reduce the number of interrupts as much as possible without risking starvation. After eliminating unnecessary interrupts, additional performance gains can be achieved by designing the ISR to execute more efficiently.

In some drivers, ISRs waste time by calling a stream's [**Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536918) method every time a hardware interrupt occurs--regardless of whether the stream is actually running. If no streams are in the RUN state, then DMA is inactive, and any time spent trying to acquire mappings, release mappings, or check for new events in any streams is wasted. In an efficient driver, the ISR verifies that a stream is running before calling the stream's **Notify** method.

However, a driver with this type of ISR needs to make sure that any pending events on a stream are triggered when the stream exits the RUN state. Otherwise, the events might be delayed or lost. This issue arises only during RUN-to-PAUSE transitions in operating systems older than Microsoft Windows XP. In Windows XP and later, the port driver automatically signals any outstanding position events immediately when a stream changes state from RUN to PAUSE. In the older operating systems, however, the miniport driver is responsible for triggering any outstanding events by making a final call to [**Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536918) immediately after the stream is paused. For more information, see PAUSE/ACQUIRE Optimizations below.

A typical WavePci miniport driver manages a single playback stream from the [KMixer system driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver). The current implementation of KMixer uses a minimum of three mapping IRPs to buffer a playback stream. Each IRP contains enough buffer storage for about 10 milliseconds of audio. If the miniport driver triggers a hardware interrupt each time the DMA controller finishes with the final mapping in an IRP, interrupts should occur at fairly regular 10-millisecond intervals, which is frequent enough to keep the DMA queue from starving. 

### <span id="Timer_DPCs"></span><span id="timer_dpcs"></span><span id="TIMER_DPCS"></span>Timer DPCs

If a driver manages any hardware-accelerated DirectSound streams, it should use a timer DPC (see [Timer Objects and DPCs](https://msdn.microsoft.com/library/windows/hardware/ff564655)) instead of DMA-driven hardware interrupts. Equivalently, a WavePci device on a PCI card with an on-board timer can use a timer-driven hardware interrupt instead of a DPC.

In the case of a DirectSound buffer, the entire buffer can be attached to a single IRP. If the buffer is large and the miniport driver schedules a hardware interrupt only when it reaches the end of the buffer, successive interrupts can occur so far apart that the DMA queue starves. Also, if the driver is managing a large number of hardware-accelerated DirectSound streams, and each stream generates its own interrupts, then the cumulative impact of all the interrupts can degrade system performance. In these circumstances, the miniport driver should avoid using hardware interrupts to schedule servicing of individual streams. Instead, it should service all streams in a single DPC that is scheduled to run at regular timer-generated intervals.

By setting the timer interval to 10 milliseconds, the interval between successive DPC executions is similar to that described previously for the hardware interrupt in the case of a single KMixer playback stream. Thus, the DPC can handle the KMixer playback stream in addition to hardware-accelerated DirectSound streams.

When the last stream exits the RUN state, the miniport driver should disable the timer DPC to avoid wasting system CPU cycles. Immediately after disabling the DPC, the driver should make sure that any clock or position events pending on previously running streams are flushed. In Windows 98/Me and Windows 2000, the driver should call [**Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536918) to trigger any pending events on the streams that are being paused. In Windows XP and later, the operating system triggers any pending events automatically when a stream exits the RUN state, without requiring intervention by the miniport driver.

### <span id="PAUSE_ACQUIRE_Optimizations"></span><span id="pause_acquire_optimizations"></span><span id="PAUSE_ACQUIRE_OPTIMIZATIONS"></span>PAUSE/ACQUIRE Optimizations

In Windows 98/Me and Windows 2000, the WavePci port driver's stream service routine (the [**RequestService**](https://msdn.microsoft.com/library/windows/hardware/ff537009) method) always generates a call to the miniport driver's [**IMiniportWavePciStream::Service**](https://msdn.microsoft.com/library/windows/hardware/ff536731) method regardless of whether the stream is in the RUN state. In these operating systems, the **Service** method should check whether the stream is running before spending time doing actual work. (However, if the miniport driver's DPC or ISR has already been optimized to call [**Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536918) only for streams that are running, adding this check to the **Service** method might be redundant.)

In Windows XP and later, this optimization is unnecessary because the [**Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536918) method calls the [**Service**](https://msdn.microsoft.com/library/windows/hardware/ff536731) method only on streams that are running.

### <span id="Using_the_IPreFetchOffset_Interface"></span><span id="using_the_iprefetchoffset_interface"></span><span id="USING_THE_IPREFETCHOFFSET_INTERFACE"></span>Using the IPreFetchOffset Interface

DirectSound users are familiar with the dual concepts of the play cursor and the write cursor. The play cursor indicates the position in the stream of the data being emitted from the device (the driver's best estimate of the sample currently at the DAC). The write position is the position in the stream of the next safe place for the client to write additional data. For WavePci, the default assumption is that the write cursor is positioned at the end of the last mapping requested. If the miniport driver has acquired a large number of outstanding mappings, the offset between the play cursor and write cursor can be very large—large enough to fail certain WHQL audio-position tests. In Windows XP and later, the [IPreFetchOffset](https://msdn.microsoft.com/library/windows/hardware/ff536951) interface addresses these issues.

The miniport driver uses [IPreFetchOffset](https://msdn.microsoft.com/library/windows/hardware/ff536951) to specify the bus-master hardware's prefetch characteristics, which are largely determined by the hardware FIFO size. The audio subsystem uses this data to set a constant offset between the play cursor and the write cursor. This constant offset, which can be significantly smaller than the default offset, takes advantage of the fact that data can be written into a mapping even after the mapping has been handed to the hardware, as long as the play cursor is far enough away from the location into which data is written. (This statement assumes that the driver does not copy or otherwise manipulate the data in mappings.) A typical offset might be on the order of 64 samples, depending on the engine design. With an offset this small, a WavePci driver can be fully responsive and functional while still requesting a large number of mappings.

Note that DirectSound currently pads the write cursor of a hardware-accelerated pin by 10 milliseconds.

For a more information, see [Prefetch Offsets](prefetch-offsets.md).

### <span id="Processing_Data_in_Mappings"></span><span id="processing_data_in_mappings"></span><span id="PROCESSING_DATA_IN_MAPPINGS"></span>Processing Data in Mappings

Avoid having your hardware driver touch the data in the mappings if at all possible. Any software processing of data contained in mappings should be split out into a software filter separate from the hardware driver. Having a hardware driver perform such processing reduces its efficiency and creates latency problems.

A hardware driver should strive to be transparent about its real hardware capabilities. The driver should never claim to provide hardware support for a data transform that is actually performed in software.

### <span id="Synchronization_Primitives"></span><span id="synchronization_primitives"></span><span id="SYNCHRONIZATION_PRIMITIVES"></span>Synchronization Primitives

A driver is less likely to have deadlock or performance problems now and in the future if its code is designed to avoid being blocked whenever possible. Specifically, a driver's thread of execution should strive to run to completion without the risk of stalling while waiting for another thread or resource. For example, driver threads can use the Interlocked*Xxx* functions (for example, see [**InterlockedIncrement**](https://msdn.microsoft.com/library/windows/hardware/ff547910)) to coordinate their accesses to certain shared resources without the risk of being blocked.

Although these are powerful techniques, you might not be able to safely remove all spin locks, mutexes, and other blocking synchronization primitives from the execution path. Use the Interlocked*Xxx* functions judiciously, with the knowledge that an indefinite wait might cause data starvation.

Above all, do not create custom synchronization primitives. The built-in Windows primitives (mutexes, spin locks, and so on) are likely to be modified as needed to support new scheduler features in the future, and a driver that uses custom constructs is virtually guaranteed not to work in the future.

### <span id="IPinCount_Interface"></span><span id="ipincount_interface"></span><span id="IPINCOUNT_INTERFACE"></span>IPinCount Interface

In Windows XP and later, the [IPinCount](https://msdn.microsoft.com/library/windows/hardware/ff536832) interface provides a way for a miniport driver to more accurately account for the hardware resources that are consumed by allocating a pin. By calling the miniport driver's [**IPinCount::PinCount**](https://msdn.microsoft.com/library/windows/hardware/ff536834) method, the port driver does the following:

-   Exposes the filter's current pin counts (as maintained by the port driver) to the miniport driver.

-   Gives the miniport driver the opportunity to revise the pin counts to dynamically reflect the current availability of hardware resources.

For some audio devices, wave streams with different attributes (3-D, stereo/mono, and so on) might also have different "weights" in terms of how many hardware resources they consume. When opening or closing a "lightweight" stream, the driver increments or decrements the count of available pins by one. When opening a "heavyweight" stream, however, the miniport driver might need to decrement the available pin count by two instead of by one in order to more accurately indicate the number of pins that can be created with the remaining resources.

The process is reversed when a heavyweight stream is closed. The available pin count might increase by more than one in order to reflect the fact that two or more lightweight streams can be created from the newly freed resources.

 

 




