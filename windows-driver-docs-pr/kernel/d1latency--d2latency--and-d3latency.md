---
title: D1Latency, D2Latency, and D3Latency
author: windows-driver-content
description: D1Latency, D2Latency, and D3Latency
MS-HAID:
- 'PwrMgmt\_e6d7f7d3-ec7d-4027-8032-e2b8ebddfbce.xml'
- 'kernel.d1latency\_\_d2latency\_\_and\_d3latency'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6ad72b77-ec36-461c-8f4f-030d67e5a135
keywords: ["D1Latency", "D2Latency", "D3Latency"]
---

# D1Latency, D2Latency, and D3Latency


## <a href="" id="ddk-d1latency-d2latency-and-d3latency-kg"></a>


The **D1Latency**, **D2Latency**, and **D3Latency** members of [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) contain the approximate time, in 100-microsecond units, that the device requires to return to the D0 state from each of the sleeping states. A driver should specify a latency time of zero for any device power state that it does not support.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20D1Latency,%20D2Latency,%20and%20D3Latency%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


