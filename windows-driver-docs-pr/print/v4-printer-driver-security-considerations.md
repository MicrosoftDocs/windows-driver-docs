---
title: V4 Printer Driver Security Considerations
description: In addition to the usual threats such as elevation of privilege, spoofed devices, or man in the middle attacks, v4 printer drivers also need to be compatible with low-rights applications like Internet Explorer 9.
ms.assetid: 8A1508C1-4856-4E3C-8378-AC5FDD55D118
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# V4 Printer Driver Security Considerations


In addition to the usual threats such as elevation of privilege, spoofed devices, or man in the middle attacks, v4 printer drivers also need to be compatible with low-rights applications like Internet Explorer 9.

XPS rendering filters and JavaScript files must all be hardened against all forms of untrusted data from applications, users, or data from across machine boundaries. Malformed PrintTickets, XPS documents, property bags, and even BidiResponses must be validated and parsed carefully and should never be used to store executable code. We recommend that partners use extensive fuzzed file testing to ensure graceful failure without compromising security integrity.

## Related topics
[V4 Printer Driver Development Best Practices](v4-printer-driver-development-best-practices.md)  



