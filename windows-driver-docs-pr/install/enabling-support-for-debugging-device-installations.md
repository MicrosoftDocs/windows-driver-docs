---
title: Enabling Support for Debugging Device Installations
description: Enabling Support for Debugging Device Installations
ms.assetid: cc47b4c9-fd1d-47c2-9af9-0b7f4a7a918a
---

# Enabling Support for Debugging Device Installations


Starting with Windows Vista, when the Plug and Play (PnP) manager detects a new device in the system, the operating system starts the device installation host process (*DrvInst.exe*) to search for and install a driver for the device.

To set the type of support the operating system provides for debugging the device installation host process, create (or modify) the following REG\_DWORD registry value on the target system to be debugged:

**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Device Installer\\DebugInstall**

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
<td align="left"><p>The device installation process will be debugged by using a user-mode debugger. For more information, see [Debugging Device Installations with a User-mode Debugger](debugging-device-installations-with-a-user-mode-debugger.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>The device installation process will be debugged by using the kernel debugger (KD). For more information, see [Debugging Device Installations with the Kernel Debugger (KD)](debugging-device-installations-with-the-kernel-debugger--kd-.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>No debugging of the device installation process. This is the default support if <strong>DebugInstall</strong> is not present in the registry</p></td>
</tr>
</tbody>
</table>

 

After the **DebugInstall** registry value is set you do not need to reboot the target system that you want to debug. However, **DebugInstall** registry value must be set before the start of the next device installation and remains in effect for each subsequent device installation until the value is set to zero.

**Note**  Be sure to reset the **DebugInstall** registry value to zero (or delete the value) as soon as it is no longer necessary to debug a device installation on the target system.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Enabling%20Support%20for%20Debugging%20Device%20Installations%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




