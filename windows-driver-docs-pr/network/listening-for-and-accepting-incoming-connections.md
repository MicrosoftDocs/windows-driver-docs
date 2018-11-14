---
title: Listening for and Accepting Incoming Connections
description: Listening for and Accepting Incoming Connections
ms.assetid: 3ec7d6d0-8b8c-4d98-9e2a-e42b52dcd544
keywords:
- Winsock Kernel WDK networking , incoming connections
- WSK WDK networking , incoming connections
- incoming connections WDK Winsock Kernel
- listening sockets WDK Winsock Kernel
- conditional acceptance WDK Winsock Kernel
- listen operations WDK Winsock Kernel
- SO_CONDITIONAL_ACCEPT
- accepting connections WDK Winsock Kernel
- WskAccept
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Listening for and Accepting Incoming Connections


After a Winsock Kernel (WSK) application binds a listening socket to a local transport address, the socket begins listening for incoming connections from remote transport addresses. A WSK application can accept an incoming connection on a listening socket by calling the [**WskAccept**](https://msdn.microsoft.com/library/windows/hardware/ff571109) function. The IRP that the application passes to the **WskAccept** function is queued until an incoming connection arrives.

The following code example shows how a WSK application can accept an incoming connection by calling the **WskAccept** function.

```C++
// Prototype for the accept IoCompletion routine
NTSTATUS
  AcceptComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    );

// Function to accept an incoming connection
NTSTATUS
  AcceptConnection(
    PWSK_SOCKET Socket,
    PVOID AcceptSocketContext,
    PWSK_CLIENT_CONNECTION_DISPATCH AcceptSocketDispatch
    )
{
  PWSK_PROVIDER_LISTEN_DISPATCH Dispatch;
  PIRP Irp;
  NTSTATUS Status;

  // Get pointer to the socket's provider dispatch structure
  Dispatch =
    (PWSK_PROVIDER_LISTEN_DISPATCH)(Socket->Dispatch);

  // Allocate an IRP
  Irp =
    IoAllocateIrp(
      1,
      FALSE
      );

  // Check result
  if (!Irp)
  {
    // Return error
    return STATUS_INSUFFICIENT_RESOURCES;
  }

  // Set the completion routine for the IRP
  IoSetCompletionRoutine(
    Irp,
    AcceptComplete,
    AcceptSocketContext,
    TRUE,
    TRUE,
    TRUE
    );

  // Initiate the accept operation on the socket
  Status =
    Dispatch->WskAccept(
      Socket,
      0,  // No flags
      AcceptSocketContext,
      AcceptSocketDispatch,
      NULL,
      NULL,
      Irp
      );

  // Return the status of the call to WskAccept()
  return Status;
}

// The accept IoCompletion routine
NTSTATUS
  AcceptComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    )
{
  UNREFERENCED_PARAMETER(DeviceObject);

  PWSK_SOCKET Socket;
  PVOID AcceptSocketContext;

  // Check the result of the accept operation
  if (Irp->IoStatus.Status == STATUS_SUCCESS)
  {
    // Get the accepted socket object from the IRP
    Socket = (PWSK_SOCKET)(Irp->IoStatus.Information);

    // Get the accepted socket's context
    AcceptSocketContext = Context;

    // Perform the next operation on the accepted socket
    ...
  }

  // Error status
  else
  {
    // Handle error
    ...
  }

  // Free the IRP
  IoFreeIrp(Irp);

  // Always return STATUS_MORE_PROCESSING_REQUIRED to
  // terminate the completion processing of the IRP.
  return STATUS_MORE_PROCESSING_REQUIRED;
}
```

As an alternative to calling the [**WskAccept**](https://msdn.microsoft.com/library/windows/hardware/ff571109) function to accept incoming connections on a listening socket, a WSK application can enable the [*WskAcceptEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571120) event callback function on the socket. If a WSK application enables the *WskAcceptEvent* event callback function on a listening socket, the WSK subsystem calls the socket's *WskAcceptEvent* event callback function whenever a new incoming connection is accepted on the socket. For more information about enabling a listening socket's *WskAcceptEvent* event callback function, see [Enabling and Disabling Event Callback Functions](enabling-and-disabling-event-callback-functions.md).

The following code example shows how a WSK application can accept an incoming connection by the WSK subsystem calling a listening socket's *WskAcceptEvent* event callback function.

```cpp
// Dispatch table of event callback functions for accepted sockets
const WSK_CLIENT_CONNECTION_DISPATCH ConnectionDispatch =
{
  .
  . // Function pointers for the event callback functions
  .
};

// Pool tag used for allocating the socket context
#define SOCKET_CONTEXT_POOL_TAG 'tpcs'

// A listening socket's WskAcceptEvent event callback function
NTSTATUS WSKAPI
  WskAcceptEvent(
    PVOID SocketContext,
    ULONG Flags,
    PSOCKADDR LocalAddress,
    PSOCKADDR RemoteAddress,
    PWSK_SOCKET AcceptSocket,
    PVOID *AcceptSocketContext,
    CONST WSK_CLIENT_CONNECTION_DISPATCH **AcceptSocketDispatch
    )
{
  PWSK_APP_SOCKET_CONTEXT SocketContext;

  // Check for a valid new socket
  if (AcceptSocket != NULL)
  {
    // Allocate the socket context
    SocketContext =
      (PWSK_APP_SOCKET_CONTEXT)
        ExAllocatePoolWithTag(
          NonPagedPool,
          sizeof(WSK_APP_SOCKET_CONTEXT),
          SOCKET_CONTEXT_POOL_TAG
          );

    // Check result of allocation
    if (SocketContext == NULL)
    {
      // Reject the socket
      return STATUS_REQUEST_NOT_ACCEPTED;
    }

    // Initialize the socket context
    SocketContext->Socket = AcceptSocket;
    ...

    // Set the accepted socket's client context
    *AcceptSocketContext = SocketContext;

    // Set the accepted socket's dispatch table of callback functions
    *AcceptSocketDispatch = ConnectionDispatch;

    // Perform additional operations on the accepted socket
    ...

    // Return status indicating that the socket was accepted
    return STATUS_SUCCESS:
  }

  // Error with listening socket
  else
  {
    // Handle error
    ...

    // Return status indicating that no socket was accepted
    return STATUS_REQUEST_NOT_ACCEPTED;
  }
}
```

A WSK application can configure a listening socket to conditionally accept incoming connections that are received on the socket. A WSK application enables conditional accept mode on a listening socket by setting the [**SO\_CONDITIONAL\_ACCEPT**](https://msdn.microsoft.com/library/windows/hardware/ff570829) socket option for the socket prior to binding the socket to a local transport address. For more information about how to set socket options, see [Performing Control Operations on a Socket](performing-control-operations-on-a-socket.md).

If conditional accept mode is enabled on a listening socket, the WSK subsystem first calls the socket's [*WskInspectEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571137) event callback function whenever a new incoming connection request is received on the socket. A socket's *WskInspectEvent* event callback function can inspect the incoming connection request to determine if the request should be accepted or rejected. To accept the request, the socket's *WskInspectEvent* event callback function returns **InspectAccept**. To reject the request, the socket's *WskInspectEvent* event callback function returns **InspectReject**. If a socket's *WskInspectEvent* event callback function cannot immediately determine if the request should be accepted or rejected, it returns **InspectPend**. In this situation, a WSK application must call the [**WskInspectComplete**](https://msdn.microsoft.com/library/windows/hardware/ff571136) function after completing the inspection process for the incoming connection request. If an incoming connection request is dropped before the socket connection is fully established, the WSK subsystem calls the WSK application's [*WskAbortEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571108) event callback function.

The following code example shows how a WSK application can inspect an incoming connection request by the WSK subsystem calling the listening socket's *WskInspectEvent* event callback function.

```C++
// Inspect ID for a pending inspection
WSK_INSPECT_ID PendingInspectID

// A listening socket's WskInspectEvent event callback function
WSK_INSPECT_ACTION WSKAPI
  WskInspectEvent(
    PVOID SocketContext,
    PSOCKADDR LocalAddress,
    PSOCKADDR RemoteAddress,
    PWSK_INSPECT_ID InspectID
    )
{
  // Check for a valid inspect ID
  if (InspectID != NULL)
  {
    // Inspect local and/or remote address of the incoming
    // connection request to determine if the connection should
    // be accepted or rejected.
    ...

    // If the incoming connection should be accepted
    if (...)
    {
      // Return status indicating that the incoming
      // connection request was accepted
      return InspectAccept;
    }

    // If the incoming connection should be rejected
    else if (...)
    {
      // Return status indicating that the incoming
      // connection request was rejected
      return InspectReject;
    }

    // Cannot determine immediately
    else
    {
      // Save the inspect ID while the inspection is pending.
      // This will be passed to WskInspectComplete when the
      // inspection process is completed.
      PendingInspectID = *InspectID;

      // Return status indicating that the result of the
      // inspection process for the incoming connection
      // request is pending
      return InspectPend;
    }
  }

  // Error with listening socket
  else
  {
    // Handle error
    ...

    // Return status indicating that a socket was not accepted
    return InspectReject;
  }
}

// A listening socket's WskAbortEvent event callback function
NTSTATUS WSKAPI
  WskAbortEvent(
    PVOID SocketContext,
    PWSK_INSPECT_ID InspectID
    )
{
  // Terminate the inspection for the incoming connection
  // request with a matching inspect ID. To test for a matching
  // inspect ID, the contents of the WSK_INSPECT_ID structures
  // must be compared, not the pointers to the structures.
  ...
}
```

If a WSK application determines that it will accept an incoming connection request on a listening socket that has conditional accept mode enabled, the incoming connection will be established and it can be accepted normally by either the application calling to the [**WskAccept**](https://msdn.microsoft.com/library/windows/hardware/ff571109) function or the WSK subsystem calling the socket's [*WskAcceptEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571120) event callback function as described previously.

 

 





