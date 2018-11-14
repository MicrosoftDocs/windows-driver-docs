---
title: Creating Sockets
description: Creating Sockets
ms.assetid: 84cd0503-15bd-401f-836c-1fdc8425d073
keywords:
- Winsock Kernel WDK networking , socket creation
- WSK WDK networking , socket creation
- listening sockets WDK Winsock Kernel
- WskSocket
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Sockets


After a Winsock Kernel (WSK) application has successfully attached to the WSK subsystem, it can create sockets that can be used for network I/O operations. A WSK application creates sockets by calling the [**WskSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571149) function. The **WskSocket** function is pointed to by the **WskSocket** member of the [**WSK\_PROVIDER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff571175) structure that was returned by the WSK subsystem during attachment.

A WSK application must specify which category of WSK socket it is creating whenever it creates a new socket. For more information about WSK socket categories, see [Winsock Kernel Socket Categories](winsock-kernel-socket-categories.md).

A WSK application must also specify the address family, socket type, and protocol whenever it creates a new socket. For more information about the address families supported by WSK, see [WSK Address Families](https://msdn.microsoft.com/library/windows/hardware/ff571151).

When creating a new socket, a WSK application must provide a socket context value and a pointer to a client dispatch table structure if the application will be enabling any event callback functions on the socket. For more information about enabling event callback functions on a socket, see [Enabling and Disabling Event Callback Functions](enabling-and-disabling-event-callback-functions.md).

If the socket is created successfully, the **IoStatus.Information** field of the IRP contains a pointer to a socket object structure ( [**WSK\_SOCKET**](https://msdn.microsoft.com/library/windows/hardware/ff571182)) for the new socket. For more information about using IRPs with WSK functions, see [Using IRPs with Winsock Kernel Functions](using-irps-with-winsock-kernel-functions.md).

The following code example shows how a WSK application can create a listening socket.

```C++
// Context structure for each socket
typedef struct _WSK_APP_SOCKET_CONTEXT {
  PWSK_SOCKET Socket;
  .
  .  // Other application-specific members
  .
} WSK_APP_SOCKET_CONTEXT, *PWSK_APP_SOCKET_CONTEXT;

// Prototype for the socket creation IoCompletion routine
NTSTATUS
  CreateListeningSocketComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    );

// Function to create a new listening socket
NTSTATUS
  CreateListeningSocket(
    PWSK_PROVIDER_NPI WskProviderNpi,
    PWSK_APP_SOCKET_CONTEXT SocketContext,
    PWSK_CLIENT_LISTEN_DISPATCH Dispatch,
    )
{
  PIRP Irp;
  NTSTATUS Status;

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
    CreateListeningSocketComplete,
    SocketContext,
    TRUE,
    TRUE,
    TRUE
    );

  // Initiate the creation of the socket
  Status =
    WskProviderNpi->Dispatch->
        WskSocket(
          WskProviderNpi->Client,
          AF_INET,
          SOCK_STREAM,
          IPPROTO_TCP,
          WSK_FLAG_LISTEN_SOCKET,
          SocketContext,
          Dispatch,
          NULL,
          NULL,
          NULL,
          Irp
          );

  // Return the status of the call to WskSocket()
  return Status;
}

// Socket creation IoCompletion routine
NTSTATUS
  CreateListeningSocketComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    )
{
  UNREFERENCED_PARAMETER(DeviceObject);

  PWSK_APP_SOCKET_CONTEXT SocketContext;

  // Check the result of the socket creation
  if (Irp->IoStatus.Status == STATUS_SUCCESS)
  {
    // Get the pointer to the socket context
    SocketContext =
      (PWSK_APP_SOCKET_CONTEXT)Context;

    // Save the socket object for the new socket
    SocketContext->Socket =
      (PWSK_SOCKET)(Irp->IoStatus.Information);

    // Set any socket options for the new socket
    ...

    // Enable any event callback functions on the new socket
    ...

    // Perform any other initializations
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

For connection-oriented sockets, a WSK application can call the [**WskSocketConnect**](https://msdn.microsoft.com/library/windows/hardware/ff571150) function to create, bind, and connect a socket in a single function call.

 

 





