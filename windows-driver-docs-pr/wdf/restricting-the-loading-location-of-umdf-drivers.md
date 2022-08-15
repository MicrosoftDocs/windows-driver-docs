---
title: Restricting the loading location of UMDF drivers
description: Provides information about restricting the loading location of UMDF drivers.
keywords:
- locations WDK UMDF
- binaries WDK UMDF
- directories WDK UMDF
- UMDriverCopy
- loading locations WDK UMDF
- INF files WDK UMDF , loading locations
ms.date: 05/12/2022
---

# Restricting the loading location of UMDF drivers

The UMDF platform will fail to load the main UMDF driver binaries from any location other than the %SystemRoot%\\System32\\Drivers\\Umdf directory or, in Windows 10 1803 and later, a [run from Driver Store](../develop/run-from-driver-store.md) location. Therefore, a UMDF INF file must restrict the location where it installs UMDF drivers to those directories. Installing in these directories also ensures that unprivileged users cannot tamper with the UMDF drivers.

To have a UMDF driver binary be a [run from Driver Store](../develop/run-from-driver-store.md) binary (Windows 10 1803 and later), the UMDF driver INF file must include an [**INF DestinationDirs Section**](../install/inf-destinationdirs-section.md) that is similar to the following code example.

```cpp
[DestinationDirs]
UMDriverCopy=13 ; makes the file 'run from Driver Store'
```

"UMDriverCopy" represents an INF-writer-determined name of a section that lists the UMDF driver binaries as shown in the following example.

```cpp
[UMDriverCopy]
WUDFOsrUsbDriver.dll
```

The [**CopyFiles directive**](../install/inf-copyfiles-directive.md) must also reference the **UMDriverCopy** section to indicate the list of UMDF driver binaries for the operating system to copy from the source media to the destination as shown in the following example.

```cpp
[OsrUsb_Install.NT]
CopyFiles=UMDriverCopy
```

To install UMDF driver binaries to %SystemRoot%\\System32\\Drivers\\Umdf instead of being 'run from Driver Store', the [**INF DestinationDirs Section**](../install/inf-destinationdirs-section.md) should instead look like the following code example.

```cpp
[DestinationDirs]
UMDriverCopy=12,UMDF ; copies to drivers\umdf
```
