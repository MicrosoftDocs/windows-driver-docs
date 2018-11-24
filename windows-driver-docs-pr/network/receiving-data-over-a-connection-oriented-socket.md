---
title: Receiving Data over a Connection-Oriented Socket
description: Receiving Data over a Connection-Oriented Socket
ms.assetid: 189fa236-25d6-4eea-ad77-df76363576db
keywords:
- connection-oriented sockets WDK Winsock Kernel
- WskReceive
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving Data over a Connection-Oriented Socket


After a Winsock Kernel (WSK) application has connected a connection-oriented socket to a remote transport address it can receive data over the socket. A WSK application can also receive data over a connection-oriented socket that it accepted on a listening socket. A WSK application receives data over a connection-oriented socket by calling the [**WskReceive**](https://msdn.microsoft.com/library/windows/hardware/ff571139) function.

The following code example shows how a WSK application can receive data over a connection-oriented socket.

```C++
// Prototype for the receive IoCompletion routine
NTSTATUS
  ReceiveComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    );

// Function to receive data
NTSTATUS
  ReceiveData(
    PWSK_SOCKET Socket,
    PWSK_BUF DataBuffer
    )
{
  PWSK_PROVIDER_CONNECTION_DISPATCH Dispatch;
  PIRP Irp;
  NTSTATUS Status;

  // Get pointer to the provider dispatch structure
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
    ReceiveComplete,
    DataBuffer,  // Use the data buffer for the context
    TRUE,
    TRUE,
    TRUE
    );

  // Initiate the receive operation on the socket
  Status =
    Dispatch->WskReceive(
      Socket,
      DataBuffer,
      0,  // No flags are specified
      Irp
      );

  // Return the status of the call to WskReceive()
  return Status;
}

// Receive IoCompletion routine
NTSTATUS
  ReceiveComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    )
{
  UNREFERENCED_PARAMETER(DeviceObject);

  PWSK_BUF DataBuffer;
  ULONG ByteCount;

  // Check the result of the receive operation
  if (Irp->IoStatus.Status == STATUS_SUCCESS)
  {
    // Get the pointer to the data buffer
    DataBuffer = (PWSK_BUF)Context;
 
    // Get the number of bytes received
    ByteCount = (ULONG)(Irp->IoStatus.Information);

    // Process the received data
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

As an alternative to calling the [**WskReceive**](https://msdn.microsoft.com/library/windows/hardware/ff571139) function to receive data over a connection-oriented socket, a WSK application can enable the [*WskReceiveEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571140) event callback function on the socket. If a WSK application enables the *WskReceiveEvent* event callback function on a connection-oriented socket, the WSK subsystem calls the socket's *WskReceiveEvent* event callback function whenever new data is received on the socket. For more information about enabling a connection-oriented socket's *WskReceiveEvent* event callback function, see [Enabling and Disabling Event Callback Functions](enabling-and-disabling-event-callback-functions.md).

The following code example shows how a WSK application can receive data by the WSK subsystem calling a connection-oriented socket's *WskReceiveEvent* event callback function.

```C++
// A connection-oriented socket&#39;s WskReceiveEvent
// event callback function
NTSTATUS WSKAPI
  WskReceiveEvent(
    PVOID SocketContext,
    ULONG Flags,
    PWSK_DATA_INDICATION DataIndication,
    SIZE_T BytesIndicated,
    SIZE_T *BytesAccepted
    )
{
  // Check for a valid data indication
  if (DataIndication != NULL)
  {
    // Loop through the list of data indication structures
    while (DataIndication != NULL)
    {
      // Process the data in the data indication structure
      ...

      // Move to the next data indication structure
      DataIndication = DataIndication->Next;
    }

    // Return status indicating the data was received
    return STATUS_SUCCESS;
  }

  // Error
  else
  {
    // Close the socket
    ...

    // Return success since no data was indicated
    return STATUS_SUCCESS;
  }
}
```

If a connection-oriented socket's [*WskReceiveEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571140) event callback function does not retrieve all of the data contained in the list of [**WSK\_DATA\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff571165) structures pointed to by the *DataIndication* parameter, it can retain the list for further processing by returning STATUS\_PENDING. In this situation, the WSK application must call the [**WskRelease**](https://msdn.microsoft.com/library/windows/hardware/ff571144) function to release the list of WSK\_DATA\_INDICATION structures back to the WSK subsystem after it has completed retrieving all of the data from the structures in the list.

If a connection-oriented socket's *WskReceiveEvent* event callback function only accepts a portion of the total number of bytes of received data, it must set the variable pointed to by the *BytesAccepted* parameter to the number of bytes of data that were actually accepted. However, if the socket's *WskReceiveEvent* event callback function accepts all of the received data, it does not need to set the variable pointed to by the *BytesAccepted* parameter.

 

 





