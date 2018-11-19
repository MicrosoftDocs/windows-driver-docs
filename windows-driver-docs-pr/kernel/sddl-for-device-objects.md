---
title: SDDL for Device Objects
description: SDDL for Device Objects
ms.assetid: c0e4432a-4429-4ecd-a2e5-f93a9e3caf48
keywords: ["device objects WDK kernel , security", "security WDK device objects", "Security Descriptor Definition Language WDK device objects", "SDDL WDK device objects", "IoCreateDeviceSecure", "security descriptors WDK device objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# SDDL for Device Objects





The Security Descriptor Definition Language (SDDL) is used to represent security descriptors. Security for device objects can be specified by an SDDL string that is [placed in an INF file](https://msdn.microsoft.com/library/windows/hardware/ff540212) or passed to [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407). The [Security Descriptor Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa379567) is fully documented in the Microsoft Windows SDK documentation.

While INF files support the full range of SDDL, only a subset of the language is supported by the **IoCreateDeviceSecure** routine. This subset is defined here.

SDDL strings for device objects are of the form "D:P" followed by one or more expressions of the form "(A;;*Access*;;;*SID*)". The *SID* value specifies a security identifier that determines to whom the *Access* value applies (for example, a user or group). The *Access* value specifies the access rights allowed for the SID. The *Access* and *SID* values are as follows.

**Note**  When using SDDL for device objects, your driver must link against Wdmsec.lib.

 

<a href="" id="access"></a>*Access*  
Specifies an [**ACCESS\_MASK**](access-mask.md) value that determines the allowed access. This value can be written either as a hexadecimal value in the form "0x*hex*", or as a sequence of two-letter symbolic codes that represent access rights.

The following codes can be used to specify generic access rights.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Generic access right</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>GA</p></td>
<td><p>GENERIC_ALL</p></td>
</tr>
<tr class="even">
<td><p>GR</p></td>
<td><p>GENERIC_READ</p></td>
</tr>
<tr class="odd">
<td><p>GW</p></td>
<td><p>GENERIC_WRITE</p></td>
</tr>
<tr class="even">
<td><p>GX</p></td>
<td><p>GENERIC_EXECUTE</p></td>
</tr>
</tbody>
</table>

 

The following codes can be used to specify specific access rights.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Specific access right</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>RC</p></td>
<td><p>READ_CONTROL</p></td>
</tr>
<tr class="even">
<td><p>SD</p></td>
<td><p>DELETE</p></td>
</tr>
<tr class="odd">
<td><p>WD</p></td>
<td><p>WRITE_DAC</p></td>
</tr>
<tr class="even">
<td><p>WO</p></td>
<td><p>WRITE_OWNER</p></td>
</tr>
</tbody>
</table>

 

Note that GENERIC\_ALL grants all the rights listed in the above two tables, including the ability to change the ACL.

<a href="" id="sid"></a>*SID*  
Specifies the SID that is granted the specified access. SIDs represent accounts, aliases, groups, users, or computers.

The following SIDs represent *accounts* on the machine.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>SID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SY</p></td>
<td><p>System</p>
<p>Represents the operating system itself, including its user-mode components.</p></td>
</tr>
<tr class="even">
<td><p>LS</p></td>
<td><p>Local Service</p>
<p>A predefined account for local services (which also belongs to Authenticated and World). This SID is available starting with Windows XP.</p></td>
</tr>
<tr class="odd">
<td><p>NS</p></td>
<td><p>Network Service</p>
<p>A predefined account for network services (which also belongs to Authenticated and World). This SID is available starting with Windows XP.</p></td>
</tr>
</tbody>
</table>

 

The following SIDs represent *groups* on the machine.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>SID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>BA</p></td>
<td><p>Administrators</p>
<p>The built-in Administrators group on the machine.</p></td>
</tr>
<tr class="even">
<td><p>BU</p></td>
<td><p>Built-in User Group</p>
<p>Group covering all local user accounts, and users on the domain.</p></td>
</tr>
<tr class="odd">
<td><p>BG</p></td>
<td><p>Built-in Guest Group</p>
<p>Group covering users logging in using the local or domain guest account.</p></td>
</tr>
</tbody>
</table>

 

The following SIDs describe the extent to which a user has been authenticated.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>SID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>AU</p></td>
<td><p>Authenticated Users</p>
<p>Any user recognized by the local machine or by a domain. Note that users logged in using the Builtin Guest account are not authenticated. However, members of the Guests group with individual accounts on the machine or the domain are authenticated.</p></td>
</tr>
<tr class="even">
<td><p>AN</p></td>
<td><p>Anonymous Logged-on User</p>
<p>Any user logged on without an identity, such as an anonymous network session. Note that users logging in using the Builtin Guest account are neither authenticated nor anonymous. This SID is available starting with Windows XP.</p></td>
</tr>
</tbody>
</table>

 

The following SIDs describe how the user logged into the machine.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>SID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>IU</p></td>
<td><p>Interactive Users</p>
<p>Users who initially logged onto the machine &quot;interactively&quot;, such as local logons and Remote Desktops logons.</p></td>
</tr>
<tr class="even">
<td><p>NU</p></td>
<td><p>Network Logon User</p>
<p>Users accessing the machine remotely, without interactive desktop access (for example, file sharing or RPC calls).</p></td>
</tr>
<tr class="odd">
<td><p>WD</p></td>
<td><p>World</p>
<p>Before Windows XP, this SID covered every session, whether authenticated users, anonymous users, or the Builtin Guest account.</p>
<p>Starting with Windows XP, this SID does not cover anonymous logon sessions; it covers only authenticated users and the Builtin Guest account.</p>
<p>Note that untrusted or &quot;restricted&quot; code is also not covered by the World SID. For more information, see the description of the Restricted Code (RC) SID in the following table.</p></td>
</tr>
</tbody>
</table>

 

The following SIDs deserve special mention.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>SID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>RC</p></td>
<td><p>Restricted Code</p>
<p>This SID is used to control access by untrusted code. ACL validation against tokens with RC consists of two checks, one against the token&#39;s normal list of SIDs (containing WD for instance), and one against a second list (typically containing RC and a subset of the original token SIDs). Access is granted only if a token passes both tests. As such, RC actually works in combination with other SIDs.</p>
<p>Any ACL that specifies RC must also specify WD. When RC is paired with WD in an ACL, a superset of Everyone including untrusted code is described.</p>
<p>Untrusted code might be code launched using the Run As option in Explorer. By default, World does not cover untrusted code.</p></td>
</tr>
<tr class="even">
<td><p>UD</p></td>
<td><p>User-Mode Drivers</p>
<p>This SID grants access to user-mode drivers. Currently, this SID covers only drivers that are written for the User-Mode Driver Framework (UMDF). This SID is available starting with Windows 8.</p>
<p>In earlier versions of Windows, which do not recognize the &quot;UD&quot; abbreviation, you must specify the fully qualified form of this SID (S-1-5-84-0-0-0-0-0) to grant access to UMDF drivers. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh439567" data-raw-source="[Controlling Device Access](https://msdn.microsoft.com/library/windows/hardware/hh439567)">Controlling Device Access</a> in the User-Mode Driver Framework documentation.</p></td>
</tr>
</tbody>
</table>

 

### SDDL Examples For Device Objects

This section describes the predefined SDDL strings found in Wdmsec.h. You can also use these as templates to define new SDDL strings for device objects.

SDDL\_DEVOBJ\_KERNEL\_ONLY

**"D:P"**

SDDL\_DEVOBJ\_KERNEL\_ONLY is the "empty" ACL. User-mode code (including processes running as system) cannot open the device.

A PnP bus driver could use this descriptor when creating a PDO. The INF file could then specify looser security settings for the device. By specifying this descriptor, the bus driver would ensure that no attempt to open the device before the INF was processed would succeed.

Similarly, a non-WDM driver could use this descriptor to make its device objects inaccessible until the appropriate user-mode program (such as an installer) sets the final security descriptor in the registry.

In all of these cases, the default is tight security, loosened as necessary.

SDDL\_DEVOBJ\_SYS\_ALL

**"D:P(A;;GA;;;SY)"**

SDDL\_DEVOBJ\_SYS\_ALL is similar to SDDL\_DEVOBJ\_KERNEL\_ONLY, except that in addition to kernel-mode code, user-mode code running as System is also allowed to open the device for any access.

A legacy driver might use this ACL to start with tight security settings, and let its service open the device up at run time to individual users by using the **SetFileSecurity** user-mode function. In this case, the service would have to be running as System.

SDDL\_DEVOBJ\_SYS\_ALL\_ADM\_ALL

**"D:P(A;;GA;;;SY)(A;;GA;;;BA)"**

SDDL\_DEVOBJ\_SYS\_ALL\_ADM\_ALL allows the kernel, system, and administrator complete control over the device. No other users may access the device.

SDDL\_DEVOBJ\_SYS\_ALL\_ADM\_RWX\_WORLD\_R

**"D:P(A;;GA;;;SY)(A;;GRGWGX;;;BA)(A;;GR;;;WD)"**

SDDL\_DEVOBJ\_SYS\_ALL\_ADM\_RWX\_WORLD\_R allows the kernel and system complete control over the device. By default the administrator can access the entire device, but cannot change the ACL (the administrator must take control of the device first.)

Everyone (the World SID) is given read access. Untrusted code cannot access the device (untrusted code might be code launched using the Run As option in Explorer. By default, World does not cover Restricted code.)

Also note that traversal access is not granted to normal users. As such, this might not be an appropriate descriptor for a device with a namespace.

SDDL\_DEVOBJ\_SYS\_ALL\_ADM\_RWX\_WORLD\_R\_RES\_R

**"D:P(A;;GA;;;SY)(A;;GRGWGX;;;BA)(A;;GR;;;WD)(A;;GR;;;RC)"**

SDDL\_DEVOBJ\_SYS\_ALL\_ADM\_RWX\_WORLD\_R\_RES\_R allows the kernel and system complete control over the device. By default the administrator can access the entire device, but cannot change the ACL (the administrator must take control of the device first.)

Everyone (the World SID) is given read access. In addition, untrusted code is also allowed to access code. Untrusted code might be code launched using the Run As option in Explorer. By default, World does not cover Restricted code.

Also note that traversal access is not granted to normal users. As such, this might not be an appropriate descriptor for a device with a namespace.

 

Note that the above SDDL strings do not include any inheritance modifiers. As such, they are only appropriate for device objects and should not be used for files or registry keys. For more information about specifying inheritance using SDDL, see the Microsoft Windows SDK documentation.

 

 




