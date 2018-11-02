---
title: Using the _analysis_assume Function to Suppress False Defects
description: Using the _analysis_assume Function to Suppress False Defects
ms.assetid: eb71a664-ada5-44e3-b75d-b1a7348b115f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the \_analysis\_assume Function to Suppress False Defects


You can provide Static Driver Verifier (SDV) with additional information about your driver source code so that during verification you can suppress the reports of false defects. The false defects occur when SDV reports an apparent rule violation, but in a situation where the driver is acting correctly.

To provide SDV with this additional information, use the **\_\_analysis\_assume** function. The function has the following syntax:

```
__analysis_assume( expression ) 
```

Where *expression* can be any expression that is assumed to evaluate to **true**.

When you use this function, SDV assumes that the condition represented by the *expression* is **true** at the point where the **\_\_analysis\_assume** function appears. The **\_\_analysis\_assume** function is only used by the static analysis tools. The function is ignored by the compiler.

If you use **\_\_analysis\_assume**, it is critically important that you are certain of the validity of the assumption you are making. If it turns out that your assumption is **false**, either now or in the future, you could be suppressing a true defect. We recommend that you always add a comment to your code that explains why you are using the **\_\_analysis\_assume** function. If you cannot write a reason for the assumption, do not suppress the defect.

You should add the **\_\_analysis\_assume** function as needed, whenever you find false defects that you can safely suppress.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

In the following code example, the KMDF rule [RequestCompletedLocal](https://msdn.microsoft.com/library/windows/hardware/ff551609) reports a defect. This is a false defect because SDV cannot correctly interpret the **switch** statement and consequently does not enter the branch where the request is completed.

In this **switch** statement, there are six possible cases. The driver has defined six IOCTL codes, so the driver will definitely take one of the branches. If one of the branches is taken, the request is completed successfully.

```
VOID
PortIOEvtIoDeviceControl(
      __in WDFQUEUE     Queue,
      __in WDFREQUEST   Request,
      __in size_t       OutputBufferLength,
  __in size_t       InputBufferLength,
  __in ULONG        IoControlCode
     )
 
     PDEVICE_CONTEXT devContext = NULL;
     WDFDEVICE device;

     PAGED_CODE();
 
     device = WdfIoQueueGetDevice(Queue);
 
     devContext = PortIOGetDeviceContext(device);
 
     switch(IoControlCode)
         case IOCTL_GPD_READ_PORT_UCHAR:
         case IOCTL_GPD_READ_PORT_USHORT:
         case IOCTL_GPD_READ_PORT_ULONG:
             PortIOIoctlReadPort(devContext,
                                 Request,
                                 OutputBufferLength,
                                 InputBufferLength,
                                 IoControlCode);
             break;

 
         case IOCTL_GPD_WRITE_PORT_UCHAR:
         case IOCTL_GPD_WRITE_PORT_USHORT:
         case IOCTL_GPD_WRITE_PORT_ULONG:    
             PortIOIoctlWritePort(devContext,
                                  Request,
                                  OutputBufferLength,
                                  InputBufferLength,
                                  IoControlCode);
             break;
 
     }
 
}
```

To safely suppress the false defect, use the **\_\_analysis\_assume** function to specify that the *IoControlCode* is guaranteed to be one of the IOCTLs that the driver has defined.

```
VOID
PortIOEvtIoDeviceControl(
      __in WDFQUEUE     Queue,
      __in WDFREQUEST   Request,
      __in size_t       OutputBufferLength,
      __in size_t       InputBufferLength,
      __in ULONG        IoControlCode
     )
 
     PDEVICE_CONTEXT devContext = NULL;
     WDFDEVICE device;

     PAGED_CODE();
 
     device = WdfIoQueueGetDevice(Queue);
 
     devContext = PortIOGetDeviceContext(device);

/* Use __analysis_assume to suppress a false defect for the SDV RequestCompletedLocal rule. 
There are only 6 possible IOCTLs for IoControlCode; each case is covered in the switch statement.
*/

 __analysis_assume( IoControlCode == IOCTL_GPD_READ_PORT_UCHAR || \
                       IoControlCode == IOCTL_GPD_READ_PORT_USHORT|| \
                       IoControlCode == IOCTL_GPD_READ_PORT_ULONG || \
                       IoControlCode == IOCTL_GPD_WRITE_PORT_UCHAR|| \
                       IoControlCode == IOCTL_GPD_WRITE_PORT_USHORT|| \
                       IoControlCode == IOCTL_GPD_WRITE_PORT_ULONG);

     switch(IoControlCode)
         case IOCTL_GPD_READ_PORT_UCHAR:
         case IOCTL_GPD_READ_PORT_USHORT:
         case IOCTL_GPD_READ_PORT_ULONG:
             PortIOIoctlReadPort(devContext,
                                 Request,
                                 OutputBufferLength,
                                 InputBufferLength,
                                 IoControlCode);
             break;

 
         case IOCTL_GPD_WRITE_PORT_UCHAR:
         case IOCTL_GPD_WRITE_PORT_USHORT:
         case IOCTL_GPD_WRITE_PORT_ULONG:    
             PortIOIoctlWritePort(devContext,
                                  Request,
                                  OutputBufferLength,
                                  InputBufferLength,
                                  IoControlCode);
             break;
 
     }
 
}
```

For another example of how you can use **\_\_analysis\_assume**, see the example code that is used in [Using \_\_sdv\_save\_request and \_\_sdv\_retrieve\_request for Deferred Procedure Calls](using---sdv-save-request-and---sdv-retrieve-request-for-deferred-proce.md). The example shows how to use **\_\_sdv\_save\_request** and **\_\_sdv\_retrieve\_request** for DPCs (workitems, Timers and so on). The **\_\_analysis\_assume** function is used to suppress false defects that might otherwise result.

 

 





