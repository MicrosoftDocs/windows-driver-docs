---
title: Using Winsock Kernel Functions vs. Event Callback Functions
description: Using Winsock Kernel Functions vs.
ms.assetid: 63a3f933-f74a-4cb8-a7a9-9498e1c17afa
keywords:
- Winsock Kernel WDK networking , functions
- WSK WDK networking , functions
- Winsock Kernel WDK networking , events
- WSK WDK networking , events
- events WDK Winsock Kernel
- functions WDK Winsock Kernel
- event callback functions WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Winsock Kernel Functions vs. Event Callback Functions


For certain socket operations, a Winsock Kernel (WSK) application can either call one of the socket's WSK functions to perform the operation or implement and enable an event callback function on the socket that the WSK subsystem calls when the [event](winsock-kernel-events.md) associated with the operation occurs. For example, when receiving data on a connection-oriented socket, a WSK application can either make calls to the socket's [**WskReceive**](https://msdn.microsoft.com/library/windows/hardware/ff571139) function, or implement and enable a [*WskReceiveEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571140) event callback function on the socket. The requirements of a WSK application dictate which method the application should use. Examples for how to use both methods are provided throughout the WSK documentation.

The following lists summarize some key points for each method.

### Using Winsock Kernel Functions

-   The WSK application drives the socket operations, meaning the WSK application controls when the socket operations occur. This might simplify the synchronization required by the WSK application.

-   The WSK application provides IRPs to the socket functions. These IRPs are queued by the WSK subsystem until the socket operation completes. For more information about using IRPs with WSK functions, see [Using IRPs with Winsock Kernel Functions](using-irps-with-winsock-kernel-functions.md).

-   The WSK application can perform blocking socket operations by waiting for the IRP for each operation to be completed by the WSK subsystem.

-   The WSK application might need to keep multiple socket operations queued in some situations in order to ensure high performance data transfer on connection-oriented sockets, to prevent incoming datagrams from being dropped on datagram sockets, or to prevent incoming connections being dropped on listening sockets.

-   The WSK application provides the data buffers for the data transfer operations. This reduces the number of times the data might need to be copied. However, if a WSK application keeps multiple data transfer operations queued, the application must provide data buffers to the WSK subsystem for each queued data transfer operation. Thus, the WSK application might require additional memory resources.

### Using Event Callback Functions

-   The WSK subsystem drives the socket operations, meaning the WSK subsystem notifies the WSK application of the socket's events by calling the socket's event callback functions. The WSK application might require more complex synchronization to handle the asynchronous nature of the event callback functions.

-   The WSK application does not use IRPs for the socket operations.

-   The WSK application does not need to queue socket operations. The WSK subsystem calls the WSK application's event callback functions as soon as the socket's events occur. If the WSK application can keep up with the rate that a socket's event callback functions are called, using event callback functions could provide the highest performance and least chance of dropping datagrams or incoming connections.

-   The WSK subsystem supplies the data buffers for data transfer operations. The WSK application must release these data buffers back to the WSK subsystem either immediately, or within a reasonable amount of time, so that the WSK subsystem does not run out of memory resources. Thus, the WSK application might need to copy the data from the data buffers that are owned by the WSK subsystem into its own data buffers.

**Note**  The above lists are not necessarily exhaustive. There might be other points to consider when choosing which method is the best choice for a particular WSK application.

 

 

 





