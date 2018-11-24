---
title: SECURITY\_DESCRIPTOR\_CONTROL
description: SECURITY\_DESCRIPTOR\_CONTROL
ms.assetid: 6a7fe617-156d-4eb0-83f7-df78104acbde
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SECURITY\_DESCRIPTOR\_CONTROL


The **SECURITY\_DESCRIPTOR\_CONTROL** type is a set of bit flags that qualify the meaning of a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff556610) structure or its components. Each security descriptor has a **Control** member that stores the **SECURITY\_DESCRIPTOR\_CONTROL** bits.

SECURITY\_DESCRIPTOR\_CONTROL

``` syntax
typedef USHORT SECURITY_DESCRIPTOR_CONTROL, *PSECURITY_DESCRIPTOR_CONTROL;
```

The control value can include a combination of the following **SECURITY\_DESCRIPTOR\_CONTROL** bit flags:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>SE_DACL_AUTO_INHERIT_REQ</p></td>
<td align="left"><p>Requests that the provider for the object protected by the security descriptor automatically propagate the DACL to existing child objects. If the provider supports automatic inheritance, it propagates the DACL to any existing child objects, and sets the SE_DACL_AUTO_INHERITED bit in the security descriptors of the object and its child objects.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SE_DACL_AUTO_INHERITED</p></td>
<td align="left"><p>Starting with Windows 2000, indicates a security descriptor in which the DACL supports automatic propagation of inheritable ACEs to existing child objects.</p>
<p>For Windows 2000 ACLs that support auto-inheritance, this bit is always set. It is used to distinguish these ACLs from Windows NT 4.0 ACLs that do not support auto-inheritance.</p>
<p>This bit is not set in security descriptors for Windows NT 4.0 and earlier, which do not support automatic propagation of inheritable ACEs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SE_DACL_DEFAULTED</p></td>
<td align="left"><p>Indicates a security descriptor with a default DACL. For example, if an object&#39;s creator does not specify a DACL, the object receives the default DACL from the creator&#39;s access token. This flag can affect how the system treats the DACL, with respect to ACE inheritance. The system ignores this flag if the SE_DACL_PRESENT flag is not set.</p>
<p>This flag is used to determine how the final DACL on the object is to be computed and is not stored physically in the security descriptor control of the securable object.</p>
<p>To set this flag, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff562781" data-raw-source="[&lt;strong&gt;RtlSetDaclSecurityDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562781)"><strong>RtlSetDaclSecurityDescriptor</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SE_DACL_PRESENT</p></td>
<td align="left"><p>Indicates a security descriptor that has a DACL. If this flag is not set, or if this flag is set and the DACL is <strong>NULL</strong>, the security descriptor allows full access to everyone.</p>
<p>This flag is used to hold the security information specified by a caller until the security descriptor is associated with a securable object. Once the security descriptor is associated with a securable object, the SE_DACL_PRESENT flag is always set in the security descriptor control.</p>
<p>To set this flag, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff562781" data-raw-source="[&lt;strong&gt;RtlSetDaclSecurityDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562781)"><strong>RtlSetDaclSecurityDescriptor</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SE_DACL_PROTECTED</p></td>
<td align="left"><p>Protects the DACL of the security descriptor from being modified by inheritable ACEs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SE_DACL_UNTRUSTED</p></td>
<td align="left"><p>Indicates that the ACL pointed to by the DACL of the security descriptor was provided by an untrusted source. If this flag is set and a compound ACE is encountered, the system will substitute known valid SIDs for the server SIDs in the ACEs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SE_GROUP_DEFAULTED</p></td>
<td align="left"><p>A default mechanism, rather than the original provider of the security descriptor, provided the security descriptor&#39;s group SID.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SE_OWNER_DEFAULTED</p></td>
<td align="left"><p>A default mechanism, rather than the original provider of the security descriptor, provided the security descriptor&#39;s owner security identifier (SID). To set this flag, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553220" data-raw-source="[&lt;strong&gt;RtlSetOwnerSecurityDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553220)"><strong>RtlSetOwnerSecurityDescriptor</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SE_RM_CONTROL_VALID</p></td>
<td align="left"><p>Indicates that the resource control manager bits in the security descriptor are valid. The resource manager control bits are eight bits in the <strong>Sbz1</strong> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556610" data-raw-source="[&lt;strong&gt;SECURITY_DESCRIPTOR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556610)"><strong>SECURITY_DESCRIPTOR</strong></a> structure that contains information specific to the resource manager accessing the structure. (For more information, see the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0 documentation.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>SE_SACL_AUTO_INHERIT_REQ</p></td>
<td align="left"><p>Requests that the provider for the object protected by the security descriptor automatically propagate the SACL to existing child objects. If the provider supports automatic inheritance, it propagates the SACL to any existing child objects, and sets the SE_SACL_AUTO_INHERITED bit in the security descriptors of the object and its child objects.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SE_SACL_AUTO_INHERITED</p></td>
<td align="left"><p>Indicates a security descriptor in which the SACL supports automatic propagation of inheritable ACEs to existing child objects. This bit is set only if the automatic inheritance algorithm has been performed for the object and its existing child objects.</p>
<p>This bit is not set in security descriptors for Windows NT 4.0 and earlier, which did not support automatic propagation of inheritable ACEs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SE_SACL_DEFAULTED</p></td>
<td align="left"><p>A default mechanism, rather than the original provider of the security descriptor, provided the SACL. This flag can affect how the system treats the SACL, with respect to ACE inheritance. The system ignores this flag if the SE_SACL_PRESENT flag is not set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SE_SACL_PRESENT</p></td>
<td align="left"><p>Indicates a security descriptor that has a SACL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SE_SACL_PROTECTED</p></td>
<td align="left"><p>Protects the SACL of the security descriptor from being modified by inheritable ACEs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SE_SELF_RELATIVE</p></td>
<td align="left"><p>Indicates a security descriptor in self-relative format with all the security information in a contiguous block of memory. If this flag is not set, the security descriptor is in absolute format. For more information, see &quot;Absolute and Self-Relative Security Descriptors&quot; in the Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SE_SERVER_SECURITY</p></td>
<td align="left"><p>Requests that the provider for the object protected by the security descriptor whose ACL should a server ACL based on the input ACL, regardless of its source (explicit or defaulting). This is done by replacing all of the GRANT ACEs with compound ACEs granting the current server. This flag is only meaningful if the subject is impersonating.</p></td>
</tr>
</tbody>
</table>

 

## Requirements


ntifs.h (include ntifs.h)

## Related topics


[**ACE**](ace.md)

[**ACL**](https://msdn.microsoft.com/library/windows/hardware/ff538866)

[**RtlSetDaclSecurityDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff562781)

[**RtlSetOwnerSecurityDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff553220)

[**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff556610)

 

 






