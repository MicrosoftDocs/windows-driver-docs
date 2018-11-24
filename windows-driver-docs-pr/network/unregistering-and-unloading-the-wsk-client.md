---
title: Unregistering and Unloading the WSK Client
description: Unregistering and Unloading the WSK Client
ms.assetid: dd9030b1-271f-46e4-9139-b49903ca8313
keywords:
- Network Module Registrar WDK Winsock Kernel
- NMR WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unregistering and Unloading the WSK Client


Any Winsock Kernel (WSK) application that uses the [Network Module Registrar (NMR)](network-module-registrar2.md) for attaching to the WSK subsystem must unregister with NMR before unloading. When a WSK application unregisters with the NMR by calling the [**NmrDeregisterClient**](https://msdn.microsoft.com/library/windows/hardware/ff568774) function, the NMR calls the application's [*ClientDetachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544908) callback function so that the application can detach itself from the WSK subsystem as part of the WSK application's unregistration process.

Furthermore, in the unlikely, but possible, case of the WSK subsystem unregistering with the NMR, the NMR also calls the WSK application's *ClientDetachProvider* callback function so that the application can detach itself from the WSK subsystem as part of the WSK subsystem's unregistration process.

The NMR calls a WSK application's *ClientDetachProvider* callback function only once. If both the WSK application and the WSK subsystem unregister with the NMR, the NMR calls the WSK application's *ClientDetachProvider* callback function only after the first unregistration is initiated.

If there are no calls in progress to any of the WSK functions in WSK\_PROVIDER\_DISPATCH at the time that the NMR calls the WSK application's *ClientDetachProvider* callback function, the WSK application should return STATUS\_SUCCESS from its *ClientDetachProvider* callback function. Otherwise, the WSK application must return STATUS\_PENDING from its *ClientDetachProvider* callback function, and it must call the [**NmrClientDetachProviderComplete**](https://msdn.microsoft.com/library/windows/hardware/ff568772) function after all of the calls in progress to the WSK functions in WSK\_PROVIDER\_DISPATCH have returned. A WSK application calls the **NmrClientDetachProviderComplete** function to notify the NMR that the application has detached from the WSK subsystem. However, the WSK subsystem will not allow the detachment procedure to be completed fully until all open sockets are closed by the WSK application. For more information, see [Closing a Socket](closing-a-socket.md).

After a WSK application has notified the NMR that detachment is complete, either by returning STATUS\_SUCCESS from its *ClientDetachProvider* callback function or by calling the **NmrClientDetachProviderComplete** function, the application must not make any further calls to any of the WSK functions in WSK\_PROVIDER\_DISPATCH.

If a WSK application implements a [*ClientCleanupBindingContext*](https://msdn.microsoft.com/library/windows/hardware/ff544904) callback function, the NMR calls the application's *ClientCleanupBindingContext* callback function after both the WSK application and the WSK subsystem have completed detachment from each other. A WSK application's *ClientCleanupBindingContext* callback function should perform any necessary cleanup of the data contained within the application's binding context structure. It should then free the memory for the binding context structure if the application dynamically allocated memory for the structure.

For example:

```C++
// ClientDetachProvider callback function
NTSTATUS
  ClientDetachProvider(
    IN PVOID ClientBindingContext
    )
{
  PWSK_APP_BINDING_CONTEXT BindingContext;

  // Get a pointer to the binding context
  BindingContext =
    (PWSK_APP_BINDING_CONTEXT)ClientBindingContext;

  // Check if there are no calls in progress to any WSK functions
  // in WSK_PROVIDER_DISPATCH and that there are no open sockets
  if (...)
  {
    // Return success status indicating that detachment is complete
    return STATUS_SUCCESS;
  }

  // There are calls in progress to one or more of the WSK functions
  // in WSK_PROVIDER_DISPATCH and/or one or more open sockets
  else
  {
    // Return pending status, indicating that detachment is pending
    // completion of the calls in progress to the WSK functions in
    // WSK_PROVIDER_DISPATCH and/or closing of the open sockets
    return STATUS_PENDING;

    // When all of the calls in progress to the WSK functions
    // in WSK_PROVIDER_DISPATCH are completed, the WSK application
    // must close all open sockets.
    //
    // After all sockets have been closed, the WSK application must
    // call the NmrClientDetachProviderComplete function with the
    // binding handle for the attachment to the WSK subsystem.
  }
}

// ClientCleanupBindingContext callback function
VOID
  ClientCleanupBindingContext(
    IN PVOID ClientBindingContext
    )
{
  PWSK_APP_BINDING_CONTEXT BindingContext;

  // Get a pointer to the binding context
  BindingContext =
    (PWSK_APP_BINDING_CONTEXT)ClientBindingContext;

  // Clean up the binding context structure
  ...

  // Free the memory for client&#39;s binding context structure
  ExFreePoolWithTag(
    BindingContext,
    BINDING_CONTEXT_POOL_TAG
    );
}
```

A WSK application's [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) function must ensure that the application is unregistered from the [NMR](network-module-registrar2.md) before the application is unloaded from system memory. A WSK application must not return from its *Unload* function until after it has been completely unregistered from the NMR. If the call to **NmrDeregisterClient** returns STATUS\_PENDING, the WSK application must call the **NmrWaitForClientDeregisterComplete** function to wait for the unregistration to complete before it returns from its *Unload* function.

For example:

```C++
// Variable containing the handle for registration with the NMR
HANDLE RegistrationHandle;

// Unload function
VOID
  Unload(
    IN PDRIVER_OBJECT DriverObject
    )
{
  NTSTATUS Status;

  // Unregister the WSK application from the NMR
  Status =
    NmrDeregisterClient(
      RegistrationHandle
      );

  // Check if pending
  if (Status == STATUS_PENDING)
  {
    // Wait for the unregistration to be completed
    NmrWaitForClientDeregisterComplete(
      RegistrationHandle
      );
  }
}
```

A WSK application is not required to call **NmrDeregisterClient** from within its *Unload* function. For example, if a WSK application is a subcomponent of a complex driver, the unregistration of the WSK application might occur when the WSK application subcomponent is deactivated. However, in such a situation the driver must still ensure that the WSK application has been completely unregistered from the NMR before returning from its *Unload* function.

 

 





