---
title: V4 Printer Driver Security Considerations
description: In addition to the usual threats such as elevation of privilege, spoofed devices, or injection attacks, v4 printer drivers also need to be compatible with low-rights applications.
ms.date: 06/08/2020
---

# V4 Printer Driver Security Considerations

In addition to the usual threats such as elevation of privilege, spoofed devices, or injection attacks, v4 printer drivers also need to be compatible with low-rights applications (for example, Internet Explorer 9).

XPS rendering filters and JavaScript files must all be hardened against all forms of untrusted data from applications, users, or data from across machine boundaries. Malformed PrintTickets, XPS documents, property bags, and even BidiResponses must be validated and parsed carefully and should never be used to store executable code. We recommend that partners use extensive fuzzed file testing to ensure graceful failure without compromising security integrity.

## Related topics

[V4 Printer Driver Development Best Practices](v4-printer-driver-development-best-practices.md)  
