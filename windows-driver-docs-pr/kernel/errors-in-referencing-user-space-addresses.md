---
title: Errors in Referencing User-Space Addresses
author: windows-driver-content
description: Errors in Referencing User-Space Addresses
ms.assetid: 87944805-e4ba-431e-b673-b0125dc9ec24
keywords: ["reliability WDK kernel , user-space addresses", "user-space address referencing WDK kernel", "referencing user-space address", "embedded pointers WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Errors in Referencing User-Space Addresses


## <a href="" id="ddk-errors-in-referencing-user-space-addresses-kg"></a>


Any driver, whether supporting IRPs or fast I/O operations, should validate any address in user space before trying to use it. The I/O manager does not validate such addresses, nor does it validate pointers that are embedded in buffers passed to drivers.

### <a href="" id="failure-to-validate-addresses-passed-in-method-neither-ioctls-and-fsctls"></a>Failure to Validate Addresses Passed in METHOD\_NEITHER IOCTLs and FSCTLs

The I/O manager does no validation whatsoever for METHOD\_NEITHER IOCTLs and FSCTLs. To ensure that user-space addresses are valid, the driver must use the [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876) and [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879) routines, enclosing all buffer references in **try/except** blocks.

In the following example, the driver assumes that the value passed in the **Type3InputBuffer** represents a valid address.

```
   case IOCTL_GET_HANDLER:
   {
      PULONG EntryPoint;

      EntryPoint =
         IrpSp->Parameters.DeviceIoControl.Type3InputBuffer; 
      *EntryPoint = (ULONG)DriverEntryPoint; 
      ...
   }
```

The following code avoids this problem:

```
   case IOCTL_GET_HANDLER:
   {
      PULONG_PTR EntryPoint;

      EntryPoint =
         IrpSp->Parameters.DeviceIoControl.Type3InputBuffer;
 
      try
      {
         if (Irp->RequestorMode != KernelMode)
         { 
            ProbeForWrite(EntryPoint,
                          sizeof(ULONG_PTR),
                          TYPE_ALIGNMENT(ULONG_PTR));
         }
         *EntryPoint = (ULONG_PTR)DriverEntryPoint;
      }
      except(EXCEPTION_EXECUTE_HANDLER)
      {
        ...
      }
      ...
   }
```

Note also that the correct code casts **DriverEntryPoint** to a ULONG\_PTR, instead of a ULONG. This change allows for use in a 64-bit Windows environment.

### Failure to validate pointers embedded in buffered I/O requests

Often drivers embed pointers within buffered requests, as in the following example:

```
   struct ret_buf
   {
      void  *arg;  // Pointer embedded in request
      int  rval;
   };

   pBuf = Irp->AssociatedIrp.SystemBuffer;
   ...
   arg = pBuf->arg;  // Fetch the embedded pointer
   ...
   // If the arg pointer is not valid, the following
   // statement can corrupt the system:
   RtlMoveMemory(arg, &amp;info, sizeof(info));
```

In this example, the driver should validate the embedded pointer by using the **Probe*Xxx*** routines enclosed in a **try/except** block in the same way as for the METHOD\_NEITHER IOCTLs described earlier. Although embedding a pointer allows a driver to return extra information, a driver can more efficiently achieve the same result by using a relative offset or a variable length buffer.

For more information about using **try/except** blocks to handle invalid addresses, see [Handling Exceptions](handling-exceptions.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Errors%20in%20Referencing%20User-Space%20Addresses%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


