---
Description: 'Instead of using the I/O Request Packet (IRP) mechanism, a USB client driver can get a reference to a bus driver interface and use it to access bus driver routines.'
MS-HAID:
- 'usbinterKG\_638eb209-5f2e-4f96-b169-beedcf106ac4.xml'
- 'buses.querying\_for\_usb\_interfaces'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Querying for Bus Driver Interfaces
author: windows-driver-content
---

# Querying for Bus Driver Interfaces


Instead of using the I/O Request Packet (IRP) mechanism, a USB client driver can get a reference to a bus driver interface and use it to access bus driver routines.

## <a href="" id="ddk-querying-for-usb-interfaces-kg"></a>


Using a bus driver interface gives the client driver several advantages:

-   It can use the interface's services without allocating an IRP.

-   It can call the interface's routines at raised IRQL.

In Windows Vista USB, client drivers can themselves expose an interface to assist the [USB Common Class Generic Parent Driver](usb-common-class-generic-parent-driver.md) in defining interface collections for the device it manages.

To get a bus driver interface, the client driver must send an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request to the bus driver. In your client driver:

1.  Create an IRP of the type IRP\_MN\_QUERY\_INTERFACE in the next stack location.
    ```
    irpstack = IoGetNextIrpStackLocation(irp);
    irpstack->MajorFunction= IRP_MJ_PNP;
    irpstack->MinorFunction= IRP_MN_QUERY_INTERFACE;
    ```

2.  Allocate memory for the interface and make the stack point to the new memory. For example to allocate memory for the [**USB\_BUS\_INTERFACE\_USBDI\_V0**](https://msdn.microsoft.com/library/windows/hardware/ff539210) interface:
    ```
    irpstack->Parameters.QueryInterface.Interface = (USB_BUS_INTERFACE_USBDI_V0) newly allocated interface buffer;
    ```

3.  Set **InterfaceSpecificData** to NULL.
    ```
    irpstack->Parameters.QueryInterface.InterfaceSpecificData = NULL;
    ```

4.  Initialize the IRP stack with the appropriate interface GUID, the size of the interface, and the version of the interface.
    ```
    irpstack->Parameters.QueryInterface.InterfaceType = &amp;USB_BUS_INTERFACE_USBDI_GUID;
    irpstack->Parameters.QueryInterface.Size = sizeof(USB_BUS_INTERFACE_USBDI_V0);
    irpstack->Parameters.QueryInterface.Version = USB_BUSIF_USBDI_VERSION_0;
    ntStatus = IoCallDriver(PDO that the client passes URBs to, irp);
    ```

5.  Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to pass the query interface IRP down the stack.
    ```
    ntStatus = IoCallDriver(PDO that the client passes URBs to, irp);
    ```

For further information about USB interfaces see [Bus Driver Interface Routines for USB Client Drivers](https://msdn.microsoft.com/library/windows/hardware/ff540134#usbdi).

## Related topics
[Developing Windows client drivers for USB devices](usb-driver-development-guide.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Querying%20for%20Bus%20Driver%20Interfaces%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


