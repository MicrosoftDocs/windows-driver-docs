---
title: Minidriver Initialization
description: Minidriver Initialization
ms.assetid: 5aa4e2c6-5848-45fe-8a89-686aae7e85e6
keywords:
- initializing streaming minidrivers WDK Windows 2000 Kernel
- Stream.sys class driver WDK Windows 2000 Kernel , initializing minidrivers
- streaming minidrivers WDK Windows 2000 Kernel , initializing
- minidrivers WDK Windows 2000 Kernel Streaming , initializing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minidriver Initialization





When the operating system first initializes the minidriver, it calls the minidriver's **DriverEntry** routine. See [**DriverEntry for Stream Class Minidrivers**](https://msdn.microsoft.com/library/windows/hardware/ff558717). The minidriver must register itself with the class driver by calling [**StreamClassRegisterMinidriver**](https://msdn.microsoft.com/library/windows/hardware/ff568263).

The minidriver passes an [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure, which provides the class driver with preliminary information, including the device-wide callbacks, [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463), [*StrMiniCancelPacket*](https://msdn.microsoft.com/library/windows/hardware/ff568448), [*StrMiniRequestTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff568473), and [*StrMiniInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff568459).

The class driver then uses [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463) to signal the minidriver that it should initialize the device. It sends the SRB\_INITIALIZE\_DEVICE request, and passes a [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff567785) structure with the needed hardware information. When completing this request, the minidriver supplies the size in bytes of the [**HW\_STREAM\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff559686) structure it uses to describe all of its streams.

Once the minidriver completes that request, the class driver uses [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463) to send the SRB\_GET\_STREAM\_INFO request. The minidriver then supplies information about all of its streams, including each stream's callbacks.

Once the class driver finishes processing the stream data, it uses [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463) to send the SRB\_INITIALIZATION\_COMPLETE request. At this point, the minidriver is ready to start handling requests on each stream.

 

 




