---
title: KS Clocks
author: windows-driver-content
description: KS Clocks
ms.assetid: e3ffc7ca-f3cd-4989-af40-78b6a2438f95
keywords:
- kernel streaming WDK , clocks
- KS WDK , clocks
- clocks WDK kernel streaming
- time WDK kernel streaming
- time stamps WDK kernel streaming
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KS Clocks


## <a href="" id="ddk-ks-clocks-ksg"></a>


If you are writing an AVStream minidriver, refer to [AVStream Clocks](avstream-clocks.md).

Kernel streaming minidrivers support clock operations by providing callbacks for the properties in the set [KSPROPSETID\_Clock](https://msdn.microsoft.com/library/windows/hardware/ff566564). To learn how to do this, see [KS Properties](ks-properties.md).

A user-mode client can request to be notified when a clock reaches a certain time stamp, or to receive periodic notification that a fixed amount of time on the clock has elapsed. To do so, clients register [**KSEVENT\_CLOCK\_POSITION\_MARK**](https://msdn.microsoft.com/library/windows/hardware/ff561811) and [**KSEVENT\_CLOCK\_INTERVAL\_MARK**](https://msdn.microsoft.com/library/windows/hardware/ff561805).

This section contains information about the following topics:

[Master Clocks](master-clocks.md)

[Default Clocks](default-clocks.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KS%20Clocks%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


