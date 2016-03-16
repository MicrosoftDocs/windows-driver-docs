---
title: Processing I/O Requests
description: Processing I/O Requests
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 90b1cc51-da40-45c1-9d6c-57f637f474d9
keywords: ["I/O requests WDK KMDF processing", "request objects WDK KMDF processing I/O requests", "request processing WDK KMDF options"]
---

# Processing I/O Requests


## <a href="" id="ddk-processing-i-o-requests-df"></a>


When a driver [receives](receiving-i-o-requests.md) an I/O request, it can:

-   [Requeue](requeuing-i-o-requests.md) the request to a different queue.

-   [Complete](completing-i-o-requests.md) the request.

-   [Cancel](canceling-i-o-requests.md) the request.

-   [Forward](forwarding-i-o-requests.md) the request to an I/O target.

The driver cannot ignore or delete the request.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Processing%20I/O%20Requests%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




