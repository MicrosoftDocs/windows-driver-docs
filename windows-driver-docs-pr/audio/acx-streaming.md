---
title: ACX Streaming
description: This article provides a summary of ACX streaming and associated buffering, which is critical to a glitch-free audio experience.
ms.date: 01/06/2026
ms.localizationpriority: medium
ms.topic: concept-article
ai.usage: ai-assisted
---

# ACX streaming

This article explains ACX streaming and buffering, which are critical to a glitch-free audio experience. It describes how the driver communicates stream state and manages the stream buffer. For a list of common ACX audio terms and an introduction to ACX, see [ACX audio class extensions overview](acx-audio-class-extensions-overview.md).

## ACX streaming types

An AcxStream represents an audio stream on a specific circuit's hardware. An AcxStream can aggregate one or more AcxElements-like objects.

ACX supports two stream types. The first stream type, the *RT Packet Stream*, lets you allocate RT packets and use them to transfer audio data to or from the device hardware, along with stream state transitions. The second stream type, the *basic stream*, supports only stream state transitions.

In a single circuit endpoint, the circuit is a streaming circuit that creates an RT Packet Stream. If two or more circuits connect to create an endpoint, the first circuit in the endpoint is the streaming circuit and creates an RT Packet Stream. Connected circuits create Basic Streams to receive events related to stream state transitions.

For more information, see *ACX Stream* in [Summary of ACX Objects](acx-summary-of-objects.md). The DDIs for streams are defined in the [acxstreams.h](/windows-hardware/drivers/ddi/acxstreams) header.

## ACX streaming communications stack

There are two types of communications for ACX streaming. One communication path controls the streaming behavior. For example, commands such as Start, Create, and Allocate, that use standard ACX communications. The ACX framework uses IO queues and passes along WDF requests using the queues. The queue behavior is hidden from the actual driver code by using event callbacks and ACX functions. The driver is also given a chance to preprocess all WDF requests.

The second and more interesting communications path handles audio streaming signaling. Signaling involves telling the driver when a packet is ready and receiving data and when the driver finishes processing a packet.

Main requirements for streaming signaling:

- Support glitch-free playback
  - Low latency
  - Any necessary locks are limited to the stream in question
- Ease of use for driver developer

To communicate with the driver to signal streaming state, ACX uses events with a shared buffer and direct IRP calls. These techniques are described next.

### Shared buffer

A shared buffer and event communicate from the driver to the client. The event and shared buffer ensure the client doesn't need to wait or poll. The client can determine everything it needs to continue streaming while reducing or eliminating the need for direct IRP calls.

The device driver uses a shared buffer to communicate to the client which packet is being rendered from or captured to. This shared buffer includes the packet count (one-based) of the last completed packet along with the QPC (QueryPerformanceCounter) value of the completion time. For the device driver, it must indicate this information by calling **[AcxRtStreamNotifyPacketComplete](/windows-hardware/drivers/ddi/acxstreams/nf-acxstreams-acxrtstreamnotifypacketcomplete)**. When the device driver calls **AcxRtStreamNotifyPacketComplete**, the ACX framework updates the shared buffer with the new packet count and QPC and signals an event shared with the client to indicate that the client can read the new packet count.

#### Direct IRP calls

Direct IRP calls communicate from the client to the driver.

The client can request the current packet count, or indicate the current packet count to the device driver at any time. These requests call the [EvtAcxStreamGetCurrentPacket](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_get_current_packet) and [EvtAcxStreamSetRenderPacket](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_set_render_packet) device driver event handlers. The client can also request the current capture packet, which calls the [EvtAcxStreamGetCapturePacket](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_get_capture_packet) device driver event handler.

#### Similarities with PortCls

The combination of direct IRP calls and shared buffer that ACX uses is similar to how PortCls communicates buffer completion handling.

To prevent glitching, drivers must ensure they do nothing that requires access to locks that are also used in the stream control paths.

## Large buffer support for low power playback

To reduce power consumption during playback, reduce the time the APU spends in a high power state. Because normal audio playback uses 10 ms buffers, the APU stays active. ACX drivers can advertise support for larger buffers, in the 1–2 second range, to let the APU enter a lower power state.

In existing streaming models, offload playback supports low power playback. An audio driver advertises support for offload playback by exposing an AudioEngine node on the wave filter for an endpoint. The AudioEngine node provides a means to control the DSP engine the driver uses to render the audio from the large buffers with the desired processing.

The AudioEngine node provides these features:

- Audio Engine Description tells the audio stack which pins on the wave filter provide offload and loopback support (and host playback support).
- Buffer Size Range tells the audio stack the minimum and maximum buffer sizes that can be supported for offload. playback. The Buffer Size Range can change dynamically based on system activity.
- Format support, including supported formats, the current device mix format, and the device format.
- Volume, including ramping support, since with the larger buffers software volume won't be responsive.
- Loopback Protection, which tells the driver to mute the AudioEngine Loopback pin if one or more of the Offloaded streams contains protected content.
- Global FX state, to enable or disable GFX on the AudioEngine.

When you create a stream on the offload pin, the stream supports volume, local FX, and loopback protection.

### Low power playback with ACX

The ACX framework uses the same model for low power playback. The driver creates three separate ACXPIN objects for host, offload, and loopback streaming, along with an ACXAUDIOENGINE element that describes which of these pins are used for host, offload, and loopback. The driver adds the pins and ACXAUDIOENGINE element to the ACXCIRCUIT during circuit creation.

### Offloaded stream creation

The driver also adds an ACXAUDIOENGINE element to streams created for offload to allow control over volume, mute, and peak meter.

