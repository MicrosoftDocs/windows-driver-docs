---
title: Minidriver Initialization
author: windows-driver-content
description: Minidriver Initialization
MS-HAID:
- 'strmini-design\_f7fb0977-cd0a-473c-b021-1678ea70b790.xml'
- 'stream.minidriver\_initialization'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5aa4e2c6-5848-45fe-8a89-686aae7e85e6
keywords: ["initializing streaming minidrivers WDK Windows 2000 Kernel", "Stream.sys class driver WDK Windows 2000 Kernel , initializing minidrivers", "streaming minidrivers WDK Windows 2000 Kernel , initializing", "minidrivers WDK Windows 2000 Kernel Streaming , initializing"]
---

# Minidriver Initialization


## <a href="" id="ddk-minidriver-initialization-ksg"></a>


When the operating system first initializes the minidriver, it calls the minidriver's **DriverEntry** routine. See [**DriverEntry for Stream Class Minidrivers**](https://msdn.microsoft.com/library/windows/hardware/ff558717). The minidriver must register itself with the class driver by calling [**StreamClassRegisterMinidriver**](https://msdn.microsoft.com/library/windows/hardware/ff568263).

The minidriver passes an [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure, which provides the class driver with preliminary information, including the device-wide callbacks, [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463), [*StrMiniCancelPacket*](https://msdn.microsoft.com/library/windows/hardware/ff568448), [*StrMiniRequestTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff568473), and [*StrMiniInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff568459).

The class driver then uses [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463) to signal the minidriver that it should initialize the device. It sends the SRB\_INITIALIZE\_DEVICE request, and passes a [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff567785) structure with the needed hardware information. When completing this request, the minidriver supplies the size in bytes of the [**HW\_STREAM\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff559686) structure it uses to describe all of its streams.

Once the minidriver completes that request, the class driver uses [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463) to send the SRB\_GET\_STREAM\_INFO request. The minidriver then supplies information about all of its streams, including each stream's callbacks.

Once the class driver finishes processing the stream data, it uses [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463) to send the SRB\_INITIALIZATION\_COMPLETE request. At this point, the minidriver is ready to start handling requests on each stream.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Minidriver%20Initialization%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


