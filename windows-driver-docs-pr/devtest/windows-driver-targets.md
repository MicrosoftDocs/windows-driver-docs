---
title: Windows driver targets
description: The WindowsDriver.Common.targets, WindowsDriver.masm.targets, and WindowsDriver.arm.targets files provide the targets that are necessary to build a driver.
ms.date: 04/20/2017
---

# Windows driver targets


The WindowsDriver.Common.targets, WindowsDriver.masm.targets, and WindowsDriver.arm.targets files provide the targets that are necessary to build a driver.

WindowsDriver.masm.targets and WindowsDriver.arm.targets define targets specifically for building assembly files.

These targets extend the Cpp targets without directly modifying them. MSBuild provides a mechanism that is independent of the structure of the original project for you to insert the behaviors while retaining the original mechanisms that are used to guarantee the ordering between the extensions.

 

 





