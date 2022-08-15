---
title: Virtual Subunit Driver Notes
description: Virtual Subunit Driver Notes
keywords:
- Avc.sys function driver WDK , virtual subunit drivers
- virtual subunit drivers WDK AV/C
- external devices WDK AV/C
- IOCTL_AVC_CLASS
ms.date: 04/20/2017
---

# Virtual Subunit Driver Notes


A virtual subunit driver responds to control, status, and notification AV/C requests and commands from external AV/C devices by using the [**IOCTL\_AVC\_CLASS**](/windows-hardware/drivers/ddi/avc/ni-avc-ioctl_avc_class) interface with *Avc.sys*.

The IOCTL\_AVC\_CLASS subfunction codes [**AVC\_FUNCTION\_GET\_REQUEST**](./avc-function-get-request.md) and [**AVC\_FUNCTION\_SEND\_RESPONSE**](./avc-function-send-response.md) are the key mechanisms by which a virtual subunit driver interacts with the rest of the virtual driver stack. A virtual subunit driver submits an **AVC\_FUNCTION\_GET\_REQUEST** IRP to *Avc.sys* in its [**IRP\_MN\_START\_DEVICE**](../kernel/irp-mn-start-device.md) routine (after IRP\_MN\_START\_DEVICE has been completed by the underlying drivers in the stack). The I/O completion routine for the **AVC\_FUNCTION\_GET\_REQUEST** IRP is called each time a request for a virtual subunit is received. The I/O completion routine must send a response (by **AVC\_FUNCTION\_SEND\_RESPONSE** with an asynchronous IRP) within 100 ms (according to the AV/C protocol rules); it may use the [**AVC\_COMMAND\_IRB**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_command_irb) structure contained in the request to send the response. Then it must resubmit an **AVC\_FUNCTION\_GET\_REQUEST** IRP before finally returning from the response's I/O completion routine.

A subunit driver in the virtual driver stack cannot send commands directly to external devices. The peer driver stack provides this functionality. However, the virtual subunit driver can use the [**AVC\_FUNCTION\_FIND\_PEER\_DO**](./avc-function-find-peer-do.md) and [**AVC\_FUNCTION\_PEER\_DO\_LIST**](./avc-function-peer-do-list.md) subfunctions of [**IOCTL\_AVC\_CLASS**](/windows-hardware/drivers/ddi/avc/ni-avc-ioctl_avc_class) to discover and reference peer instances of *Avc.sys* and then to interact with external AV/C subunits.

For each virtual subunit enumerated, *Avc.sys* creates a corresponding device object. Consequently, as a virtual subunit is added and removed, *Avc.sys* triggers an IEEE 1394 bus reset. This reset allows other devices on the IEEE 1394 bus to detect the new functionality being exposed on the computer. Virtual subunit drivers are loaded based on the *Avc.sys* instance's registry settings and can be added and removed at run time by IOCTL code requests. Note that *Avc.sys* cannot distinguish between multiple virtual subunits of the same type, so adding and removing these subunits loads and unloads the corresponding virtual subunit driver with the highest subunit identifier.

A virtual subunit driver can be thick or thin. The only requirement is that it be written as a WDM driver. A thick driver implements most, if not all, functionality of the virtual device. A thin driver provides a proxy interface to the virtual device functionality, which can be another driver or a user-mode component. The interface between user mode and the virtual subunit driver is implementation-specific and can be accomplished through IOCTL codes, private device interfaces (see [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface)), or through [Windows Management Instrumentation](../kernel/implementing-wmi.md) (WMI).

The VEN\_ and MOD\_ values are the same as specified in the INF file that caused the virtual instance of *61883.sys* to load. The TYP\_ and ID\_ values are as specified when *Avc.sys* enumerates the virtual subunit.

The enumeration of the virtual subunit is accomplished by using the [**IOCTL\_AVC\_UPDATE\_VIRTUAL\_SUBUNIT\_INFO**](/windows-hardware/drivers/ddi/avc/ni-avc-ioctl_avc_update_virtual_subunit_info), [**IOCTL\_AVC\_REMOVE\_VIRTUAL\_SUBUNIT\_INFO**](/windows-hardware/drivers/ddi/avc/ni-avc-ioctl_avc_remove_virtual_subunit_info), and [**IOCTL\_AVC\_BUS\_RESET**](/windows-hardware/drivers/ddi/avc/ni-avc-ioctl_avc_bus_reset) IOCTL codes.

It is necessary to send the proper IEEE 1394 IOCTLs, **IEEE1394\_API\_ADD\_VIRTUAL\_DEVICE** and **IEEE1394\_API\_REMOVE\_VIRTUAL\_DEVICE** to begin the enumeration process. For more information (subcommands of IOCTL\_IEEE1394\_API\_REQUEST). The *61883.inf* file already contains a device identifier (ID) for this purpose: V1394\\A02D&10001, although a different identifier might be provided in a custom INF file.

An alternate way to statically enumerate a virtual subunit can be accomplished by using an INF file.

Each value under the Virtual Device List key is a packed subunit address (subunit type and maximum identifier combined, as described in the AV/C General Specification). The name that is associated with the subunit address does not matter, although it must be unique for that instance. When created programmatically, the value names are given sequential numbers to avoid collisions.

For example, to create a single virtual tuner subunit through an INF file, use the following **AddReg** directive:

```INF
[Subunit_Device.NT.HW.AddReg]
HKR,%VirtualAvc.DeviceList%,Tuner,0x00000001,0x28 ;0x00000001 = Binary value, 0x28 = Registry key value
```

This directive adds a REG\_BINARY value of 0x28 (subunit type 0x5 packed into the most significant five bits and maximum identifier of 0x0 packed into the least significant three bits). A maximum identifier of 0x0 here means that there will be a single subunit of that type.

**Note**  : It is also necessary to define the `%VirtualAvc.DeviceList%` token in the `[Strings]` section of the subunit's INF file.
