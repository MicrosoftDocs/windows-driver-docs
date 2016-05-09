---
title: Access Control List
author: windows-driver-content
description: Access Control List
ms.assetid: e682c2cc-ddd7-482b-b4f2-3e163d914752
keywords: ["security descriptors WDK file systems , access control list", "descriptors WDK file systems , access control list", "access control list WDK file systems", "ACL WDK file systems", "discretionary ACL WDK file systems", "system ACL WDK file systems", "mandatory controls WDK file systems", "protected objects WDK file systems", "object security WDK file systems", "access control entry WDK file systems", "ACE WDK file systems"]
---

# Access Control List


## <span id="ddk_access_control_list_if"></span><span id="DDK_ACCESS_CONTROL_LIST_IF"></span>


An access control list (ACL) is a list of ACEs created by the operating system to control the security behavior associated with a given (protected) object of some sort. In Windows there are two types of ACLs:

-   **Discretionary ACL**--this is a list of zero or more ACEs that describe the access rights for a protected object. It is discretionary because the access granted is at the discretion of the owner or any user with appropriate rights.

-   **System ACL**--this is a list of zero or more ACEs that describe the auditing and alarm policy for a protected object.

The term "discretionary" refers to the differentiation between mandatory and discretionary control. In an environment that uses mandatory controls, the owner of an object may not be able to grant access to the object. In a discretionary environment, such as Windows, the owner of an object is allowed to grant such access. Mandatory controls are normally associated with very tight security environments, such as those using compartmentalized security, where the system must prevent disclosure of sensitive information between users on the same system.

A driver constructing an ACL would follow a few key steps:

1.  Allocate storage for the ACL.

2.  Initialize the ACL.

3.  Add zero (or more) ACEs to the ACL.

The following code examples demonstrate how to construct an ACL:

```
    dacl = ExAllocatePool(PagedPool, PAGE_SIZE);
    if (!dacl) {
        return;
    }
    status = RtlCreateAcl(dacl, PAGE_SIZE, ACL_REVISION);
    if (!NT_SUCCESS(status)) {
        ExFreePool(dacl);
        return;
    }
```

The previous code fragment creates an empty ACL. The code sample allocates a significant amount of memory, since we do not know the size required for the ACL.

At this point, the ACL is empty because it has no ACE entries. An empty ACL denies access to anyone trying to access the object because there are no entries that grant such access. The following code fragment adds an ACE to this ACL:

```
    status = RtlAddAccessAllowedAce(dacl, ACL_REVISION,  FILE_ALL_ACCESS, SeExports->SeWorldSid);
    if (!NT_SUCCESS(status)) {
        ExFreePool(dacl);
        return;
    }
```

This entry would now grant access to any entity that accessed the object. This is the purpose of world access SID (SeWorldSid), which is usually represented as "Everyone" access in other Windows system utilities.

Note that when constructing ACLs, it is important to order access denied ACE entries at the beginning of the ACL, and then access allowed ACE entries at the end of the ACL. This is because when the security reference monitor does the evaluation of the ACL it will grant access if it finds an ACE granting access, before it finds the denied ACEs. This behavior is well documented in the Microsoft Windows SDK, but it relates to the specific mechanism the security reference monitor uses to determine whether access should be granted or denied.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Access%20Control%20List%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


