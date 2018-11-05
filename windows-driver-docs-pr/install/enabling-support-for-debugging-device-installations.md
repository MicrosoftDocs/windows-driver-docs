---
title: Enabling Support for Debugging Device Installations
description: Enabling Support for Debugging Device Installations
ms.assetid: cc47b4c9-fd1d-47c2-9af9-0b7f4a7a918a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling Support for Debugging Device Installations


Starting with Windows Vista, when the Plug and Play (PnP) manager detects a new device in the system, the operating system starts the device installation host process (*DrvInst.exe*) to search for and install a driver for the device.

To set the type of support the operating system provides for debugging the device installation host process, create (or modify) the following [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) registry value on the target system to be debugged:

**HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Device Installer\\DebugInstall**

The following table describes the types of debugging support that is specified by using the **DebugInstall** registry value.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">DebugInstall value</th>
<th align="left">Debugging support</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>The device installation process will be debugged by using a user-mode debugger. For more information, see <a href="debugging-device-installations-with-a-user-mode-debugger.md" data-raw-source="[Debugging Device Installations with a User-mode Debugger](debugging-device-installations-with-a-user-mode-debugger.md)">Debugging Device Installations with a User-mode Debugger</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>The device installation process will be debugged by using the kernel debugger (KD). For more information, see <a href="debugging-device-installations-with-the-kernel-debugger--kd-.md" data-raw-source="[Debugging Device Installations with the Kernel Debugger (KD)](debugging-device-installations-with-the-kernel-debugger--kd-.md)">Debugging Device Installations with the Kernel Debugger (KD)</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>No debugging of the device installation process. This is the default support if <strong>DebugInstall</strong> is not present in the registry</p></td>
</tr>
</tbody>
</table>

 

After the **DebugInstall** registry value is set you do not need to reboot the target system that you want to debug. However, **DebugInstall** registry value must be set before the start of the next device installation and remains in effect for each subsequent device installation until the value is set to zero.

**Note**  Be sure to reset the **DebugInstall** registry value to zero (or delete the value) as soon as it is no longer necessary to debug a device installation on the target system.

 

 

 





