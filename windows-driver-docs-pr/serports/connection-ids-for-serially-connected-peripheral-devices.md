---
title: Connection IDs for Serially Connected Peripheral Devices
author: windows-driver-content
description: If you write a driver for a peripheral device that is connected to a serial port managed by SerCx2, the list of hardware resources that the driver receives includes a connection ID that encapsulates the device connection information from the platform firmware.
ms.assetid: 9A688552-DFAF-48A1-935D-70C3B13F30EC
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Connection IDs for Serially Connected Peripheral Devices


SerCx2 manages serial ports to which peripheral devices are permanently connected. Because these physical connections are fixed, they can be described in the ACPI firmware for the hardware platform. If you write a driver for a peripheral device that is connected to a serial port managed by SerCx2, the list of hardware resources that the driver receives includes a *connection ID* that encapsulates the device connection information from the platform firmware.

At system startup, the Plug and Play (PnP) manager enumerates both PnP devices and non-PnP devices. For a non-PnP peripheral device that has a fixed connection to a serial port, the PnP manager queries the hardware platform's ACPI firmware to obtain a set of connection parameters that describe how to access the device. These connection parameters identify the serial controller for the port to which the device is connected, and include other information, such as the baud rate and flow-control settings, that the serial controller requires to communicate with the device.

The PnP manager assigns a connection ID to represent the connection parameters for this peripheral device. The PnP manager stores this ID and the connection parameters together in a system datastore called the *resource hub*. (The resource hub is an internal datastore in which the PnP manager stores configuration information about a serially connected peripheral device.) The connection ID encapsulates these parameters so that the peripheral driver can treat them as opaque.

The peripheral driver receives the connection ID for the serially connected peripheral device as part of the driver's assigned hardware resources. When the peripheral driver calls a system function to open a connection to the peripheral device, the driver supplies the connection ID, which the system function uses to retrieve the device's connection parameters from the resource hub.

For code examples of UMDF and KMDF drivers that use connection IDs to open logical connections to serially connected peripheral devices, see the following topics:

[Connecting a UMDF Peripheral Driver to a Serial Port](connecting-a-umdf-peripheral-device-driver-to-a-serial-port.md)
[Connecting a KMDF Peripheral Driver to a Serial Port](connecting-a-kmdf-peripheral-device-driver-to-a-serial-port.md)
A client that opens a connection to a peripheral device on a serial port has exclusive access to the port until the connection is closed. An attempt by another client to open a second connection to the same port fails.

Immediately after opening a serial port, a client should assume that the port is in an unknown or undefined state. The client is responsible for configuring the port so that it is ready to use.

To configure a serial port for operation, the client sends I/O control (IOCTL) requests to the serial controller. Typically, the client sends an [**IOCTL\_SERIAL\_APPLY\_DEFAULT\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/hh406621) request to the controller to set the port to its default configuration. If necessary, the client can send additional serial IOCTLs to override one or more default configuration settings. For example, Windows defines serial IOCTLs to change the baud rate, the flow-control parameters, the line-control settings, and the time-out values for read and write requests. For a list of serial IOCTLs that are supported by SerCx2, see [Serial I/O Request Interface](serial-i-o-request-interface.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Connection%20IDs%20for%20Serially%20Connected%20Peripheral%20Devices%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


