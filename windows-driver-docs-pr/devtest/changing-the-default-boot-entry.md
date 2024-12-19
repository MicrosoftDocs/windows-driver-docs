---
title: Changing the Default Boot Entry
description: Changing the Default Boot Entry
keywords:
- default boot entries
- Boot.ini files WDK , default boot entries
- boot options WDK , default boot entries
- identifying boot entry
- current boot entry WDK
- NVRAM boot options WDK , default boot entries
- EFI NVRAM boot options WDK , default boot entries
ms.date: 12/12/2024
---

# Changing the Default Boot Entry

The default boot entry is the entry that the boot loader selects when the boot menu time-out expires. You can change the default boot entry to ensure that the operating system configuration that you prefer is loaded automatically.

For Windows, you can use BCDEdit to change the default boot entry.

> [!CAUTION]
> Administrative privileges are required to use BCDEdit to modify BCD. Changing some boot entry options using the **BCDEdit /set** command could render your computer inoperable. As an alternative, use the System Configuration utility (MSConfig.exe) to change boot settings. For more information, see *[How to open MSConfig in Windows 10](https://support.microsoft.com/help/4026130/windows-how-to-open-msconfig-in-windows-10)*.

## Using BCDEdit

You can specify the default boot entry using the **/default** option. The syntax to specify the default operating system is as follows:

```
bcdedit /default <ID>
```

The *&lt;ID&gt;* is the GUID for the Windows boot loader boot entry that is associated with the operating system that you want to designate as the default. You must include the braces (**{ }**) around the GUID, for example:

```
bcdedit /default {cbd971bf-b7b8-4885-951a-fa03044f5d71}
```

To change the default boot entry to the earlier Windows operating system loader on a multiboot computer, set *&lt;ID&gt;* to **{ntldr}**, which is the reserved name for the GUID that is associated with Ntldr. This might present another menu depending on entries in Boot.ini file.

```
bcdedit /default {ntldr}
```

