---
title: Minidriver Flow of Control
author: windows-driver-content
description: Minidriver Flow of Control
ms.assetid: c3c23d32-4023-445b-bd89-e0b454bec1ed
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , flow of control
- streaming minidrivers WDK Windows 2000 Kernel , flow of control
- minidrivers WDK Windows 2000 Kernel Streaming , flow of control
- uninitialized streaming minidrivers WDK streaming minidriver
- initializing streaming minidrivers WDK Windows 2000 Kernel
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Minidriver Flow of Control


## <a href="" id="ddk-minidriver-flow-of-control-ksg"></a>


The following set of steps is typically followed in initializing, using, and uninitializing streaming minidrivers. The following referenced commands and structures are described elsewhere in this documentation.

**The steps followed in initializing, using, and uninitializing streaming minidrivers are**

1.  The hardware adapter supported by the minidriver is detected by the Plug and Play enumerator. The enumerator checks the registry to resolve any symbolic references and passes the request to the I/O subsystem.

2.  The I/O subsystem loads the minidriver and calls the minidriver's **DriverEntry** routine (see [**DriverEntry for Stream Class Minidrivers**](https://msdn.microsoft.com/library/windows/hardware/ff558717)) where a [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure is allocated and initialized. A file object is created from the information in the **DriverEntry** routine.

3.  The minidriver's **DriverEntry** routine then calls the stream class driver's [**StreamClassRegisterMinidriver**](https://msdn.microsoft.com/library/windows/hardware/ff568263) function and passes the [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure as a parameter. The HW\_INITIALIZATION\_DATA structure includes the addresses of minidriver functions that handle SRBs. This allows the minidriver to respond to SRBs sent by the class driver.

4.  During initialization, the stream class driver calls the function specified in the [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure's **HwReceivePacket** member (see [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463)) with and SRB with the **Command** member set to SRB\_INITIALIZE\_DEVICE. The minidriver then initializes the hardware adapter.

5.  The stream class driver calls the function specified in the [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure's **HwReceivePacket** member with SRB\_GET\_STREAM\_INFO. The minidriver then returns information about the streams it supports.

6.  The stream class driver calls the function specified in the **HW\_INITIALIZATION\_DATA** structure's **HwReceivePacket** member with SRB\_OPEN\_STREAM, with a [**HW\_STREAM\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff559697) structure. The minidriver performs the necessary hardware action to open the specified stream.

7.  The stream class driver sends or requests data from the stream by passing a SRB\_READ\_DATA or SRB\_WRITE\_DATA command to the function specified in the **ReceiveDataPacket** member of the HW\_STREAM\_OBJECT structure for the stream.

8.  The stream class driver gets and sets properties and other control information for the stream by passing the appropriate stream request block ([**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702)) to the function specified in the **ReceiveControlPacket** member of the HW\_STREAM\_OBJECT structure for the stream.

9.  When the system is through using a stream, the stream class driver calls the function specified in the [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure's **HwReceivePacket** member with SRB\_CLOSE\_STREAM. The minidriver then closes the specified stream.

10. When it is time to uninitialize the adapter, the stream class driver calls the function specified in the [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure's **HwReceivePacket** member with SRB\_UNINITIALIZE\_DEVICE. The minidriver then uninitializes the device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Minidriver%20Flow%20of%20Control%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


