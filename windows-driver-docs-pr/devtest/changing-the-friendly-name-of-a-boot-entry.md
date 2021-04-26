---
title: Changing the Friendly Name of a Boot Entry
description: Changing the Friendly Name of a Boot Entry
keywords:
- names WDK boot options
- friendly names WDK boot options
- renaming boot entries WDK
- Boot.ini files WDK , friendly names
- boot options WDK , friendly names
ms.date: 01/02/2019
ms.localizationpriority: medium
---

# Changing the Friendly Name of a Boot Entry


In Windows, the items that appear in the Windows Boot Manager are the descriptions of each boot entry.

Typically, after you copy a boot entry, you change the friendly name of the newly created entry to distinguish it from the original.

You can also change the friendly name to make it easier to recognize customized boot entries. A string that precisely describes the entry can save significant time and effort.

For example, the following friendly name strings add little value.

```
"Windows 10 Debug1"
"Windows 10 Debug2"
```

However, more precise strings, such as the ones that follow, make the boot choice much easier.

```
"Windows 10 kdnet"
"Windows 10 NullModem"
```

**Note**   When a boot entry is configured for debugging ([/debug /debugport](https://support.microsoft.com/help/833721/available-switch-options-for-the-windows-xp-and-the-windows-server-200)) or for Emergency Management Services (EMS) ([/redirect](https://support.microsoft.com/help/833721/available-switch-options-for-the-windows-xp-and-the-windows-server-200)) on an x86- or an x64-based system, the boot loader appends a bracketed phrase (\[debugger enabled\] or \[ems enabled\]) to the friendly name that appears in the boot menu.
However, the boot loader omits the bracketed phrase from the boot menu when the friendly name and the bracketed phrase together exceed 70 characters. To restore the bracketed phrase, shorten the friendly name.

To change the friendly name of a boot entry in a Boot.ini file, you can use Bootcfg or edit the Boot.ini file in Notepad. On systems that store boot options in EFI NVRAM, use Bootcfg.

To change the friendly name of a boot entry for Windows, use BCDEdit. 

> [!CAUTION]
> Administrative privileges are required to update the boot configuration. Changing some boot entry options could render your computer inoperable. 


## <span id="using_bcdedit"></span><span id="USING_BCDEDIT"></span>Using BCDEdit

To change the description of a boot entry as it appears on the boot menu, you can use the **/set** *IDdescription* option. The command uses the following syntax. The ID is the GUID that is associated with the boot entry (or one of the well-known identifiers, for example, {current}).

> [!NOTE]
> If you are using [Windows PowerShell](/powershell/scripting/overview), you must use quotes around the boot entry identifier, for example: **"{49916baf-0e08-11db-9af4-000bdbd316a0}"** or **"{current}"**.


```console
bcdedit /set ID description "The new description"
```

For example:

```console
bcdedit /set {802d5e32-0784-11da-bd33-000476eba25f} description "Windows 10 NullModem"
```

To change the description of the boot entry that corresponds to the operating system that is currently running, use the following example:

```console
bcdedit /set {current} description "Windows 10 NullModem"
```

You can also change the description when you copy an existing boot entry using the **/d** option.

```console
bcdedit /copy {current} /d "Windows 10 NullModem"
```



## <span id="using_bootcfg"></span><span id="USING_BOOTCFG"></span>Using Bootcfg

With Bootcfg, you can change the friendly name of a boot entry only while copying the entry. Use the Bootcfg **/copy** switch to copy the entry and change its friendly name.

The following Bootcfg command copies the first boot entry to create a new entry. The **/ID** switch specifies the line number of the entry being copied. The **/d** (description) switch specifies the friendly name of the newly-created entry.

```console
bootcfg /copy /ID 1 /d "Windows 10 Debug"
```

For complete instructions for using Bootcfg, see Help and Support Services. For examples, see [Using Boot Parameters](using-boot-parameters.md).

## <span id="editing_the_boot_ini_file"></span><span id="EDITING_THE_BOOT_INI_FILE"></span>Editing the Boot.ini File

In the Boot.ini file, the friendly name of a boot entry appears in the boot entry in quotation marks.

For example, the following sample from a Boot.ini file has duplicate boot entries for Microsoft Windows 10 Professional.

```console
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows 10 Professional" /fastdetect
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows 10 Professional" /fastdetect
```

To change the friendly name of a boot entry, type over the quoted string in the boot entry. In the following example, because the first entry will be customized for debugging, the name is changed to Windows 10 Debug.

```console
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Windows 10 Debug" /fastdetect
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows 10 Professional" /fastdetect
```
