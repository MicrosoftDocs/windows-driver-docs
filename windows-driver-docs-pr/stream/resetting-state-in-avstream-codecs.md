---
title: Resetting State in AVStream Codecs
author: windows-driver-content
description: Resetting State in AVStream Codecs
ms.assetid: c50014fe-bff0-43f4-8552-24e8e97f636b
keywords: ["AVStream hardware codec support WDK , resetting state"]
---

# Resetting State in AVStream Codecs


To discard the stream data and reset the streaming state, the media streaming pipeline sends MFT\_MESSAGE\_COMMAND\_FLUSH to an MFT. When a HW MFT receives an MFT\_MESSAGE\_COMMAND\_FLUSH, the MFT sends [**IOCTL\_KS\_RESET\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff560832) with a value of KSRESET\_BEGIN to the input and output pins. Minidrivers should subscribe to receive reset notification by specifying an [*AVStrMiniPinReset*](https://msdn.microsoft.com/library/windows/hardware/ff556354) callback in the **Reset** member of [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535).

When the driver receives this IOCTL, it should delete all outstanding clone pointers and reset all previous internal states. After the driver has flushed pending IO requests, it receives another IOCTL\_KS\_RESET\_STATE with a value of KSRESET\_END.

At this point, the minidriver should be ready to accept new input from the next stream.

Be aware that for reset to work correctly, the minidriver must specify the topology connection between the input and output pins by supplying an array of type [**KSTOPOLOGY\_CONNECTION**](https://msdn.microsoft.com/library/windows/hardware/ff567148) in the **Connections** member of the [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) structure.

A reset IOCTL is also sent in the following scenario. When the driver sets the KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM flag on a stream header and unlocks the stream pointer, KS flushes the queue, which generates an IOCTL\_KS\_RESET\_STATE call with a value of KSRESET\_END into the driver.

In this case, when the driver receives an end request without a preceding begin request, the driver should set [**KSPIN**](https://msdn.microsoft.com/library/windows/hardware/ff563483).**ResetState** to KSRESET\_END. This case applies only to output pins.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Resetting%20State%20in%20AVStream%20Codecs%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


