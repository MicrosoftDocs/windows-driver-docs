---
title: Framework Request Objects
author: windows-driver-content
description: Framework Request Objects
ms.assetid: 564f3600-4784-4a37-ac13-38338c38a9d2
keywords: ["I/O requests WDK KMDF , request objects", "request objects WDK KMDF", "request processing WDK KMDF , request objects", "framework objects WDK KMDF , I/O request objects", "request objects WDK KMDF , about request objects"]
---

# Framework Request Objects


## <a href="" id="ddk-framework-request-objects-df"></a>


Framework request objects represent I/O requests that the I/O manager has sent to a driver. Framework-based drivers process each I/O request by calling [framework request object methods](https://msdn.microsoft.com/library/windows/hardware/dn265664).

Each I/O request contains a WDM *I/O request packet* ([**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) structure), but framework-based drivers typically do not need to access the IRP structure.

## In this section


-   [Creating Framework Request Objects](creating-framework-request-objects.md)
-   [Using Request Object Context](using-request-object-context.md)
-   [Request Ownership](request-ownership.md)
-   [Processing I/O Requests](processing-i-o-requests.md)
-   [Obtaining Information About an I/O Request](obtaining-information-about-an-i-o-request.md)
-   [Accessing Data Buffers in WDF Drivers (KMDF or UMDF)](accessing-data-buffers-in-wdf-drivers.md)
-   [Managing Buffer Access Methods in UMDF Drivers](managing-buffer-access-methods-in-umdf-drivers.md)
-   [Reusing Framework Request Objects](reusing-framework-request-objects.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Request%20Objects%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




