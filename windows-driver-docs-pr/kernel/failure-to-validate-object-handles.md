---
title: Failure to Validate Object Handles
description: Failure to Validate Object Handles
ms.assetid: 67d52ca8-4e86-4fe2-a541-f7a0e4040b93
keywords: ["reliability WDK kernel , object handle validation", "validation failures WDK kernel", "object handles WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Failure to Validate Object Handles





Some drivers must manipulate objects passed to them by callers or must handle two file objects at the same time. For example, a modem driver might receive a handle to an event object, or a network driver might receive handles to two different file objects. The driver must validate these handles. Because they are passed by a caller, and not through the I/O manager, the I/O manager cannot perform any validation checks.

For example, in the following code snippet, the driver has been passed the handle **AscInfo-&gt;AddressHandle**, but has not validated it before calling [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679):

```cpp
   //
   // This handle is embedded in a buffered request.
   //
   status = ObReferenceObjectByHandle(
                      AscInfo->AddressHandle,
                      0,
                      NULL,
                      KernelMode,
                      &fileObject,
                      NULL);

   if (NT_SUCCESS(status)) {
       if ( (fileObject->DeviceObject == DeviceObject) &&
            (fileObject->FsContext2 == TRANSPORT_SOCK) ) {
```

Although the call to **ObReferenceObjectByHandle** succeeds, the code fails to ensure that the returned pointer references a file object; it trusts the caller to pass in the correct information.

Even if all the parameters for the call to **ObReferenceObjectByHandle** are correct, and the call succeeds, a driver can still get unexpected results if the file object is not intended for its driver. In the following code fragment, the driver assumes that a successful call returns a pointer to the file object it expected:

```cpp
   status = ObReferenceObjectByHandle (
                             AcpInfo->Handle,
                             0L,
                             DesiredAccess,
                             *IoFileObjectType,
                             Irp->RequestorMode,
                             (PVOID *)&AcpEndpointFileObject,
                             NULL);

   if ( !NT_SUCCESS(status) ) {
      goto complete;
   }
   AcpEndpoint = AcpEndpointFileObject->FsContext;

   if ( AcpEndpoint->Type != BlockTypeEndpoint ) 
```

Although **ObReferenceObjectByHandle** returns a pointer to a file object, the driver has no guarantee that the pointer references the file object it expected. In this case, the driver should validate the pointer before accessing the driver-specific data at **AcpEndpointFileObject-&gt;FsContext**.

To avoid such problems, a driver should check for valid data, as follows:

-   Check the object type to make sure it is what the driver expects.

-   Ensure that the requested access is appropriate for the object type and required tasks. If your driver performs a fast file copy, for instance, make sure the handle has read access.

-   Be sure to specify the correct access mode (**UserMode** or **KernelMode**) and that the access mode is compatible with the access requested.

-   If the driver expects a handle to a file object that the driver itself created, validate the handle against the device object or driver. However, be careful not to break filters that send I/O requests for strange devices.

-   If your driver supports multiple kinds of file objects (such as the control channels, address objects, and connections of TDI drivers or Volume, Directory, and File objects of file systems), make sure you have a way to differentiate them.

 

 




