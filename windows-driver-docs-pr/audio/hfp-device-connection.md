---
title: HFP device connection
description: This article discusses how the audio system determines and handles connection status information for a Bluetooth hands-free profile (HFP) device.
ms.date: 07/27/2023
---

# HFP device connection

This article discusses how the audio system determines and handles connection status information for a Bluetooth hands-free profile (HFP) device.

The audio driver must support [**KSPROPERTY_JACK_DESCRIPTION**](./ksproperty-jack-description.md) and maintain an *IsConnected* field in the filter factory context. The driver uses this value when handling the **KSPROPERTY_JACK_DESCRIPTION** property.

When [**IOCTL_BTHHFP_DEVICE_GET_CONNECTION_STATUS_UPDATE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_connection_status_update) completes successfully, the audio driver updates *IsConnected* with the new connection status. If the status has changed, the audio driver raises the [**KSEVENT_PINCAPS_JACKINFOCHANGE**](./ksevent-pincaps-jackinfochange.md) event, causing the audio system to reevaluate the connection state. The audio driver then calls another instance of **IOCTL_BTHHFP_DEVICE_GET_CONNECTION_STATUS_UPDATE** to receive the next status change. If an earlier status change request is still pending, this second call fails, and the audio driver doesn't update its connection status and doesn't make another request for status change information.

As discussed in [Kernel streaming considerations](kernel-streaming-considerations.md), the audio driver must support [**KSPROPERTY_ONESHOT_RECONNECT**](./ksproperty-oneshot-reconnect.md) and [**KSPROPERTY_ONESHOT_DISCONNECT**](./ksproperty-oneshot-disconnect.md). The handlers for these properties must send REQUESTCONNECT and REQUESTDISCONNECT IOCTLs, respectively, to the HFP driver. These IOCTLs complete quickly, and the audio driver needs to be ready to respond to the returned results.

This article also covers other Bluetooth audio device connection-related factors that the audio driver developer must be aware of.

## Stream channel

The stream channel represents the audio driver's allocation of over-the-air bandwidth. For the most part, this is the SCO channel. However, some of the details of managing the SCO channel status are handled entirely within the HFP driver. This includes for example remote disconnects which may be due to call scenarios where the HF initiates an audio transfer to the AG (with the PC playing the role of the AG in this case).

## Audio filter pin states

The audio driver implements KS pin state handlers for two KS pins. The SCO stream channel is required for either of these pins to transfer data over the air. When either of these pins transitions to KSSTATE_ACQUIRE, the audio driver opens the channel by sending [**IOCTL_BTHHFP_STREAM_OPEN**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_stream_open) to the HFP driver. This asynchronous call may take several seconds to complete. The audio driver doesn't need to implement its own timeout mechanism and should wait for the IOCTL to complete before completing the transition to KSSTATE_ACQUIRE.

When both KS pins transition to KSSTATE_STOP, the audio driver sends [**IOCTL_BTHHFP_STREAM_CLOSE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_stream_close) to the HFP driver, which completes quickly.

To determine when to send **IOCTL_BTHHFP_STREAM_OPEN** and **IOCTL_BTHHFP_STREAM_CLOSE**, the audio driver can use a simple reference counting mechanism to track the number of pins that require the SCO stream channel. The audio driver would open and close the SCO stream channel when the reference count changes from 0 to 1.

On **IOCTL_BTHHFP_STREAM_OPEN**, the HFP driver requests an SCO channel, if one is not already open, and completes the request with the results from the SCO request. On **IOCTL_BTHHFP_STREAM_CLOSE**, the HFP driver requests a SCO channel disconnect, if one is open.

## Remote SCO connect and disconnect

On a remote SCO disconnect, if the stream channel is closed, the HFP driver does nothing. If the stream channel is opened, the HFP driver starts a reconnect timer. When the timer expires, if SCO is still disconnected and the stream channel is still open, the driver requests a SCO channel. Note that no audio data transfers over the air while SCO is disconnected, so there will be a gap in audio during this period. If the SCO request fails, the HFP driver signals a stream channel status change to the audio driver by completing any invoking [**IOCTL_BTHHFP_STREAM_GET_STATUS_UPDATE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_stream_get_status_update). This should be rare, as remote SCO disconnect is normally associated with the HF device requesting transfer of call audio to the audio gateway. The audio driver should consider this a mid-stream error condition.

This procedure allows time for a VoIP application to receive an audio transfer callback from the CallButtons API and cleanly release its audio resources on the HFP endpoint, instead of causing streaming errors.

On a remote SCO connect, if the stream channel is open, the driver simply accepts the connection. If the stream channel is closed, the HFP driver accepts the connection and starts a disconnect timer. When the disconnect timer expires, if SCO is still connected and the stream channel is still closed, the driver breaks the SCO connection.

This procedure allows time for a VoIP application to receive an audio transfer callback from the CallButtons API and establish audio resources on the HFP endpoint, without prematurely rejecting or closing the SCO connection.

## Related topics

- [Theory of Bluetooth bypass audio streaming](theory-of-operation.md)
- [Bluetooth Low Energy (LE) Audio](../bluetooth/bluetooth-low-energy-audio.md)
