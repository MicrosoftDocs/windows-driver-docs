---
title: Access Control Entry
author: windows-driver-content
description: Access Control Entry
ms.assetid: 4dc72f43-e5a7-441d-8586-f8893b9c1084
keywords: ["security descriptors WDK file systems , access control entry", "descriptors WDK file systems , access control entry", "access control entry WDK file systems", "ACE WDK file systems", "security identifiers WDK file systems", "SIDs WDK file systems"]
---

# Access Control Entry


## <span id="ddk_access_control_entry_if"></span><span id="DDK_ACCESS_CONTROL_ENTRY_IF"></span>


An access control entry (ACE) describes access rights associated with a particular SID. The access control entry is evaluated by the operating system in order to compute the effective access granted to a particular program based upon its credentials. For example, when a user logs on to the computer, and then executes a program, the program uses the credentials associated with that particular user's account.

Thus, when a program attempts to open an object, Windows compares the credentials associated with the program against the security controls associated with the object. The security reference monitor then uses the ACE information to determine if the program should be allowed or denied access to the given object. Thus, the ACE determines the behavior of the security subsystem.

The following figure illustrates the access control entry.

![diagram illustrating the access control entry](images/fssecurity-04.png)

There are five types of ACEs used by the security subsystem. The **Type** member of the ACE structure controls the interpretation of the ACE. The defined types are:

-   **ACCESS\_ALLOWED\_ACE\_TYPE**—this type indicates that the ACE specifies access rights that will be granted to the specific SID.

-   **ACCESS\_DENIED\_ACE\_TYPE**—this type indicates that the ACE specifies access rights that are to be denied to the specific SID.

-   **SYSTEM\_AUDIT\_ACE\_TYPE**—this type indicates that the ACE specifies auditing behavior.

-   **SYSTEM\_ALARM\_ACE\_TYPE**—this type indicates that the ACE specifies alarm behavior.

-   **ACCESS\_ALLOWED\_COMPOUND\_ACE\_TYPE**—this type indicates that the ACE is tied to a particular server and the entity it is impersonating.

Thus, three of the types are used to control programmatic access to an object, while the other two are used to control the audit and alarm behavior of the security subsystem when the object is accessed. Note that the actual behavior of the security subsystem is computed by combining the information for some or all of the ACEs associated with the object.

A driver may construct an access control entry of ACCESS\_ALLOWED\_ACE\_TYPE using the routine [**RtlAddAccessAllowedAce**](https://msdn.microsoft.com/library/windows/hardware/ff552092). For adding the other types of ACE entries, driver writers must construct their own functions because the WDK does not provide any other support routines.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Access%20Control%20Entry%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


