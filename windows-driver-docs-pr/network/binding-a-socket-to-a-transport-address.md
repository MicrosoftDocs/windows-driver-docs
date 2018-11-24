---
title: Binding a Socket to a Transport Address
description: Binding a Socket to a Transport Address
ms.assetid: b76bb601-536f-43de-b91c-932f4f08c274
keywords:
- Winsock Kernel WDK networking , local transport addresses
- WSK WDK networking , local transport addresses
- binding sockets WDK Winsock Kernel
- local transport address bindings WDK Winsock Kernel
- transport addresses WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Binding a Socket to a Transport Address


After a Winsock Kernel (WSK) application has successfully created a socket, it can bind that socket to a local transport address. A listening socket must be bound to a local transport address before it can accept incoming connections. A datagram socket must be bound to a local transport address before it can send or receive datagrams. A connection-oriented socket must be bound to a local transport address before it can connect to a remote transport address.

**Note**  Basic sockets do not support sending or receiving network data. Therefore, a WSK application cannot bind a basic socket to a local transport address.

 

A WSK application binds a socket to a local transport address by calling the [**WskBind**](https://msdn.microsoft.com/library/windows/hardware/ff571121) function. The **WskBind** function is pointed to by the **WskBind** member of the socket's provider dispatch structure. A socket's provider dispatch structure is pointed to by the **Dispatch** member of the socket object structure ( [**WSK\_SOCKET**](https://msdn.microsoft.com/library/windows/hardware/ff571182)) that was returned by the WSK subsystem during the creation of the socket.

A socket can be bound to a local wildcard address. For more information about the behavior of a socket that has been bound to a local wildcard address, see **WskBind**.

The following code example shows how a WSK application can bind a listening socket to a local transport address.

```C++
// Prototype for the bind IoCompletion routine
NTSTATUS
  BindComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    );

// Function to bind a listening socket to a local transport address
NTSTATUS
  BindListeningSocket(
    PWSK_SOCKET Socket,
    PSOCKADDR LocalAddress
    )
{
  PWSK_PROVIDER_LISTEN_DISPATCH Dispatch;
  PIRP Irp;
  NTSTATUS Status;

  // Get pointer to the socket&#39;s provider dispatch structure
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
    BindComplete,
    Socket,  // Use the socket object for the context
    TRUE,
    TRUE,
    TRUE
    );

  // Initiate the bind operation on the socket
  Status =
    Dispatch->WskBind(
      Socket,
      LocalAddress,
      0,  // No flags
      Irp
      );

  // Return the status of the call to WskBind()
  return Status;
}

// Bind IoCompletion routine
NTSTATUS
  BindComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    )
{
  UNREFERENCED_PARAMETER(DeviceObject);

  PWSK_SOCKET Socket;

  // Check the result of the bind operation
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

For connection-oriented sockets, a WSK application can call the [**WskSocketConnect**](https://msdn.microsoft.com/library/windows/hardware/ff571150) function to create, bind, and connect a socket in a single function call.

 

 





