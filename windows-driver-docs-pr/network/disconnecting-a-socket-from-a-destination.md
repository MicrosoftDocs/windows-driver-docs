---
title: Disconnecting a Socket from a Destination
description: Disconnecting a Socket from a Destination
ms.assetid: 83755eb4-a24e-4fef-858d-d58318227dc0
keywords:
- Winsock Kernel WDK networking , disconnecting
- WSK WDK networking , disconnecting
- established socket connections WDK Winsock Kernel
- connections WDK Winsock Kernel
- disconnections WDK Winsock Kernel
- destination connections WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Disconnecting a Socket from a Destination


When a Winsock Kernel (WSK) application has finished sending and receiving data over an established socket connection, it can disconnect the connection-oriented socket from the remote transport address to which it is connected. A WSK application disconnects a socket from a remote transport address by calling the [**WskDisconnect**](https://msdn.microsoft.com/library/windows/hardware/ff571129) function. A WSK application can perform either an *abortive disconnect* or a *graceful disconnect* of the socket. For more information about the difference between an abortive disconnect and a graceful disconnect, see **WskDisconnect**.

The following code example shows how a WSK application can gracefully disconnect a connection-oriented socket from a remote transport address.

```C++
// Prototype for the disconnect IoCompletion routine
NTSTATUS
  DisconnectComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    );

// Function to disconnect a socket from a remote transport address
NTSTATUS
  DisconnectSocket(
    PWSK_SOCKET Socket
    )
{
  PWSK_PROVIDER_CONNECTION_DISPATCH Dispatch;
  PIRP Irp;
  NTSTATUS Status;
 
  // Get pointer to the socket&#39;s provider dispatch structure
  Dispatch =
    (PWSK_PROVIDER_CONNECTION_DISPATCH)(Socket->Dispatch);

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
    DisconnectComplete,
    Socket,  // Use the socket object for the context
    TRUE,
    TRUE,
    TRUE
    );

  // Initiate the disconnect operation on the socket
  Status =
    Dispatch->WskDisconnect(
      Socket,
      NULL,  // No final data to be transmitted
      0,     // No flags (graceful disconnect)
      Irp
      );

  // Return the status of the call to WskDisconnect()
  return Status;
}

// Disconnect IoCompletion routine
NTSTATUS
  DisconnectComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    )
{
  UNREFERENCED_PARAMETER(DeviceObject);

  PWSK_SOCKET Socket;

  // Check the result of the disconnect operation
  if (Irp->IoStatus.Status == STATUS_SUCCESS)
  {
    // Get the socket object from the context
    Socket = (PWSK_SOCKET)Context;

    // Perform the next operation on the socket
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

If a WSK application performs a graceful disconnect of a socket, the application can send a final buffer of data to the remote transport address before the socket is disconnected by passing a pointer to a [**WSK\_BUF**](https://msdn.microsoft.com/library/windows/hardware/ff571153) structure to the [**WskDisconnect**](https://msdn.microsoft.com/library/windows/hardware/ff571129) function.

If a WSK application closes a connection-oriented socket without first disconnecting the socket from the remote transport address to which it is connected, the WSK subsystem automatically performs an abortive disconnect of the socket prior to closing the socket. For more information about closing a socket, see [Closing a Socket](closing-a-socket.md).

 

 





