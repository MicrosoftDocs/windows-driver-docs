---
title: Remote NDIS Messaging
description: Remote NDIS Messaging
ms.assetid: 6364a9a1-c65f-463d-971b-cf94cd2a5cde
keywords:
- Remote NDIS WDK networking , messaging
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Remote NDIS Messaging





There are two types of Remote NDIS messages: *control messages* and *data messages*. Control messages allow the host and Remote NDIS device to communicate with each other over the communication channel. Data messages contain the message data information needed for the communication between the host and device and are communicated over the data channel.

-   **Remote NDIS Control Messages**

    Remote NDIS control messages can be sent by the host to the Remote NDIS device and by the Remote NDIS device to the host. The following Remote NDIS control messages must be supported by an Ethernet 802.3 connectionless device:

    [REMOTE\_NDIS\_INITIALIZE\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570624)

    [REMOTE\_NDIS\_INITIALIZE\_CMPLT](https://msdn.microsoft.com/library/windows/hardware/ff570621)

    [REMOTE\_NDIS\_HALT\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570613)

    [REMOTE\_NDIS\_QUERY\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570641)

    [REMOTE\_NDIS\_QUERY\_CMPLT](https://msdn.microsoft.com/library/windows/hardware/ff570638)

    [REMOTE\_NDIS\_SET\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570654)

    [REMOTE\_NDIS\_SET\_CMPLT](https://msdn.microsoft.com/library/windows/hardware/ff570651)

    [REMOTE\_NDIS\_RESET\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570648)

    [REMOTE\_NDIS\_RESET\_CMPLT](https://msdn.microsoft.com/library/windows/hardware/ff570645)

    [REMOTE\_NDIS\_INDICATE\_STATUS\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570617)

    [REMOTE\_NDIS\_KEEPALIVE\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570629)

    [REMOTE\_NDIS\_KEEPALIVE\_CMPLT](https://msdn.microsoft.com/library/windows/hardware/ff570626)

-   **Remote NDIS Data Message**

    A Remote NDIS device must send and receive data through Remote NDIS data packets contained in the [REMOTE\_NDIS\_PACKET\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570635) message structure. Remote NDIS data packets may also contain out of band data as well as the data that goes across the network.

    Both connectionless (for example, 802.3) and connection-oriented (for example, ATM) devices use the same **REMOTE\_NDIS\_PACKET\_MSG** message structure, in order to facilitate common code for packet processing.

 

 





