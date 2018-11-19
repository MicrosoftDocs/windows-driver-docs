---
title: Resetting State in AVStream Codecs
description: Resetting State in AVStream Codecs
ms.assetid: c50014fe-bff0-43f4-8552-24e8e97f636b
keywords:
- AVStream hardware codec support WDK , resetting state
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Resetting State in AVStream Codecs


To discard the stream data and reset the streaming state, the media streaming pipeline sends MFT\_MESSAGE\_COMMAND\_FLUSH to an MFT. When a HW MFT receives an MFT\_MESSAGE\_COMMAND\_FLUSH, the MFT sends [**IOCTL\_KS\_RESET\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff560832) with a value of KSRESET\_BEGIN to the input and output pins. Minidrivers should subscribe to receive reset notification by specifying an [*AVStrMiniPinReset*](https://msdn.microsoft.com/library/windows/hardware/ff556354) callback in the **Reset** member of [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535).

When the driver receives this IOCTL, it should delete all outstanding clone pointers and reset all previous internal states. After the driver has flushed pending IO requests, it receives another IOCTL\_KS\_RESET\_STATE with a value of KSRESET\_END.

At this point, the minidriver should be ready to accept new input from the next stream.

Be aware that for reset to work correctly, the minidriver must specify the topology connection between the input and output pins by supplying an array of type [**KSTOPOLOGY\_CONNECTION**](https://msdn.microsoft.com/library/windows/hardware/ff567148) in the **Connections** member of the [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) structure.

A reset IOCTL is also sent in the following scenario. When the driver sets the KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM flag on a stream header and unlocks the stream pointer, KS flushes the queue, which generates an IOCTL\_KS\_RESET\_STATE call with a value of KSRESET\_END into the driver.

In this case, when the driver receives an end request without a preceding begin request, the driver should set [**KSPIN**](https://msdn.microsoft.com/library/windows/hardware/ff563483).**ResetState** to KSRESET\_END. This case applies only to output pins.

 

 




