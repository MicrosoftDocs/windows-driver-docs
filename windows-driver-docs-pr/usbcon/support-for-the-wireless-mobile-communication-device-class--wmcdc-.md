---
Description: Support for the Wireless Mobile Communication Device Class
title: Support for the Wireless Mobile Communication Device Class
author: windows-driver-content
---

# Support for the Wireless Mobile Communication Device Class


In Windows Vista the [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) provides support for devices that are included in the Universal Serial Bus (USB) Communication Device Class (CDC) and USB Wireless Mobile Communication Device Class (WMCDC).

The USB Wireless Mobile Communication Device Class (WMCDC) specification establishes a standard for connection, control, and content exchange between a host and a wireless mobile device (for example, a cell phone) when the device is connected to a USB port. WMCDC is an extension of the communication device class (CDC), which includes a broad range of communication and networking devices. This section describes the architecture that supports CDC and WMCDC devices in Windows operating systems.

WMCDC devices consist of multiple functions that are grouped into *logical handsets*. Most WMCDC devices have a single logical handset, but a device might have multiple logical handsets. Logical handsets typically include functions such as a data/fax modem, an object store, and a call control facility. A logical handset might also include supporting functions that are defined by other USB specifications such as the USB Audio Class specification, the USB Human Input Device (HID) class specification, and the USB Video Class specification.

The Windows WMCDC architecture uses native Windows drivers to manage the functions of your WMCDC device. For example, you can use the Windows telephony application program interface (TAPI) subsystem to manage the voice and data/fax modem functions of your device and the Windows network driver interface specification (NDIS) subsystem to manage the device's Ethernet LAN function. Furthermore, you can manage some functions, such as an Object Exchange Protocol (OBEX) function, in user-mode software with the assistance of the [WinUSB](winusb.md) (Winusb.sys).

The following figure shows an example driver stack for a WMCDC device.

![sample device configuration and driver stack](images/wmcdc-architecture.png)

In the preceding figure, the WMCDC device contains a single logical handset: an OBEX function and a modem function. A vendor-supplied INF file loads native Windows drivers to manage the modem. The OBEX function is managed by a vendor-supplied user-mode driver that runs in the [User-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff561365) (UMDF). The user-mode driver uses the Windows Portable Devices (WPD) protocol to communicate with user applications and the interface that the [WinUSB](winusb.md) exports to communicate with the USB stack. In general, a vendor-supplied INF file will load a separate instance of Winusb.sys for each interface collection that uses Winusb.sys.

### Registry Settings

The USB stack does not automatically support WMCDC. You must provide an INF file that loads an instance of Usbccgp.sys. The INF file must contain an **AddReg** section that sets the **EnumeratorClass** registry value in the software key that is associated with Usbccgp.sys to a REG\_BINARY value that is constructed from three numbers: 0x02, 0x00, and 0x 00. The following code example from an example INF file illustrates how to set **EnumeratorClass** to the appropriate value.

```
[CCGPDriverInstall.NT]
Include=usb.inf
Needs=Composite.Dev.NT
AddReg=CCGPDriverInstall.AddReg

[CCGPDriverInstall.NT.Services]
Include=usb.inf
Needs=Composite.Dev.NT.Services

[CCGPDriverInstall.AddReg]
HKR,,EnumeratorClass, 0x00000001,02,00,00
```

The value that you must assign to **EnumeratorClass** is constructed from three 1-byte binary values that are represented in the INF file by pairs of hexadecimal digits: 02, 00, and 00. These three numbers correspond to the values that the USB Implementers Forum has assigned to the CDC device class, CDC device subclass and CDC device protocol, respectively.

For more information about how to configure the registry to correctly enumerate your WMCDC device, see [Enumerating Interface Collections on WMCDC](enumerating-interface-collections-on-wireless-mobile-communication-dev.md).

The following topics further describe the WMCDC:

[Enumerating Interface Collections on WMCDC](enumerating-interface-collections-on-wireless-mobile-communication-dev.md)

[Handling CDC and WMCDC Interface Collections](handling-cdc-and-wmcdc-interface-collections.md)

[CDC and WMCDC Control Models](cdc-and-wmcdc-control-models.md)

## Related topics
[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Support%20for%20the%20Wireless%20Mobile%20Communication%20Device%20Class%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


