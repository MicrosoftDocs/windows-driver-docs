---
title: Auditing
description: Auditing
ms.assetid: 0a703a27-91d6-41fc-bd46-a9486842a150
keywords:
- security WDK file systems , auditing
- auditing WDK file systems
- events WDK file systems
- SeAuditingFileEvents
- SeOpenObjectAuditAlarm
- event WDK See also events
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Auditing


## <span id="ddk_auditing_if"></span><span id="DDK_AUDITING_IF"></span>


One of the tenets of good security design is to admit that there is no such thing as a secure system. Developers for the system must be aware that people will circumvent whatever security is present. This could be done actively, for example, by probing the security subsystem to find and exploit holes within the system. Or this could be accidental, for example, inadvertently overwriting or deleting critical data. Whatever the cause, it is imperative to construct a system that can detect such breaches.

The auditing system within Windows provides a mechanism for tracking specific security events so that the log can be analyzed at a later time to perform post-mortem analysis of a damaged or compromised system. The auditing mechanism on Windows intimately involves the file system because the file system is responsible for maintaining the persistent storage of system data. For many systems, security needs are much lower, and in those cases, auditing is disabled. File systems must be implemented in such a way that they can address the concerns of both these environments.

Key routines for auditing include:

-   [**SeAuditingFileEvents**](https://msdn.microsoft.com/library/windows/hardware/ff554770)--this routine determines whether file auditing has been enabled on the system; this is a global policy check to determine whether a full audit check should be done. This routine was introduced to optimize the security system operations.

-   [**SeOpenObjectAuditAlarm**](https://msdn.microsoft.com/library/windows/hardware/ff556682)--this routine performs the primary audit operations in the Windows system (audits an attempt to open an object). Note that it is the attempt to access the object that is audited, not whether access to the object was successful or unsuccessful.

There is no requirement for auditing. None of the sample file systems (FAT or CDFS, for example) in the IFS section of the WDK implement auditing. However, from a security perspective, auditing is important because it allows administrators to monitor the security behavior of the system.

 

 




