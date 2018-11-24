---
title: Errors in Referencing User-Space Addresses
description: Errors in Referencing User-Space Addresses
ms.assetid: 87944805-e4ba-431e-b673-b0125dc9ec24
keywords: ["reliability WDK kernel , user-space addresses", "user-space address referencing WDK kernel", "referencing user-space address", "embedded pointers WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Errors in Referencing User-Space Addresses





Any driver, whether supporting IRPs or fast I/O operations, should validate any address in user space before trying to use it. The I/O manager does not validate such addresses, nor does it validate pointers that are embedded in buffers passed to drivers.

### <a href="" id="failure-to-validate-addresses-passed-in-method-neither-ioctls-and-fsctls"></a>Failure to Validate Addresses Passed in METHOD\_NEITHER IOCTLs and FSCTLs

The I/O manager does no validation whatsoever for METHOD\_NEITHER IOCTLs and FSCTLs. To ensure that user-space addresses are valid, the driver must use the [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876) and [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879) routines, enclosing all buffer references in **try/except** blocks.

In the following example, the driver assumes that the value passed in the **Type3InputBuffer** represents a valid address.

```cpp
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

```cpp
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

```cpp
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
   RtlMoveMemory(arg, &info, sizeof(info));
```

In this example, the driver should validate the embedded pointer by using the **Probe*Xxx*** routines enclosed in a **try/except** block in the same way as for the METHOD\_NEITHER IOCTLs described earlier. Although embedding a pointer allows a driver to return extra information, a driver can more efficiently achieve the same result by using a relative offset or a variable length buffer.

For more information about using **try/except** blocks to handle invalid addresses, see [Handling Exceptions](handling-exceptions.md).

 

 




