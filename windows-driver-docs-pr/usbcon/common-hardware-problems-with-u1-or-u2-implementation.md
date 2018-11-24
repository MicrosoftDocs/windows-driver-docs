---
Description: This topic discusses the LPM mechanism for saving power and described various common problems seen in current USB 3.0 hardware.
title: Common hardware problems with U1 or U2 implementation
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Common hardware problems with U1 or U2 implementation


This topic discusses the LPM mechanism for saving power and described various common problems seen in current USB 3.0 hardware. USB-IF certification requires that devices, hubs, and controllers implement U1 and U2 correctly. The certification aims at enforcing that requirement through compliance tests. The Microsoft USB driver stack (included with Windows 8) takes full advantage of the U1 and U2 mechanism to achieve maximum power savings. Therefore problems such as those described in this topic will be seen more frequently. Those problems can lead to poor user experience and might prevent Windows from achieving the power savings offered by the USB 3.0 specification.

Hardware vendors must take steps to avoid the issues that are described in this topic. For currently released hardware with problems, vendors should release updated firmware with fixes as soon as possible and must work with their partners to ensure that the updates are provided to customers.

LPM can significantly save power and lead to longer battery life. Therefore, it is imperative that both software and hardware should support LPM to its fullest extent. However, some of the early prototypes of USB 3.0 hardware have common problems in the LPM implementation that can lead to poor end-user experience. The purpose of this section is to identify those problems.

## Device-related issues


-   **No support for U1 or U2**

    Some devices never initiate U1 and U2 transitions and always reject transitions that are initiated by the host, even though there are no transfers for a long time and the performance effect of LPM is not likely to be significant. Those devices not only prevent power savings for their link but also prevent any upstream links from entering U1 or U2.

-   **Incorrect deferred packet implementation**

    As described in [Packet Deferring](u1-and-u2-transitions.md#packet-deferring), after a device has sent ERDY, the device must keep the link in U0 until the host sends a response to ERDY or **tERDYTimeout** occurs. Some devices fail to send ERDY after getting a deferred packet notification. This can lead to a problematic situation where a transfer never completes.

-   **Failure to send Ping.LPFS in U1**

    The US port of the device should keep sending **Ping.LPFS** when the link is in U1. Some devices fail to do that, which causes the link partner to assume that the device has been removed. That can cause the link to enter an error state and can cause re-enumeration of the device.

-   **Failure of SET\_SEL transfer**

    The software sends a SET\_SEL control transfer to inform the device about the various exit latencies from U1 and U2. Some devices stall that transfer. That can lead to enumeration failure or can lead to software not enabling U1 or U2 for the device.

-   **Failure of SET\_FEATURE (U1\_ENABLE or U2\_ENABLE) transfer**

    The software enables or disables the ability of the device to initiate a U1 or U2 transition by sending a SET\_FEATURE control transfer. Some devices stall that transfer. This can lead to enumeration failure or the software not enabling U1 or U2 for the device.

## Hub or controller-related issues


-   **No support of U1 or U2 timers**

    One of the most common problems with LPM implementation is the failure to initiate U1 or U2 transition when the timer expires. Even after the software has programmed U1 or U2 timeout values for DS ports, some hubs or controllers do not initiate a transition to U1 or U2 on the expiration of the timer. This behavior prevents power savings through LPM.

-   **Hard-coded U1 or U2 time-out values**

    Some host controllers support U1 and U2 transitions but have a hard-coded time-out value. Before this time-out, they do not initiate these transitions and reject transitions initiated by the link partner. This behavior results in missed opportunities for U1 and U2 transitions and thus can prevent some power savings.

-   **Incorrect implementation of deferred packet**

    As described in [Packet Deferring](u1-and-u2-transitions.md#packet-deferring), hubs are responsible for sending the deferred bit packet header back to the host that must process the packet, similar to a NRDY notification from the device. Some hubs fail to send the deferred packet to the host or the device. Some hosts do not correctly process the deferred bit packet or re-send the transfer when the device ultimately sends ERDY. This leads to transfer failures and unreliable behavior.

-   **Not sending upstream port to U2 when no device connected**

    Some hubs fail to initiate a U1 or U2 transition for the US port when there are no downstream devices connected. Some hubs send the link to U1 but do not send to U2 in this scenario. This issue has been observed in many of the current shipping implementations of USB 3.0 hardware, as of the release date of this paper. This behavior prevents optimum power savings.

-   **Not transitioning the US port from U1 to U2**

    Some hubs fail to transition the US port from U1 to U0 to U2 when the hub’s DS ports transition from U1 to U2 or a lower state. That occurs if the inactivity timer of the DS port to which the hub is connected is set to 0xFF. This behavior prevents optimum power savings.

-   **Transition from U1/U2 to U3**

    If a DS port of a hub or controller is in U1 or U2 and the software initiates a U3 transition on the port, the parent hub or controller is responsible for first transitioning the link to U0 and then to U3. Some hubs and controllers do not handle that requirement properly. This can cause the link to enter an error state and can cause re-enumeration of the device.  

 

 




