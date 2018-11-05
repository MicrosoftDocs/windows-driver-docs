---
title: Remote NDIS Concepts and Definitions
description: Remote NDIS Concepts and Definitions
ms.assetid: caf01e69-9368-4b9b-a343-ef17a2154bb8
keywords:
- Remote NDIS WDK networking , concepts
- Remote NDIS WDK networking , definitions
- Remote NDIS WDK networking , control channels
- Remote NDIS WDK networking , data channels
- Remote NDIS WDK networking , halt
- control channels WDK networking
- control channels WDK networking , initialization
- control channels WDK networking , teardown
- data channels WDK networking
- data channels WDK networking , initialization
- data channels WDK networking , teardown
- Remote NDIS WDK networking , device states
- device states WDK networking
- Remote NDIS WDK networking , flow control
- Remote NDIS WDK networking , resetting communication channels
- communication channels WDK networking
- Remote NDIS WDK networking , message encapsulation
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Remote NDIS Concepts and Definitions





This section presents an overview of the Remote NDIS requirements on the communication channel and lower-layer drivers that are used to communicate between the host and the Remote NDIS device. Device state transitions and major operations such as initialization, halt and reset are also described in this section.

-   **Control Channel**

    The control channel must be reliable and ensure sequenced delivery. It is used for all communication except for the transmission of network data packets. All required control messages, except [REMOTE\_NDIS\_HALT\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570613) and [REMOTE\_NDIS\_INDICATE\_STATUS\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570617), are request and response exchanges initiated by the host. The device must respond within the time-out period as specified for each bus.

-   **Data Channel**

    The data channel is used exclusively for the transmission of network data packets. It may consist of multiple subchannels (for example, for varying quality of service) as defined for the appropriate bus.

-   **Initialization and Teardown**

    The control and data channels are initialized and set up as specified for the appropriate bus. The host sends a [REMOTE\_NDIS\_INITIALIZE\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570624) message to the Remote NDIS device. The Remote NDIS device provides information about its type (connectionless or connection-oriented), supported medium, and version in the response message [REMOTE\_NDIS\_INITIALIZE\_CMPLT](https://msdn.microsoft.com/library/windows/hardware/ff570621).

    Either the host or the Remote NDIS device can tear down the communication channel through the [REMOTE\_NDIS\_HALT\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570613) message. All outstanding requests and packets are discarded on receipt of this message.

-   **Device State Definitions**

    Following bus-level initialization, the device is said to be in the RNDIS-uninitialized state. Upon receiving a [REMOTE\_NDIS\_INITIALIZE\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570624) and responding with a REMOTE\_NDIS\_INITIALIZE\_CMPLT with a status of RNDIS\_STATUS\_SUCCESS, the device enters the RNDIS-initialized state.

    Upon receiving REMOTE\_NDIS\_SET\_MSG specifying a nonzero filter value for OID\_GEN\_CURRENT\_PACKET\_FILTER, the device enters the RNDIS-data-initialized state.

    When in the state RNDIS-data-initialized, reception of a REMOTE\_NDIS\_SET\_MSG specifying a zero filter value for OID\_GEN\_CURRENT\_PACKET\_FILTER forces the device back to the RNDIS-initialized state.

    Reception of REMOTE\_NDIS\_HALT\_MSG or a bus-level disconnect or hard-reset at any time forces the device to the RNDIS-uninitialized state.

-   **Halt**

    At any time that the device is in the RNDIS-initialized or RNDIS-data-initialized state, the host computer may terminate the Remote NDIS functionality of the device by sending REMOTE\_NDIS\_HALT\_MSG to the device.

-   **Resetting the Communication Channel**

    The communication channel is reset when an error, such as message time-out, occurs. The host may initiate a reset at any time when the device is in the RNDIS-initialized state by sending the message [REMOTE\_NDIS\_RESET\_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570648) to the device and the device must send a response message when it has completed the reset. For example, the host may initiate a reset when an error, such as a message time-out, has occurred.

    Note that this is a soft reset in the sense that any handles (for example, VCs for connection-oriented devices) continue to be valid after the reset. The Remote NDIS device discards all outstanding requests and packets as part of the reset process. The remote device might reset some of its hardware components, but keeps the communication channel intact.

    If the Remote NDIS device performs a reboot, this event is equivalent to "Remove" followed by "Add" Plug and Play events. The host NDIS miniport driver will be halted and removed, and a new instance will be added and started. All bus-level and Remote NDIS initialization will be re-executed. A Remote NDIS device may reboot itself in the event of a critical device failure.

-   **Flow Control**

    The Remote NDIS device may need to exercise flow control to prevent the host from overflowing its data buffers with packets. Any flow control provisions or requirements are bus specific.

-   **Numeric Byte Ordering**

    All numeric values in Remote NDIS messages must be coded in little-endian format (least significant byte first).

-   **NDIS Message Encapsulation**

    There is no Remote NDIS specification for the way NDIS messages are encapsulated in native bus messages or primitives.

 

 





