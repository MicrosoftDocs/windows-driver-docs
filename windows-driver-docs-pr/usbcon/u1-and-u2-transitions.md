---
Description: This topic first describes the initial setup that is done by the software to enable U1 and U2 transitions, and then describes how these transitions occur in the hardware.
title: U1 and U2 transitions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# U1 and U2 transitions


This topic first describes the initial setup that is done by the software to enable U1 and U2 transitions, and then describes how these transitions occur in the hardware.

## Initial setup by software


This topic describes how software enumerates a device.

For U1 or U2 transitions to occur, software performs the following steps during the enumeration of a device.

1.  Software exchanges U1 or U2 exit latency information with the device during the enumeration process. As the first part of this exchange, the device-specific latencies are filled in by the device in bU1DevExitLat and wU2DevExitLat fields of the SuperSpeed USB device capability (defined in Section 9.6.2.2 of the USB 3.0 specification). As the second part of the exchange, the host informs the device about overall exit latencies for the device by sending a SET\_SEL control transfer, as per section 9.4.12 of the USB 3.0 specification. The latency information includes the latencies that are associated with upstream links and controller.
2.  For the DS port to which the device is attached, the software configures two values: PORT\_U1\_TIMEOUT and PORT\_U2\_TIMEOUT. While deciding these values, the software takes into consideration the characteristics of the device (such as the type of endpoints) and the latencies that are associated with bringing the device back from U1 or U2 to U0. The following table describes the timeout values.

    **Table 1. PORT\_U1\_TIMEOUT and PORT\_U2\_TIMEOUT values**

    | Value   | Description                                                                                                                                                                                                                  |
    |---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | 01H-FEH | DS port must initiate transitions after a period of inactivity. The exact period is derived from the timeout value. The port must accept transitions that are initiated by the link partner unless there is pending traffic. |
    | FFH     | DS port must not initiate transitions but must accept transitions that are initiated by the link partner unless there is pending traffic.                                                                                    |
    | 0       | DS port must not initiate transitions and must not accept transitions that are initiated by the link partner.                                                                                                                |

     

3.  If the PORT\_U2\_TIMEOUT value is between 01H-FEH, there is an additional step that occurs in the hardware as a result of step 2. The DS port informs its link partner about that value. The importance of this step is described in "Direct Transition from U1 to U2".
4.  For every device or hub, the software configures two values: U1\_ENABLE and U2\_ENABLE by sending SET\_FEATURE (U1\_ENABLE/U2\_ENABLE) control transfers. The following table describes those values.

    **Table 2. U1\_ENABLE and U2\_ENABLE values**

    | Value    | Description                                                                                                                       |
    |----------|-----------------------------------------------------------------------------------------------------------------------------------|
    | Enabled  | US port can initiate transitions and accept transitions that are initiated by the link partner if permitted by the device policy. |
    | Disabled | US port must not initiate transitions but can accept transitions that are initiated by the link partner.                          |

     
## Hardware transitions


This topic describes hardware transitions to U1 and U2.

After the initial setup by the software, the hardware transitions to U1 and u2 autonomously without further intervention from the software.

A link is in working state (U0) as long as it is actively transferring packets. The link is considered to be idle when no packets are being transmitted. In idle state, any link partner can initiate a transition to U1 or U2. The other link partner can choose to accept or reject the transition. If the link partner accepts the transition, the link moves to that U state. If it rejects the transition, the link remains in U0.

### DS port-initiated transitions


A DS port implements a timer mechanism that tracks inactivity on the port. The timer gets reset whenever that port sends or receives a packet. The timer also gets reset when the software programs new timeout values. If the software has programmed the DS port to initiate only U1 or U2 transitions, the DS port starts the timer when the link first enters U0. The timer value is based on the U1 (or U2) timeout value that was programmed by the software. If the link is in U0 when the timer expires, the DS port initiates the U1 (or U2) transition.

The US port link partner can choose to reject the transition if the device knows that the transition can affect the device’s ability to meet the performance or latency requirements. For example, if the device has sent an ERDY notification and is expecting a transfer request from the host, then the device might reject U1 or U2 state transitions in the meantime.

If the software has programmed the DS port to initiate both U1 and U2 transitions, the DS port first initiates the U1 transition based on the timer (described earlier in this section). The transition from U1 to U2 is described in this topic in **Direct Transition from U1 to U2**.

If a link is in U1 or U2, a DS port can bring the port back into U0 anytime it receives traffic for the device attached to the port.

### Device (US port)-initiated transitions


