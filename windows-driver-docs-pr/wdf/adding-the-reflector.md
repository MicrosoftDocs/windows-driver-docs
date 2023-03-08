---
title: Specifying the Reflector in an INF File
description: Specifying the Reflector in an INF File
keywords:
- reflectors WDK UMDF
- AddService
- INF files WDK UMDF , reflectors
- function drivers WDK UMDF
- filter drivers WDK UMDF
- loading reflectors WDK UMDF
ms.date: 03/07/2023
---

# Specifying the Reflector in an INF File

Starting in Windows 11, the recommended way to add the reflector (WUDFRd.sys) to the kernel-mode device stack is to reference the system-supplied WudfRd.inf file in the INF file of a UMDF driver.

> [!NOTE]
> WudfRd.inf is included only with Windows 11 and later. It is located in the `\windows\inf` folder.

On Windows 10 and earlier, to add the reflector (WUDFRd.sys), the INF file of a UMDF driver must include an [**AddService directive**](../install/inf-addservice-directive.md) in an [**INF DDInstall.Services section**](../install/inf-ddinstall-services-section.md) as well as a service-install-section. While this method still works on Windows 11 and later, it is not recommended.

In both methods, the reflector can be an upper filter, a lower filter, or the service for the device, depending on the configuration of the user-mode stack.

## Referencing WudfRd.inf (Windows 11 and later)

You can find a sample INF that uses this technique at [echoum.inx](https://github.com/microsoft/Windows-driver-samples/blob/develop/general/echo/umdf2/driver/AutoSync/echoum.inx).  Alternatively, use one of the following snippets.

To install the WudfRd service as the function driver for the device:

```inf
[DDInstall]
Include=WUDFRD.inf
Needs=WUDFRD.NT
; also include any existing DDInstall directives

[DDInstall.HW]
Include=WUDFRD.inf
Needs=WUDFRD.NT.HW
; also include any existing DDInstall.HW directives

[DDInstall.Services]
Include=WUDFRD.inf
Needs=WUDFRD.NT.Services
; also include any existing any DDInstall.Services directives
```

To install the WudfRd service as an upper filter driver:

```inf
[DDInstall] 
Include=WUDFRD.inf
Needs=WUDFRD_UpperFilter.NT
; also include any existing DDInstall directives

[DDInstall.HW]
Include=WUDFRD.inf
Needs=WUDFRD_UpperFilter.NT.HW
; also include any existing DDInstall.HW directives

[DDInstall.Services]
Include=WUDFRD.inf
Needs=WUDFRD_UpperFilter.NT.Services
; also include any existing any DDInstall.Services directives

[DDInstall.Filters]
Include=WUDFRD.inf
Needs=WUDFRD_UpperFilter.NT.Filters
```

To install the WudfRd service as a lower filter driver:

```inf
[DDInstall] 
Include=WUDFRD.inf
Needs=WUDFRD_LowerFilter.NT
; also include any existing DDInstall directives

[DDInstall.HW]
Include=WUDFRD.inf
Needs=WUDFRD_LowerFilter.NT.HW
; also include any existing DDInstall.HW directives

[DDInstall.Services]
Include=WUDFRD.inf
Needs=WUDFRD_LowerFilter.NT.Services
; also include any existing any DDInstall.Services directives

[DDInstall.Filters]
Include=WUDFRD.inf
Needs=WUDFRD_LowerFilter.NT.Filters
```

## Using an AddService directive (Windows 10 and earlier)

The following code example shows how the INF file for a UMDF function driver might add the reflector.

```inf
[Skeleton_Install.Services]
AddService=WUDFRd,0x000001fa,WUDFRD_ServiceInstall
```

In this example, the driver specifies the 0x2 (SPSVCINST\_ASSOCSERVICE) flag (ORed into the *flags* parameter above) to assign the reflector as the function driver in the kernel-mode device stack.

The **AddService** directive also sets the 0x000001f8 flags to prevent overwriting any preexisting configuration for the service. For more information about these flags, see the *flags* parameter of the [**AddService directive**](../install/inf-addservice-directive.md).

The following code example, taken from the WUDFVhidmini sample, shows an **AddService** directive for a UMDF filter driver.

```inf
[hidumdf.win8.NT.Services]
AddService=WUDFRd,0x000001f8,WUDFRD_ServiceInstall  
AddService=mshidumdf, 0x000001fa, mshidumdf.AddService

[WudfVhidmini_AddReg]
HKR,,"LowerFilters",0x00010008,"WUDFRd" ; FLG_ADDREG_TYPE_MULTI_SZ | FLG_ADDREG_APPEND
```

In this case, the mshidumdf service is associated with the FDO for the device stack, and the reflector is a lower filter.

### Providing a service-install-section


The **AddService** directive references an service-install-section similar to the following code example. The **ServiceType** entry specifies 1 or 0x00000001, which indicates that the INF installs support for one or more devices. The **StartType** entry specifies when to start the driver. The **ErrorControl** entry specifies the level of error control that the driver provides. The **ServiceBinary** entry specifies the path to the binary (the reflector) for the service.

```inf
[WUDFRD_ServiceInstall]
DisplayName = "Windows Driver Frameworks - User-mode Driver Framework Reflector"
ServiceType=1
StartType=3
ErrorControl=1
ServiceBinary=%12%\WUDFRd.sys
```
