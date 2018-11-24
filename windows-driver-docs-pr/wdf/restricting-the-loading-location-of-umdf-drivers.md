---
title: Restricting the Loading Location of UMDF Drivers
description: Restricting the Loading Location of UMDF Drivers
ms.assetid: eac19fa8-2889-4cc3-9f4b-d11d7d3ed684
keywords:
- locations WDK UMDF
- binaries WDK UMDF
- directories WDK UMDF
- UMDriverCopy
- loading locations WDK UMDF
- INF files WDK UMDF , loading locations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Restricting the Loading Location of UMDF Drivers


The UMDF platform will fail to load the main UMDF driver binaries from any location other than the %SystemRoot%\\System32\\Drivers\\Umdf directory. Therefore, a UMDF INF file must restrict the location where it installs UMDF drivers to that directory. Installing in this directory also ensures that unprivileged users cannot tamper with the UMDF drivers.

To install UMDF driver binaries to %SystemRoot%\\System32\\Drivers\\Umdf, the UMDF driver INF file must include an [**INF DestinationDirs Section**](https://msdn.microsoft.com/library/windows/hardware/ff547383) that is similar to the following code example.

```cpp
[DestinationDirs]
UMDriverCopy=12,UMDF ; copies to drivers\umdf
```

"UMDriverCopy" represents an INF-writer-determined name of a section that lists the UMDF driver binaries as shown in the following example.

```cpp
[UMDriverCopy]
WUDFOsrUsbDriver.dll
```

The [**CopyFiles directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) must also reference the **UMDriverCopy** section to indicate the list of UMDF driver binaries for the operating system to copy from the source media to the destination as shown in the following example.

```cpp
[OsrUsb_Install.NT]
CopyFiles=UMDriverCopy
```

 

 





