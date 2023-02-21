---
title: Accessing a Device on a SerCx2-Managed Serial Port
description: SerCx2 and a serial controller driver jointly manage a serial port to which a peripheral device is permanently connected.
ms.date: 01/20/2023
---

# Accessing a Device on a SerCx2-Managed Serial Port


SerCx2 and a serial controller driver jointly manage a serial port to which a peripheral device is permanently connected. To access a peripheral device on a SerCx2-managed serial port, your peripheral driver opens a logical connection to the serial port and obtains a file handle to represent this connection. Then the driver uses this handle to send I/O requests to the port.

## In this section

- [Peripheral Drivers for Devices on SerCx2-Managed Serial Ports](peripheral-drivers-for-devices-on-sercx2-managed-serial-ports.md)  

    Typically, a serial port managed by SerCx2 is permanently connected to a peripheral device. This device is controlled by a peripheral driver that sends I/O requests to the serial port. These requests transfer data to and from the device, and configure the state of the serial port. I/O requests sent by the peripheral driver are jointly handled by SerCx2 and an associated serial controller driver.

- [Opening a SerCx2-Managed Serial Port](opening-a-sercx2-managed-serial-port.md)

    If your peripheral driver controls a device on a serial port that is jointly managed by SerCx2 and a serial controller driver, your driver can open a logical connection to this port and then send I/O requests to the device through the port.

- [SerCx2 Handling of Read and Write Requests](sercx2-handling-of-read-and-write-requests.md)

    A peripheral driver sends write ([**IRP_MJ_WRITE**](../kernel/irp-mj-write.md)) and read ([**IRP_MJ_READ**](../kernel/irp-mj-read.md)) requests to a port on a serial controller to transfer data to and from a peripheral device that is connected to the port. The way in which SerCx2 handles these requests is well-defined, even when the requests time out or are canceled.

- [Reading Data from a SerCx2-Managed Serial Port](reading-data-from-a-sercx2-managed-serial-port.md)

    A serial controller (or UART) typically includes a receive FIFO. This FIFO provides hardware-controlled buffering of data received from the peripheral device that is connected to the serial port. To read data from the receive FIFO, the peripheral driver for this device sends read ([**IRP_MJ_READ**](../kernel/irp-mj-read.md)) requests to the serial port.

- [Device Interface publication for a SerCx or SerCx2-managed Serial Port](device-interface-publication-sercx.md)

    Starting with Windows 10 version 1903 and later, system manufacturers or integrators may opt-in via ACPI to have SerCx/SerCx2 expose serial ports to applications and services as a device interface.