### Streaming diagram

This diagram shows a multi-stack ACX driver.

:::image type="content" source="images/audio-acx-multi-stack-kernel-streaming.png" alt-text="Diagram illustrating DSP, CODEC, and AMP boxes with a kernel streaming interface on top.":::

Each ACX driver controls a separate part of the audio hardware, which might come from a different vendor. ACX provides a compatible kernel streaming interface so applications run without changes.

#### Stream pins

Each ACXCIRCUIT has at least one Sink Pin and one Source Pin. These Pins are used by the ACX framework to expose the circuit's connections to the audio stack. For a Render circuit, the Source Pin is used to control the render behavior of any stream created from the circuit. For a Capture circuit, the Sink Pin is used to control the capture behavior of any stream created from the circuit.

ACXPIN is the object used to control streaming in the Audio Path. The streaming ACXCIRCUIT is responsible for creating the appropriate ACXPIN objects for the Endpoint Audio Path at circuit creation time and registering the ACXPINs with ACX. The ACXCIRCUIT only creates the render or capture pins for the circuit. The ACX framework creates the other pin needed to connect to and communicate with the circuit.

#### Streaming circuit

When an endpoint is composed of a single circuit, that circuit is the streaming circuit.

When an endpoint is composed of more than one circuit created by one or more device drivers, the ACXCOMPOSITETEMPLATE that describes the composed endpoint determines the specific order that connects the circuits. The first circuit in the endpoint is the streaming circuit for the endpoint.

The streaming circuit should use [AcxRtStreamCreate](/windows-hardware/drivers/ddi/acxstreams/nf-acxstreams-acxrtstreamcreate) to create an RT Packet Stream in response to [EvtAcxCircuitCreateStream](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_create_stream). The ACXSTREAM created with AcxRtStreamCreate allows the streaming circuit driver to allocate the buffer used for streaming and to control the streaming flow in response to the client and hardware needs.

Following circuits in the endpoint should use [AcxStreamCreate](/windows-hardware/drivers/ddi/acxstreams/nf-acxstreams-acxstreamcreate) to create a Basic Stream in response to EvtAcxCircuitCreateStream. The ACXSTREAM objects created with AcxStreamCreate by the following circuits allow the drivers to configure hardware in response to stream state changes such as Pause or Run.

The streaming ACXCIRCUIT receives the first request to create a stream. The request includes the device, the pin, and the data format (including mode).

Each ACXCIRCUIT in the Audio Path creates an ACXSTREAM object that represents the circuit's stream instance. The ACX framework links the ACXSTREAM objects together, similar to how it links ACXCIRCUIT objects.

#### Upstream and downstream circuits

Stream creation starts at the streaming circuit and is forwarded to each downstream circuit in the order the circuits are connected. The connections are made between bridge pins created with Communication equal to AcxPinCommunicationNone. The ACX framework creates one or more bridge pins for a circuit if the driver doesn't add them at circuit creation time.

For each circuit starting with the streaming circuit, the AcxPinTypeSource bridge pin connects to the next downstream circuit. The final circuit has an endpoint pin describing the audio endpoint hardware (such as whether the endpoint is a Microphone or Speaker and whether the Jack is plugged in).

For each circuit following the streaming circuit, the AcxPinTypeSink bridge pin connects to the next upstream circuit.

#### Stream format negotiation

The driver advertises the supported formats for stream creation by adding the supported formats per mode to the ACXPIN used for stream creation with [AcxPinAssignModeDataFormatList](/windows-hardware/drivers/ddi/acxpin/nf-acxpin-acxpinassignmodedataformatlist) and [AcxPinGetRawDataFormatList](/windows-hardware/drivers/ddi/acxpin/nf-acxpin-acxpingetrawdataformatlist). For multi circuit endpoints, an ACXSTREAMBRIDGE can be used to coordinate mode and format support between ACX Circuits. The streaming ACXPINs created by the streaming circuit determine the supported stream formats for the endpoint. The formats used by the following circuits are determined by the bridge pin of the previous circuit in the endpoint.

By default, the ACX framework creates an ACXSTREAMBRIDGE between each circuit in a multi circuit endpoint. The default ACXSTREAMBRIDGE uses the RAW mode's default format of the bridge pin of the upstream circuit when forwarding the stream creation request to the downstream circuit. If the upstream circuit's bridge pin has no formats, the original stream format is used. If the connected pin of the downstream circuit doesn't support the format being used, stream creation fails.

If a device circuit is performing a stream format change, the device driver should add the downstream format to the downstream bridge pin.

#### Stream creation

The first step in Stream Creation is creating the ACXSTREAM instance for each ACXCIRCUIT in the Endpoint Audio Path. ACX calls each circuit's [EvtAcxCircuitCreateStream](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_create_stream). ACX starts with the head circuit and call each circuit's EvtAcxCircuitCreateStream in order, ending with the tail circuit. The order can be reversed by specifying the AcxStreamBridgeInvertChangeStateSequence flag (defined in [ACX_STREAM_BRIDGE_CONFIG_FLAGS](/windows-hardware/drivers/ddi/acxstreams/ne-acxstreams-acx_stream_bridge_config_flags)) for the Stream Bridge. After all circuits create a stream object, the stream objects handle streaming logic.

The Stream Creation Request is sent to the appropriate PIN generated as part of the head circuit's topology generation by calling the EvtAcxCircuitCreateStream specified during head circuit creation.

The streaming circuit is the upstream circuit that initially handles the stream creation request.

