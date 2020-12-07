---
title: Receiving Data over a Datagram Socket
description: Receiving Data over a Datagram Socket
keywords:
- receiving datagrams
- datagram sockets WDK Winsock Kernel
- WskReceiveFrom
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving Data over a Datagram Socket


After a Winsock Kernel (WSK) application has bound a datagram socket to a local transport address it can receive datagrams over the socket. A WSK application receives a datagram over a datagram socket by calling the [**WskReceiveFrom**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive_from) function.

The following code example shows how a WSK application can receive a datagram over a datagram socket.

```C++
// Prototype for the receive datagram IoCompletion routine
NTSTATUS
  ReceiveDatagramComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    );

// Function to receive a datagram
NTSTATUS
  ReceiveDatagram(
    PWSK_SOCKET Socket,
    PWSK_BUF DatagramBuffer
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
    ReceiveDatagramComplete,
    DatagramBuffer,  // Use the datagram buffer for the context
    TRUE,
    TRUE,
    TRUE
    );

  // Initiate the receive operation on the socket
  Status =
    Dispatch->WskReceiveFrom(
      Socket,
      DatagramBuffer,
      0,  // No flags are specified
      NULL,  // Not interested in the remote address
      NULL,  // Not interested in any associated control information
      NULL,
      NULL,
      Irp
      );

  // Return the status of the call to WskReceiveFrom()
  return Status;
}

// Receive datagram IoCompletion routine
NTSTATUS
  ReceiveDatagramComplete(
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

    // Process the received datagram
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

As an alternative to calling the [**WskReceiveFrom**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive_from) function to receive each datagram over a datagram socket, a WSK application can enable the [*WskReceiveFromEvent*](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive_from_event) event callback function on the socket. If a WSK application enables the *WskReceiveFromEvent* event callback function on a datagram socket, the WSK subsystem calls the socket's *WskReceiveFromEvent* event callback function whenever new datagrams are received on the socket. For more information about enabling a datagram socket's *WskReceiveFromEvent* event callback function, see [Enabling and Disabling Event Callback Functions](enabling-and-disabling-event-callback-functions.md).

The following code example shows how a WSK application can receive datagrams by the WSK subsystem by calling a datagram socket's *WskReceiveFromEvent* event callback function.

```C++
// A datagram socket's WskReceiveFromEvent
// event callback function
NTSTATUS WSKAPI
  WskReceiveFromEvent(
    PVOID SocketContext,
    ULONG Flags,
    PWSK_DATAGRAM_INDICATION DataIndication
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

    // Return status indicating the datagrams were received
    return STATUS_SUCCESS;
  }

  // Error
  else
  {
    // Close the socket
    ...

    // Return success since no datagrams were indicated
    return STATUS_SUCCESS;
  }
}
```

If a datagram socket's [*WskReceiveFromEvent*](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive_from_event) event callback function does not retrieve all of the datagrams from the list of [**WSK\_DATAGRAM\_INDICATION**](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_datagram_indication) structures pointed to by the *DataIndication* parameter, it can retain the list for further processing by returning STATUS\_PENDING. In this situation, the WSK application must call the [**WskRelease**](/previous-versions/windows/hardware/drivers/ff571144(v=vs.85)) function to release the list of WSK\_DATAGRAM\_INDICATION structures back to the WSK subsystem after it has completed retrieving all of the datagrams from the structures in the list.

 

