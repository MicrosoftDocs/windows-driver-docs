---
Description: How a USB multi-function device, called a composite driver, registers and unregisters the composite device with the underlying USB driver stack.
title: How to Register a Composite Device
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to Register a Composite Device


This topic describes how a driver of a USB multi-function device, called a composite driver, can register and unregister the composite device with the underlying USB driver stack. The Microsoft-provided driver, Usbccgp.sys, is the default composite driver that is loaded by Windows. The procedure in this topic applies to a custom Windows Driver Model (WDM)-based composite driver that replaces Usbccgp.sys.

A Universal Serial Bus (USB) device can provide multiple functions that are active simultaneously. Such multi-function devices are also known as *composite devices*. For example, a composite device might define a function for the keyboard functionality and another function for the mouse. The functions of the device are enumerated by the composite driver. The composite driver can manage those functions itself in a monolithic model or create physical device objects (PDOs) for each of the functions. Those individual PDOs are managed by their respective USB function drivers, the keyboard driver and the mouse driver.

The USB 3.0 specification defines the *function suspend and remote wake-up feature* that enables individual functions to enter and exit low-power states without affecting the power state of other functions or the entire device. For more information about the feature, see [How to Implement Function Suspend in a Composite Driver](how-to--implement-remote-and-function-wake-support.md).

To use the feature, the composite driver needs to register the device with the underlying USB driver stack. Because the feature applies to USB 3.0 devices, the composite driver must make sure that the underlying stack supports version USBD\_INTERFACE\_VERSION\_602. Through the registration request, the composite driver:

-   Informs the underlying USB driver stack that the driver is responsible for sending a request to arm a function for remote wake-up. The remote wake-up request is processed by the USB driver stack, which sends the necessary protocol requests to the device.
-   Obtains a list of function handles (one per function) assigned by the USB driver stack. The composite driver can then use a function handle in the driver's the request for remote wake-up of the function associated with the handle.

Typically a composite driver sends the registration request in the driver's AddDevice or the start-device routine to handle [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749). Consequently, the composite driver releases the resources that are allocated for the registration in the driver's unload routines such as stop-device ([**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755)) or remove-device routine ([**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738)).

### Prerequisites

Before sending the registration request, make sure that:

-   You have the number of functions in the device. That number can be derived the descriptors retrieved by the get-configuration request.
-   You have obtained a USBD handle in a previous call to [**USBD\_CreateHandle**](https://msdn.microsoft.com/library/windows/hardware/hh406241).
-   The underlying USB driver stack supports USB 3.0 devices. To do so, call [**USBD\_IsInterfaceVersionSupported**](https://msdn.microsoft.com/library/windows/hardware/hh406233) and pass USBD\_INTERFACE\_VERSION\_602 as the version to check.

For a code example, see [How to Implement Function Suspend in a Composite Driver](how-to--implement-remote-and-function-wake-support.md).
Instructions
------------

### Register a Composite Device

The following procedure describes how you should build and send a registration request to associate a composite driver with the USB driver stack.

1.  Allocate a [**COMPOSITE\_DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh450801) structure and initialize it by calling the [**COMPOSITE\_DEVICE\_CAPABILITIES\_INIT**](https://msdn.microsoft.com/library/windows/hardware/hh450803) macro.
2.  Set the **CapabilityFunctionSuspend** member of [**COMPOSITE\_DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh450801) to 1.
3.  Allocate a [**REGISTER\_COMPOSITE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/hh450898) structure and initialize the structure by calling the [**USBD\_BuildRegisterCompositeDevice**](https://msdn.microsoft.com/library/windows/hardware/hh406229) routine. In the call, specify the USBD handle, the initialized [**COMPOSITE\_DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh450801) structure, and the number of functions.
4.  Allocate an I/O request packet (IRP) by calling [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) and get a pointer to the IRP's first stack location ([**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)) by calling [**IoGetNextIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549266).
5.  Allocate memory for a buffer that is large enough to hold an array of function handles (USBD\_FUNCTION\_HANDLE). The number of elements in the array must be the number of PDOs.
6.  Build the request by setting the following members of the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659):
    -   Specify the type of request by setting **Parameters.DeviceIoControl.IoControlCode** to [**IOCTL\_INTERNAL\_USB\_REGISTER\_COMPOSITE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/hh450854).
    -   Specify the input parameter by setting **Parameters.Others.Argument1** to the address of the initialized [**REGISTER\_COMPOSITE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/hh450898) structure.
    -   Specify the output parameter by setting **AssociatedIrp.SystemBuffer** to the buffer that was allocated in step 5.

7.  Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to send the request by passing the IRP to the next stack location.

Upon completion, inspect the array of function handles that is returned by the USB driver stack. You can store the array in the driver's device context for future use.

The following code example shows how to build and send a registration request. The example assumes that the composite driver stores the previously obtained number of functions and the USBD handle in the driver's device context.

```ManagedCPlusPlus
VOID  RegisterCompositeDriver(PPARENT_FDO_EXT parentFdoExt)  
{  
    PIRP                            irp;  
    REGISTER_COMPOSITE_DRIVER       registerInfo;  
    COMPOSITE_DRIVER_CAPABILITIES   capabilities;  
    NTSTATUS                        status;  
    PVOID                           buffer;  
    ULONG                           bufSize;  
    PIO_STACK_LOCATION              nextSp;  

    buffer = NULL;  

    COMPOSITE_DRIVER_CAPABILITIES_INIT(&capabilities);  
    capabilities.CapabilityFunctionSuspend = 1;  

    USBD_BuildRegisterCompositeDriver(parentFdoExt->usbdHandle,  
        capabilities,  
        parentFdoExt->numFunctions,  
        &registerInfo);  

    irp = IoAllocateIrp(parentFdoExt->topDevObj->StackSize, FALSE);  

    if (irp == NULL) 
    {  
        //IoAllocateIrp failed.
        status = STATUS_INSUFFICIENT_RESOURCES;  
        goto ExitRegisterCompositeDriver;    
    }  

    nextSp = IoGetNextIrpStackLocation(irp);  

    bufSize = parentFdoExt->numFunctions * sizeof(USBD_FUNCTION_HANDLE);  

    buffer = ExAllocatePoolWithTag (NonPagedPool, bufSize, POOL_TAG);  

    if (buffer == NULL) 
    {  
        // Memory alloc for function-handles failed.
        status = STATUS_INSUFFICIENT_RESOURCES;  
        goto ExitRegisterCompositeDriver;    
    }  

    nextSp->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;     
    nextSp->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DRIVER;  

    //Set the input buffer in Argument1      
    nextSp->Parameters.Others.Argument1 = &registerInfo;  

    //Set the output buffer in SystemBuffer field for USBD_FUNCTION_HANDLE.      
    irp->AssociatedIrp.SystemBuffer = buffer;  

    // Pass the IRP down to the next device object in the stack. Not shown.
    status = CallNextDriverSync(parentFdoExt, irp, FALSE);  

    if (!NT_SUCCESS(status))
    {  
        //Failed to register the composite driver.
        goto ExitRegisterCompositeDriver;    
    }  

    parentFdoExt->compositeDriverRegistered = TRUE;  

    parentFdoExt->functionHandleArray = (PUSBD_FUNCTION_HANDLE) buffer;  

End:  
    if (!NT_SUCCESS(status)) 
    {  
        if (buffer != NULL) 
        {  
            ExFreePoolWithTag (buffer, POOL_TAG);  
            buffer = NULL;  
        }  
    }  

    if (irp != NULL) 
    {  
        IoFreeIrp(irp);  
        irp = NULL;  
    }  

    return;  
}
```

### Unregister the Composite Device

1.  Allocate an IRP by calling [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) and get a pointer to the IRP's first stack location ([**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)) by calling [**IoGetNextIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549266).
2.  Build the request by setting the **Parameters.DeviceIoControl.IoControlCode** member of [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) to [**IOCTL\_INTERNAL\_USB\_UNREGISTER\_COMPOSITE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/hh450855).
3.  Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to send the request by passing the IRP to the next stack location.

The [**IOCTL\_INTERNAL\_USB\_UNREGISTER\_COMPOSITE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/hh450855) request is sent once by the composite driver in the context of remove-device routine. The purpose of the request is to remove the association between the USB driver stack and the composite driver and its enumerated function. The request also cleans up any resources that were created to maintain that association and all function handles that were returned in the previous registration request.

The following code example shows how to build and send a request to unregister the composite device. The example assumes that the composite driver was previously registered through a registration request as described earlier in this topic.

```ManagedCPlusPlus
VOID  UnregisterCompositeDriver(  
    PPARENT_FDO_EXT parentFdoExt )  
{  
    PIRP                irp;  
    PIO_STACK_LOCATION  nextSp;  
    NTSTATUS            status;  

    PAGED_CODE();  

    irp = IoAllocateIrp(parentFdoExt->topDevObj->StackSize, FALSE);  

    if (irp == NULL) 
    {  
        //IoAllocateIrp failed.
        status = STATUS_INSUFFICIENT_RESOURCES;  
        return;  
    }  

    nextSp = IoGetNextIrpStackLocation(irp);  

    nextSp->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;     
    nextSp->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_USB_UNREGISTER_COMPOSITE_DRIVER;  

    // Pass the IRP down to the next device object in the stack. Not shown.
    status = CallNextDriverSync(parentFdoExt, irp, FALSE);  

    if (NT_SUCCESS(status)) 
    {  
        parentFdoExt->compositeDriverRegistered = FALSE;      
    }  

    IoFreeIrp(irp);  

    return;  
}
```

## Related topics
[**IOCTL\_INTERNAL\_USB\_REGISTER\_COMPOSITE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/hh450854)  
[**IOCTL\_INTERNAL\_USB\_UNREGISTER\_COMPOSITE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/hh450855)  