- It updates the ACXSTREAM_INIT structure, assigning AcxStreamCallbacks and AcxRtStreamCallbacks
- It creates the ACXSTREAM object using AcxRtStreamCreate
- It creates any stream-specific elements (for example, ACXVOLUME or ACXAUDIOENGINE)
- It adds the elements to the ACXSTREAM object
- It returns the ACXSTREAM object that was created to the ACX framework

ACX then forwards the stream creation to the next downstream circuit.

- It updates the ACXSTREAM_INIT structure, assigning AcxStreamCallbacks
- It creates the ACXSTREAM object using AcxStreamCreate
- It creates any stream-specific elements
- It adds the elements to the ACXSTREAM object
- It returns the ACXSTREAM object that was created to the ACX framework

The communication channel between circuits in an audio path uses ACXTARGETSTREAM objects. Each circuit has access to an IO Queue for the circuit in front of it and the circuit behind it in the Endpoint Audio Path. The Endpoint Audio Path is linear and bidirectional. The ACX framework handles the actual IO Queue processing.

While creating the ACXSTREAM object, each circuit can add Context information to the ACXSTREAM object to store and track private data for the stream.

#### Render stream example

Creating a render stream on an Endpoint Audio Path composed of three circuits: DSP, CODEC, and AMP. The DSP circuit functions as the streaming circuit, and has provided an EvtAcxPinCreateStream handler. The DSP circuit also functions as a filter circuit: depending on the stream mode and configuration, it can apply signal processing to the audio data. The CODEC circuit represents the DAC, providing the audio sink functionality. The AMP circuit represents the analog hardware between the DAC and the speaker. The AMP circuit might handle jack detection or other endpoint hardware details.

1. AudioKSE calls NtCreateFile to create a stream.
2. This filters through ACX and ends with calling the DSP circuit's EvtAcxPinCreateStream with the pin, dataformat (including mode), and device information.
3. The DSP circuit validates the dataformat information to ensure it can handle the created stream.
4. The DSP circuit creates the ACXSTREAM object to represent the stream.
5. The DSP circuit allocates a private context structure and associates it with the ACXSTREAM.
6. The DSP circuit returns flow of execution to the ACX framework, which then calls into the next circuit in the Endpoint Audio Path, the CODEC circuit.
7. The CODEC circuit validates the dataformat information to confirm it can handle rendering the data.
8. The CODEC circuit allocates a private context structure and associates it with the ACXSTREAM.
9. The CODEC circuit adds itself as a stream sink to the ACXSTREAM.
10. The CODEC circuit returns flow of execution to the ACX framework, which then calls into the next circuit in the Endpoint Audio Path, the AMP circuit.
11. The AMP circuit allocates a private context structure and associates it with the ACXSTREAM.
12. The AMP circuit returns flow of execution to the ACX framework. At this point, stream creation is complete.

#### Large buffer streams

Large buffer streams are created on the ACXPIN designated for Offload by the ACXCIRCUIT's ACXAUDIOENGINE element.

To support offload streams, the device driver should do the following actions during streaming circuit creation:

1. Create the Host, Offload, and Loopback ACXPIN objects and add them to the ACXCIRCUIT.
2. Create ACXVOLUME, ACXMUTE, and ACXPEAKMETER elements. These won't be added directly to the ACXCIRCUIT.
3. Initialize an [ACX_AUDIOENGINE_CONFIG structure](/windows-hardware/drivers/ddi/acxelements/ns-acxelements-acx_audioengine_config), assigning the HostPin, OffloadPin, LoopbackPin, VolumeElement, MuteElement, and PeakMeterElement objects.
4. Create the ACXAUDIOENGINE element.

Drivers need to perform similar steps to add an ACXSTREAMAUDIOENGINE element when creating a stream on the Offload pin.

## Stream resource allocation

The streaming model for ACX is packet-based, with support for one or two packets for a stream. The Render or Capture ACXPIN for the streaming circuit is given a request to allocate the memory packets that are used in the stream. To support Rebalance, the allocated memory must be system memory instead of device memory mapped into the system. The driver can use existing WDF functions to perform the allocation, and return an array of pointers to the buffer allocations. If the driver requires a single contiguous block, it can allocate both packets as a single buffer. The second packet has `WdfMemoryDescriptorTypeInvalid` and the offset of the second packet is into the buffer described by the first packet.

If a single packet is allocated, the driver must allocate a page-aligned buffer with a length that is page-divisible. The offset for the single packet also must be 0. The ACX framework maps this packet into user mode twice, back to back:

| packet 0 | packet 0 |

This enables GetBuffer to return a pointer to a single contiguous memory buffer that can span from the end of the buffer to the beginning without requiring the application to handle wrapping the memory access.

If two packets are allocated, they're mapped into user mode:

| packet 0  | packet 1 |

With the initial ACX packet streaming, there are only two packets allocated at the beginning. After the allocation and mapping are performed, the client virtual memory mapping remains valid, without changing for the life of the stream. There's one event associated with the stream to indicate packet completion for both packets. There's also a shared buffer that the ACX framework uses to communicate which packet finished with the event.

