---
title: Connection IDs for SPB-Connected Peripheral Devices
description: Before a driver can send I/O requests to a peripheral device on a simple peripheral bus (SPB), the driver must open a logical connection to the device.
ms.date: 04/20/2017
---

# Connection IDs for SPB-Connected Peripheral Devices


Before a driver can send I/O requests to a peripheral device on a [simple peripheral bus](/previous-versions/hh450903(v=vs.85)) (SPB), the driver must open a logical connection to the device. Through this connection, the driver can send read and write requests to transfer data to and from the device. Additionally, the driver can send I/O control (IOCTL) requests to the device to perform SPB-specific operations.




At system startup, the Plug and Play (PnP) manager enumerates both PnP devices and non-PnP devices. For a non-PnP peripheral device that has a fixed connection to an SPB, the PnP manager queries the hardware platform's ACPI firmware to obtain a set of connection parameters that describe how to access the device. These connection parameters identify the SPB controller for the bus to which the device is connected, and include other information, such as the bus address and bus clock frequency, that the controller requires to communicate with the device.

The PnP manager assigns an identifier—called a *connection ID*—to the connection parameters for the SPB-connected peripheral device. The PnP manager stores this ID and the connection parameters together in a system datastore called the *resource hub*. (The resource hub is an internal datastore in which the PnP manager stores configuration information about an SPB-connected peripheral device.) The connection ID encapsulates these parameters so that the driver doesn't need to explicitly provide them.

The driver for an SPB-connected peripheral device receives the connection ID for the device as part of the driver's assigned hardware resources. When the driver for the peripheral device calls a system function to open a connection to the device, the driver supplies the connection ID, which the function uses to retrieve the device's connection parameters from the resource hub.

The driver developer can use either the [User-Mode Driver Framework](../wdf/overview-of-the-umdf.md) (UMDF) or the [Kernel-Mode Driver Framework](../wdf/index.md) (KMDF) to build the driver for the SPB-connected peripheral device. A UMDF driver receives its resources (which include the connection ID) when the framework calls the driver's [**IPnpCallbackHardware2::OnPrepareHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware-onpreparehardware) method. A KMDF driver receives its hardware resources during an [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback.

To enable a UMDF peripheral driver to receive connection IDs in its resource list, the INF file that installs the driver must include the following directive in its WDF-specific **DDInstall** section:

**UmdfDirectHardwareAccess = AllowDirectHardwareAccess**
For more information about this directive, see [Specifying WDF Directives in INF Files](../wdf/specifying-wdf-directives-in-inf-files.md). For an example of a INX file (used to build the corresponding INF file) that uses this directive, see the [SpbAccelerometer](https://go.microsoft.com/fwlink/p/?LinkId=618052) driver sample.

The connection ID that the driver receives as a resource is a 64-bit integer, but the driver must incorporate this ID into a device path name that can be used to retrieve the connection parameters from the resource hub. To create the device path name, the driver calls the **RESOURCE\_HUB\_CREATE\_PATH\_FROM\_ID** function, which is declared in the Reshub.h header file.

To open a logical connection to the SPB-connected peripheral device, a UMDF driver calls the [**IWDFRemoteTarget::OpenFileByName**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfremotetarget-openfilebyname) method, and a KMDF driver calls the [**WdfIoTargetOpen**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetopen) method. Either method requires the device path name as an input parameter.

For UMDF and KMDF code examples that use connection IDs to open logical connections to SPB-connected peripheral devices, see the following topics:

[Hardware Resources for User-Mode SPB Peripheral Drivers](./hardware-resources-for-user-mode-spb-peripheral-drivers.md)
[Hardware Resources for Kernel-Mode SPB Peripheral Drivers](./hardware-resources-for-kernel-mode-spb-peripheral-drivers.md)
User-mode applications cannot open logical connections to SPB-connected peripheral devices and cannot send I/O requests directly to these devices.

Only one driver can hold an open logical connection to an SPB-connected peripheral device at a time. An attempt by another driver to open a second connection to the same device fails.

 

