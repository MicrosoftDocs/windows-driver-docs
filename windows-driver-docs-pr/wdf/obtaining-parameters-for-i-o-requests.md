---
title: Obtaining Parameters for I/O Requests
description: Obtaining Parameters for I/O Requests
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 1ba1fdcf-99bd-44e3-adbf-5dc93a790900
keywords: ["I/O requests WDK UMDF obtaining parameters", "request processing WDK UMDF obtaining parameters"]
---

# Obtaining Parameters for I/O Requests


\[This topic applies to UMDF 1.*x*.\]

When a driver receives an I/O request, the driver can use the following methods of the [IWDFIoRequest](https://msdn.microsoft.com/library/windows/hardware/ff558985) interface to obtain parameters related to the request:

[**IWDFIoRequest::GetCreateParameters**](https://msdn.microsoft.com/library/windows/hardware/ff559088) or [**IWDFIoRequest2::GetCreateParametersEx**](https://msdn.microsoft.com/library/windows/hardware/ff558989)

[**IWDFIoRequest::GetDeviceIoControlParameters**](https://msdn.microsoft.com/library/windows/hardware/ff559095)

[**IWDFIoRequest::GetReadParameters**](https://msdn.microsoft.com/library/windows/hardware/ff559113)

[**IWDFIoRequest::GetWriteParameters**](https://msdn.microsoft.com/library/windows/hardware/ff559130)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Obtaining%20Parameters%20for%20I/O%20Requests%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




