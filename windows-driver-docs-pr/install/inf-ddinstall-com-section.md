---
title: INF DDInstall.COM Section
description: The DDInstall.COM section contains one or more INF AddComServer directives that reference additional INF-writer-defined sections in an INF file.
ms.date: 06/02/2023
---

# INF DDInstall.COM Section

Each per-Models DDInstall.COM section contains one or more [INF AddComServer directives](inf-addcomserver-directive.md) that reference additional INF-writer-defined sections in an INF file. This section is supported for Windows 11 version \<TBD\> and later.

```inf
[install-section-name.COM] |
[install-section-name.nt.COM] |
[install-section-name.ntarm.COM] |
[install-section-name.ntarm64.COM] |
[install-section-name.ntamd64.COM]

AddComServer = [com-server-name], [flags], com-server-install-section
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...] 
```

At least one *AddComServer* directive is required to register COM servers.

## Entries

**AddComServer**=*com-server-name,flags,com-server-install-section*

This directive references an INF-writer-defined com-server-install-section elsewhere in the INF file. This can be used one or more times to register multiple COM servers. For more information see, [INF AddComServer directive](inf-addcomserver-directive.md) and for COM servers in general, see [COM Clients and Servers](/windows/win32/com/com-clients-and-servers)

**Include**=*filename.inf[,filename2.inf]*

This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device. If this entry is specified, a **Needs** entry is also usually required.

**Needs**=*inf-section-name[,inf-section-name]*

This optional entry specifies the section that must be processed during the installation of this device. Typically, the section is a DDInstall.COM section within a system-supplied INF file that is listed in an Include entry. However, it can be any section that is referenced within a DDInstall.COM section.

## Remarks

COM binaries are installed into place using the *[CopyFiles](inf-copyfiles-directive.md)* directive in the DDInstall section. Binaries should be installed into a location relative to the driver package's [driver store path](../develop/run-from-driver-store.md) (for example, DIRID 13). Likewise, device installation writes COM registrations under device relative registry locations.

Clients must call **[CoRegisterDeviceCatalog](/windows/win32/api/combaseapi/nf-combaseapi-coregisterdevicecatalog)** on a worker thread before calling **[CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance)**. This makes the COM server registrations available in the process for the COM runtime to use.

DDInstall.COM section should have the same platform and operating system decorations as their related DDInstall sections. For example, an install-section-name.ntamd64 section would have a corresponding install-section-name.ntamd64.COM section. The specified DDInstall section must be referenced in a device/models-specific entry under the per-manufacturer Models section of the INF file. The case-insensitive extensions to the install-section-name shown in the formal syntax statement can be inserted into such a DDInstall.COM section name in cross-platform INF files.

For more information about how to use the system-defined .nt, .ntia64, .ntamd64, .ntarm, and .ntarm64 extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## Examples

```inf
[Device_Install.COM]
AddComServer   = VendorComServer,, VendorComServer_Inst

[VendorComServer_Inst]
ServerType     = 1 ; in-proc
ServerBinary   = %13%\Vendor_ComServer.dll
Description    = %Vendor_ComServer_Desc%
AddComClass    = VendorComClass, {bb2b85ab-9473-42e5-8d1a-0f01d3879879},, Vendor_ComClass_Inst

[Vendor_ComClass_Inst]
ThreadingModel = Neutral

[Strings]
%Vendor_ComServer_Desc%="Vendor Com Server"
```

## See also

- [Using a Component INF File](using-a-component-inf-file.md)
- [INF AddComServer directive](inf-addcomserver-directive.md)
