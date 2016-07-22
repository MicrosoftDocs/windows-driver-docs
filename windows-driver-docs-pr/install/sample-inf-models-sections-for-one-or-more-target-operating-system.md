---
title: Sample INF Models Sections for One or More Target Operating Systems
description: Sample INF Models Sections for One or More Target Operating Systems
ms.assetid: bc1d9a5f-573f-4773-8716-8ac53478d0ee
---

# Sample INF Models Sections for One or More Target Operating Systems


This topic shows a sample INF file that installs a driver package on various operating systems and platforms. This INF file has the following INF sections and directives:

-   A decorated [**INF Manufacturer section**](inf-manufacturer-section.md) with various [**INF *Models* sections**](inf-models-section.md) for device installation on x86-based systems that are running:

    -   Microsoft Windows 2000

    -   Windows XP

    -   Windows Vista or later versions of Windows

-   A decorated [**INF Manufacturer section**](inf-manufacturer-section.md) with various [**INF *Models* sections**](inf-models-section.md) for device installation on x86- and AMD64-based systems that are running Windows Vista or later versions of Windows.

-   An [**INF *DDInstall***](inf-ddinstall-section.md) and [***DDInstall*.Services**](inf-ddinstall-services-section.md) that creates the service and registry entries on the target x86- and AMD64-based systems.

-   [**INF CopyFiles directives**](inf-copyfiles-directive.md) that copies platform-specific files to the target x86- and AMD64-based systems.

``` syntax
[Version]
Signature       = "$Windows NT$"
Class           = Net
ClassGUID       = {4d36e972-e325-11ce-bfc1-08002be10318}
Provider        = %Msft%
DriverVer       = 10/01/2002,6.0.5019.0

[Manufacturer]
%Msft%          = Msft, NTx86.6.0, NTamd64.6.0

; ----------------------------------------------------------------------
; Models Section
; ----------------------------------------------------------------------

;For Windows 2000 and Windows XP

[Msft]
%NetVMini.DeviceDesc%   = NetVMini.NTx86.ndi, root\NetVMini ; Root enumerated 
%NetVMini.DeviceDesc%   = NetVMini.NTx86.ndi, {b85b7c50-6a01-11d2-b841-00c04fad5171}\NetVMini ; Toaster Bus enumerated 

;For Windows Vista and later

[Msft.NTx86.6.0]
%NetVMini.DeviceDesc%    = NetVMini.NTx86.ndi, root\NetVMini ; Root enumerated 
%NetVMini.DeviceDesc%    = NetVMini.NTx86.ndi, {b85b7c50-6a01-11d2-b841-00c04fad5171}\NetVMini ; Toaster Bus enumerated 

[Msft.NTamd64.6.0]
%NetVMini.DeviceDesc%    = NetVMini.NTamd64.ndi, root\NetVMini ; Root enumerated 
%NetVMini.DeviceDesc%    = NetVMini.NTamd64.ndi, {b85b7c50-6a01-11d2-b841-00c04fad5171}\NetVMini ; Toaster Bus enumerated 

; ----------------------------------------------------------------------
; NT x86 DDInstall and DDInstall.Service Sections
; ----------------------------------------------------------------------
[NetVMini.NTx86.ndi]
Characteristics = 0x1 ; NCF_VIRTUAL
AddReg          = NetVMini.Reg
CopyFiles       = NetVMini.NTx86.CopyFiles

[NetVMini.NTx86.ndi.Services]
AddService      = NetVMini, 2, NetVMini.NTx86.Service

[NetVMini.NTx86.Service]
DisplayName     = %NetVMini.Service.DispName%
ServiceType     = 1 ;SERVICE_KERNEL_DRIVER
StartType       = 3 ;SERVICE_DEMAND_START
ErrorControl    = 1 ;SERVICE_ERROR_NORMAL
ServiceBinary   = %12%\netvmini_32.sys
LoadOrderGroup  = NDIS
AddReg          = TextModeFlags.Reg

; ----------------------------------------------------------------------
; NT x64 DDInstall and DDInstall.Service Sections
; ----------------------------------------------------------------------
[NetVMini.NTamd64.ndi]
Characteristics = 0x1 ; NCF_VIRTUAL
AddReg          = NetVMini.Reg
CopyFiles       = NetVMini.NTamd64.CopyFiles

[NetVMini.NTamd64.ndi.Services]
AddService      = NetVMini, 2, NetVMini.NTamd64.Service

[NetVMini.NTamd64.Service]
DisplayName     = %NetVMini.Service.DispName%
ServiceType     = 1 ;SERVICE_KERNEL_DRIVER
StartType       = 3 ;SERVICE_DEMAND_START
ErrorControl    = 1 ;SERVICE_ERROR_NORMAL
ServiceBinary   = %12%\netvmini_64.sys
LoadOrderGroup  = NDIS
AddReg          = TextModeFlags.Reg

; ----------------------------------------------------------------------
; Registry Section
; ----------------------------------------------------------------------
[NetVMini.Reg]
HKR,    ,               BusNumber,           0, "0" 
HKR, Ndi,               Service,             0, "NetVMini"
HKR, Ndi\Interfaces,    UpperRange,          0, "ndis5"
HKR, Ndi\Interfaces,    LowerRange,          0, "Ethernet"

[TextModeFlags.Reg]
HKR, , TextModeFlags,    0x00010001, 0x0001

; ----------------------------------------------------------------------
; Disk/FIle Sections
; ----------------------------------------------------------------------
[SourceDisksNames]
1 = %DiskId1%,"",,

[SourceDisksFiles]
netvmini_32.sys = 1,,
netvmini_64.sys = 1,,

[DestinationDirs]
DefaultDestDir             = 12
NetVMini.NTx86.CopyFiles   = 12
NetVMini.NTamd64.CopyFiles = 12

[NetVMini.NTx86.CopyFiles]
netvmini_32.sys,,,2

[NetVMini.NTamd64.CopyFiles]
netvmini_64.sys,,,2

; ----------------------------------------------------------------------
; Strings Section
; ----------------------------------------------------------------------
[Strings]
Msft                       = "Microsoft"      

NetVMini.DeviceDesc        = "Microsoft Virtual Ethernet Adapter"
NetVMini.Service.DispName  = "Microsoft Virtual Miniport"
DiskId1                    = "Microsoft Virtual Miniport Device Installation Disk #1"
```

The sample INF file (*MultiOS.inf*), which is included in the Windows Driver Kit (WDK), shows how a single INF file can be used to install a device on multiple versions of Windows. This file is in the *src\\print\\infs\\MultiOS* directory of the WDK.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Sample%20INF%20Models%20Sections%20for%20One%20or%20More%20Target%20Operating%20Systems%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




