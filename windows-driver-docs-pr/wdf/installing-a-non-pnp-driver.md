---
title: Installing a Non-PnP Driver
description: Installing a Non-PnP Driver
keywords:
- Kernel-Mode Driver Framework WDK , installing drivers
- framework-based drivers WDK KMDF , installing
- INF files WDK KMDF , non-PnP drivers
- non-PnP drivers WDK KMDF
ms.date: 03/12/2020
---

# Installing a Non-PnP Driver


If your KMDF driver supports a non-Plug and Play (PnP) device on Windows 10, use the same approach as that shown in the [Non-PnP Driver Sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/ioctl/kmdf), but remove references to INF files and co-installers. For example, you do not need the following:

```
#define NONPNP_INF_FILENAME  L"\\nonpnp.inf"
#define WDF_SECTION_NAME L"nonpnp.NT.Wdf"
 
LoadWdfCoInstaller
UnloadWdfCoInstaller
 
PFN_WDFPREDEVICEINSTALLEX pfnWdfPreDeviceInstallEx;
PFN_WDFPOSTDEVICEINSTALL   pfnWdfPostDeviceInstall;
PFN_WDFPREDEVICEREMOVE     pfnWdfPreDeviceRemove;
PFN_WDFPOSTDEVICEREMOVE   pfnWdfPostDeviceRemove;
```

For a non-PnP KMDF driver, simply call the SCM API to create the service. For more info, see [Installing a Service](/windows/win32/services/installing-a-service).
