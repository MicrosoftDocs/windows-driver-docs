---
title: Windows security model
description: The Windows security model is based primarily on per-object rights, with a small number of system-wide privileges.
ms.assetid: 3A7ECA7C-1FE6-4ADB-97A9-A61C6FCE9F04
---

# Windows security model


**Last updated:**

-   July 7, 2004

The Windows security model is based primarily on per-object rights, with a small number of system-wide privileges. Objects that can be secured include, —but are not limited to, —processes, threads, events and other synchronization objects, as well as files, directories, and devices.

For each type of object, the generic read, write, and execute rights map into detailed object-specific rights. For example, for files and directories, possible rights include the right to read or write the file or directory, the right to read or write extended file attributes, the right to traverse a directory, and the right to write an object’s security descriptor. For more information, including a complete list of rights, see “Security (General)” in the “Security” section of the [MSDN Library](http://msdn.microsoft.com/).

The security model involves the following concepts:

-   Security identifiers (SIDs)
-   Access tokens
-   Security descriptors
-   Access Control Lists (ACLs)
-   Privileges

## <span id="Security_Identifiers__SIDs_"></span><span id="security_identifiers__sids_"></span><span id="SECURITY_IDENTIFIERS__SIDS_"></span>Security Identifiers (SIDs)


A security identifier (SID, also called a *principal*) identifies a user, a group, or a logon session. Each user has a unique SID, which is retrieved by the operating system at logon.

SIDs are issued by an authority such as the operating system or a domain server. Some SIDs are well-known and have names as well as identifiers. For example, the SID S-1-1-0 identifies Everyone (or World).

## <span id="Access_tokens"></span><span id="access_tokens"></span><span id="ACCESS_TOKENS"></span>Access tokens


Every process has an access token. The access token describes the complete security context of the process. It contains the SID of the user, the SID of the groups to which the user belongs, and the SID of the logon session, as well as a list of the system-wide privileges granted to the user.

By default, the system uses the primary access token for a process whenever a thread of the process interacts with a securable object. However, a thread can impersonate a client account. When a thread impersonates, it has an impersonation token in addition to its own primary token. The impersonation token describes the security context of the user account that the thread is impersonating. Impersonation is especially common in Remote Procedure Call (RPC) handling.

An access token that describes a restricted security context for a thread or process is called a restricted token. The SIDs in a *restricted token* can be set only to deny access, not to allow access, to securable objects. In addition, the token can describe a limited set of system-wide privileges. The user’s SID and identity remain the same, but the user’s access rights are limited while the process is using the restricted token. The **CreateRestrictedToken** function creates a restricted token.

Restricted tokens are useful for running untrusted code, such as email attachments. Windows XP uses a restricted token when you right-click an executable file, select **Run As**, and select **Protect my computer and data from unauthorized program activity**.

## <span id="Security_descriptors"></span><span id="security_descriptors"></span><span id="SECURITY_DESCRIPTORS"></span>Security descriptors


Every named Windows object has a security descriptor; some unnamed objects do, too. The security descriptor describes the owner and group SIDs for the object along with its ACLs.

An object’s security descriptor is usually created by the function that creates the object. When a driver calls the **IoCreateDevice** or **IoCreateDeviceSecure** routine to create a device object, the system applies a security descriptor to the created device object and sets ACLs for the object. For most devices, ACLs are specified in the device Information (INF) file.

## <span id="Access_Control_Lists"></span><span id="access_control_lists"></span><span id="ACCESS_CONTROL_LISTS"></span>Access Control Lists


Access Control Lists (ACLs) enable fine-grained control over access to objects. An ACL is part of the security descriptor for each object.

Each ACL contains zero or more access control entries (ACE). Each ACE, in turn, contains a single SID that identifies a user, group, or computer and a list of rights that are denied or allowed for that SID.

### <span id="ACLs_for_device_objects"></span><span id="acls_for_device_objects"></span><span id="ACLS_FOR_DEVICE_OBJECTS"></span>ACLs for device objects

The ACL for a device object can be set in any of three ways:

-   Set in the default security descriptor for its device type.
-   Created programmatically by the **RtlCreateSecurityDescriptor** function and set by the **RtlSetDaclSecurityDescriptor** function.
-   Specified in Security Descriptor Definition Language (SDDL) in the device’s INF file or in a call to the **IoCreateDeviceSecure** routine.

All new drivers should use SDDL in the INF file to specify ACLs for their device objects.

SDDL is an extensible description language that enables components to create ACLs in a string format. SDDL is used by both user-mode and kernel-mode code. The following figure shows the format of SDDL strings for device objects.

![sddl strings for device objects](images/wsm-sddlstrings.gif)

The Access value specifies the type of access allowed. The SID value specifies a security identifier that determines to whom the Access value applies (for example, a user or group).

For example, the following SDDL string allows the System (SY) access to everything and allows everyone else (WD) only read access:

``` syntax
“D:P(A;;GA;;;SY)(A;;GR;;;WD)”
```

The header file wdmsec.h also includes a set of predefined SDDL strings that are suitable for device objects. For example, the header file defines SDDL\_DEVOBJ\_SYS\_ALL\_ADM\_RWX\_WORLD\_RWX\_RES\_RWX as follows:

``` syntax
"D:P(A;;GA;;;SY)(A;;GRGWGX;;;BA)(A;;GRGWGX;;;WD)(A;;GRGWGX;;;RC)"
```

The first segment of this string allows the kernel and operating system (SY) complete control over the device. The second segment allows anyone in the built-in Administrators group (BA) to access the entire device, but not to change the ACL. The third segment allows everyone (WD) to read or write to the device, and the fourth segment grants the same rights to untrusted code (RC). Drivers can use the predefined strings as is or as models for device-object-specific strings.

All device objects in a stack should have the same ACLs. Changing the ACLs on one device object in the stack changes the ACLs on the entire device stack.

However, adding a new device object to the stack does not change any ACLs, either those of the new device object (if it has ACLs) or those of any existing device objects in the stack. When a driver creates a new device object and attaches it to the top of the stack, the driver should copy the ACLs for the stack to the new device object by copying the **DeviceObject.Characteristics** field from the next lower driver.

The **IoCreateDeviceSecure** routine supports a subset of SDDL strings that use predefined SIDs such as WD and SY. User-mode APIs and INF files support the full SDDL syntax.

### <span id="Security_checks_using_ACLs"></span><span id="security_checks_using_acls"></span><span id="SECURITY_CHECKS_USING_ACLS"></span>Security checks using ACLs

When a process requests access to an object, security checks compare the ACLs for the object against the SIDs in the caller’s access token.

The system compares the ACEs in a strict top-down order and stops on the first relevant match. Therefore, when creating an ACL, you should always put denial ACEs above the corresponding grant ACEs. The following examples show how the comparison proceeds.

**Example 1: Comparing an ACL to an access token**

Example 1 shows how the system compares an ACL to the access token for a caller’s process. Assume that the caller wants to open a file that has the ACL that is shown in the following table.

**Sample File ACL**

| Permission | SID        | Access                |
|------------|------------|-----------------------|
| Allow      | Accounting | Write, delete         |
| Allow      | Sales      | Append                |
| Deny       | Legal      | Append, write, delete |
| Allow      | Everyone   | Read                  |

 

This ACL has four ACEs, which apply specifically to the Accounting, Sales, Legal, and Everyone groups.

Next, assume the access token for the requesting process contains SIDs for one user and three groups, in the following order:

User Jim (S-1-5-21…)

Group Accounting (S-1-5-22…)

Group Legal (S-1-5-23…)

Group Everyone (S-1-1-0)

When comparing a file ACL to an access token, the system first looks for an ACE for user Jim in the file’s ACL. None appears, so next it looks for an ACE for the Accounting group. As shown in the previous table, an ACE for the Accounting group appears as the first entry in the file’s ACL, so Jim'’s process is granted the right to write or delete the file and the comparison stops. If the ACE for the Legal group instead preceded the ACE for the Accounting group in the ACL, the process would be denied write, append, and delete access to the file.

**Example 2: Comparing an ACL to a restricted token**

The system compares an ACL to a restricted token in the same way that it compares those in a token that is not restricted. However, a denial SID in a restricted token can match only a Deny ACE in an ACL.

Example 2 shows how the system compares a file’s ACL with a restricted token. Assume the file has the same ACL shown in the previous table. In this example, however, the process has a restricted token that contains the following SIDs:

User Jim (S-1-5-21…) Deny

Group Accounting (S-1-5-22…) Deny

Group Legal (S-1-5-23…) Deny

Group Everyone (S-1-1-0)

The file’s ACL does not list Jim’s SID, so the system proceeds to the Accounting group SID. Although the file’s ACL has an ACE for the Accounting group, this ACE allows access; therefore, it does not match the SID in the process’s restricted token, which denies access. As a result, the system proceeds to the Legal group SID. The ACL for the file contains an ACE for the Legal group that denies access, so the process cannot write, append, or delete the file.

## <span id="Privileges"></span><span id="privileges"></span><span id="PRIVILEGES"></span>Privileges


A privilege is the right for a user to perform a system-related operation on the local computer, such as loading a driver, changing the time, or shutting down the system.

Privileges are different from access rights because they apply to system-related tasks and resources rather than objects, and because they are assigned to a user or group by a system administrator, rather than by the operating system.

The access token for each process contains a list of the privileges granted to the process. Privileges must be specifically enabled before use. An administrator enables and audits the use of privileges by using **Administrative Tools** in the Windows Control Panel; privileges can also be enabled programmatically.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Windows%20security%20model%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




