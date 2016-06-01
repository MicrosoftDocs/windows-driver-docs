---
Description: 'Before a driver can send I/O requests to a peripheral device on a simple peripheral bus (SPB), the driver must open a logical connection to the device.'
MS-HAID: 'SPB.connection\_ids\_for\_spb\_connected\_peripheral\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: 'Connection IDs for SPB-Connected Peripheral Devices'
author: windows-driver-content
---

# Connection IDs for SPB-Connected Peripheral Devices


Before a driver can send I/O requests to a peripheral device on a [simple peripheral bus](buses.simple_peripheral_buses) (SPB), the driver must open a logical connection to the device. Through this connection, the driver can send read and write requests to transfer data to and from the device. Additionally, the driver can send I/O control (IOCTL) requests to the device to perform SPB-specific operations.

## <a href="" id="connection-ids-sbp-peripheral-devices"></a>


At system startup, the Plug and Play (PnP) manager enumerates both PnP devices and non-PnP devices. For a non-PnP peripheral device that has a fixed connection to an SPB, the PnP manager queries the hardware platform's ACPI firmware to obtain a set of connection parameters that describe how to access the device. These connection parameters identify the SPB controller for the bus to which the device is connected, and include other information, such as the bus address and bus clock frequency, that the controller requires to communicate with the device.

The PnP manager assigns an identifier—called a *connection ID*—to the connection parameters for the SPB-connected peripheral device. The PnP manager stores this ID and the connection parameters together in a system datastore called the *resource hub*. (The resource hub is an internal datastore in which the PnP manager stores configuration information about an SPB-connected peripheral device.) The connection ID encapsulates these parameters so that the driver doesn't need to explicitly provide them.

The driver for an SPB-connected peripheral device receives the connection ID for the device as part of the driver's assigned hardware resources. When the driver for the peripheral device calls a system function to open a connection to the device, the driver supplies the connection ID, which the function uses to retrieve the device's connection parameters from the resource hub.

The driver developer can use either the [User-Mode Driver Framework](umdf.overview_of_the_umdf) (UMDF) or the [Kernel-Mode Driver Framework](kmdf.kernel_mode_driver_framework_overview) (KMDF) to build the driver for the SPB-connected peripheral device. A UMDF driver receives its resources (which include the connection ID) when the framework calls the driver's [**IPnpCallbackHardware2::OnPrepareHardware**](umdf.ipnpcallbackhardware_onpreparehardware) method. A KMDF driver receives its hardware resources during an [*EvtDevicePrepareHardware*](kmdf.evtdevicepreparehardware) callback.

To enable a UMDF peripheral driver to receive connection IDs in its resource list, the INF file that installs the driver must include the following directive in its WDF-specific **DDInstall** section:

**UmdfDirectHardwareAccess = AllowDirectHardwareAccess**
For more information about this directive, see [Specifying WDF Directives in INF Files](umdf.specifying_wdf_directives_in_inf_files). For an example of a INX file (used to build the corresponding INF file) that uses this directive, see the [SpbAccelerometer](http://go.microsoft.com/fwlink/p/?LinkId=618052) driver sample.

The connection ID that the driver receives as a resource is a 64-bit integer, but the driver must incorporate this ID into a device path name that can be used to retrieve the connection parameters from the resource hub. To create the device path name, the driver calls the **RESOURCE\_HUB\_CREATE\_PATH\_FROM\_ID** function, which is declared in the Reshub.h header file.

To open a logical connection to the SPB-connected peripheral device, a UMDF driver calls the [**IWDFRemoteTarget::OpenFileByName**](umdf.iwdfremotetarget_openfilebyname) method, and a KMDF driver calls the [**WdfIoTargetOpen**](kmdf.wdfiotargetopen) method. Either method requires the device path name as an input parameter.

For UMDF and KMDF code examples that use connection IDs to open logical connections to SPB-connected peripheral devices, see the following topics:

[Hardware Resources for User-Mode SPB Peripheral Drivers](buses.hardware_resources_for_user_mode_spb_peripheral_drivers)
[Hardware Resources for Kernel-Mode SPB Peripheral Drivers](buses.hardware_resources_for_kernel_mode_spb_peripheral_drivers)
User-mode applications cannot open logical connections to SPB-connected peripheral devices and cannot send I/O requests directly to these devices.

Only one driver can hold an open logical connection to an SPB-connected peripheral device at a time. An attempt by another driver to open a second connection to the same device fails.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BSPB\buses%5D:%20Connection%20IDs%20for%20SPB-Connected%20Peripheral%20Devices%20%20RELEASE:%20%286/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


