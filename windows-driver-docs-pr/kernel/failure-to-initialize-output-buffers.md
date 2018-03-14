---
title: Failure to Initialize Output Buffers
author: windows-driver-content
description: Failure to Initialize Output Buffers
ms.assetid: 8c038a94-8506-44e3-ac7f-82b58d791124
keywords: ["output buffers WDK kernel", "initializing output buffers"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Failure to Initialize Output Buffers


## <a href="" id="ddk-failure-to-initialize-output-buffers-kg"></a>


Drivers should initialize all output buffers with zeros before returning them to the caller. Failing to initialize a buffer can result in garbage data in any uninitialized bytes.

In the following example, a driver returns garbage in unused bytes.

```
   case IOCTL_GET_NAME: {
      ...
      ...
      outputBufferLength = 
         ioStack->Parameters.DeviceIoControl.OutputBufferLength;
      outputBuffer = (PGET_NAME) Irp->AssociatedIrp.SystemBuffer;
 
      if (outputBufferLength >= sizeof(GET_NAME)) {
         length = outputBufferLength - sizeof(GET_NAME);
 
         ntStatus = IoGetDeviceProperty(
                        DeviceExtension->PhysicalDeviceObject,
                        DevicePropertyDriverKeyName,
                        length,
                        outputBuffer->DriverKeyName,
                        &length);

         outputBuffer->ActualLength =
                        length + sizeof(GET_NAME);

         Irp->IoStatus.Information = outputBufferLength;
 
      } else {
         ntStatus = STATUS_BUFFER_TOO_SMALL;
      }
```

Setting **IoStatus.Information** to the output buffer size causes the whole output buffer to be returned to the caller. The I/O manager does not initialize the data beyond the size of the input buffer—the input and output buffers overlap for a buffered request. Because the system support routine [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) does not write the entire buffer, this IOCTL returns uninitialized data to the caller.

Some drivers use the **Information** field to return codes that provide extra details about I/O requests. Before doing so, such drivers should check the IRP flags to ensure that IRP\_INPUT\_OPERATION is not set. When this flag is not set, the IOCTL or FSCTL does not have an output buffer, so the **Information** field need not supply a buffer size. In this case. the driver can safely use the **Information** field to return its own code.

 

 




