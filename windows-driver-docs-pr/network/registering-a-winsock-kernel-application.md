---
title: Registering a Winsock Kernel Application
description: Registering a Winsock Kernel Application
ms.assetid: aaba39b8-8609-46e6-906d-3f050d91af7f
keywords:
- Winsock Kernel WDK networking , registering
- registering Winsock Kernel applications
- WSK WDK networking , registering
- WSK WDK networking , provider NPI captures
- capturing WSK provider NPI WDK networking
- client objects WDK Winsock Kernel
- WskRegister
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering a Winsock Kernel Application


### WSK Client Object Registration

A Winsock Kernel (WSK) application must register as a WSK client by calling the [**WskRegister**](https://msdn.microsoft.com/library/windows/hardware/ff571143) function. **WskRegister** requires the WSK application to initialize and pass a pointer to its WSK client's [Network Programming Interface (NPI)](network-programming-interface.md)(a [**WSK\_CLIENT\_NPI**](https://msdn.microsoft.com/library/windows/hardware/ff571163) structure) and a WSK registration object (a [**WSK\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff571178) structure) that will be initialized by **WskRegister** upon successful return.

The following code example shows how a WSK application can register as a WSK client.

```C++
// Include the WSK header file
#include "wsk.h"

// WSK Client Dispatch table that denotes the WSK version
// that the WSK application wants to use and optionally a pointer
// to the WskClientEvent callback function
const WSK_CLIENT_DISPATCH WskAppDispatch = {
  MAKE_WSK_VERSION(1,0), // Use WSK version 1.0
  0,    // Reserved
  NULL  // WskClientEvent callback not required for WSK version 1.0
};

// WSK Registration object
WSK_REGISTRATION WskRegistration;

// DriverEntry function
NTSTATUS
  DriverEntry(
    PDRIVER_OBJECT DriverObject,
    PUNICODE_STRING RegistryPath
    )
{
  NTSTATUS Status;
  WSK_CLIENT_NPI wskClientNpi;

  .
  . 
  .

  // Register the WSK application
  wskClientNpi.ClientContext = NULL;
  wskClientNpi.Dispatch = &WskAppDispatch;
  Status = WskRegister(&wskClientNpi, &WskRegistration);

  if(!NT_SUCCESS(Status)) {
      .
      .
      .
      return Status;
  }

  .
  . 
  .
}
```

A WSK application is not required to call [**WskRegister**](https://msdn.microsoft.com/library/windows/hardware/ff571143) from within its **DriverEntry** function. For example, if a WSK application is a subcomponent of a complex driver, the registration of the application might occur only when the WSK application subcomponent is activated.

A WSK application must keep the [**WSK\_CLIENT\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff571159) structure passed to **WskRegister** valid and resident in memory until [**WskDeregister**](https://msdn.microsoft.com/library/windows/hardware/ff571128) is called and the registration is no longer valid. The [**WSK\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff571178) structure must also be kept valid and resident in memory until the WSK application stops making calls to the other [WSK registration functions](https://msdn.microsoft.com/library/windows/hardware/ff571179). The previous code example keeps these two structures in the global data section of the driver, thereby keeping the structure data resident in memory until the driver is unloaded.

### WSK Provider NPI Capture

After a WSK application has registered as a WSK client with [**WskRegister**](https://msdn.microsoft.com/library/windows/hardware/ff571143), it must use the [**WskCaptureProviderNPI**](https://msdn.microsoft.com/library/windows/hardware/ff571122) function to capture the WSK provider NPI from the WSK subsystem in order to start using the WSK interface.

Because the WSK subsystem might not yet be ready when a WSK application attempts to capture the WSK provider NPI, the **WskCaptureProviderNPI** function allows the WSK application to poll or wait for the WSK subsystem to become ready as follows:

-   If the *WaitTimeout* parameter is WSK\_NO\_WAIT, the function will always return immediately without waiting.

-   If *WaitTimeout* is WSK\_INFINITE\_WAIT, the function will wait until the WSK subsystem becomes ready.

-   If *WaitTimeout* is any other value, the function will return either when the WSK subsystem becomes ready or when the wait time, in milliseconds, reaches the value of *WaitTimeout*, whichever occurs first.

**Important**  To avoid adversely affecting the start of other drivers and services, a WSK application that calls **WskCaptureProviderNPI** from its **DriverEntry** function should not set the *WaitTimeout* parameter to WSK\_INFINITE\_WAIT or an excessive wait time. Also, if a WSK application starts very early in the system startup phase, it should wait for the WSK subsystem to become ready in a different worker thread than the one in which **DriverEntry** runs.

 

If the call to **WskCaptureProviderNPI** fails with STATUS\_NOINTERFACE, the WSK application can use the [**WskQueryProviderCharacteristics**](https://msdn.microsoft.com/library/windows/hardware/ff571138) function to discover the range of WSK NPI versions supported by the WSK subsystem. The WSK application can call **WskDeregister** to unregister its current registration instance, and then register again by using a different [**WSK\_CLIENT\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff571159) instance that uses a supported WSK NPI version.

When **WskCaptureProviderNPI** returns successfully, its *WskProviderNpi* parameter points to a WSK provider NPI ( [**WSK\_PROVIDER\_NPI**](https://msdn.microsoft.com/library/windows/hardware/ff571177)) ready for use by the WSK application. The WSK\_PROVIDER\_NPI structure contains pointers to the WSK client object ( [**WSK\_CLIENT**](https://msdn.microsoft.com/library/windows/hardware/ff571155)) and the [**WSK\_PROVIDER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff571175) dispatch table of WSK functions that the WSK application can use to create WSK sockets and perform other operations on the WSK client object. After the WSK application is finished using the WSK\_PROVIDER\_DISPATCH functions, it must release the WSK provider NPI by calling [**WskReleaseProviderNPI**](https://msdn.microsoft.com/library/windows/hardware/ff571145).

The following code example shows how a WSK application can capture the WSK provider NPI, use it to create a socket, and then release it.

```C++
// WSK application routine that waits for WSK subsystem
// to become ready and captures the WSK Provider NPI
NTSTATUS
  WskAppWorkerRoutine(
    )
{
  NTSTATUS Status;
  WSK_PROVIDER_NPI wskProviderNpi;
 
  // Capture the WSK Provider NPI. If WSK subsystem is not ready yet,
  // wait until it becomes ready.
  Status = WskCaptureProviderNPI(
    &WskRegistration, // must have been initialized with WskRegister
    WSK_INFINITE_WAIT,
    &wskProviderNpi
    );

  if(!NT_SUCCESS(Status))
  {
    // The WSK Provider NPI could not be captured.
    if( Status == STATUS_NOINTERFACE ) {
      // WSK application&#39;s requested version is not supported
    }
    else if( status == STATUS_DEVICE_NOT_READY ) {
      // WskDeregister was invoked in another thread thereby causing
      // WskCaptureProviderNPI to be canceled.
    } 
    else {
      // Some other unexpected failure has occurred
    }

    return Status;
  }

  // The WSK Provider NPI has been captured.
  // Create and set up a listening socket that accepts
   // incoming connections.
  Status = CreateListeningSocket(&wskProviderNpi, ...);

  // The WSK Provider NPI will not be used any more.
  // So, release it here immediately.
  WskReleaseProviderNPI(&WskRegistration);

  // Return result of socket creation routine
  return Status;

}
```

A WSK application can call [**WskCaptureProviderNPI**](https://msdn.microsoft.com/library/windows/hardware/ff571122) more than once. For each call to **WskCaptureProviderNPI** that returns successfully, there must be a corresponding call to [**WskReleaseProviderNPI**](https://msdn.microsoft.com/library/windows/hardware/ff571145). A WSK application must not make any further calls to the functions in [**WSK\_PROVIDER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff571175) after calling **WskReleaseProviderNPI**.

 

 





