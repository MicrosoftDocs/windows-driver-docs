---
title: Auditing
description: Auditing
ms.assetid: 0a703a27-91d6-41fc-bd46-a9486842a150
keywords: ["security WDK file systems , auditing", "auditing WDK file systems", "events WDK file systems", "SeAuditingFileEvents", "SeOpenObjectAuditAlarm", "event WDK See also events"]
---

# Auditing


## <span id="ddk_auditing_if"></span><span id="DDK_AUDITING_IF"></span>


One of the tenets of good security design is to admit that there is no such thing as a secure system. Developers for the system must be aware that people will circumvent whatever security is present. This could be done actively, for example, by probing the security subsystem to find and exploit holes within the system. Or this could be accidental, for example, inadvertently overwriting or deleting critical data. Whatever the cause, it is imperative to construct a system that can detect such breaches.

The auditing system within Windows provides a mechanism for tracking specific security events so that the log can be analyzed at a later time to perform post-mortem analysis of a damaged or compromised system. The auditing mechanism on Windows intimately involves the file system because the file system is responsible for maintaining the persistent storage of system data. For many systems, security needs are much lower, and in those cases, auditing is disabled. File systems must be implemented in such a way that they can address the concerns of both these environments.

Key routines for auditing include:

-   [**SeAuditingFileEvents**](https://msdn.microsoft.com/library/windows/hardware/ff554770)--this routine determines whether file auditing has been enabled on the system; this is a global policy check to determine whether a full audit check should be done. This routine was introduced to optimize the security system operations.

-   [**SeOpenObjectAuditAlarm**](https://msdn.microsoft.com/library/windows/hardware/ff556682)--this routine performs the primary audit operations in the Windows system (audits an attempt to open an object). Note that it is the attempt to access the object that is audited, not whether access to the object was successful or unsuccessful.

There is no requirement for auditing. None of the sample file systems (FAT or CDFS, for example) in the IFS section of the WDK implement auditing. However, from a security perspective, auditing is important because it allows administrators to monitor the security behavior of the system.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Auditing%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




