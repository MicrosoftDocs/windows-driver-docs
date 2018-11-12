---
title: Forcing a System Crash from the Keyboard
description: Forcing a System Crash from the Keyboard
ms.assetid: 0c3ec6f3-d233-46e4-b599-1a0f89318ed2
keywords: ["boot process, causing system crash from keyboard", "CTRL+SCROLL LOCK", "system crash, causing from keyboard", "bug check, causing from keyboard", "keyboard-caused system crash", "USB keyboard and system crash", "PS/2 keyboard and system crash", "forcing system crash from keyboard"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Forcing a System Crash from the Keyboard


## <span id="ddk_forcing_a_system_crash_from_the_keyboard_dbg"></span><span id="DDK_FORCING_A_SYSTEM_CRASH_FROM_THE_KEYBOARD_DBG"></span>


Most of the following keyboards can cause a system crash directly:

<span id="________PS_2_keyboards_connected_on_i8042prt_ports_______"></span><span id="________ps_2_keyboards_connected_on_i8042prt_ports_______"></span><span id="________PS_2_KEYBOARDS_CONNECTED_ON_I8042PRT_PORTS_______"></span> PS/2 keyboards connected on i8042prt ports   
This feature is available in Windows 2000 and later versions of Windows operating system.

<span id="________USB_keyboards_______"></span><span id="________usb_keyboards_______"></span><span id="________USB_KEYBOARDS_______"></span> USB keyboards   
This feature is available in:

-   Windows Server 2003 Service Pack 1 if the hotfix available with [KB 244139](https://go.microsoft.com/fwlink/p/?linkid=106065) is installed.

-   Windows Server 2003 (with Service Pack 2 or later).

-   Windows Vista Service Pack 1 if the hotfix available with [KB 971284](https://go.microsoft.com/fwlink/p/?LinkId=241349) is installed.

-   Windows Vista Service Pack 2.

-   Windows Server 2008 Service Pack 1 if the hotfix available with [KB 971284](https://go.microsoft.com/fwlink/p/?LinkId=241349) is installed.
-   Windows Server 2008 (with Service Pack 2 or later).
-   Windows 7 and later versions of Windows operating system.

**Note**  This feature is not available in Windows XP.

 

You must ensure the following three settings before the keyboard can cause a system crash:

1.  If you wish a crash dump file to be written, you must enable such dump files, choose the path and file name, and select the size of the dump file. For more information, see [Enabling a Kernel-Mode Dump File](enabling-a-kernel-mode-dump-file.md).

2.  With PS/2 keyboards, you must enable the keyboard-initiated crash in the registry. In the registry key **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\i8042prt\\Parameters**, create a value named **CrashOnCtrlScroll**, and set it equal to a REG\_DWORD value of 0x01.

3.  With USB keyboards, you must enable the keyboard-initiated crash in the registry. In the registry key **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\kbdhid\\Parameters,** create a value named **CrashOnCtrlScroll**, and set it equal to a REG\_DWORD value of 0x01.

You must restart the system for these settings to take effect.

After this is completed, the keyboard crash can be initiated by using the following hotkey sequence: Hold down the rightmost CTRL key, and press the SCROLL LOCK key twice.

The system then calls **KeBugCheck** and issues [**bug check 0xE2**](bug-check-0xe2--manually-initiated-crash.md) (MANUALLY\_INITIATED\_CRASH). Unless crash dumps have been disabled, a crash dump file is written at this point.

If a kernel debugger is attached to the crashed machine, the machine will break into the kernel debugger after the crash dump file has been written.

For more information on using this feature, refer to the article [Generate a memory dump file by using the keyboard (KB 244139)](https://go.microsoft.com/fwlink/p/?linkid=106065).

### <span id="defining_alternate_keyboard_shortcuts_to_force_a_system_crash_from_the"></span><span id="DEFINING_ALTERNATE_KEYBOARD_SHORTCUTS_TO_FORCE_A_SYSTEM_CRASH_FROM_THE"></span>Defining Alternate Keyboard Shortcuts to Force a System Crash from the Keyboard

You can configure values under the following registry subkeys for different keyboard shortcut sequences to generate the memory dump file:

-   For PS/2 keyboards:

    **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\i8042prt\\crashdump**

-   For USB keyboards:

    **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\kbdhid\\crashdump**

You must create the following registry REG\_DWORD values under these subkeys:

<span id="Dump1Keys"></span><span id="dump1keys"></span><span id="DUMP1KEYS"></span>**Dump1Keys**  
The **Dump1Keys** registry value is a bit map of the first hot key to use. For example, instead of using the rightmost CTRL key to initiate the hot key sequence, you can set the first hot key to be the leftmost SHIFT key.

The values for the first hot key are described in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">First key used in the keyboard shortcut sequence</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x01</p></td>
<td align="left"><p>Rightmost SHIFT key</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x02</p></td>
<td align="left"><p>Rightmost CTRL key</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x04</p></td>
<td align="left"><p>Rightmost ALT key</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10</p></td>
<td align="left"><p>Leftmost SHIFT key</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x20</p></td>
<td align="left"><p>Leftmost CTRL key</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x40</p></td>
<td align="left"><p>Leftmost ALT key</p></td>
</tr>
</tbody>
</table>

 

**Note**  You can assign **Dump1Keys** a value that enables one or more keys as the first key used in the keyboard shortcut sequence. For example, assign **Dump1Keys** a value of 0x11 to define both the rightmost and leftmost SHIFT keys as the first key in the keyboard shortcut sequence.

 

<span id="Dump2Key"></span><span id="dump2key"></span><span id="DUMP2KEY"></span>**Dump2Key**  
The **Dump2Key** registry value is the index into the scancode table for the keyboard layout of the target computer. The following is the actual table in the driver.

```cpp
const UCHAR keyToScanTbl[134] = { 
        0x00,0x29,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,
        0x0A,0x0B,0x0C,0x0D,0x7D,0x0E,0x0F,0x10,0x11,0x12,
        0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1A,0x1B,0x00,
        0x3A,0x1E,0x1F,0x20,0x21,0x22,0x23,0x24,0x25,0x26,
        0x27,0x28,0x2B,0x1C,0x2A,0x00,0x2C,0x2D,0x2E,0x2F,
        0x30,0x31,0x32,0x33,0x34,0x35,0x73,0x36,0x1D,0x00,
        0x38,0x39,0xB8,0x00,0x9D,0x00,0x00,0x00,0x00,0x00,
        0x00,0x00,0x00,0x00,0x00,0xD2,0xD3,0x00,0x00,0xCB,
        0xC7,0xCF,0x00,0xC8,0xD0,0xC9,0xD1,0x00,0x00,0xCD,
        0x45,0x47,0x4B,0x4F,0x00,0xB5,0x48,0x4C,0x50,0x52,
        0x37,0x49,0x4D,0x51,0x53,0x4A,0x4E,0x00,0x9C,0x00,
        0x01,0x00,0x3B,0x3C,0x3D,0x3E,0x3F,0x40,0x41,0x42,
        0x43,0x44,0x57,0x58,0x00,0x46,0x00,0x00,0x00,0x00,
        0x00,0x7B,0x79,0x70 };
```

**Note**   Index 124 (sysreq) is a special case because an 84-key keyboard has a different scan code.

 

If you define alternate keyboard shortcuts to force a system crash from a USB or PS/2 keyboard, you must either set the **CrashOnCtrlScroll** registry value to 0 or remove it from the registry.

### <span id="limitations"></span><span id="LIMITATIONS"></span>Limitations

It is possible for a system to freeze in such a way that the keyboard shortcut sequence will not work. However, this should be a very rare occurrence. Using the keyboard shortcut sequence to initiate a crash will work even in many instances where CTRL+ALT+DELETE does not work.

Forcing a system crash from the keyboard does not work if the computer stops responding at a high interrupt request level (IRQL). This limitation exists because the Kbdhid.sys driver, which allows the memory dump process to run, operates at a lower IRQL than the i8042prt.sys driver.

 

 





