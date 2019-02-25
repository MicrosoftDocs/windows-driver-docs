---
title: Enabling and Disabling Event Callback Functions
description: Enabling and Disabling Event Callback Functions
ms.assetid: 52654788-31e2-47c1-8154-f40c42168708
keywords:
- WSK WDK networking , events
- events WDK Winsock Kernel
- functions WDK Winsock Kernel
- event callback functions WDK Winsock Kernel
- SO_WSK_EVENT_CALLBACK
- WSK_SET_STATIC_EVENT_CALLBACKS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling and Disabling Event Callback Functions


A Winsock Kernel (WSK) application can implement event callback functions that the WSK subsystem calls asynchronously to notify the application when certain [events](winsock-kernel-events.md) occur on a socket. A WSK application can provide a client [dispatch table](winsock-kernel-dispatch-tables.md) structure to the WSK subsystem whenever it creates a socket or accepts a socket on a listening socket. This dispatch table contains pointers to the WSK application's event callback functions for the new socket. If a WSK application does not implement any event callback functions for a particular socket, then it does not need to provide a client dispatch table structure to the WSK subsystem for that socket.

All of a socket's event callback functions, except for a listening socket's [*WskInspectEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571137) and [*WskAbortEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571108) event callback functions, can be enabled or disabled by using the [**SO\_WSK\_EVENT\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff570834) socket option. A WSK application can enable multiple event callback functions on a socket at the same time. However, a WSK application must disable each event callback function individually.

The following code example shows how a WSK application can use the SO\_WSK\_EVENT\_CALLBACK socket option to enable the [*WskDisconnectEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571130) and [*WskReceiveEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571140) event callback functions on a connection-oriented socket.

```C++
// Function to enable the WskDisconnectEvent and WskReceiveEvent
// event callback functions on a connection-oriented socket
NTSTATUS
  EnableDisconnectAndRecieveCallbacks(
    PWSK_SOCKET Socket
    )
{
  PWSK_PROVIDER_CONNECTION_DISPATCH Dispatch;
  WSK_EVENT_CALLBACK_CONTROL EventCallbackControl;
  NTSTATUS Status;

  // Get pointer to the socket&#39;s provider dispatch structure
  Dispatch =
    (PWSK_PROVIDER_CONNECTION_DISPATCH)(Socket->Dispatch);

  // Specify the WSK NPI identifier
  EventCallbackControl.NpiId = &NPI_WSK_INTERFACE_ID;

  // Set the event flags for the event callback functions that
  // are to be enabled on the socket
  EventCallbackControl.EventMask =
    WSK_EVENT_DISCONNECT | WSK_EVENT_RECEIVE;

  // Initiate the control operation on the socket
  Status =
    Dispatch->WskControlSocket(
      Socket,
      WskSetOption,
      SO_WSK_EVENT_CALLBACK,
      SOL_SOCKET,
      sizeof(WSK_EVENT_CALLBACK_CONTROL),
      &EventCallbackControl,
      0,
      NULL,
      NULL,
      NULL  // No IRP for this control operation
      );

  // Return the status of the call to WskControlSocket()
  return Status;
}
```

The following code example shows how a WSK application can use the [**SO\_WSK\_EVENT\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff570834) socket option to disable the [*WskReceiveEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571140) event callback functions on a connection-oriented socket.

