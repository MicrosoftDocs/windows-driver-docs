---
title: Applying Security Descriptors on the Device Object
description: Applying Security Descriptors on the Device Object
ms.assetid: c0697021-cf78-4b85-b959-342179da5621
keywords:
- security descriptors WDK file systems , applying on device object
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Applying Security Descriptors on the Device Object


## <span id="ddk_applying_security_descriptors_on_the_device_object_if"></span><span id="DDK_APPLYING_SECURITY_DESCRIPTORS_ON_THE_DEVICE_OBJECT_IF"></span>


Most drivers use the access controls applied by the I/O manager against their device objects to protect themselves from inappropriate access. The simplest approach for most drivers is to apply an explicit security descriptor when the driver is installed. In an INF file, such security descriptors are described by the "Security" entry in the AddReg section. For more information about the complete language used to describe security descriptors, see Security Descriptor Definition Language in the Microsoft Windows SDK documentation.

The basic format of a security descriptor using the Security Descriptor Definition Language (SDDL) includes the following distinct pieces of a standard security descriptor:

-   The owner SID.

-   The group SID.

-   The discretionary access control list (DACL).

-   The system access control list (SACL).

Thus, the description within an INF script for a security descriptor is:

```cpp
O:owner-sidG:group-sidD:dacl-flags(ace)(ace)S:sacl-flags(ace)(ace)
```

The individual access control entries describe the access to be granted or denied to a particular group or user as specified by the security identifier or SID. For example, an INF file might contain a line such as:

```cpp
"D:P(A;CI;GR;;;BU)(A;CI;GR;;;PU)(A;CI;GA;;;BA)(A;CI;GA;;;SY)(A;CI;GA;;;NS)(A;CI;GA;;;LS)(A;CI;CCDCLCSWRPSDRC;;;S-1-5-32-556)"
```

The example above came from a NETTCPIP.INF file from a Microsoft Windows XP Service Pack 1 (SP1) system.

In this instance, there is no owner or group specified, so they default to the predefined or default values. The **D** indicates that this is a DACL. The **P** indicates that this is a protected ACL and does not inherit any rights from the containing object's security descriptor. The protected ACL prevents more lenient security on the parent from being inherited. The parenthetical expression indicates a single access control entry (ACE). An access control entry that uses the SDDL is made up of several distinct semicolon-separated components. In order, they are as follows:

-   The type indicator for the ACE. There are four unique types for DACLs and four different types for SACLs.

-   The **flags** field used to describe inheritance of this ACE for child objects or auditing and alarm policy for SACLs.

-   The **rights** field indicates which rights are granted or denied by the ACE. This field can either specify a specific numeric value indicating the generic, standard, and specific rights applicable to this ACE or use a string description of common access rights.

-   An object GUID if the DACL is an object-specific ACE structure.

-   An inherited object GUID if the DACL is an object-specific ACE structure

-   A SID indicating the security entity to which this ACE applies.

Thus, interpreting the sample security descriptor, the "A" leading up the ACE indicates that this is an "access allowed" entry. The alternative is an "access denied" entry, which is only infrequently used and is denoted by a leading "D" character. The **flags** field specifies Container Inherit (CI), which indicates that this ACE is inherited by sub-objects.

The **rights** field values encode specific rights that include generic rights and standard rights. For example, "GR" indicates "generic read" access and "GA" indicates "generic all" access, both of which are generic rights. A number of special rights follow these generic rights. In the sample above, "CC" indicates create child access, which is specific to file and directory rights. The sample above also includes other standard rights after the "CC" string including "DC" for delete child access, "LC" for list child access, "SW" for self-right access, "RP" for read property access, "SD" for standard delete access, and "RC" for read control access.

The SID entry strings in the sample above include "PU" for power users, "BU" for built-in users, "BA" for "built-in administrators, "LS" for the local service account, "SY" for the local system, and "NS" for the network service account. So in the example above, users are given generic read access on the object. In contrast, built-in administrators, the local service account, the local system, and the network service are given generic all access (read, write, and execute). The complete set of all possible rights and standard SID strings are documented in the Windows SDK.

These ACLs will be applied to all device objects created by a given driver. A driver can also control the security settings of specific objects by using the new function, [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407), when creating a named device object. The **IoCreateDeviceSecure** function is available on Windows XP Service Pack 1 and Windows Server 2003 and later. Using **IoCreateDeviceSecure**, the security descriptor to be applied to the device object is described using a subset of the full Security Descriptor Definition Language that is appropriate to device objects.

The purpose of applying specific security descriptors to device objects is to ensure that appropriate security checks are done against the device whenever an application attempts to access the device itself. For device objects that contain a name structure (the namespace of a file system, for example), the details of managing access to this device namespace belong to the driver, not to the I/O manager.

An interesting issue in these cases is how to handle security at the boundary between the I/O manager responsible for checking access to the driver device object and the device driver, which implements whatever security policy is appropriate for the driver. Traditionally, if the object being opened is the name of the device itself, the I/O manager will perform a full access check against the device object directly using its security descriptor. However, if the object being opened indicates a path inside the driver itself, the I/O manager will only check to ensure that traverse access is granted to the device object. Typically, this traverse right is granted because most threads have been granted **SeChangeNotifyPrivilege**, which corresponds with granting the traverse right to the directory. A device that does not support name structure would normally request that the I/O manager perform a full security check. This is done by setting the **FILE\_DEVICE\_SECURE\_OPEN** bit in the device characteristics field. A driver that includes a mix of such device objects should set this characteristic for those devices that do not support name structure. For example, a file system would set this option on its named device object (which does not support a naming structure), but would not set this option on its unnamed device objects (a volume, for example), which do support naming structure. Failing to set this bit correctly is a common bug in drivers and can allow inappropriate access to the device. For drivers that use the attachment interface ([**IoAttachDeviceToDeviceStackSafe**](https://msdn.microsoft.com/library/windows/hardware/ff548236), for example), the **FILE\_DEVICE\_SECURE\_OPEN** bit is set if this field is set in the device to which the driver is attaching. So, filter drivers don't need to worry about this particular aspect of security checking.

 

 




