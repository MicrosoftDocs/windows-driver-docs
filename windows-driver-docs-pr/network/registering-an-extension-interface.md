---
title: Registering an Extension Interface
description: Registering an Extension Interface
ms.assetid: 33dc32da-9bc1-40b4-8737-ec132ec36708
keywords:
- Winsock Kernel WDK networking , extension interfaces
- WSK WDK networking , extension interfaces
- extension interfaces WDK Winsock Kernel
- registering Winsock Kernel extension interfaces
- SIO_WSK_REGISTER_EXTENSION
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering an Extension Interface


After a Winsock Kernel (WSK) application has successfully created a socket, it can register that socket for one or more of the [extension interfaces](winsock-kernel-extension-interfaces.md) that are supported by the WSK subsystem. A WSK application determines which set of extension interfaces are supported by the WSK subsystem by examining the **Version** member of the [**WSK\_PROVIDER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff571175) structure that the WSK subsystem returned to the application during attachment.

Each extension interface is defined by an NPI that is independent of the WSK NPI. Note, however, that the NPIs for extension interfaces do not support NPI-specific characteristics.

A WSK application registers for an extension interface by executing the [**SIO\_WSK\_REGISTER\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff570819) socket IOCTL operation on the socket. For more information about executing socket IOCTL operations, see [Performing Control Operations on a Socket](performing-control-operations-on-a-socket.md).

If a WSK application attempts to register a socket for an extension interface that is not supported by the WSK subsystem, the SIO\_WSK\_REGISTER\_EXTENSION socket IOCTL operation will return STATUS\_NOT\_SUPPORTED.

For example, suppose that an extension interface is defined as in the following code example.

```C++
const NPIID EXAMPLE_EXTIF_NPIID = {...};

typedef struct _EXAMPLE_EXTIF_PROVIDER_DISPATCH {
  .
  . // Function pointers for the functions that are
  . // defined by the extension interface.
  .
} EXAMPLE_EXTIF_PROVIDER_DISPATCH, *PEXAMPLE_EXTIF_PROVIDER_DISPATCH;

typedef struct _EXAMPLE_EXTIF_CLIENT_DISPATCH {
  .
  . // Function pointers for the callback functions
  . // that are defined by the extension interface.
  .
} EXAMPLE_EXTIF_CLIENT_DISPATCH, *PEXAMPLE_EXTIF_CLIENT_DISPATCH;
```

The following shows how a WSK application can register for this extension interface for a connection-oriented socket.

```C++
// Client dispatch structure for the extension interface
const EXAMPLE_EXTIF_CLIENT_DISPATCH ExtIfClientDispatch = {
  .
  . // The WSK application&#39;s callback functions
  . // for the extension interface
  .
};

// Context structure type for the example extension interface
typedef struct _EXAMPLE_EXTIF_CLIENT_CONTEXT
{
  const EXAMPLE_EXTIF_PROVIDER_DISPATCH *ExtIfProviderDispatch;
  PVOID ExtIfProviderContext;
    .
    .  // Other application-specific members
    .
} EXAMPLE_EXTIF_CLIENT_CONTEXT, *PEXAMPLE_EXTIF_CLIENT_CONTEXT;

// Function to register the example extension interface
NTSTATUS
  RegisterExampleExtIf(
    PWSK_SOCKET Socket,
    PEXAMPLE_EXTIF_CLIENT_CONTEXT ExtIfClientContext
    )
{
  PWSK_PROVIDER_CONNECTION_DISPATCH Dispatch;
  WSK_EXTENSION_CONTROL_IN ExtensionControlIn;
  WSK_EXTENSION_CONTROL_OUT ExtensionControlOut;
  NTSTATUS Status;

  // Get pointer to the socket&#39;s provider dispatch structure
  Dispatch =
    (PWSK_PROVIDER_CONNECTION_DISPATCH)(Socket->Dispatch);

  // Fill in the WSK_EXTENSION_CONTROL_IN structure
  ExtensionControlIn.NpiId = &EXAMPLE_EXTIF_NPIID;
  ExtensionControlIn.ClientContext = ExtIfClientContext;
  ExtensionControlIn.ClientDispatch = &ExtIfClientDispatch;

  // Initiate the IOCTL operation on the socket
  Status =
    Dispatch->WskControlSocket(
      Socket,
      WskIoctl,
      SIO_WSK_REGISTER_EXTENSION,
      0,
      sizeof(WSK_EXTENSION_CONTROL_IN),
      &ExtensionControlIn,
      sizeof(WSK_EXTENSION_CONTROL_OUT),
      &ExtensionControlOut,
      NULL,
      NULL  // No IRP used for this IOCTL operation
      );

  // Check result
  if (Status == STATUS_SUCCESS)
  {
    // Save provider dispatch table and provider context
    ExtIfClientContext->ExtIfProviderDispatch =
      (const EXAMPLE_EXTIF_PROVIDER_DISPATCH *)
        ExtensionControlOut.ProviderDispatch;
    ExtIfClientContext->ExtIfProviderContext =
      ExtensionControlOut.ProviderContext;
  }

  // Return the status of the call to WskControlSocket()
  return Status;
}
```

A WSK application registers for extension interfaces on a socket-by-socket basis.

 

 





