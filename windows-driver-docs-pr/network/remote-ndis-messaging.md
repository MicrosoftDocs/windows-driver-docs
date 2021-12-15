---
title: Remote NDIS Messaging
description: Remote NDIS Messaging
keywords:
- Remote NDIS WDK networking , messaging
ms.date: 04/20/2017
---

# Remote NDIS Messaging





There are two types of Remote NDIS messages: *control messages* and *data messages*. Control messages allow the host and Remote NDIS device to communicate with each other over the communication channel. Data messages contain the message data information needed for the communication between the host and device and are communicated over the data channel.

-   **Remote NDIS Control Messages**

    Remote NDIS control messages can be sent by the host to the Remote NDIS device and by the Remote NDIS device to the host. The following Remote NDIS control messages must be supported by an Ethernet 802.3 connectionless device:

    [REMOTE\_NDIS\_INITIALIZE\_MSG](/previous-versions/ff570624(v=vs.85))

    [REMOTE\_NDIS\_INITIALIZE\_CMPLT](/previous-versions/ff570621(v=vs.85))

    [REMOTE\_NDIS\_HALT\_MSG](/previous-versions/ff570613(v=vs.85))

    [REMOTE\_NDIS\_QUERY\_MSG](/previous-versions/ff570641(v=vs.85))

    [REMOTE\_NDIS\_QUERY\_CMPLT](/previous-versions/ff570638(v=vs.85))

    [REMOTE\_NDIS\_SET\_MSG](/previous-versions/ff570654(v=vs.85))

    [REMOTE\_NDIS\_SET\_CMPLT](/previous-versions/ff570651(v=vs.85))

    [REMOTE\_NDIS\_RESET\_MSG](/previous-versions/ff570648(v=vs.85))

    [REMOTE\_NDIS\_RESET\_CMPLT](/previous-versions/ff570645(v=vs.85))

    [REMOTE\_NDIS\_INDICATE\_STATUS\_MSG](/previous-versions/ff570617(v=vs.85))

    [REMOTE\_NDIS\_KEEPALIVE\_MSG](/previous-versions/ff570629(v=vs.85))

    [REMOTE\_NDIS\_KEEPALIVE\_CMPLT](/previous-versions/ff570626(v=vs.85))

-   **Remote NDIS Data Message**

    A Remote NDIS device must send and receive data through Remote NDIS data packets contained in the [REMOTE\_NDIS\_PACKET\_MSG](/previous-versions/ff570635(v=vs.85)) message structure. Remote NDIS data packets may also contain out of band data as well as the data that goes across the network.

    Both connectionless (for example, 802.3) and connection-oriented (for example, ATM) devices use the same **REMOTE\_NDIS\_PACKET\_MSG** message structure, in order to facilitate common code for packet processing.

 

