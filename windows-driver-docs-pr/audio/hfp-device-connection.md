---
title: HFP Device Connection
description: The HFP Device connection topic discusses how the audio system determines and handles connection status information for a Bluetooth hands-free profile (HFP) device.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HFP Device Connection


The HFP Device connection topic discusses how the audio system determines and handles connection status information for a Bluetooth hands-free profile (HFP) device.

As required for all audio drivers, the audio driver must support [**KSPROPERTY\_JACK\_DESCRIPTION**](./ksproperty-jack-description.md). The audio driver maintains an *IsConnected* field in the filter factory context. The audio driver uses this value when handling the **KSPROPERTY\_JACK\_DESCRIPTION** property.

When [**IOCTL\_BTHHFP\_DEVICE\_GET\_CONNECTION\_STATUS\_UPDATE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_connection_status_update) completes successfully, then the audio driver updates *IsConnected* with the new connection status. If the status has changed, the audio driver raises the [**KSEVENT\_PINCAPS\_JACKINFOCHANGE**](./ksevent-pincaps-jackinfochange.md) event, which causes the audio system to reevaluate the connection state. The audio driver then calls another instance of **IOCTL\_BTHHFP\_DEVICE\_GET\_CONNECTION\_STATUS\_UPDATE** to receive the next status change. If there is an earlier status change request that is still pending, then this second call will fail, the audio driver doesn't update its connection status, and doesn't make another request for status change information.

As discussed in [Kernel Streaming Considerations](kernel-streaming-considerations.md), the audio driver must support [**KSPROPERTY\_ONESHOT\_RECONNECT**](./ksproperty-oneshot-reconnect.md) and [**KSPROPERTY\_ONESHOT\_DISCONNECT**](./ksproperty-oneshot-disconnect.md), and the handlers for these properties must send REQUESTCONNECT and REQUESTDISCONNECT IOCTLs respectively, to the HFP driver. These IOCTLs complete quickly, and the audio driver needs to be ready to respond to the returned results.

Here are some other Bluetooth audio device connection-related factors that the audio driver developer must be aware of.

## <span id="Stream_channel"></span><span id="stream_channel"></span><span id="STREAM_CHANNEL"></span>Stream channel


The Stream Channel represents the audio driver’s allocation of over-the-air bandwidth. For the most part, this is the SCO channel. However, some of the details of managing the SCO channel status are handled entirely within the HFP driver. This includes for example remote disconnects which may be due to call scenarios where the HF initiates an audio transfer to the AG (where the PC plays the role of the AG in this case).

## <span id="Audio_filter_pin_states"></span><span id="audio_filter_pin_states"></span><span id="AUDIO_FILTER_PIN_STATES"></span>Audio filter pin states


The audio driver implements a KS pin state handlers (similar to AVStrMiniPinSetDeviceState) for two KS pins. The SCO stream channel is required for either of these pins to transfer data over the air. When either of these pins transitions to KSSTATE\_ACQUIRE, the audio driver opens the channel by sending [**IOCTL\_BTHHFP\_STREAM\_OPEN**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_stream_open) to the HFP driver. This is an asynchronous call and may take several seconds to complete. The audio driver does not need to implement its own timeout mechanism and should wait for the IOCTL to complete before completing the transition to KSSTATE\_ACQUIRE.

When both KS pins transition to KSSTATE\_STOP, the audio driver sends [**IOCTL\_BTHHFP\_STREAM\_CLOSE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_stream_close) to the HFP driver. This completes quickly.

To determine when to send **IOCTL\_BTHHFP\_STREAM\_OPEN** and **IOCTL\_BTHHFP\_STREAM\_CLOSE**, the audio driver can use a simple reference counting mechanism to track the number of pins that require the SCO stream channel. The audio driver would open and close the SCO stream channel when the reference count changes from 0 to 1.

On **IOCTL\_BTHHFP\_STREAM\_OPEN**, the HFP driver requests an SCO channel, if one is not already open, and completes the request with the results from the SCO request. On **IOCTL\_BTHHFP\_STREAM\_CLOSE** the HFP driver requests a SCO channel disconnect, if one is open.

## <span id="Remote_SCO_connect_and_disconnect"></span><span id="remote_sco_connect_and_disconnect"></span><span id="REMOTE_SCO_CONNECT_AND_DISCONNECT"></span>Remote SCO connect and disconnect


On a remote SCO disconnect, if the Stream Channel is closed, the HFP driver does nothing. If the Stream Channel is opened the HFP driver will start a reconnect timer. When the timer expires, if SCO is still disconnected and Stream Channel is still open then the driver will request a SCO channel. Note that no audio data transfers over the air while SCO is disconnected so there will be a gap in audio during this period. If the SCO request fails then the HFP driver will signal a Stream Channel status change to the audio driver by completing any invoking [**IOCTL\_BTHHFP\_STREAM\_GET\_STATUS\_UPDATE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_stream_get_status_update). This should be rare, as remote SCO disconnect is normally associated with the HF device requesting transfer of call audio to the audio gateway. The audio driver should consider this a mid-stream error condition.

This procedure allows time for a VoIP application to receive an audio transfer callback from the CallButtons API and cleanly release its audio resources on the HFP endpoint, instead of causing streaming errors.

On a remote SCO connect, if the Stream Channel is open the driver simply accepts the connection. If the Stream Channel is closed, then the HFP driver accepts the connection and also starts a disconnect timer. When the disconnect timer expires, if SCO is still connected and the Stream channel is still closed, then the driver will break the SCO connection.

This procedure allows time for a VoIP application to receive an audio transfer callback from the CallButtons API and establish audio resources on the HFP endpoint, without prematurely rejecting or closing the SCO connection.

## <span id="related_topics"></span>Related topics
[Theory of Operation](theory-of-operation.md)
