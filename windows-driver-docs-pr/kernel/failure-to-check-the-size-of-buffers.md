---
title: Failure to Check the Size of Buffers
description: Failure to Check the Size of Buffers
ms.assetid: e9d9a5d9-19a5-4a1d-95f9-df2021c51c41
keywords: ["buffer size WDK kernel", "input buffers WDK kernel", "output buffers WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Failure to Check the Size of Buffers





When handling IOCTLs and FSCTLs that implement buffered I/O, a driver should always check the sizes of the input and output buffers to ensure that the buffers can hold all the requested data. If the request specifies FILE\_ANY\_ACCESS, as most driver IOCTLs and FSCTLs do, any caller that has a handle to the device has access to buffered IOCTL or FSCTL requests for that device, and could read or write data beyond the end of the buffer.

### Input Buffer Size

For example, assume that the following code appears in a routine that is called from a *Dispatch* routine, and that the driver has not validated the buffer sizes passed in the IRP:

```cpp
   switch (ControlCode)
      ...
      ...
      case IOCTL_NEW_ADDRESS:{
         tNEW_ADDRESS *pNewAddress = 
            pIrp->AssociatedIrp.SystemBuffer;

         pDeviceContext->Addr = RtlUlongByteSwap (pNewAddress->Address);
```

The example does not check the buffer sizes before the assignment statement (highlighted). As a result, the **pNewAddress-&gt;Address** reference in the next line can fault if the input buffer is not big enough to contain a tNEW\_ADDRESS structure.

The following code checks the buffer sizes, avoiding the potential problem:

```cpp
   case IOCTL_NEW_ADDRESS: {
      tNEW_ADDRESS *pNewAddress =
         pIrp->AssociatedIrp.SystemBuffer;

      if (pIrpSp->Parameters.DeviceIoControl.InputBufferLength >=
             sizeof(tNEW_ADDRESS)) {
         pDeviceContext->Addr = RtlUlongByteSwap (pNewAddress->Address);
```

Code to handle other buffered I/O, such as WMI requests that use variable size buffers, can have similar errors.

### Output Buffer Size

Output buffer problems are similar to input buffer problems. They can easily corrupt pool, and user-mode callers may be unaware that any error has occurred.

In the following example, the driver fails to check the size of the **SystemBuffer**:

```cpp
   case IOCTL_GET_INFO: {

       Info = Irp->AssociatedIrp.SystemBuffer;

       Info->NumIF = NumIF;
       ...
       ...
       Irp->IoStatus.Information =
             NumIF*sizeof(GET_INFO_ITEM)+sizeof(ULONG);
       Irp->IoStatus.Status = ntStatus;
   }
```

Assuming that the **NumIF** field of the system buffer specifies the number of input items, this example can set **IoStatus.Information** to a value larger than the output buffer and thus return too much information to the user-mode code. If an application is improperly coded, and calls with too small an output buffer, the preceding code could corrupt the pool by writing beyond the end of the system buffer.

Remember that the I/O manager assumes that the value in the **Information** field is valid. If a caller passes in a valid kernel-mode address for the output buffer and a size of zero bytes, serious problems can occur if the driver does not check the output buffer size and thus find the error.

 

 




