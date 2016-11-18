---
title: WIA Security and Security Descriptors
author: windows-driver-content
description: WIA Security and Security Descriptors
MS-HAID:
- 'WIA\_best\_practice\_28714e9d-052f-4dc3-8e3c-cb32460535c1.xml'
- 'image.wia\_security\_and\_security\_descriptors'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2919f3fc-1eb5-4801-a589-ae3000320763
---

# WIA Security and Security Descriptors


## <a href="" id="ddk-wia-security-and-security-descriptors-si"></a>


Many of the solutions to the problems listed in [Common WIA Security Problems](common-wia-security-problems.md) require the objects in question to have security descriptors that grant access to the appropriate entities, such as **LocalService** accounts.

Generally, the **LocalService** account has access to resources whose ACLs allow access by a **LocalService** account, Everyone, or Authenticated users. The service cannot share objects (pipes, file mapping, synchronization, and so on) with other applications, unless it creates a discretionary access control list(DACL) that allows a user or group of users access to the object.

The following code example illustrates how to set the security descriptor. This approach can be used if an application and driver need to share a named event object.

```
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
//  interactive user&#39;s account.
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

```
[DDInstallSection]
Addreg=MyAddReg

[DDInstallSection.MyAddReg]
HKLM,"SOFTWARE\MyCompany\MySpecialKey\"

[DDInstallSection.MyAddReg.Security]
"D:(A;CIOI;GA;;;BA)(A;CIOI;GA;;;LS)"
```

For more information about INF files, see [INF Files for WIA Devices](inf-files-for-wia-devices.md).

See the Windows Security documentation on MSDN For more information about the Windows Security model. Driver writers should also be aware of general security best practices that reduce the chance of destructive users successfully exploiting vulnerabilities in their drivers. "*Writing Secure Code*" (ISBN 0-7356-1588-8) from Microsoft Press is one of the several helpful resources available.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Security%20and%20Security%20Descriptors%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


