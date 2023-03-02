---
title: INF DDInstall.MigrateToDevNode section
description: INF DDInstall.MigrateToDevNode section
keywords:
- INF files WDK non-HID keyboard/mouse
- DDInstall.MigrateToDevNode section
ms.date: 03/02/2023
ms.topic: reference
---

# INF DDInstall.MigrateToDevNode section

\[***install-section-name***.MigrateToDevNode\]

\[***install-section-name***.nt.MigrateToDevNode\]

\[***install-section-name***.ntx86.MigrateToDevNode\]

\[***install-section-name***.ntia64.MigrateToDevNode\]

*ServiceName* **=** *value-name* \[**,** *value-name*\],...

The keyboard and mouse class installers copy the entry values specified by the list of *value-name* strings from the registry key **HKLM\\System\\CurrentControlSet\\Services\\***ServiceName***\\Parameters** to the device node of the device being installed.

## Entries and Values

- *ServiceName*: Specifies the service name associated with a device port (for example, **i8042prt**, **sermouse**, and so on).
- *value-name*: Specifies an entry value under the registry key **HKLM\\System\\CurrentControlSet\\Services\\***ServiceName***\\Parameters**.

## Remarks

Microsoft supports INF *DDinstall*.**MigratetoDevNode** sections primarily to facilitate porting Windows NT 4.0 legacy devices to Windows 2000 and later.

The keyboard and mouse class installers copy all the *value-name* entry values before the system starts the device stack. The specified entry values can be any valid registry entry values. The *value-name* entry values are not deleted from the **...\\***ServiceName_**\\Parameters** registry key.
