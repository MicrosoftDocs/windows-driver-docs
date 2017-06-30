---
title: Failure to Validate Object Handles
author: windows-driver-content
description: Failure to Validate Object Handles
ms.assetid: 67d52ca8-4e86-4fe2-a541-f7a0e4040b93
keywords: ["reliability WDK kernel , object handle validation", "validation failures WDK kernel", "object handles WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Failure to Validate Object Handles


## <a href="" id="ddk-failure-to-validate-object-handles-kg"></a>


Some drivers must manipulate objects passed to them by callers or must handle two file objects at the same time. For example, a modem driver might receive a handle to an event object, or a network driver might receive handles to two different file objects. The driver must validate these handles. Because they are passed by a caller, and not through the I/O manager, the I/O manager cannot perform any validation checks.

For example, in the following code snippet, the driver has been passed the handle **AscInfo-&gt;AddressHandle**, but has not validated it before calling [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679):

```
   //
   // This handle is embedded in a buffered request.
   //
   status = ObReferenceObjectByHandle(
                      AscInfo->AddressHandle,
                      0,
                      NULL,
                      KernelMode,
                      &amp;fileObject,
                      NULL);

   if (NT_SUCCESS(status)) {
       if ( (fileObject->DeviceObject == DeviceObject) &amp;&amp;
            (fileObject->FsContext2 == TRANSPORT_SOCK) ) {
```

Although the call to **ObReferenceObjectByHandle** succeeds, the code fails to ensure that the returned pointer references a file object; it trusts the caller to pass in the correct information.

Even if all the parameters for the call to **ObReferenceObjectByHandle** are correct, and the call succeeds, a driver can still get unexpected results if the file object is not intended for its driver. In the following code fragment, the driver assumes that a successful call returns a pointer to the file object it expected:

```
   status = ObReferenceObjectByHandle (
                             AcpInfo->Handle,
                             0L,
                             DesiredAccess,
                             *IoFileObjectType,
                             Irp->RequestorMode,
                             (PVOID *)&amp;AcpEndpointFileObject,
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Failure%20to%20Validate%20Object%20Handles%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


