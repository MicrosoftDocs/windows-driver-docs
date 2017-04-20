---
title: V4 Printer Driver Security Considerations
author: windows-driver-content
description: In addition to the usual threats such as elevation of privilege, spoofed devices, or man in the middle attacks, v4 printer drivers also need to be compatible with low-rights applications like Internet Explorer 9.
ms.assetid: 8A1508C1-4856-4E3C-8378-AC5FDD55D118
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# V4 Printer Driver Security Considerations


In addition to the usual threats such as elevation of privilege, spoofed devices, or man in the middle attacks, v4 printer drivers also need to be compatible with low-rights applications like Internet Explorer 9.

XPS rendering filters and JavaScript files must all be hardened against all forms of untrusted data from applications, users, or data from across machine boundaries. Malformed PrintTickets, XPS documents, property bags, and even BidiResponses must be validated and parsed carefully and should never be used to store executable code. We recommend that partners use extensive fuzzed file testing to ensure graceful failure without compromising security integrity.

## Related topics
[V4 Printer Driver Development Best Practices](v4-printer-driver-development-best-practices.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20V4%20Printer%20Driver%20Security%20Considerations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


