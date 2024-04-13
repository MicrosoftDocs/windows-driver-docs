---
title: Minidriver Flow of Control
description: Minidriver Flow of Control
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , flow of control
- streaming minidrivers WDK Windows 2000 Kernel , flow of control
- minidrivers WDK Windows 2000 Kernel Streaming , flow of control
- uninitialized streaming minidrivers WDK streaming minidriver
- initializing streaming minidrivers WDK Windows 2000 Kernel
ms.date: 04/20/2017
---

# Minidriver Flow of Control





The following set of steps is typically followed in initializing, using, and uninitializing streaming minidrivers. The following referenced commands and structures are described elsewhere in this documentation.

**The steps followed in initializing, using, and uninitializing streaming minidrivers are**

1.  The hardware adapter supported by the minidriver is detected by the Plug and Play enumerator. The enumerator checks the registry to resolve any symbolic references and passes the request to the I/O subsystem.

2.  The I/O subsystem loads the minidriver and calls the minidriver's **DriverEntry** routine (see [**DriverEntry for Stream Class Minidrivers**](/previous-versions/ff558717(v=vs.85))) where a [**HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_initialization_data) structure is allocated and initialized. A file object is created from the information in the **DriverEntry** routine.

3.  The minidriver's **DriverEntry** routine then calls the stream class driver's [**StreamClassRegisterMinidriver**](/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassregisteradapter) function and passes the [**HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_initialization_data) structure as a parameter. The HW\_INITIALIZATION\_DATA structure includes the addresses of minidriver functions that handle SRBs. This allows the minidriver to respond to SRBs sent by the class driver.

4.  During initialization, the stream class driver calls the function specified in the [**HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_initialization_data) structure's **HwReceivePacket** member (see [*StrMiniReceiveDevicePacket*](/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_receive_device_srb)) with and SRB with the **Command** member set to SRB\_INITIALIZE\_DEVICE. The minidriver then initializes the hardware adapter.

5.  The stream class driver calls the function specified in the [**HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_initialization_data) structure's **HwReceivePacket** member with SRB\_GET\_STREAM\_INFO. The minidriver then returns information about the streams it supports.

6.  The stream class driver calls the function specified in the **HW\_INITIALIZATION\_DATA** structure's **HwReceivePacket** member with SRB\_OPEN\_STREAM, with a [**HW\_STREAM\_OBJECT**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_object) structure. The minidriver performs the necessary hardware action to open the specified stream.

7.  The stream class driver sends or requests data from the stream by passing a SRB\_READ\_DATA or SRB\_WRITE\_DATA command to the function specified in the **ReceiveDataPacket** member of the HW\_STREAM\_OBJECT structure for the stream.

8.  The stream class driver gets and sets properties and other control information for the stream by passing the appropriate stream request block ([**HW\_STREAM\_REQUEST\_BLOCK**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_request_block)) to the function specified in the **ReceiveControlPacket** member of the HW\_STREAM\_OBJECT structure for the stream.

9.  When the system is through using a stream, the stream class driver calls the function specified in the [**HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_initialization_data) structure's **HwReceivePacket** member with SRB\_CLOSE\_STREAM. The minidriver then closes the specified stream.

10. When it is time to uninitialize the adapter, the stream class driver calls the function specified in the [**HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_initialization_data) structure's **HwReceivePacket** member with SRB\_UNINITIALIZE\_DEVICE. The minidriver then uninitializes the device.

 