For PacketCount=1, if the application asks for 10 ms of data, the audio stack sends a request for a single 10-ms buffer to the driver (it doesn't double the buffer size sent to the driver).

The driver allocates a page aligned buffer that's at least 10 ms long. For a 48k 2ch 2 bytes per sample stream, the smallest timer driven buffer that can be allocated is 1,024 samples (one page of memory), which is 21.333 ms. For a 48k 8ch 2 bytes per sample stream, the smallest timer driven buffer that can be allocated is 512 samples (one page of memory) or 10.667 ms. For a 48k 6ch 2 bytes per sample stream, the smallest timer driven buffer is still 1,024 samples (three pages of memory, to make sure the end of a sample aligns with the end of the buffer), which is 21.333 ms.

The ACX framework maps this page aligned buffer into the user mode process twice, back to back. The user mode process can then write up to a buffer's worth of data into the user mode mapping starting anywhere in the buffer without having to do any wrapping.

The driver calls NotifyPacketComplete after it reads the entire packet from system memory, so the system knows it can write the next packet of audio data to the packet's buffer.

There's a delay between NotifyPacketComplete and when the last sample of that packet is rendered. This delay is expressed as the result from `EvtAcxStreamGetHwLatency`.

### Ping-pong buffers

Ping-pong buffers can be used, where one buffer is being read (ping), while the other is being filled (pong). This allows one buffer to be processed while the other collects the next set of data. In ACX the driver internally takes care of switching when a buffer is filled. After the ping buffer is filled, it's notified with a registered callback. In the callback, the processed buffer's address is obtained, and the buffer is resubmitted. Meanwhile, the pong buffer collects data in the background. This mechanism ensures continuous data processing without interruptions.

For a ping-pong buffer, the requested packet size is for a single buffer (either ping or pong), and the packet count is two.

When sharing a single buffer between two packets, configure the second packet as described in the [EVT_ACX_STREAM_ALLOCATE_RTPACKETS callback function](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_allocate_rtpackets). The part of the buffer described by the first packet (memory, offset, and length) is the ping buffer, while the part described by the second packet (no memory to indicate the buffer is shared with the first packet, plus offset that points to the buffer just after the first packet) is the pong buffer.

### Adding additional information to the packet header

It's only possible to add additional information to the packet header information, for example for logging or bookkeeping, at the beginning of the packet for ping/pong event driven streams (where packet count = 2). For timer driven streams with only one packet, the packet must be fully page aligned (starting and ending on a page boundary) because the packet is mapped into user mode twice.

:::image type="content" source="images/audio-acx-stream-two-buffers.png" alt-text="Diagram illustrating two buffers and how they're accessed in kernel and user mode memory.":::

In this case, the app can write past the end of the first mapping into the second mapping, which writes at the end of the system buffer then at the beginning of the same system buffer.

The single allocated buffer must be page aligned because the virtual memory mapping into user mode happens on a per-page basis.

### Timer-driven buffers

Timer-driven buffers in ACX can be used to ensure a glitch-free audio experience by maintaining precise timing and synchronization. For timer-driven buffers in ACX:

- The client uses the value from EvtAcxStreamGetPresentationPosition to determine how many frames can be written.
- The presentation position needs to be updated more than once per pass through the buffer. The client writes to the buffer starting at the position it last wrote to through the position the driver reports (which should be the data the hardware consumed since the last time the position was queried).
- The more granular the position, the less likely you are to experience glitching.
- In timer-driven buffers the DSP can't just consume the entire buffer before updating the position.
- In timer-driven, the driver could potentially split the one timer-driven buffer into multiple DSP buffers, updating position as the DSP works through each buffer (for example, a 20-ms timer-driven buffer split into 10 2-ms buffers would behave reasonably well in timer-driven mode).

### Large buffer streams packet sizes

When exposing support for Large Buffers, the driver will also provide a callback that is used to determine the minimum and maximum packet sizes for Large Buffer playback.

The packet size for stream buffer allocation is determined based on the minimum and maximum.

Because the minimum and maximum buffer sizes can be volatile, the driver can fail the packet allocation call if there are changes to the minimum and maximum buffer sizes.

### Specifying ACX buffer constraints

To specify ACX buffer constraints, ACX drivers can use the KS/PortCls properties setting - [KSAUDIO_PACKETSIZE_CONSTRAINTS2](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints2) and the [KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT structure](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_signalprocessingmode_constraint).

The following code sample shows how to set buffer size constraints for WaveRT buffers for different signal processing modes.

```cpp
//
// Describe buffer size constraints for WaveRT buffers
// Note: 10msec for each of the Modes is the default system behavior.
//
static struct
{
    KSAUDIO_PACKETSIZE_CONSTRAINTS2                 TransportPacketConstraints;         // 1
    KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT    AdditionalProcessingConstraints[4]; // + 4 = 5
} DspR_RtPacketSizeConstraints =
{
    {
        10 * HNSTIME_PER_MILLISECOND,                           // 10 ms minimum processing interval
        FILE_BYTE_ALIGNMENT,                                    // 1 byte packet size alignment
        0,                                                      // no maximum packet size constraint
        5,                                                      // 5 processing constraints follow
        {
            STATIC_AUDIO_SIGNALPROCESSINGMODE_RAW,              // constraint for raw processing mode
            0,                                                  // NA samples per processing frame
            10 * HNSTIME_PER_MILLISECOND,                       // 100000 hns (10ms) per processing frame
        },
    },
    {
        {
            STATIC_AUDIO_SIGNALPROCESSINGMODE_DEFAULT,          // constraint for default processing mode
            0,                                                  // NA samples per processing frame
            10 * HNSTIME_PER_MILLISECOND,                       // 100000 hns (10ms) per processing frame
        },
        {
            STATIC_AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS,   // constraint for movie communications mode
            0,                                                  // NA samples per processing frame
            10 * HNSTIME_PER_MILLISECOND,                       // 100000 hns (10ms) per processing frame
        },
        {
            STATIC_AUDIO_SIGNALPROCESSINGMODE_MEDIA,            // constraint for default media mode
            0,                                                  // NA samples per processing frame
            10 * HNSTIME_PER_MILLISECOND,                       // 100000 hns (10ms) per processing frame
        },
        {
            STATIC_AUDIO_SIGNALPROCESSINGMODE_MOVIE,            // constraint for movie movie mode
            0,                                                  // NA samples per processing frame
            10 * HNSTIME_PER_MILLISECOND,                       // 100000 hns (10ms) per processing frame
        },
    }
};
```

A DSP_DEVPROPERTY structure is used to store the constraints.

```cpp
typedef struct _DSP_DEVPROPERTY {
    const DEVPROPKEY   *PropertyKey;
    DEVPROPTYPE Type;
    ULONG BufferSize;
    __field_bcount_opt(BufferSize) PVOID Buffer;
} DSP_DEVPROPERTY, PDSP_DEVPROPERTY;
```

And an array of those structures is created.

```cpp
const DSP_DEVPROPERTY DspR_InterfaceProperties[] =
{
    {
        &DEVPKEY_KsAudio_PacketSize_Constraints2,       // Key
        DEVPROP_TYPE_BINARY,                            // Type
        sizeof(DspR_RtPacketSizeConstraints),           // BufferSize
        &DspR_RtPacketSizeConstraints,                  // Buffer
    },
};
```

Later in the EvtCircuitCompositeCircuitInitialize function, the AddPropertyToCircuitInterface helper function is used to add the array of interface properties to the circuit.

```cpp
   // Set RT buffer constraints.
    //
    status = AddPropertyToCircuitInterface(Circuit, ARRAYSIZE(DspC_InterfaceProperties), DspC_InterfaceProperties);
```

The AddPropertyToCircuitInterface helper function takes the [AcxCircuitGetSymbolicLinkName](/windows-hardware/drivers/ddi/acxcircuit/nf-acxcircuit-acxcircuitgetsymboliclinkname) for the circuit and then calls [IoGetDeviceInterfaceAlias](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfacealias) to locate the audio interface used by the circuit.

Then the SetDeviceInterfacePropertyDataMultiple function calls [IoSetDeviceInterfacePropertyData function](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacepropertydata) to modify the current value of the device interface property - the KS audio property values on the audio interface for the ACXCIRCUIT.

```cpp
PAGED_CODE_SEG
NTSTATUS AddPropertyToCircuitInterface(
    _In_ ACXCIRCUIT                                         Circuit,
    _In_ ULONG                                              PropertyCount,
    _In_reads_opt_(PropertyCount) const DSP_DEVPROPERTY   * Properties
)
{
    PAGED_CODE();

    NTSTATUS        status      = STATUS_UNSUCCESSFUL;
    UNICODE_STRING  acxLink     = {0};
    UNICODE_STRING  audioLink   = {0};
    WDFSTRING       wdfLink     = AcxCircuitGetSymbolicLinkName(Circuit);
    bool            freeStr     = false;

    // Get the underline unicode string.
    WdfStringGetUnicodeString(wdfLink, &acxLink);

    // Make sure there is a string.
    if (!acxLink.Length || !acxLink.Buffer)
    {
        status = STATUS_INVALID_DEVICE_STATE;
        DrvLogError(g_BthLeVDspLog, FLAG_INIT,
            L"AcxCircuitGetSymbolicLinkName failed, Circuit: %p, %!STATUS!",
            Circuit, status);
        goto exit;
    }

    // Get the audio interface.
    status = IoGetDeviceInterfaceAlias(&acxLink, &KSCATEGORY_AUDIO, &audioLink);
    if (!NT_SUCCESS(status))
    {
        DrvLogError(g_BthLeVDspLog, FLAG_INIT,
            L"IoGetDeviceInterfaceAlias failed, Circuit: %p, symbolic link name: %wZ, %!STATUS!",
            Circuit, &acxLink, status);
        goto exit;
    }

    freeStr = true;

    // Set specified properties on the audio interface for the ACXCIRCUIT.
    status = SetDeviceInterfacePropertyDataMultiple(&audioLink, PropertyCount, Properties);
    if (!NT_SUCCESS(status))
    {
        DrvLogError(g_BthLeVDspLog, FLAG_INIT,
            L"SetDeviceInterfacePropertyDataMultiple failed, Circuit: %p, symbolic link name: %wZ, %!STATUS!",
            Circuit, &audioLink, status);
        goto exit;
    }

    status = STATUS_SUCCESS;

exit:

    if (freeStr)
    {
        RtlFreeUnicodeString(&audioLink);
        freeStr = false;
    }

    return status;
}
```

### Stream state changes

When a stream state change occurs, each stream object in the Endpoint Audio Path for the stream receives a notification event from the ACX framework. The order in which this happens depends on the state change and the flow of the stream.

- For render streams going from a less-active state to a more-active state, the streaming circuit (which registered the SINK) receives the event first. Once the circuit handles the event, the next circuit in the Endpoint Audio Path receives the event.
- For render streams going from a more-active state to a less-active state, the streaming circuit receives the event last.

- For Capture streams going from a less-active state to a more-active state, the streaming circuit receives the event last.
- For Capture streams going from a more-active state to a less-active state, the streaming circuit receives the event first.

The ordering is the default provided by the ACX framework. A driver can request the opposite behavior by setting AcxStreamBridgeInvertChangeStateSequence (defined in [ACX_STREAM_BRIDGE_CONFIG_FLAGS](/windows-hardware/drivers/ddi/acxstreams/ne-acxstreams-acx_stream_bridge_config_flags)) when creating the ACXSTREAMBRIDGE that the driver adds to the streaming circuit.

### Streaming audio data

After you create the stream and allocate the appropriate buffers, the stream is in the Pause state and waits for the stream to start. When the client puts the stream into Play state, the ACX framework calls all ACXSTREAM objects associated with the stream to indicate the stream state is in Play. The ACXPIN is then placed in the Play state, and data starts flowing.

#### Rendering audio data

After you create the stream and allocate the resources, the application calls Start on the stream to start playback. The application should call GetBuffer/ReleaseBuffer before starting the stream to make sure the first packet that starts playing has valid audio data.

The client starts by prerolling a buffer. When the client calls ReleaseBuffer, this translates to a call in AudioKSE that calls into the ACX layer, which calls [EvtAcxStreamSetRenderPacket](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_set_render_packet) on the active ACXSTREAM. The property includes the packet index (zero-based) and, if appropriate, an EOS flag with the byte offset of the end of the stream in the current packet.

After the streaming circuit finishes with a packet, it triggers the buffer complete notification that releases clients waiting to fill the next packet with render audio data.

The Timer Driven streaming mode is supported and is indicated by using a PacketCount value of 1 when you call the driver's [EvtAcxStreamAllocateRtPackets](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_allocate_rtpackets) callback.

#### Capturing audio data

When the stream runs, the source circuit fills the capture packet with audio data. After the first packet is filled, the source circuit releases the packet to the ACX framework. At this point, the ACX framework signals the stream notification event.

After the stream notification has been signaled, the client can send [KSPROPERTY_RTAUDIO_GETREADPACKET](./ksproperty-rtaudio-getreadpacket.md) to get the index (zero-based) of the packet that's finished capturing. When the client sends GETCAPTUREPACKET, the driver can assume all previous packets are processed and are available for filling.

For Burst capture, the source circuit can release a new packet to the ACX framework as soon as GETREADPACKET has been called.

The client can also use [KSPROPERTY_RTAUDIO_PACKETVREGISTER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_packetvregister_property) to get a pointer to the RTAUDIO_PACKETVREGISTER structure for the stream. The ACX framework updates this structure before signaling packet complete.

##### Legacy KS kernel streaming behavior

Sometimes, such as when a driver implements burst capture (like a keyword spotter), you need to use the legacy kernel streaming packet handling behavior instead of PacketVRegister. To use the previous packet-based behavior, the driver returns STATUS_NOT_SUPPORTED for [KSPROPERTY_RTAUDIO_PACKETVREGISTER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_packetvregister_property).

The following sample shows how to do this in the [AcxStreamInitAssignAcxRequestPreprocessCallback](/windows-hardware/drivers/ddi/acxstreams/nf-acxstreams-acxstreaminitassignacxrequestpreprocesscallback) for an ACXSTREAM. For more information, see [AcxStreamDispatchAcxRequest](/windows-hardware/drivers/ddi/acxstreams/nf-acxstreams-acxstreamdispatchacxrequest).

```cpp
Circuit_EvtStreamRequestPreprocess(
    _In_  ACXOBJECT  Object,
    _In_  ACXCONTEXT DriverContext,
    _In_  WDFREQUEST Request)
{
    ACX_REQUEST_PARAMETERS params;
    PCIRCUIT_STREAM_CONTEXT streamCtx;

    streamCtx = GetCircuitStreamContext(Object);
    // The driver would define the pin type to track which pin is the keyword pin.
    // The driver would add this to the driver-defined context when the stream is created.
    // The driver would use AcxStreamInitAssignAcxRequestPreprocessCallback to set
    // the Circuit_EvtStreamRequestPreprocess callback for the stream.
    if (streamCtx && streamCtx->PinType == CapturePinTypeKeyword)
    {
        if (IsEqualGUID(params.Parameters.Property.Set, KSPROPSETID_RtAudio) &&
            params.Parameters.Property.Id == KSPROPERTY_RTAUDIO_PACKETVREGISTER)
        {
            status = STATUS_NOT_SUPPORTED;
            outDataCb = 0;

            WdfRequestCompleteWithInformation(Request, status, outDataCb);
            return;
        }
    }

    (VOID)AcxStreamDispatchAcxRequest((ACXSTREAM)Object, Request);
}
```

#### Stream position

The ACX framework calls the [EvtAcxStreamGetPresentationPosition](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_get_presentation_position)   callback to get the current stream position. The current stream position includes the PlayOffset and the WriteOffset.

The WaveRT streaming model allows the audio driver to expose an HW position register to the client. The ACX streaming model won't support exposing any HW registers since these would prevent a rebalance from happening.

Each time the streaming circuit completes a packet, it calls [AcxRtStreamNotifyPacketComplete](/windows-hardware/drivers/ddi/acxstreams/nf-acxstreams-acxrtstreamnotifypacketcomplete) with the zero-based packet index and the QPC value taken as close to packet completion as possible (for example, the Interrupt Service Routine can calculate the QPC value). Clients can get this information through [KSPROPERTY_RTAUDIO_PACKETVREGISTER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_packetvregister_property), which returns a pointer to a structure that contains the CompletedPacketCount, the CompletedPacketQPC, and a value that combines the two (so the client can check that the CompletedPacketCount and CompletedPacketQPC are from the same packet).

#### Stream state transitions

After a stream has been created, ACX will transition the stream to different states using the following callbacks:

- [EvtAcxStreamPrepareHardware](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_prepare_hardware) transitions the stream from the AcxStreamStateStop state to the AcxStreamStatePause state. The driver should reserve required hardware such as DMA Engines when it receives EvtAcxStreamPrepareHardware.
- [EvtAcxStreamRun](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_run) transitions the stream from the AcxStreamStatePause state to the AcxStreamStateRun state.
- [EvtAcxStreamPause](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_pause) transitions the stream from the AcxStreamStateRun state to the AcxStreamStatePause state.
- [EvtAcxStreamReleaseHardware](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_release_hardware) transitions the stream from the AcxStreamStatePause state to the AcxStreamStateStop state. The driver should release required hardware such as DMA engines when it receives EvtAcxStreamReleaseHardware.

The stream might receive the EvtAcxStreamPrepareHardware callback after it receives the EvtAcxStreamReleaseHardware callback. This transitions the stream back to the AcxStreamStatePause state.

Packet allocation with EvtAcxStreamAllocateRtPackets normally happens before the first call to EvtAcxStreamPrepareHardware. The allocated packets are normally freed with EvtAcxStreamFreeRtPackets after the last call to EvtAcxStreamReleaseHardware. This ordering isn't guaranteed.

The AcxStreamStateAcquire state isn't used. ACX removes the need for the driver to have the acquire state because this state is implicit with the prepare hardware ([EvtAcxStreamPrepareHardware](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_prepare_hardware)) and release hardware ([EvtAcxStreamReleaseHardware](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_release_hardware)) callbacks.

### Large buffer streams and offload engine support

ACX uses the ACXAUDIOENGINE element to designate an ACXPIN that will handle Offload stream creation and the different elements required for offload stream volume, mute, and peak meter state. This is similar to the existing audio engine node in WaveRT drivers.

## Stream close process

When the client closes the stream, the driver receives EvtAcxStreamPause and EvtAcxStreamReleaseHardware before the ACXSTREAM object is deleted by the ACX framework. The driver can supply the standard WDF EvtCleanupCallback entry in the [WDF_OBJECT_ATTRIBUTES structure](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) when calling AcxStreamCreate to perform final cleanup for the ACXSTREAM. WDF calls EvtCleanupCallback when the framework tries to delete the object. Don't use EvtDestroyCallback, which is called only after all references to the object are released, which is indeterminate.

The driver should clean up system memory resources associated with the ACXSTREAM object in EvtCleanupCallback if the resources aren't already cleaned up in EvtAcxStreamReleaseHardware.

The driver shouldn't clean up resources that support the stream until the client requests it.

The AcxStreamStateAcquire state isn't used. ACX removes the need for the driver to have the acquire state because this state is implicit with the prepare hardware (EvtAcxStreamPrepareHardware) and release hardware (EvtAcxStreamReleaseHardware) callbacks.

### Stream surprise removal and invalidation

If the driver determines the stream is invalid (for example, the jack is unplugged), the circuit shuts down all streams.

### Stream memory cleanup

The disposal of the stream's resources can be done in the driver's stream context cleanup (not destroy). Don't put the disposal of anything that's shared in an object's context destroy callback. This guidance applies to all ACX objects.

The destroy callback is invoked after the last reference is gone, which is indeterminate.

In general, the stream's cleanup callback is called when the handle is closed. One exception is when the driver creates the stream in its callback. If ACX fails to add this stream to its stream bridge just before returning from the stream create operation, the stream is canceled asynchronously, and the current thread returns an error to the create stream client. The stream shouldn't have any memory allocations at this point. For more information, see [EVT_ACX_STREAM_RELEASE_HARDWARE callback](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_release_hardware).

### Stream memory clean-up sequence

The stream buffer is a system resource and you should release it only when the user mode client closes the stream's handle. The buffer (which is different from the device's hardware resources) has the same lifetime as the stream's handle. When the client closes the handle, ACX invokes the stream object's cleanup callback, and then the stream object's delete callback when the reference count on the object goes to zero.

