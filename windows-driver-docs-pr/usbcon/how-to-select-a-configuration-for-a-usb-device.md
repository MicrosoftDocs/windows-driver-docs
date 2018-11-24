---
Description: In this topic, you will learn about how to select a configuration in a universal serial bus (USB) device.
title: How to select a configuration for a USB device
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to select a configuration for a USB device


In this topic, you will learn about how to select a configuration in a universal serial bus (USB) device.

To select a configuration for a USB device, the client driver for the device must choose at least one of the supported configurations and specify the alternate settings of each interface to use. The client driver packages those choices in a *select-configuration request* and sends the request to the Microsoft-provided USB driver stack, specifically the USB bus driver (USB hub PDO). The USB bus driver selects each interface in the specified configuration and sets up a communication channel, or *pipe*, to each endpoint within the interface. After the request completes, the client driver receives a handle for the selected configuration, and pipe handles for the endpoints that are defined in the active alternate setting for each interface. The client driver can then use the received handles to change configuration settings and to send I/O read and write requests to a particular endpoint.

A client driver sends a select-configuration request in a [USB Request Block (URB)](communicating-with-a-usb-device.md) of the type URB\_FUNCTION\_SELECT\_CONFIGURATION. The procedure in this topic describes how to use the [**USBD\_SelectConfigUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406243) routine to build that URB. The routine allocates memory for an URB, formats the URB for a select-configuration request, and returns the address of the URB to the client driver.

