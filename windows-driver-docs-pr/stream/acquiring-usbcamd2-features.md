---
title: Acquiring USBCAMD2 Features
description: Acquiring USBCAMD2 Features
keywords:
- Windows 2000 Kernel Streaming Model WDK , USBCAMD2 minidriver library
- Streaming Model WDK Windows 2000 Kernel , USBCAMD2 minidriver library
- Kernel Streaming Model WDK , USBCAMD2 minidriver library
- USBCAMD2 features WDK Windows 2000 Kernel Streaming
- USB-based streaming cameras WDK USBCAMD2
- cameras WDK USBCAMD2
- IRP_MN_QUERY_INTERFACE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Acquiring USBCAMD2 Features


You must acquire a pointer to the [**USBCAMD\_INTERFACE**](/windows-hardware/drivers/ddi/usbcamdi/ns-usbcamdi-usbcamd_interface) structure before you can use the new USBCAMD2 features. To acquire the pointer, build and send an [**IRP\_MN\_QUERY\_INTERFACE**](../kernel/irp-mn-query-interface.md) request from the camera minidriver's [**SRB\_INITIALIZATION\_COMPLETE**](./srb-initialization-complete.md) handler in the [*AdapterReceivePacket*](/windows-hardware/drivers/ddi/usbcamdi/nc-usbcamdi-padapter_receive_packet_routine) callback function. The USBCAMD2 minidriver library processes this IRP and returns a direct-call interface of type USBCAMD\_INTERFACE to the camera minidriver. The interface is essentially a table of function pointers.

The following code demonstrates how to build and send the IRP\_MN\_QUERY\_INTERFACE request from the camera minidriver:

```cpp
KeInitializeEvent(&Event, NotificationEvent, FALSE);
Irp = IoBuildSynchronousFsdRequest(
    IRP_MJ_PNP,
    pDeviceObject,
    NULL,
    0,
    NULL,
    &Event,
    &IoStatusBlock);

if (NULL != Irp)
{
    Irp->RequestorMode = KernelMode;
    IrpStackNext = IoGetNextIrpStackLocation(Irp);
    //
    // Create an interface query out of the Irp.
    //
    IrpStackNext->MinorFunction = IRP_MN_QUERY_INTERFACE;
    IrpStackNext->Parameters.QueryInterface.InterfaceType = (GUID*)&GUID_USBCAMD_INTERFACE;
    IrpStackNext->Parameters.QueryInterface.Size = sizeof(*pUsbcamdInterface);
    IrpStackNext->Parameters.QueryInterface.Version = USBCAMD_VERSION_200;
    IrpStackNext->Parameters.QueryInterface.Interface = (PINTERFACE)pUsbcamdInterface;
    IrpStackNext->Parameters.QueryInterface.InterfaceSpecificData = NULL;
    Status = IoCallDriver(pDeviceObject, Irp);
    if (STATUS_PENDING == Status)
    {
        //
        // This  waits using KernelMode so that the stack, and therefore the
        // event on that stack, is not paged out.
        //
        KeWaitForSingleObject(&Event, Executive, KernelMode, FALSE, NULL);
        Status = IoStatusBlock.Status;
    }

}
else
{
    Status = STATUS_INSUFFICIENT_RESOURCES;
}
```

 