It's possible for ACX to defer a STREAM obj deletion to a work-item when the driver created a stream-obj and then it failed the create-stream callback. To prevent a deadlock with a shutdown WDF thread, ACX defers the deletion to a different thread. To avoid any possible side-effects of this behavior (deferred release of resources), the driver can release the allocated stream resources before it returns an error from the stream-create.

The driver must free the audio buffers when ACX invokes the [EVT_ACX_STREAM_FREE_RTPACKETS callback](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_free_rtpackets). This callback occurs when the user closes the stream handles.

Because RT buffers are mapped in user mode, the buffer lifetime is the same as the handle lifetime. The driver shouldn't release or free the audio buffers before ACX invokes this callback.

[EVT_ACX_STREAM_FREE_RTPACKETS callback](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_free_rtpackets) should be call after [EVT_ACX_STREAM_RELEASE_HARDWARE callback](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_release_hardware) and end before EvtDeviceReleaseHardware.

This callback might happen after the driver processes the WDF release hardware callback because the user mode client can hold on to its handles for a long time. The driver shouldn't wait for these handles to go away. This action creates a 0x9f DRIVER_POWER_STATE_FAILURE bug check. See [EVT_WDF_DEVICE_RELEASE_HARDWARE callback function](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) for more information.

This EvtDeviceReleaseHardware code from the sample ACX driver shows an example of calling [AcxDeviceRemoveCircuit](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceremovecircuit) and then releasing the streaming hardware memory.

