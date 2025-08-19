---
title: Auditing in File Systems
description: Auditing
keywords:
- security, file systems , auditing, WDK
- auditing file systems, WDK
- events WDK file systems
- SeAuditingFileEvents
- SeAuditingFileOrGlobalEvents
- SeOpenObjectAuditAlarm
- event WDK See also events
ms.date: 07/11/2024
ms.topic: concept-article
---

# Auditing in file systems

One of the tenets of good security design is to admit that there's no such thing as a secure system. Developers know that certain people try to circumvent whatever security is present. This circumvention could be done actively, for example, by bad actors probing the security subsystem to find and exploit holes. Or it could be accidental, for example, inadvertently overwriting or deleting critical data. Whatever the cause, it's imperative to construct a system that can detect such breaches.

The auditing system within Windows provides a mechanism for tracking specific security events so that the log can be analyzed at a later time to perform post-mortem analysis of a damaged or compromised system. This auditing mechanism intimately involves the file system because the file system is responsible for maintaining the persistent storage of system data. For many systems, security needs are lower, and in those cases, auditing is disabled. File systems must be implemented in such a way that they can address the concerns of both these environments.

Key routines for auditing include:

* [**SeAuditingFileEvents**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seauditingfileevents), which determines whether file auditing is enabled on the system. This global policy check determines whether a full audit check should be done. It was introduced to optimize the security system operations.

* [**SeAuditingFileOrGlobalEvents**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seauditingfileorglobalevents), which determines whether file or global auditing is enabled on the system. This global policy check determines whether a full audit check should be done on file events or global events. It was introduced to optimize the security system operations.

* [**SeOpenObjectAuditAlarm**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seopenobjectauditalarm), which performs the primary audit operations in the Windows system. It audits an attempt to open an object. It doesn't audit whether access to the object was successful or unsuccessful.

There's no requirement for auditing. For example, the [FastFAT and CDFS sample file systems](https://github.com/microsoft/Windows-driver-samples/tree/main/filesys) don't implement auditing. However, from a security perspective, auditing is important because it allows administrators to monitor the security behavior of the system.