A device can choose to initiate a transition from U0 to U1 or U0 to U2, as long as the capability is enabled by the software. If the device transitions a link to U1, the link can transition to U2 directly based on the U2 timer of the DS port (described in "Direct Transition from U1 to U2". However, if the U2 timer is not set, the device cannot initiate a direct transition from U1 to U2 on its own. In that case, the device must bring the link back to U0 before initiating the transition to U2.

While deciding when to initiate those transitions, a device should consider its exit latencies and performance requirements. To help the device make informed decisions about how aggressively it can initiate the transitions, software also provides various exit latency values as described earlier in this document in "Initial setup by software".

If the link is in U1 or U2, a US port can bring the port back into U0 at any time. Typically, the US port initiates the transition to U0 when it knows that it is about to send any packets to the host or if it is anticipating a packet from the host.

### Advantages of device-initiated LPM


The timer values that are set by the software for DS ports are based on general heuristics. While choosing those timer values, software ensures that the device performance is not impaired. In order to maintain the device’s performance, software cannot choose values that are too small. Because DS port- initiated transitions are based on the timers and do not take into account the exact state of the device, this mechanism cannot take advantage of all the possible opportunities of sending the device to U1 or U2 state.

The device, on the other hand, has accurate knowledge about its characteristics and current state. Therefore, it can make an intelligent guess about when the next transfer is going to take place. Based on that information, the device can (and should) choose to actively initiate these transitions without significantly affecting the performance.

For example, the device has sent a NRDY notification on one of its endpoints and knows that there will not be traffic for a while. In that case, the device can immediately initiate a transition to U1 or U2. Just before sending the ERDY notification, the device can bring the link back to U0 in preparation for sending that data. For details about this process, see section C.3.1 of the USB 3.0 specification.

## Direct transition from U1 to U2


If the link is in U1, it is possible that the link can directly transition to U2 without entering U0 in between. That can occur regardless of which link partner initiated the transition to U1. However, the U1 to U2 transition can occur only if the U2 timeout on the DS port of the link is set to a value between 01H-FEH.

The "Initial setup by software" section describes an additional step that allows the DS port to communicate the timeout value to its link partner. After the link has entered U1, both link partners start a timer using the timeout value set according to the U2 timeout value of the DS port. If the timer is not reset due to traffic and expires, both link partners silently transition to U2 without any explicit communication between them.

### Transitions from U1 or U2 to U3


Transitions to U1 or U2 are initiated in the hardware autonomously but the transition to U3 is initiated by the software. Because U3 transition is initiated only after a period of inactivity, it is quite likely that the link was in U1 or U2 (rather than U0) before the transition.

The USB 3.0 specification does not define direct transitions from U1 or U2 to U3. The parent hub or controller is responsible for automatically transitioning the link to U0 and then transitioning it to U3.

### U1 or U2 transitions for hubs


The USB 3.0 specification provides specific guidelines for hubs about when to initiate U state transitions on its US port. If all the DS ports are in link state U1 or lower, the hub should initiate a U1 transition on its US port, assuming that the software enabled the hub to initiate the U1 transition.

Similarly, if all DS ports are in link state U2 or lower, the hub should initiate a U2 transition on its US port, assuming that the software enabled the hub to initiate the U2 transition.

**Note**  
If there is no device attached to a DS port, the port’s state is Rx.Detect, which is lower than U2. So if there are no devices attached, the hub should send its US port to U2. Also, if all the DS ports were initially in U1 or lower and they transition to U2 or lower, the hub should transition the US port from U1 to U2. Because that transition is not based on U2 activity timer, the hub must bring its US port to U0 and then send it to U2.

 

## Packet deferring


The USB 3.0 specification describes a mechanism known as packet deferring (see section C.1.2.2). The mechanism is used to minimize the effect of LPM on bus utilization.

If a host sends a transfer request to a device, whose upstream link is in U1 or U2, the host could end up wasting bus bandwidth by waiting for the link to come back to U0 and then for the device to respond. To avoid that wait, the parent hub responds on behalf of the device by sending a deferred packet header back to the host. The host processes the deferred packet header in a manner similar to NRDY, and is then free to initiate transfers with other endpoints. In parallel, the hub initiates a U0 transition on the link and then informs the device about the deferred packet. The device then sends ERDY to the host to indicate that the device is now ready for the transfer. The host can then reschedule the transfer to the device.

An important responsibility of the device is that after sending ERDY, the device is responsible for keeping the link in U0 until the host sends a response to ERDY or until the **tERDYTimeout** (500 milliseconds) time elapses. During that time, the device must not initiate a U1 or U2 transition and should also reject any transition initiated by its link partner.

 

 
 

 

 