```cpp
    RETURN_NTSTATUS_IF_FAILED(AcxDeviceRemoveCircuit(Device, devCtx->Render));
    RETURN_NTSTATUS_IF_FAILED(AcxDeviceRemoveCircuit(Device, devCtx->Capture));

    // NOTE: Release streaming h/w resources here.

    CSaveData::DestroyWorkItems();
    CWaveReader::DestroyWorkItems();
```

In summary:

- WDF device release hardware: release device's hardware resources.
- [AcxStreamFreeRtPackets](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_free_rtpackets): release or free the audio buffer associated with the handle.

For more information about managing WDF and circuit objects, see [ACX WDF Driver Lifetime Management](acx-wdf-driver-lifetime-management.md).

## Streaming DDIs

### Streaming structures

#### [ACX_RTPACKET structure](/windows-hardware/drivers/ddi/acxstreams/ns-acxstreams-acx_rtpacket)

This structure represents a single allocated packet. The PacketBuffer can be a WDFMEMORY handle, an MDL, or a Buffer. It has an associated initialization function, [ACX_RTPACKET_INIT](/windows-hardware/drivers/ddi/acxstreams/nf-acxstreams-acx_rtpacket_init).

#### [ACX_STREAM_CALLBACKS](/windows-hardware/drivers/ddi/acxstreams/ns-acxstreams-acx_stream_callbacks)

