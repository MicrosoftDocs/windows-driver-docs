---
title: Requirements for TCP Chimney NICs for Blind-Reset Attacks
description: TCP Chimney NICs must follow the security guidelines outlined in the IETF memo of Improving TCP's Robustness to Blind In-Window Attacks, sections 3, 4, and 5. This section describes those guidelines.
ms.assetid: e9cf6a7f-2c97-495c-a082-268b933daf60
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requirements for TCP Chimney NICs for Blind-Reset Attacks


\[The TCP chimney offload feature is deprecated and may be removed from future versions of the operating system.\]

TCP Chimney NICs must follow the security guidelines outlined in the IETF memo of [Improving TCP's Robustness to Blind In-Window Attacks](http://go.microsoft.com/fwlink/p/?linkid=181776), sections 3, 4, and 5. This section describes those guidelines.

**Note**  This Internet-Draft is cited as a work in progress.

 

## Implementing Blind-Reset Attack Mitigation


An implementation must send a challenging ACK upon receiving a SYN regardless of its sequence number. However, the TCP Chimney NIC should terminate the connection if the seqNumber of an incoming SYN matches RcvNext.

The IETF draft recommends ACK throttling for sending a challenging ACK. However, it does not specify details for a throttling mechanism. The TCP Chimney NIC is not required to throttle an ACK for a SYN that is outside the receive window, and can send a challenging ACK for each such SYN. The TCP Chimney NIC should implement ACK throttling for an in-window but out-of-order SYN by sending one challenging ACK per 3 second period. The TCP Chimney NIC should silently drop an RST segment that is outside the receive window. It should not send more than one challenging ACK for an in-window but out-of-order RST as long as it is in the RST validation period. That is, it should not send more than one challenging ACK until either an acceptable segment arrives or the connection times out due to keep-alive probes.

Upon receiving an in-window but out-of-order SYN or RST, the TCP Chimney NIC should start the keep-alive timer, if it is not already running, to expire after 5 minutes. After that period, the TCP Chimney NIC should start sending keep-alive probes. The number and frequency of keep-alive probes are determined by KaProbeCount and KaInterval cached state variables. If these variables are set to zero, then the TCP Chimney NIC should use default values of 10 for KaProbeCount and 1 second for KaInterval .

## Blind-Reset Attack Algorithm


Below is a summary of the algorithm for mitigating blind-reset attacks, to be implemented by the TCP Chimney NIC:

-   If a received RST segment is outside receive window, then silently drop the segment.
-   If a received RST segment whose seqNumber value equals RcvNext, then indicate TcpIndicateAbort event to the host stack.
-   If a received RST segment is in-window but out-of-order, then send challenging ACK if no such ACK has yet been sent. Also, if sent challenging ACK, start Keepalive timer to expire after 5 minutes if it is not already running. If the timer is running but would not expire before 5 minutes, then restart timer to expire after 5 minutes.
-   If a received SYN segment is outside window, then send an ACK.
-   If a received SYN segment's seqNumber value equals RcvNext, then upload the connection in CLOSED state.
-   If a received SYN segment is in-window but out-of-order, then send a challenging ACK but do not send more than 1 such ACK per 3-second period. Also, if sent challenging ACK, start a Keepalive timer to expire after 5 minutes if it is not already running. If the timer is running but wouldn't expire before 5 minutes, then restart the timer to expire after 5 minutes.
-   If no acceptable segment arrives before the Keepalive timer expires, then continue sending the remaining keep-alive probes. If all keep-alive probes have been sent, then upload the connection in CLOSED state. Each keep-alive probe should be sent after a period of KaInterval. The total number of keep-alive probes should not exceed KaProbeCount cached state variable. If the connection was offloaded with a non-zero value of KeepAlive.ProbeCount delegated state variable, then that number should be included when counting the number of probes to be sent.
-   If the connection is uploaded during blind-reset attack mitigation, then set KeepAlive.ProbeCount and KeepAlive.TimeoutDelta to reflect the number of probes sent and time remaining until the next probe.
-   If an acceptable segment has been received, then stop the Keepalive timer if and only if the timer was started because of in-window but out-of-order SYN or RST, as described above. Otherwise, if the keep-alive option is enabled on the connection, then restart the timer to resume a normal keep-alive operation.

 

 





