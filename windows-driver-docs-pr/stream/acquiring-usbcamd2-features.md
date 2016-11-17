---
title: Acquiring USBCAMD2 Features
author: windows-driver-content
description: Acquiring USBCAMD2 Features
MS-HAID:
- 'usbcmdds\_fac0626a-aef5-4985-8a6b-ad6f8eb2b18d.xml'
- 'stream.acquiring\_usbcamd2\_features'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 39db38a8-8279-4c61-9010-cc6d4767efc2
keywords: ["Windows 2000 Kernel Streaming Model WDK , USBCAMD2 minidriver library", "Streaming Model WDK Windows 2000 Kernel , USBCAMD2 minidriver library", "Kernel Streaming Model WDK , USBCAMD2 minidriver library", "USBCAMD2 features WDK Windows 2000 Kernel Streaming", "USB-based streaming cameras WDK USBCAMD2", "cameras WDK USBCAMD2", "IRP_MN_QUERY_INTERFACE"]
---

# Acquiring USBCAMD2 Features


You must acquire a pointer to the [**USBCAMD\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff568605) structure before you can use the new USBCAMD2 features. To acquire the pointer, build and send an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request from the camera minidriver's [**SRB\_INITIALIZATION\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/ff568182) handler in the [*AdapterReceivePacket*](https://msdn.microsoft.com/library/windows/hardware/ff554080) callback function. The USBCAMD2 minidriver library processes this IRP and returns a direct-call interface of type USBCAMD\_INTERFACE to the camera minidriver. The interface is essentially a table of function pointers.

The following code demonstrates how to build and send the IRP\_MN\_QUERY\_INTERFACE request from the camera minidriver:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Acquiring%20USBCAMD2%20Features%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