Alternately, you can allocate an [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) structure and then format the URB manually or by calling the [**UsbBuildSelectConfigurationRequest**](https://msdn.microsoft.com/library/windows/hardware/ff538968) macro.

### Prerequisites

-   In Windows 8, [**USBD\_SelectConfigUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406243) replaces [**USBD\_CreateConfigurationRequestEx**](https://msdn.microsoft.com/library/windows/hardware/ff539029).
-   Before sending a select-configuration request, you must have a USBD handle for your client driver's registration with the USB driver stack. To create a USBD handle call [**USBD\_CreateHandle**](https://msdn.microsoft.com/library/windows/hardware/hh406241).
-   Make sure you have obtained the configuration descriptor ([**USB\_CONFIGURATION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff539241) structure) of the configuration to select. Typically, you submit an URB of the type URB\_FUNCTION\_GET\_DESCRIPTOR\_FROM\_DEVICE (see [**\_URB\_CONTROL\_DESCRIPTOR\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff540357)) to retrieve information about device configuration. For more information, see [USB Configuration Descriptors](usb-configuration-descriptors.md).

Instructions
------------

### <a href="" id="create-an-array-of-usbd-interface-list-entry-structures-"></a>Step 1: Create an array of USBD\_INTERFACE\_LIST\_ENTRY structures.

1.  Get the number of interfaces in the configuration. This information is contained in the **bNumInterfaces** member of the [**USB\_CONFIGURATION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff539241) structure.
2.  Create an array of [**USBD\_INTERFACE\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff539076) structures. The number of elements in the array must be one more than the number of interfaces. Initialize the array by calling [**RtlZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563610).

    The client driver specifies alternate settings in each interface to enable, in the array of [**USBD\_INTERFACE\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff539076) structures.

    -   The **InterfaceDescriptor** member of each structure points to the interface descriptor that contains the alternate setting.
    -   The **Interface** member of each structure points to an [**USBD\_INTERFACE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539068) structure that contains pipe information in its **Pipes** member. **Pipes** stores information about each endpoint defined in the alternate setting.

3.  Obtain an interface descriptor for each interface (or its alternate setting) in the configuration. You can obtain those interface descriptors by calling [**USBD\_ParseConfigurationDescriptorEx**](https://msdn.microsoft.com/library/windows/hardware/ff539102).

    **About Function Drivers for a USB Composite Device:  **

    If the USB device is a composite device, the configuration is selected by the Microsoft-provided [USB Generic Parent Driver](usb-common-class-generic-parent-driver.md) (Usbccgp.sys). A client driver, which is one of the function drivers of the composite device, cannot change the configuration but the driver can still send a select-configuration request through Usbccgp.sys.

    Before sending that request, the client driver must submit a URB\_FUNCTION\_GET\_DESCRIPTOR\_FROM\_DEVICE request. In response, Usbccgp.sys retrieves a *partial configuration descriptor* that only contains interface descriptors and other descriptors that pertain to the specific function for which the client driver is loaded. The number of interfaces reported in the **bNumInterfaces** field of a partial configuration descriptor is less than the total number of interfaces defined for the entire USB composite device. In addition, in a partial configuration descriptor, an interface descriptor's **bInterfaceNumber** indicates the actual interface number relative to the entire device. For example, Usbccgp.sys might report a partial configuration descriptor with **bNumInterfaces** value of 2 and **bInterfaceNumber** value of 4 for the first interface. Note that the interface number is greater than the number of interfaces reported.

    While enumerating interfaces in a partial configuration, avoid searching for interfaces by calculating interface numbers based on the number of interfaces. In the preceding example, if [**USBD\_ParseConfigurationDescriptorEx**](https://msdn.microsoft.com/library/windows/hardware/ff539102) is called in a loop that starts at zero, ends at `(bNumInterfaces - 1)`, and increments the interface index (specified in the *InterfaceNumber* parameter) in each iteration, the routine fails to get the correct interface. Instead, make sure that you search for all interfaces in the configuration descriptor by passing -1 in *InterfaceNumber*. For implementation details, see the code example in this section.

    For information about how Usbccgp.sys handles a select-configuration request sent by a client driver, see [Configuring Usbccgp.sys to Select a Non-Default USB Configuration](selecting-the-configuration-for-a-multiple-interface--composite--usb-d.md).

4.  For each element (except the last element) in the array, set the **InterfaceDescriptor** member to the address of an interface descriptor. For the first element in the array, set the **InterfaceDescriptor** member to the address of the interface descriptor that represents the first interface in the configuration. Similarly for the *n*th element in the array, set the **InterfaceDescriptor** member to the address of the interface descriptor that represents the *n*th interface in the configuration.
5.  The **InterfaceDescriptor** member of the last element must be set to NULL.

### <a href="" id="get-a-pointer-to-an-urb-allocated-by-the-usb-driver-stack-"></a>Step 2: Get a pointer to an URB allocated by the USB driver stack.

Next, call [**USBD\_SelectConfigUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406243) by specifying the configuration to select and the populated array of [**USBD\_INTERFACE\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff539076) structures. The routine performs the following tasks:

-   Creates an URB and fills it with information about the specified configuration, its interfaces and endpoints, and sets the request type to URB\_FUNCTION\_SELECT\_CONFIGURATION.
-   Within that URB, allocates a [**USBD\_INTERFACE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539068) structure for each interface descriptor that the client driver specifies.
-   Sets the **Interface** member of the *n*th element of the caller-provided [**USBD\_INTERFACE\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff539076) array to the address of the corresponding [**USBD\_INTERFACE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539068) structure in the URB.
-   Initializes the **InterfaceNumber**, **AlternateSetting**, **NumberOfPipes**, **Pipes\[i\].MaximumTransferSize**, and **Pipes\[i\].PipeFlags** members.

    **Note**  In Windows 7 and ealier, the client driver created an URB for a select-configuration request by calling [**USBD\_CreateConfigurationRequestEx**](https://msdn.microsoft.com/library/windows/hardware/ff539029). In Windows 2000 **USBD\_CreateConfigurationRequestEx** initializes **Pipes\[i\].MaximumTransferSize** to the default maximum transfer size for a single URB read/write request. The client driver can specify a different maximum transfer size in the **Pipes\[i\].MaximumTransferSize**. The USB stack ignores this value in Windows XP, Windows Server 2003, and later versions of the operating system. For more information about **MaximumTransferSize**, see "Setting USB Transfer and Packet Sizes" in [USB Bandwidth Allocation](usb-bandwidth-allocation.md).

### <a href="" id="submit-the-urb-to-the-usb-driver-stack-"></a>Step 3: Submit the URB to the USB driver stack.

To submit the URB to the USB driver stack, the client driver must send an [**IOCTL\_INTERNAL\_USB\_SUBMIT\_URB**](https://msdn.microsoft.com/library/windows/hardware/ff537271) I/O control request . For information about submitting an URB, see [How to Submit an URB](send-requests-to-the-usb-driver-stack.md).

After receiving the URB, the USB driver stack fills the rest of the members of each [**USBD\_INTERFACE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539068) structure. In particular, the **Pipes** array member is filled with information about the pipes associated with the endpoints of the interface.

### <a href="" id="on-request-completion--inspect-the-usbd-interface-information-structures-and-the-urb-"></a>Step 4: On request completion, inspect the USBD\_INTERFACE\_INFORMATION structures and the URB.

After the USB driver stack completes the IRP for the request, the stack returns the list of alternate settings and the related interfaces in the [**USBD\_INTERFACE\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff539076) array.

1.  The **Pipes** member of each [**USBD\_INTERFACE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539068) structure points to an array of [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114) structures that contains information about the pipes associated with each endpoint of that particular interface. The client driver can obtain pipe handles from **Pipes\[i\].PipeHandle** and use them to send I/O requests to specific pipes. The **Pipes\[i\].PipeType** member specifies the type of endpoint and transfer supported by that pipe.

2.  Within the **UrbSelectConfiguration** member of the URB, the USB driver stack returns a handle that you can use to select an alternate interface setting by submitting another URB of the type URB\_FUNCTION\_SELECT\_INTERFACE (*select-interface request*). To allocate and build the URB structure for that request, call [**USBD\_SelectInterfaceUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406245).

    The select-configuration request and select-interface request might fail if there is insufficient bandwidth to support the isochronous, control, and interrupt endpoints within the enabled interfaces. In that case, the USB bus driver sets the **Status** member of the URB header to USBD\_STATUS\_NO\_BANDWIDTH.

The following example code shows how to create an array of [**USBD\_INTERFACE\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff539076) structures and call [**USBD\_SelectConfigUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406243). The example sends the request synchronously by calling SubmitUrbSync. To see the code example for SubmitUrbSync, see [How to Submit an URB](send-requests-to-the-usb-driver-stack.md).

```ManagedCPlusPlus
/*++

Routine Description:
This helper routine selects the specified configuration.

Arguments:
USBDHandle - USBD handle that is retrieved by the 
client driver in a previous call to the USBD_CreateHandle routine.

ConfigurationDescriptor - Pointer to the configuration
descriptor for the device. The caller receives this pointer
from the URB_FUNCTION_GET_DESCRIPTOR_FROM_DEVICE request.

Return Value: NT status value
--*/

NTSTATUS SelectConfiguration (PDEVICE_OBJECT DeviceObject,
                              PUSB_CONFIGURATION_DESCRIPTOR ConfigurationDescriptor)
{
    PDEVICE_EXTENSION deviceExtension;
    PIO_STACK_LOCATION nextStack;
    PIRP irp;
    PURB urb = NULL;

    KEVENT    kEvent;
    NTSTATUS ntStatus;    

    PUSBD_INTERFACE_LIST_ENTRY   interfaceList = NULL; 
    PUSB_INTERFACE_DESCRIPTOR    interfaceDescriptor = NULL;
    PUSBD_INTERFACE_INFORMATION  Interface = NULL;
    USBD_PIPE_HANDLE             pipeHandle;

    ULONG                        interfaceIndex;

    PUCHAR StartPosition = (PUCHAR)ConfigurationDescriptor;

    deviceExtension = (PDEVICE_EXTENSION)DeviceObject->DeviceExtension;

    // Allocate an array for the list of interfaces
    // The number of elements must be one more than number of interfaces.
    interfaceList = (PUSBD_INTERFACE_LIST_ENTRY)ExAllocatePool (
        NonPagedPool, 
        sizeof(USBD_INTERFACE_LIST_ENTRY) *
        (deviceExtension->NumInterfaces + 1));

    if(!interfaceList)
    {
        //Failed to allocate memory
        ntStatus = STATUS_INSUFFICIENT_RESOURCES;
        goto Exit;
    }

    // Initialize the array by setting all members to NULL.
    RtlZeroMemory (interfaceList, sizeof (
        USBD_INTERFACE_LIST_ENTRY) *
        (deviceExtension->NumInterfaces + 1));

    // Enumerate interfaces in the configuration.
    for ( interfaceIndex = 0; 
        interfaceIndex < deviceExtension->NumInterfaces; 
        interfaceIndex++) 
    {
        interfaceDescriptor = USBD_ParseConfigurationDescriptorEx(
            ConfigurationDescriptor, 
            StartPosition, // StartPosition 
            -1,            // InterfaceNumber
            0,             // AlternateSetting
            -1,            // InterfaceClass
            -1,            // InterfaceSubClass
            -1);           // InterfaceProtocol

        if (!interfaceDescriptor) 
        {
            ntStatus = STATUS_INSUFFICIENT_RESOURCES;
            goto Exit;
        }

        // Set the interface entry
        interfaceList[interfaceIndex].InterfaceDescriptor = interfaceDescriptor;
        interfaceList[interfaceIndex].Interface = NULL;

        // Move the position to the next interface descriptor
        StartPosition = (PUCHAR)interfaceDescriptor + interfaceDescriptor->bLength;

    }

    // Make sure that the InterfaceDescriptor member of the last element to NULL.
    interfaceList[deviceExtension->NumInterfaces].InterfaceDescriptor = NULL;

    // Allocate and build an URB for the select-configuration request.
    ntStatus = USBD_SelectConfigUrbAllocateAndBuild(
        deviceExtension->UsbdHandle, 
        ConfigurationDescriptor, 
        interfaceList,
        &urb);

    if(!NT_SUCCESS(ntStatus)) 
    {
        goto Exit;
    }

    // Allocate the IRP to send the buffer down the USB stack.
    // The IRP will be freed by IO manager.
    irp = IoAllocateIrp((deviceExtension->NextDeviceObject->StackSize)+1, TRUE);  

    if (!irp)
    {
        //Irp could not be allocated.
        ntStatus = STATUS_INSUFFICIENT_RESOURCES;
        goto Exit;
    }

    ntStatus = SubmitUrbSync( 
        deviceExtension->NextDeviceObject, 
        irp, 
        urb, 
        CompletionRoutine);

    // Enumerate the pipes in the interface information array, which is now filled with pipe
    // information.

    for ( interfaceIndex = 0; 
        interfaceIndex < deviceExtension->NumInterfaces; 
        interfaceIndex++) 
    {
        ULONG i;

        Interface = interfaceList[interfaceIndex].Interface;

        for(i=0; i < Interface->NumberOfPipes; i++) 
        {
            pipeHandle = Interface->Pipes[i].PipeHandle;

            if (Interface->Pipes[i].PipeType == UsbdPipeTypeInterrupt)
            {
                deviceExtension->InterruptPipe = pipeHandle;
            }
            if (Interface->Pipes[i].PipeType == UsbdPipeTypeBulk && USB_ENDPOINT_DIRECTION_IN (Interface->Pipes[i].EndpointAddress))
            {
                deviceExtension->BulkInPipe = pipeHandle;
            }
            if (Interface->Pipes[i].PipeType == UsbdPipeTypeBulk && USB_ENDPOINT_DIRECTION_OUT (Interface->Pipes[i].EndpointAddress))
            {
                deviceExtension->BulkOutPipe = pipeHandle;
            }
        }
    }

Exit:

    if(interfaceList) 
    {
        ExFreePool(interfaceList);
        interfaceList = NULL;
    }

    if (urb)
    {
        USBD_UrbFree( deviceExtension->UsbdHandle, urb); 
    }


    return ntStatus;

}

NTSTATUS CompletionRoutine ( PDEVICE_OBJECT DeviceObject,
                            PIRP           Irp,
                            PVOID          Context)
{
    PKEVENT kevent;

    kevent = (PKEVENT) Context;

    if (Irp->PendingReturned == TRUE)
    {
        KeSetEvent(kevent, IO_NO_INCREMENT, FALSE);
    }

    KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, "Select-configuration request completed. \n" ));


    return STATUS_MORE_PROCESSING_REQUIRED;
}
```

Remarks
-------

**Disabling a Configuration for a USB Device:  **

To disable a USB device, create and submit a select-configuration request with a NULL configuration descriptor. For that type of request, you can reuse the URB that you created for request that selected a configuration in the device. Alternately, you can allocate a new URB by calling [**USBD\_UrbAllocate**](https://msdn.microsoft.com/library/windows/hardware/hh406250). Before submitting the request you must format the URB by using the [**UsbBuildSelectConfigurationRequest**](https://msdn.microsoft.com/library/windows/hardware/ff538968) macro as shown in the following example code.

```ManagedCPlusPlus
URB Urb;
UsbBuildSelectConfigurationRequest(
  &Urb,
  sizeof(_URB_SELECT_CONFIGURATION),
  NULL
);
```

## Related topics
[Configuring Usbccgp.sys to Select a Non-Default USB Configuration](selecting-the-configuration-for-a-multiple-interface--composite--usb-d.md)  
[USB device configuration](configuring-usb-devices.md)  
[Allocating and Building URBs](how-to-add-xrb-support-for-client-drivers.md)  



