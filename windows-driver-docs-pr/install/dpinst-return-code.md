---
title: DPInst Return Code
description: DPInst Return Code
ms.date: 11/29/2022
---

# DPInst Return Code

> [!IMPORTANT]
> Starting in Windows 10 Version 1607 (Redstone 1), the Driver Install Frameworks (DIFx) tools, including DPInst.exe, are deprecated and are no longer included in the WDK. For recommendations on alternatives, see [DIFx Guidelines](./difx-guidelines.md). This page is provided for reference purposes only, and is not updated.

When DPInst finishes an installation, the DPInst executable file returns a return code to the application that called it. You can use this return code to determine the status of the driver installation when you run DPInst at a command prompt or call it from a higher-level installation application.

The return code is a DWORD (0xWWXXYYZZ), where the meaning of the four single-byte fields 0xWW, 0xXX, 0xYY, and 0xZZ are defined in the following table.

|Field|Meaning|
|-|-|
|0xWW| If a driver package could not be installed, the 0x80 bit is set. If a computer restart is necessary, the 0x40 bit is set. Otherwise, no bits are set.|
|0xXX| The number of driver packages that could not be installed.|
|0xYY| The number of driver packages that were copied to the DIFx driver store but were not installed on a device.|
|0xZZ| The number of driver packages that were installed on a device.|

The following table lists some example return codes and their meanings.

|Example return code|Meaning|
|-|-|
|0x00000001|One driver package was present and was successfully installed.|
|0x00000002|Two driver packages were present and were successfully installed.|
|0x40000002|Two driver packages were present and were successfully installed on devices. A computer restart is required to complete the installation.|
|0x00000100|One driver package was present and was copied to the DIFx driver store, but it was not installed on a device.|
|0x80010000|One driver package was present, but it could not be installed.|
|0xC0010001|One driver package could not be installed and one driver package was installed. A computer restart is required to complete the installation.|
