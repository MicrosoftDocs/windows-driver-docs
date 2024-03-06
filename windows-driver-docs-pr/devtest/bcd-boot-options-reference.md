---
title: BCDEdit Options Reference
description: BCDEdit Options Reference
ms.date: 09/25/2020
---

# BCDEdit Options Reference

*Boot entry parameters*, or *boot parameters*, are optional, system-specific settings that represent configuration options. You can add boot parameters to a boot entry for an operating system. They are stored in a boot configuration data (BCD) store.

This section describes the boot options for supported versions of Windows that are related to developing, testing, and debugging drivers on computers with x86-based and x64-based processors. You can add these parameters to the boot entries for Windows operating systems.

> [!CAUTION]
> Administrative privileges are required to use BCDEdit to modify BCD. Changing some boot entry options using the **BCDEdit /set** command could render your computer inoperable. As an alternative, use the System Configuration utility (MSConfig.exe) to change boot settings. For more information, see *[How to open MSConfig in Windows 10](https://support.microsoft.com/help/4026130/windows-how-to-open-msconfig-in-windows-10)*.

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

## In this section

|Topic|Description|
|--- |--- |
|[BCDEdit /bootdebug](bcdedit--bootdebug.md)|The /bootdebug boot option enables or disables boot debugging of the current or specified Windows operating system boot entry.|
|[BCDEdit /bootsequence](bcdedit--bootsequence.md)|Sets the one-time boot sequence for the boot manager. |
|[BCDEdit /dbgsettings](bcdedit--dbgsettings.md)|The /dbgsettings option sets or displays the current global debugger settings for the computer. To enable or disable the kernel debugger, use the BCDEdit /debug option.|
|[BCDEdit /debug](bcdedit--debug.md)|The /debug boot option enables or disables kernel debugging of the Windows operating system associated with the specified boot entry or the current boot entry.|
|[BCDEdit /default](bcdedit--default.md)| Sets the default entry that the boot manager will use.|
|[BCDEdit /deletevalue](bcdedit--deletevalue.md)|The /deletevalue option deletes or removes a boot entry option (and its value) from the Windows boot configuration data store (BCD). Use the BCDEdit /deletevalue command to remove options that were added using BCDEdit /set command. You might need to remove boot entry options when you are testing and debugging your driver.|
|[BCDEdit /displayorder](bcdedit--displayorder.md)|Sets the order in which the boot manager displays the multiboot menu.|
|[BCDEdit /ems](bcdedit--ems.md)|The /ems option enables or disables Emergency Management Services (EMS) for the specified operating system boot entry.|
|[BCDEdit /emssettings](bcdedit--emssettings.md)|The /emssettings option sets the global Emergency Management Services (EMS) settings for the computer. To enable or disable EMS, use the /ems option. The /emssettings option does not enable or disable EMS for any boot entry.|
|[BCDEdit /enum](bcdedit--enum.md)|The /enum command lists entries in boot configuration data (BCD) store. |
|[BCDEdit /event](bcdedit--event.md)|The /event command enables or disables the remote event logging for the specified boot entry. |
|[BCDEdit /hypervisorsettings](bcdedit--hypervisorsettings.md)|The /hypervisorsettings option sets or displays the hypervisor debugger settings for the system. |
|[BCDEdit /set](bcdedit--set.md)|The BCDEdit /set command sets a boot entry option value in the Windows boot configuration data store (BCD). Use the BCDEdit /set command to configure specific boot entry elements, such as kernel debugger settings, memory options, or options that enable test-signed kernel-mode code or load alternate hardware abstraction layer (HAL) and kernel files. To remove a boot entry option, use the BCDEdit /deletevalue command.|
|[BCDEdit /timeout](bcdedit--timeout.md)|Sets the boot manager time-out value. |
|[BCDEdit /tooldisplayorder](bcdedit--toolsdisplayorder.md)|Sets the order in which the boot manager displays the tools menu. |

## See also

[Adding Boot Entries](./adding-boot-entries.md)
