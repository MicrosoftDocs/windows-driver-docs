---
title: Connection IDs for Serially Connected Peripheral Devices
description: If you write a driver for a peripheral device that is connected to a serial port managed by SerCx2, the list of hardware resources that the driver receives includes a connection ID that encapsulates the device connection information from the platform firmware.
ms.assetid: 9A688552-DFAF-48A1-935D-70C3B13F30EC
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




