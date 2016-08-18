---
title: Introduction to WIA
author: windows-driver-content
description: Introduction to WIA
MS-HAID:
- 'WIA\_intro\_5478aa76-1f52-423b-990f-82dcd7015ec6.xml'
- 'image.introduction\_to\_wia'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 51674b06-f9d5-4e35-a2ec-9d6cc0a09ef3
---

# Introduction to WIA


## <a href="" id="ddk-introduction-to-wia-si"></a>


The Microsoft Windows Image Acquisition (WIA) interface is both an application programming interface (API) and a device driver interface (DDI). The WIA API is designed to allow applications to:

-   Run in a robust and stable environment.

-   Minimize interoperability problems.

-   Enumerate available image acquisition devices.

-   Create connections to multiple devices simultaneously.

-   Query properties of devices in a standard and expandable manner.

-   Acquire device data using standard and high performance transfer mechanisms.

-   Maintain image properties across data transfers.

-   Be notified of a wide variety of device events.

The WIA DDI is designed to minimize the amount of code a hardware vendor must write, while maintaining the flexibility to craft individual solutions. This is accomplished by:

-   Providing a standard device service library that performs most driver operations.

-   Promoting industry device communications standards, such as the Picture Transfer Protocol (PTP), so that one WIA driver supports most WIA devices.

This section presents a brief overview of WIA in the following areas:

[WIA Architecture Overview](wia-architecture-overview.md)

[WIA Core Components](wia-core-components.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Introduction%20to%20WIA%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


