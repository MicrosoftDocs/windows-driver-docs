---
title: LowerLogoVersion
description: LowerLogoVersion is a device setup class property that affects the signature score of a driver package.
keywords:
- LowerLogoVersion
ms.date: 04/12/2022
---

# LowerLogoVersion

**LowerLogoVersion** is a [device setup class property](accessing-device-setup-class-properties.md) that affects the signature score of a driver package as follows:

- Windows assigns the best signature score to driver packages that have a WHQL signature for a Windows version that is the same or later than the **LowerLogoVersion** value.

- Windows assigns the next best signature score to a driver package that was signed by a third-party using Authenticode technology and to a driver package that has a WHQL signature for a Windows version earlier than the **LowerLogoVersion** value.

A **LowerLogoVersion** value is a NULL-terminated string that specifies the Windows version, as indicated in the following table.

| Windows version | LowerLogoVersion value |
|--|--|
| Windows 7 | 6.1 |
| Windows Server 2008 | 6.1 |
| Windows Vista | 6.0 |
| Windows Server 2003 | 5.2 |
| Windows XP | 5.1 |
| Windows 2000 | 5.0 |

The system default **LowerLogoVersion** value for a system-defined [device setup class](./overview-of-device-setup-classes.md) is "5.1." This means that drivers that have a WHQL signature for Windows Server 2003 and Windows XP have the same signature score as a driver that is signed by Microsoft for Windows Vista and later versions of Windows.

For more information about driver package ranking, see [How Windows ranks driver packages](how-setup-ranks-drivers--windows-vista-and-later-.md).
