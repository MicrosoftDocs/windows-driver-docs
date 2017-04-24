---
title: Installing a Non-PnP Driver
author: windows-driver-content
description: Installing a Non-PnP Driver
ms.assetid: 99676d85-feb2-482c-a91b-cfc48be5904c
keywords:
- Kernel-Mode Driver Framework WDK , installing drivers
- framework-based drivers WDK KMDF , installing
- INF files WDK KMDF , non-PnP drivers
- non-PnP drivers WDK KMDF
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing a Non-PnP Driver


If your driver does not support a Plug and Play (PnP) device, your driver package must include an INF file that contains an INF *DDInstall***.CoInstallers** section and INF *DDInstall***.WDF** section that are described in [Using the KMDF Co-installer](installing-the-framework-s-co-installer.md).

In addition, you must provide an installer that loads your driver and the framework's co-installer. The co-installer provides [**WdfPreDeviceInstall**](https://msdn.microsoft.com/library/windows/hardware/ff548835), [**WdfPreDeviceInstallEx**](https://msdn.microsoft.com/library/windows/hardware/ff548839), [**WdfPostDeviceInstall**](https://msdn.microsoft.com/library/windows/hardware/ff548829), [**WdfPreDeviceRemove**](https://msdn.microsoft.com/library/windows/hardware/ff548840), and [**WdfPostDeviceRemove**](https://msdn.microsoft.com/library/windows/hardware/ff548833) functions that the driver's installer must call.

For an example of how to write an installer for a non-PnP driver, see the installer that is included with the [NONPNP](sample-kmdf-drivers.md) sample.

 

 





