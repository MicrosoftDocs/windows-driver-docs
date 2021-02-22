---
title: Serial Device Control Requests
description: Serial Device Control Requests
keywords:
- serial devices WDK , device control requests
- device control requests WDK serial devices
- Serial driver WDK , device control requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Serial Device Control Requests

Serial provides device control requests to control the operation of serial devices that support a 16550 UART-compatible interface.

Serial supports **IOCTL\_SERIAL\_XXX** requests that a client can use to perform the following tasks:

- Get and set control registers and control signals.

- Get and set line control and modem control.

- Set FIFO control.

- Get and set handshake and flow control operation and parameters.

- Get and set wait events.

- Purge internal buffers, set the receive buffer size, and reset the device.

- Get and set timeouts that are used for read and write requests.

- Get and clear performance statistics.

- Get status information.

- Get properties of the device.

Serial supports **IOCTL\_SERIAL\_INTERNAL\_XXX** requests that a trusted kernel-mode client can use to perform the following tasks:

- Set basic settings on a device and restore previous settings.

- Disable and enable the wait/wake operation of a device.

For more information about the high-level operation of [COM ports](configuration-of-com-ports.md), see the information about the communication resources that are supported by the Windows Base Services in the Microsoft Windows SDK.

For more information about Serial I/O requests, see the [Serial Port](/windows-hardware/drivers/ddi/_serports/) reference topics.

For more information about the IOCTL\_SERIAL\_XXX and IOCTL\_SERIAL\_INTERNAL\_XXX requests see the [ntddser.h](/windows-hardware/drivers/ddi/ntddser/) header.
