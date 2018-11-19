---
title: Failure to Validate Variable-Length Buffers
description: Failure to Validate Variable-Length Buffers
ms.assetid: 0cc4be22-8197-421a-a5a6-2e7b89a79a38
keywords: ["input buffers WDK kernel", "variable-length input buffers WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Failure to Validate Variable-Length Buffers





Drivers often accept input buffers with fixed headers and trailing variable length data, as in the following example:

```cpp
   typedef struct _WAIT_FOR_BUFFER {
      LARGE_INTEGER Timeout;
      ULONG NameLength;
      BOOLEAN TimeoutSpecified;
      WCHAR Name[1];
   } WAIT_FOR_BUFFER, *PWAIT_FOR_BUFFER;

   if (InputBufferLength < sizeof(WAIT_FOR_BUFFER)) {
      IoCompleteRequest( Irp, STATUS_INVALID_PARAMETER );
      return( STATUS_INVALID_PARAMETER );
   }

   WaitBuffer = Irp->AssociatedIrp.SystemBuffer;

   if (FIELD_OFFSET(WAIT_FOR_BUFFER, Name[0]) +
          WaitBuffer->NameLength > InputBufferLength) {
       IoCompleteRequest( Irp, STATUS_INVALID_PARAMETER );
       return( STATUS_INVALID_PARAMETER );
   }
```

If **WaitBuffer-&gt;NameLength** is a very large ULONG value, adding it to the offset could cause an integer overflow. Instead, a driver should subtract the offset from the **InputBufferLength**, and compare the result with **WaitBuffer-&gt;NameLength**, as in the following example:

```cpp
   if (InputBufferLength < sizeof(WAIT_FOR_BUFFER)) {
      IoCompleteRequest( Irp, STATUS_INVALID_PARAMETER );
      Return( STATUS_INVALID_PARAMETER );
   }

   WaitBuffer = Irp->AssociatedIrp.SystemBuffer;

   if ((InputBufferLength -
         FIELD_OFFSET(WAIT_FOR_BUFFER, Name[0])  >
         WaitBuffer->NameLength) {
      IoCompleteRequest( Irp, STATUS_INVALID_PARAMETER );
      return( STATUS_INVALID_PARAMETER );
   }
```

The subtraction above cannot underflow because the first **if** statement ensures that the **InputBufferLength** is greater than or equal to the size of **WAIT\_FOR\_BUFFER**.

The following shows a more complicated overflow problem:

```cpp
   case IOCTL_SET_VALUE:
      dwSize = sizeof(SET_VALUE);

      if (inputBufferLength < dwSize) {
         ntStatus = STATUS_BUFFER_TOO_SMALL;
         break;
      }

      dwSize = FIELD_OFFSET(SET_VALUE, pInfo[0]) +
                  pSetValue->NumEntries * sizeof(SET_VALUE_INFO);

      if (inputBufferLength < dwSize) {
         ntStatus = STATUS_BUFFER_TOO_SMALL;
         break;
      }
```

In this example, an integer overflow can occur during multiplication. If the size of the **SET\_VALUE\_INFO** structure is a multiple of 2, a **NumEntries** value such as 0x80000000 results in an overflow, when the bits are shifted left during multiplication. However, the buffer size will nevertheless pass the validation test, because the overflow causes **dwSize** to appear quite small. To avoid this problem, subtract the lengths as in the previous example, divide by **sizeof**(**SET\_VALUE\_INFO**), and compare the result with **NumEntries**.

 

 




