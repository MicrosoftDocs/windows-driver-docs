---
title: Reading Data from a SerCx2-Managed Serial Port
description: A serial controller (or UART) typically includes a receive FIFO.
ms.assetid: 36522E60-3616-4431-8C8C-3EAC4A6E4422
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reading Data from a SerCx2-Managed Serial Port


A serial controller (or UART) typically includes a receive FIFO. This FIFO provides hardware-controlled buffering of data received from the peripheral device that is connected to the serial port. To read data from the receive FIFO, the peripheral driver for this device sends read ([**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff546883)) requests to the serial port.

If the serial port continues to receive data faster than the peripheral driver can read the data, the receive FIFO can overflow. To prevent data loss due to overflow, the peripheral driver should typically configure the serial port to use hardware flow control. With flow control, the serial controller hardware automatically signals the peripheral device to stop sending data when the receive FIFO is nearly full. As a rule, serial ports that are managed by SerCx2 should use hardware flow control. For more information, see [Flow control details](#flow-control-details).

However, flow control should not be used to stop the peripheral device from sending data for too long a time or the device might not continue to operate correctly. For example, the peripheral device might have an internal data buffer that can overflow if the device is prevented for too long from sending data from this buffer to the serial port.

**On this page**

-   [Using asynchronous read requests](#using-asynchronous-read-requests)
-   [Interval time-out details](#interval-time-out-details)
-   [Flow control details](#flow-control-details)

## Using asynchronous read requests


To avoid incorrect operation and possible data loss, the peripheral driver is responsible for reading the data from the serial controller's receive FIFO in a timely way. Typically, before data is received, the peripheral driver sends an asynchronous read request to the serial port in anticipation of the future arrival of data from the peripheral device. This read request stays pending in the SerCx2 I/O queue until data is available to be read from the receive FIFO.

On most hardware platforms, a peripheral driver does not need to have more than one such read request pending at a time. In rare cases, a driver might need to have more than one outstanding read request if, after data is received, a read request takes so long to process before it can be completed that the resulting data backup causes the peripheral device to lose data or otherwise behave incorrectly.

Assuming that the peripheral driver has only one such read request pending at a time, the required size of the data buffer in this request depends largely on the known behavior of the peripheral device. For example, if the driver knows in advance how many bytes of data to expect from the device, the driver sets the buffer size in the request to this number of bytes. The read request is completed as soon as the buffer is filled with data from the receive FIFO. In response, the driver can asynchronously send a new read request to wait for the next block of data.

However, the peripheral driver might not know in advance how much data to expect from the peripheral device. In this case, the driver sets the data buffer in the read request to an appropriate size, and then relies on an interval time-out to identify the end of the data from the peripheral device. Choosing an appropriate size for the read buffer might require detailed knowledge about how the peripheral device operates. If the read buffer is too small, the driver will have to send one or more additional read requests to finish reading the data.

## Interval time-out details


To set the time-out parameters for read and write requests, a peripheral driver can send an [**IOCTL\_SERIAL\_SET\_TIMEOUTS**](https://msdn.microsoft.com/library/windows/hardware/ff546772) request to the serial port. Time-outs for reads are controlled by the **ReadIntervalTimeout**, **ReadTotalTimeoutMultiplier**, and **ReadTotalTimeoutConstant** parameter values in this request. **ReadIntervalTimeout** specifies the maximum time interval allowed between two consecutive bytes in a receive transaction. If **ReadTotalTimeoutMultiplier** and **ReadTotalTimeoutConstant** are both zero, and the serial controller's receive FIFO is empty when a read request is sent to the serial port, this request does not time out (and so remains pending in the SerCx2 I/O queue) until after the port receives at least one byte of new data. For more information, see [**SERIAL\_TIMEOUTS**](https://msdn.microsoft.com/library/windows/hardware/hh439614).

A serial port on a System on a Chip (SoC) integrated circuit might be able to receive data from a peripheral device at peak rates of several megabits per second or greater. The developer of the peripheral driver for this device might be tempted to set the interval time-out value (as specified by the **ReadIntervalTimeout** parameter) to a millisecond or less, but this value is unlikely to have the desired effect. That's because the accuracy of the timer that is used to detect interval time-outs is limited by the granularity of the system clock.

For example, if the system clock period is 15 milliseconds, and the driver sets the **ReadIntervalTimeout** value to 1 millisecond, a byte-to-byte interval anywhere in the range from 0 to a little over 15 milliseconds might trigger a time out. Occasionally, this setting might cause a time-out to occur in the middle of a data transmission from the peripheral device. To ensure that a time-out can occur only after this transmission is finished, the driver can set **ReadIntervalTimeout** to a value somewhat greater than 15 milliseconds. For example, if **ReadIntervalTimeout** is set to 20 milliseconds, a byte-to-byte interval of 30 milliseconds reliably triggers a time out, and an interval of 15 milliseconds or less does not trigger a time out.

For more information about how timer accuracy depends on the system clock, see [Timer Accuracy](https://msdn.microsoft.com/library/windows/hardware/jj602805).

## Flow control details


As a best practice, peripheral drivers that use SerCx2-managed serial ports should configure these ports to use hardware flow control to prevent the receive FIFO from overflowing. In the absence of a pending read request, SerCx2 provides no software buffering of receive data that exceeds the capacity of the receive FIFO. If this FIFO is allowed to overflow, data is lost.

To enable hardware flow control, a peripheral driver might send an [**IOCTL\_SERIAL\_SET\_HANDFLOW**](https://msdn.microsoft.com/library/windows/hardware/ff546736) request to set the handshake and flow-control settings for the serial port. Or, the driver might send an [**IOCTL\_SERIAL\_APPLY\_DEFAULT\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/hh406621) request to configure the serial port to use a set of default hardware settings that include hardware flow control. The **IOCTL\_SERIAL\_SET\_HANDFLOW** request uses the [**SERIAL\_HANDFLOW**](https://msdn.microsoft.com/library/windows/hardware/jj680685) structure to describe the flow-control settings. An **IOCTL\_SERIAL\_APPLY\_DEFAULT\_CONFIGURATION** request might contain similar information in a vendor-specified data format.

If the peripheral driver uses an **IOCTL\_SERIAL\_SET\_HANDFLOW** request to enable hardware flow control, the driver should set the following flags in the **SERIAL\_HANDFLOW** structure in this request:

-   The SERIAL\_CTS\_HANDSHAKE flag in the **ControlHandShake** member of the structure. This flag enables the serial port to use flow control for receive operations.
-   The SERIAL\_RTS\_CONTROL and SERIAL\_RTS\_HANDSHAKE flags in the **FlowReplace** member. These flags enable the serial port to use flow control for transmit operations.

 

 




