---
title: Idle Power Management Configuration and Usage
description: Idle Power Management Configuration and Usage
ms.date: 06/27/2024
ms.topic: how-to
---

# Idle Power Management Configuration and Usage

Storport Idle Power Management (IPM) isn't enabled by default. It can be enabled in the registry by setting the "EnableIdlePowerManagement" value in the "StorPort" subkey of the device's hardware key to any nonzero value. To do so, use the device INF file or manually edit the registry using the registry editor.

The following sample text shows what you need to add to your device's INF file to enable the Storport IPM feature.

``` inf
[DDInstall.HW]
; Enables Storport IPM for this adapter
HKR, "StorPort", "EnableIdlePowerManagement", 0x00010001, 0x01
```

Add this text only within the INF file's DDInstall.HW section where HKR points to the hardware key and not the service key. For more information about how to change an INF file, see [Introduction to Registry Keys for Drivers](https://go.microsoft.com/fwlink/p/?linkid=144533).

A command line tool (*Powercfg.exe*) can also be used. Type **powercfg /?** for usage information at the command prompt.
