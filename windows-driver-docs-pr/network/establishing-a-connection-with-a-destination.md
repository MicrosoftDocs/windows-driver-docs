---
title: Establishing a Connection with a Destination
description: Establishing a Connection with a Destination
ms.assetid: 1258ee32-3914-4832-b98b-361dace0abaf
keywords:
- Winsock Kernel WDK networking , remote transport addresses
- WSK WDK networking , remote transport addresses
- remote transport address bindings WDK Winsock Kernel
- transport addresses WDK Winsock Kernel
- established socket connections WDK Winsock Kernel
- connections WDK Winsock Kernel
- destination connections WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Establishing a Connection with a Destination


After a Winsock Kernel (WSK) application has bound a connection-oriented socket to a local transport address, it can connect the socket to a remote transport address in order to establish a connection with the remote system. A WSK application must connect a connection-oriented socket to a remote transport address before it can send or receive data over the socket.

A WSK application connects a socket to a remote transport address by calling the [**WskConnect**](https://msdn.microsoft.com/library/windows/hardware/ff571125) function. The **WskConnect** function is pointed to by the **WskConnect** member of the socket's provider dispatch structure. A socket's provider dispatch structure is pointed to by the **Dispatch** member of the socket object structure ( [**WSK\_SOCKET**](https://msdn.microsoft.com/library/windows/hardware/ff571182)) that was returned by the WSK subsystem during the creation of the socket.

The following code example shows how a WSK application can connect a connection-oriented socket to a remote transport address.

```C++
// Prototype for the connect IoCompletion routine
NTSTATUS
  ConnectComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    );

// Function to connect a socket to a remote transport address
NTSTATUS
  ConnectSocket(
    PWSK_SOCKET Socket,
    PSOCKADDR RemoteAddress
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
    ConnectComplete,
    Socket,  // Use the socket object for the context
    TRUE,
    TRUE,
    TRUE
    );

  // Initiate the connect operation on the socket
  Status =
    Dispatch->WskConnect(
      Socket,
      RemoteAddress,
      0,  // No flags
      Irp
      );

  // Return the status of the call to WskConnect()
  return Status;
}

// Connect IoCompletion routine
NTSTATUS
  ConnectComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    )
{
  UNREFERENCED_PARAMETER(DeviceObject);

  PWSK_SOCKET Socket;

  // Check the result of the connect operation
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

A WSK application can call the [**WskSocketConnect**](https://msdn.microsoft.com/library/windows/hardware/ff571150) function to create, bind, and connect a connection-oriented socket in a single function call.

 

 





