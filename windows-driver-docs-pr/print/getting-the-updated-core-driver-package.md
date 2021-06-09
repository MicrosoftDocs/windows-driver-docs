---
title: Getting the Updated Core Driver Package
description: Getting the Updated Core Driver Package
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Getting the Updated Core Driver Package

After you [obtain](constructing-a-package-aware-driver-with-updated-core-drivers.md) the Microsoft standalone update (MSU) file containing the updated core driver package, the next step is to expand the contents of the MSU file.

To make the contents of the core driver package accessible to the PnP installer, open a Command Prompt window and use the expand command to expand the MSU file. Also expand the appropriate cabinet (.cab) file, which has a name that starts with "Windows6.0-", that is contained in the MSU file.

The following example shows how to use the [**expand**](/previous-versions/windows/it-pro/windows-xp/bb490903(v=technet.10)) command, which should be executed in the directory that contains the MSU file:

```cpp
expand Windows6.0-KB123456-x86.MSU [dest directory] -F:*
expand Windows6.0-KB123456-x86.CAB [dest directory] -F:*
```

Following these two commands, the directory will contain a number of manifest files and subdirectories. One of these subdirectories will contain Ntprint.inf and the uncompressed driver components. This directory has a name that begins with the processor architecture for the fix (for example, x86), to which is appended "ntprint.inf", a GUID, and additional tracking information.
