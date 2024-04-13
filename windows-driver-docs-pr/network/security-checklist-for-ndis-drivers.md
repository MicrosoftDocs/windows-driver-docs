---
title: Security Checklist for NDIS Drivers
description: Security Checklist for NDIS Drivers
ms.date: 03/02/2023
---

# Security Checklist for NDIS Drivers





To make sure that your driver follows good security practices, do the following:

-   If it is possible, avoid code that parses the packet payload information for any reason. We recommend that you remove any such code, particularly in handling offload verification, from your driver's packet handling dispatch routines.

-   Check your driver's send and receive code paths and carefully verify any code that parses the packet payload information for any reason.

-   Thoroughly review the driver code for security holes and test your driver before you release the driver. Make sure that you verify all error paths as well as the normal code paths.

-   Run random packet generation tests to make sure that your drivers can resist bad packet information. In the future, such tests will be mandatory for device logo certification.

 

 