This structure identifies the driver callbacks for streaming to the ACX framework. This structure is a part of the [ACX_PIN_CONFIG structure](/windows-hardware/drivers/ddi/acxpin/ns-acxpin-acx_pin_config).

### Streaming callbacks

#### EvtAcxStreamAllocateRtPackets

The [EvtAcxStreamAllocateRtPackets](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_allocate_rtpackets) event tells the driver to allocate RtPackets for streaming. An AcxRtStream receives PacketCount = 2 for event driven streaming or PacketCount = 1 for timer based streaming. If the driver uses a single buffer for both packets, the second RtPacketBuffer should have a [WDF_MEMORY_DESCRIPTOR](/windows-hardware/drivers/ddi/wdfmemory/ns-wdfmemory-_wdf_memory_descriptor) with Type = WdfMemoryDescriptorTypeInvalid with an RtPacketOffset that aligns with the end of the first packet (packet[2].RtPacketOffset = packet[1].RtPacketOffset+packet[1].RtPacketSize).

#### EvtAcxStreamFreeRtPackets

The [EvtAcxStreamFreeRtPackets](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_free_rtpackets) event tells the driver to free the RtPackets that were allocated in a previous call to EvtAcxStreamAllocateRtPackets. The same packets from that call are included.

#### EvtAcxStreamGetHwLatency

