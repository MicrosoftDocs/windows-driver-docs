---
title: WIA Security and Security Descriptors
description: WIA Security and Security Descriptors
ms.assetid: 2919f3fc-1eb5-4801-a589-ae3000320763
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Security and Security Descriptors





Many of the solutions to the problems listed in [Common WIA Security Problems](common-wia-security-problems.md) require the objects in question to have security descriptors that grant access to the appropriate entities, such as **LocalService** accounts.

Generally, the **LocalService** account has access to resources whose ACLs allow access by a **LocalService** account, Everyone, or Authenticated users. The service cannot share objects (pipes, file mapping, synchronization, and so on) with other applications, unless it creates a discretionary access control list(DACL) that allows a user or group of users access to the object.

The following code example illustrates how to set the security descriptor. This approach can be used if an application and driver need to share a named event object.

```cpp
//
//  Security descriptor in SDDL form:
//  D:           - Indicates what follows is a 
//                 Discretionary Access Control List (DACL)
//  (A;;GA;;;LS) - Grants generic all access to LocalService
//  (A;;GA;;;BA) - Grants generic all access to Built-in Admins
//  (A;;GA;;;IU) - Grants generic all access to Interactive User 
//
#define MY_EVENT_DACL TEXT("D:(A;;GA;;;LS)(A;;GA;;;BA)(A;;GA;;;IU)")

//
//  Allocate appropriate security attributes for the named event
//  to be shared between driver and app running under 
//  interactive user's account.
//
SECURITY_ATTRIBUTES sa = { sizeof(sa), FALSE, NULL };
if(ConvertStringSecurityDescriptorToSecurityDescriptor(
              MY_EVENT_DACL,
              SDDL_REVISION_1, 
              &(sa.lpSecurityDescriptor), NULL))
{
  h_MyEvent = CreateEvent(&sa,           // Our security descriptor 
                                         //  allowing access to 
                                         //  Admins, LocalService
                                         //  and the Interactive
                                         //  User
                          bManualReset,
                          bInitialState, 
                          tszName);
  if (h_MyEvent != NULL)
  {
      //  Success!
  }
  else
  {
      // Failed.  Do error cleanup...
      .
      .
      .
  }
}
else
{
  // Failed.  Do error cleanup...
  .
  .
  .
}
```

Registry keys can also be created with the appropriate ACLs through an INF file. For example, to create a registry key in the SOFTWARE key that is accessible only to Administrators and the driver running under **LocalService**, add the following entries to your INF file:

```INF
[DDInstallSection]
Addreg=MyAddReg

[DDInstallSection.MyAddReg]
HKLM,"SOFTWARE\MyCompany\MySpecialKey\"

[DDInstallSection.MyAddReg.Security]
"D:(A;CIOI;GA;;;BA)(A;CIOI;GA;;;LS)"
```

For more information about INF files, see [INF Files for WIA Devices](inf-files-for-wia-devices.md).

See the Windows Security documentation for more information about the Windows Security model. Driver writers should also be aware of general security best practices that reduce the chance of destructive users successfully exploiting vulnerabilities in their drivers. "*Writing Secure Code*" (ISBN 0-7356-1588-8) from Microsoft Press is one of the several helpful resources available.

 

 




