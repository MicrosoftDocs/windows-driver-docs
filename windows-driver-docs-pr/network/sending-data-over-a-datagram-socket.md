---
title: Sending Data over a Datagram Socket
description: Sending Data over a Datagram Socket
ms.assetid: 5748ac2a-177f-4fe9-a55b-85eec45d5afa
keywords:
- sending datagrams
- datagram sockets WDK Winsock Kernel
- WskSendTo
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending Data over a Datagram Socket


After a Winsock Kernel (WSK) application has bound a datagram socket to a local transport address it can send datagrams over the socket. A WSK application sends a datagram over a datagram socket by calling the [**WskSendTo**](https://msdn.microsoft.com/library/windows/hardware/ff571148) function.

The following code example shows how a WSK application can send a datagram over a datagram socket.

```C++
// Prototype for the send datagram IoCompletion routine
NTSTATUS
  SendDatagramComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    );

// Function to send a datagram
NTSTATUS
  SendDatagram(
    PWSK_SOCKET Socket,
    PWSK_BUF DatagramBuffer,
    PSOCKADDR RemoteAddress
    )
{
  PWSK_PROVIDER_DATAGRAM_DISPATCH Dispatch;
  PIRP Irp;
  NTSTATUS Status;

  // Get pointer to the provider dispatch structure
  Dispatch =
    (PWSK_PROVIDER_DATAGRAM_DISPATCH)(Socket->Dispatch);

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
    SendDatagramComplete,
    DatagramBuffer,  // Use the datagram buffer for the context
    TRUE,
    TRUE,
    TRUE
    );

  // Initiate the send operation on the socket
  Status =
    Dispatch->WskSendTo(
      Socket,
      DatagramBuffer,
      0,  // No flags
      RemoteAddress,
      0,
      NULL,  // No associated control info
      Irp
      );

  // Return the status of the call to WskSendTo()
  return Status;
}

// Send datagram IoCompletion routine
NTSTATUS
  SendDatagramComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    )
{
  UNREFERENCED_PARAMETER(DeviceObject);

  PWSK_BUF DatagramBuffer;
  ULONG ByteCount;

  // Check the result of the send operation
  if (Irp->IoStatus.Status == STATUS_SUCCESS)
  {
    // Get the pointer to the datagram buffer
    DatagramBuffer = (PWSK_BUF)Context;

    // Get the number of bytes sent
    ByteCount = (ULONG)(Irp->IoStatus.Information);

    // Re-use or free the datagram buffer
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

If the WSK application has set either a fixed remote transport address or a fixed destination transport address for the datagram socket, the *RemoteAddress* parameter passed to the [**WskSendTo**](https://msdn.microsoft.com/library/windows/hardware/ff571148) function is optional and can be **NULL**. If **NULL**, the datagram is sent to the fixed remote transport address or the fixed destination transport address. If non-**NULL**, the datagram is sent to the specified remote transport address.

For more information about setting a fixed remote transport address for a datagram socket, see [**SIO\_WSK\_SET\_REMOTE\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff570820).

For more information about setting a fixed destination transport address for a datagram socket, see [**SIO\_WSK\_SET\_SENDTO\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff570821).

 

 