The [EvtAcxStreamGetHwLatency](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_get_hw_latency) event tells the driver to provide stream latency for the specific circuit of this stream (overall latency will be a sum of the latency of the different circuits). The FifoSize is in bytes and the Delay is in 100-nanosecond units.

#### EvtAcxStreamSetRenderPacket

The [EvtAcxStreamSetRenderPacket](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_set_render_packet) event tells the driver which packet was just released by the client. If there are no glitches, this packet should be (CurrentRenderPacket + 1), where CurrentRenderPacket is the packet the driver is currently streaming from.

Flags can be 0 or `KSSTREAM_HEADER_OPTIONSF_ENDOFSTREAM = 0x200`, indicating the Packet is the last packet in the stream, and EosPacketLength is a valid length in bytes for the packet. For more information, see *OptionsFlags* in [KSSTREAM_HEADER structure (ks.h)](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header).

The driver continues to increase the CurrentRenderPacket as packets are rendered instead of changing its CurrentRenderPacket to match this value.

#### EvtAcxStreamGetCurrentPacket

The [EvtAcxStreamGetCurrentPacket](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_get_current_packet) tells the driver to indicate which packet (zero-based) is currently being rendered to the hardware or is currently being filled by the capture hardware.

#### EvtAcxStreamGetCapturePacket

The [EvtAcxStreamGetCapturePacket](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_get_capture_packet) tells the driver to indicate which packet (zero-based) was filled most recently, including the QPC value at the time the driver started filling the packet.

#### EvtAcxStreamGetPresentationPosition

The [EvtAcxStreamGetPresentationPosition](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_get_presentation_position) tells the driver to indicate the current position along with the QPC value at the time the current position was calculated.

### STREAM STATE EVENTS

The following APIs manage the streaming state for an ACXSTREAM.

- [EVT_ACX_STREAM_PREPARE_HARDWARE](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_prepare_hardware)
- [EVT_ACX_STREAM_RELEASE_HARDWARE](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_release_hardware)
- [EVT_ACX_STREAM_RUN](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_run)
- [EVT_ACX_STREAM_PAUSE](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_pause)

### Streaming ACX APIs

#### [AcxStreamCreate](/windows-hardware/drivers/ddi/acxstreams/nf-acxstreams-acxstreamcreate)

AcxStreamCreate creates an ACX Stream that can be used to control streaming behavior.

#### [AcxRtStreamCreate](/windows-hardware/drivers/ddi/acxstreams/nf-acxstreams-acxrtstreamcreate)

AcxRtStreamCreate creates an ACX Stream that can be used to control streaming behavior and handle packet allocation and communicate streaming state.

#### [AcxRtStreamNotifyPacketComplete](/windows-hardware/drivers/ddi/acxstreams/nf-acxstreams-acxrtstreamnotifypacketcomplete)

The driver calls this ACX API when a packet has completed. The packet completion time and the zero-based Packet index are included to improve client performance. The ACX framework sets any notification events associated with the stream.

## See also

- [ACX audio class extensions overview](acx-audio-class-extensions-overview.md)
- [ACX reference documentation](acx-reference.md)
- [Summary of ACX Objects](acx-summary-of-objects.md)
