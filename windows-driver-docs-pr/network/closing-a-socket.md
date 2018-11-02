---
title: Closing a Socket
description: Closing a Socket
ms.assetid: 3fa2d5c3-7b52-4bbe-b99d-ef3be19c7c7e
keywords:
- Winsock Kernel WDK networking , socket closing
- WSK WDK networking , socket closing
- closing sockets
- WskCloseSocket
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Closing a Socket


When a Winsock Kernel (WSK) application has finished using a socket, it should close the socket and free up any associated resources. A WSK application must close all open sockets before the application can detach itself from the WSK subsystem. For more information about detaching a WSK application from the WSK subsystem, see [Unregistering a Winsock Kernel Application](unregistering-a-winsock-kernel-application.md).

A WSK application closes a socket by calling the [**WskCloseSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571124) function. Before calling the **WskCloseSocket** function, a WSK application must ensure that there are no other function calls in progress to any of the socket's functions, including any extension functions in any of the application's other threads. However, a WSK application can call **WskCloseSocket** if there are pending IRPs from prior calls to the socket's functions that have not yet completed.

The method that a WSK application uses to ensure that there are no other function calls in progress to any of the socket's functions before it calls the **WskCloseSocket** function is dependent upon the design of the application. For example, if a WSK application might need to close a socket in one thread while there could be calls in progress to that socket's other functions in one or more other threads, then the application would typically use a reference counter to track the number of function calls that are currently in progress on the socket. In this situation, the WSK application atomically tests and increments a socket's reference counter before it calls one of the socket's functions, and then atomically decrements the socket's reference counter when the function returns. When the reference counter is zero, the WSK application can safely call the **WskCloseSocket** function to close the socket.

On the other hand, if the design of the WSK application guarantees that there will not be any calls in progress to a particular socket's functions in any other threads when the application calls the **WskCloseSocket** function to close the socket, then the WSK application does not need to use a reference counter to track the number of function calls that are currently in progress on the socket. For example, if the WSK application performs all of its socket operations for a particular socket from a single thread, then the application can safely call the **WskCloseSocket** function from within that thread without the need for a reference counter.

Calling the **WskCloseSocket** function causes the WSK subsystem to cancel and complete all pending IRPs from prior calls to the socket's functions. The WSK subsystem also ensures that any event callback functions in progress have returned control back to the WSK subsystem before the close operation is completed.

The following code example shows how a WSK application can close a socket.

```C++
// Prototype for the socket close IoCompletion routine
NTSTATUS
  CloseSocketComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    );

// Function to close a socket
NTSTATUS
  CloseSocket(
    PWSK_SOCKET Socket,
    PWSK_APP_SOCKET_CONTEXT SocketContext
    )
{
  PWSK_PROVIDER_BASIC_DISPATCH Dispatch;
  PIRP Irp;
  NTSTATUS Status;

  // Get pointer to the socket&#39;s provider dispatch structure
  Dispatch =
    (PWSK_PROVIDER_BASIC_DISPATCH)(Socket->Dispatch);

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
    CloseSocketComplete,
    SocketContext,
    TRUE,
    TRUE,
    TRUE
    );

  // Initiate the close operation on the socket
  Status =
    Dispatch->WskCloseSocket(
      Socket,
      Irp
      );

  // Return the status of the call to WskCloseSocket()
  return Status;
}

// Socket close IoCompletion routine
NTSTATUS
  CloseSocketComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    )
{
  UNREFERENCED_PARAMETER(DeviceObject);

  PWSK_APP_SOCKET_CONTEXT SocketContext;

  // Check the result of the socket close operation
  if (Irp->IoStatus.Status == STATUS_SUCCESS)
  {
    // Get the pointer to the socket context
    SocketContext =
      (PWSK_APP_SOCKET_CONTEXT)Context;

    // Perform any cleanup and/or deallocation of the socket context
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

After a WSK application has called [**WskCloseSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571124), it should not make any further calls to any of the socket's functions.

If a WSK application closes a connection-oriented socket that has not been previously disconnected in both directions, the WSK subsystem automatically performs an abortive disconnect of the socket before closing the socket. For more information about disconnecting a socket, see [Disconnecting a Socket from a Destination](disconnecting-a-socket-from-a-destination.md).

 

 





