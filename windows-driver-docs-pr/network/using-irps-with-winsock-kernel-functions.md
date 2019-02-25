---
title: Using IRPs with Winsock Kernel Functions
description: Using IRPs with Winsock Kernel Functions
ms.assetid: eb7af09c-2312-4127-a0dc-324b208c1455
keywords:
- Winsock Kernel WDK networking , IRPs
- WSK WDK networking , IRPs
- IRPs WDK Winsock Kernel
- functions WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using IRPs with Winsock Kernel Functions


The Winsock Kernel (WSK) [Network Programming Interface (NPI)](network-programming-interface.md) uses IRPs for asynchronous completion of network I/O operations. Each WSK function takes a pointer to an IRP as a parameter. The WSK subsystem completes the IRP after the operation performed by the WSK function is complete.

An IRP that a WSK application uses to pass to a WSK function can originate in one of the following ways.

-   The WSK application allocates the IRP by calling the [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) function. In this situation, the WSK application must allocate the IRP with at least one I/O stack location.

-   The WSK application reuses a completed IRP that it previously allocated. In this situation, the WSK must call the [**IoReuseIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549661) function to reinitialize the IRP.

-   The WSK application uses an IRP that was passed down to it either by a higher level driver or by the I/O manager. In this situation, the IRP must have at least one remaining I/O stack location available for use by the WSK subsystem.

After a WSK application has an IRP to use for calling a WSK function, it can set an [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for the IRP to be called when the IRP is completed by the WSK subsystem. A WSK application sets an **IoCompletion** routine for an IRP by calling the [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) function. Depending upon how the IRP originated, an **IoCompletion** routine is either required or optional.

-   If the WSK application allocated the IRP, or is reusing an IRP that it previously allocated, then it must set an **IoCompletion** routine for the IRP before calling a WSK function. In this situation, the WSK application must specify **TRUE** for the *InvokeOnSuccess*, *InvokeOnError*, and *InvokeOnCancel* parameters that are passed to the **IoSetCompletionRoutine** function to ensure that the **IoCompletion** routine is always called. Furthermore, the **IoCompletion** routine that is set for the IRP must always return STATUS\_MORE\_PROCESSING\_REQUIRED to terminate the completion processing of the IRP. If the WSK application is done using the IRP after the **IoCompletion** routine has been called, then it should call the [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113) function to free the IRP before returning from the **IoCompletion** routine. If the WSK application does not free the IRP then it can reuse the IRP for a call to another WSK function.

-   If the WSK application uses an IRP that was passed down to it by a higher level driver or by the I/O manager, it should set an **IoCompletion** routine for the IRP before calling the WSK function only if it must be notified when the operation performed by the WSK function has completed. If the WSK application does not set an **IoCompletion** routine for the IRP, then when the IRP is completed the IRP will be passed back up to the higher level driver or to the I/O manager as per normal IRP completion processing. If the WSK application sets an **IoCompletion** routine for the IRP, the **IoCompletion** routine can either return STATUS\_SUCCESS or STATUS\_MORE\_PROCESSING\_REQUIRED. If the **IoCompletion** routine returns STATUS\_SUCCESS, the IRP completion processing will continue normally. If the **IoCompletion** routine returns STATUS\_MORE\_PROCESSING\_REQUIRED, the WSK application must complete the IRP by calling [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) after it has finished processing the results of the operation that was performed by the WSK function. A WSK application should never free an IRP that was passed down to it by a higher level driver or by the I/O manager.

**Note**  If the WSK application sets an **IoCompletion** routine for an IRP that was passed down to it by a higher level driver or by the I/O manager, then the **IoCompletion** routine must check the **PendingReturned** member of the IRP and call the [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) function if the **PendingReturned** member is **TRUE**. For more information, see [Implementing an IoCompletion Routine](https://msdn.microsoft.com/library/windows/hardware/ff547084).

 

A WSK application does not initialize the IRPs that it passes to the WSK functions other than setting an **IoCompletion** routine. When a WSK application passes an IRP to a WSK function, the WSK subsystem sets up the next I/O stack location on behalf of the application.

The following code example shows how a WSK application can allocate and use an IRP when performing a receive operation on a socket.

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

The model shown in the previous example, where the WSK application allocates an IRP and then frees it in the completion routine, is the model that is used in the examples throughout the remainder of the WSK documentation.

The following code example shows how a WSK application can use an IRP that has been passed to it by a higher level driver or by the I/O manager when performing a receive operation on a socket.

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
    PWSK_BUF DataBuffer,
    PIRP Irp;  // IRP from a higher level driver or the I/O manager
    )
{
  PWSK_PROVIDER_CONNECTION_DISPATCH Dispatch;
  NTSTATUS Status;

  // Get pointer to the provider dispatch structure
  Dispatch =
    (PWSK_PROVIDER_CONNECTION_DISPATCH)(Socket->Dispatch);

  // Set the completion routine for the IRP such that it is
  // only called if the receive operation succeeds.
  IoSetCompletionRoutine(
    Irp,
    ReceiveComplete,
    DataBuffer,  // Use the data buffer for the context
    TRUE,
    FALSE,
    FALSE
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

  // Since the completion routine was only specified to
  // be called if the operation succeeds, this should
  // always be true.
  ASSERT(Irp->IoStatus.Status == STATUS_SUCCESS);

  // Check the pending status of the IRP
  if (Irp->PendingReturned == TRUE)
  {
    // Mark the IRP as pending
    IoMarkIrpPending(Irp);
  }

  // Get the pointer to the data buffer
  DataBuffer = (PWSK_BUF)Context;
 
  // Get the number of bytes received
  ByteCount = (ULONG)(Irp->IoStatus.Information);

  // Process the received data
  ...

  // Return STATUS_SUCCESS to continue the
  // completion processing of the IRP.
  return STATUS_SUCCESS;
}
```

For more information about using IRPs, see [Handling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff546847).

 

 