```C++
// Prototype for the disable disconnect IoCompletion routine
NTSTATUS
  DisableDisconnectComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    );

// Function to disable the WskDisconnectEvent event
// callback functions on a connection-oriented socket
NTSTATUS
  DisableDisconnectCallback(
    PWSK_SOCKET Socket
    )
{
  PWSK_PROVIDER_CONNECTION_DISPATCH Dispatch;
  PIRP Irp;
  WSK_EVENT_CALLBACK_CONTROL EventCallbackControl;
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
 DisableDisconnectComplete,
    Socket,  // Use the socket object for the context
    TRUE,
    TRUE,
    TRUE
    );

  // Specify the WSK NPI identifier
  EventCallbackControl.NpiId = &NPI_WSK_INTERFACE_ID;

  // Set the event flag for the event callback function that
  // is to be disabled on the socket along with the disable flag
  EventCallbackControl.EventMask =
    WSK_EVENT_DISCONNECT | WSK_EVENT_DISABLE;

  // Initiate the control operation on the socket
  Status =
    Dispatch->WskControlSocket(
      Socket,
      WskSetOption,
      SO_WSK_EVENT_CALLBACK,
      SOL_SOCKET,
      sizeof(WSK_EVENT_CALLBACK_CONTROL),
      &EventCallbackControl,
      0,
      NULL,
      NULL,
      Irp
      );

  // Return the status of the call to WskControlSocket()
  return Status;
}

// Disable disconnect IoCompletion routine
NTSTATUS
  DisableDisconnectComplete(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PVOID Context
    )
{
  UNREFERENCED_PARAMETER(DeviceObject);

  PWSK_SOCKET Socket;

  // Check the result of the control operation
  if (Irp->IoStatus.Status == STATUS_SUCCESS)
  {
    // The WskDisconnectEvent event callback
    // function is now disabled

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

For listening sockets, the [*WskInspectEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571137) and [*WskAbortEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571108) event callback functions are enabled only if the WSK application enables conditional accept mode on the socket. A WSK application enables conditional accept mode on a listening socket by setting the [**SO\_CONDITIONAL\_ACCEPT**](https://msdn.microsoft.com/library/windows/hardware/ff570829) socket option for the socket prior to binding the socket to a local transport address. For more information about how to set socket options, see [Performing Control Operations on a Socket](performing-control-operations-on-a-socket.md).

After conditional accept mode has been enabled on a listening socket, the socket's *WskInspectEvent* and *WskAbortEvent* event callback functions cannot be disabled. For more information about conditionally accepting incoming connections on listening sockets, see [Listening for and Accepting Incoming Connections](listening-for-and-accepting-incoming-connections.md).

A listening socket can automatically enable event callback functions on connection-oriented sockets that are accepted by the listening socket's [*WskAcceptEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571120) event callback function. A WSK application automatically enables these callback functions by enabling the connection-oriented socket event callback functions on the listening socket. For more information about this process, see [**SO\_WSK\_EVENT\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff570834).

If a WSK application always enables certain event callback functions on every socket that it creates, the application can configure the WSK subsystem to automatically enable those event callback functions by using the [**WSK\_SET\_STATIC\_EVENT\_CALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff571181) client control operation. The event callback functions that are enabled in this manner are always enabled and cannot be disabled or re-enabled later by the WSK application. If a WSK application always enables certain event callback functions on every socket that it creates, the application should use this method to automatically enable those event callback functions because it will yield much better performance.

The following code example shows how a WSK application can use the WSK\_SET\_STATIC\_EVENT\_CALLBACKS client control operation to automatically enable the [*WskReceiveFromEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571142) event callback function on datagram sockets and the [*WskReceiveEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571140) event callback function on connection-oriented sockets.

```C++
// Function to set static event callbacks
NTSTATUS
  SetStaticEventCallbacks(
    PWSK_APP_BINDING_CONTEXT BindingContext,
    )
{
  WSK_EVENT_CALLBACK_CONTROL EventCallbackControl;
  NTSTATUS Status;

  // Specify the WSK NPI identifier
  EventCallbackControl.NpiId = &NPI_WSK_INTERFACE_ID;

  // Set the event flags for the event callback functions that
  // are to be automatically enabled on every new socket
  EventCallbackControl.EventMask =
    WSK_EVENT_RECEIVE_FROM | WSK_EVENT_RECEIVE;

  // Perform client control operation
  Status =
    BindingContext->
      WskProviderDispatch->
        WskControlClient(
          BindingContext->WskClient,
          WSK_SET_STATIC_EVENT_CALLBACKS,
          sizeof(WSK_EVENT_CALLBACK_CONTROL),
          &EventCallbackControl,
          0,
          NULL,
          NULL,
          NULL  // No IRP for this control operation
          );

  // Return status of client control operation
  return Status;
}
```

If a WSK application uses the WSK\_SET\_STATIC\_EVENT\_CALLBACKS client control operation to automatically enable certain event callback functions, it must do so before it creates any sockets.

 

 





