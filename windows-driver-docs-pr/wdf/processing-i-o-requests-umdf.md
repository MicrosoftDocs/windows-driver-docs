---
title: Processing I/O Requests
description: Processing I/O Requests
ms.assetid: d12e879e-3aeb-4e88-82de-47e06e7ac482
keywords: ["I/O requests WDK UMDF", "request processing WDK UMDF", "User-Mode Driver Framework WDK , I/O requests", "UMDF WDK , I/O requests", "user-mode drivers WDK UMDF , I/O requests", "processing I/O requests WDK UMDF"]
---

# Processing I/O Requests


\[This topic applies to UMDF 1.*x*.\]

## In this section


-   [I/O Request Processing Operation Flow](i-o-request-processing-operation-flow.md)
-   [Sending I/O Requests to Lower Drivers](sending-i-o-requests-to-lower-drivers.md)
-   [Obtaining Parameters for I/O Requests](obtaining-parameters-for-i-o-requests.md)
-   [Canceling I/O Requests](canceling-i-o-requests-umdf.md)
-   [Completing I/O Requests](completing-i-o-requests-umdf.md)
-   [Accessing Data Buffers in UMDF Drivers](accessing-data-buffers-in-umdf-1-x-drivers.md)
-   [Reusing Framework Request Objects](reusing-framework-request-objects-umdf.md)
-   [Handling Client Impersonation in UMDF 1.x Drivers](handling-client-impersonation-in-umdf-1-x-drivers.md)
-   [Preventing an Imbalance of Create and Close Notifications to a Driver](preventing-an-imbalance-of-create-and-close-notifications-to-a-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Processing%20I/O%20Requests%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




