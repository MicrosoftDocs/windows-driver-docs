---
title: Boot Parameters to Enable EMS Redirection
description: Boot Parameters to Enable EMS Redirection
ms.assetid: b93fd580-0e1d-4b1e-8358-1c6ce7e2eb5e
keywords:
- boot parameters WDK
- boot entry parameters WDK
- Emergency Management Services WDK boot parameters
- EMS redirection WDK boot parameters
- remote administration WDK boot parameters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Boot Parameters to Enable EMS Redirection


## <span id="ddk_boot_parameters_to_enable_ems_redirection_tools"></span><span id="DDK_BOOT_PARAMETERS_TO_ENABLE_EMS_REDIRECTION_TOOLS"></span>


Emergency Management Services (EMS) technology allows you to control the selected components of servers remotely, even when a server is not connected to the network or to other standard remote-administration tools. EMS is supported on all versions of Windows Server 2003 operating systems for x86-, x64-, and Itanium-based computers.

For more information about EMS, search for Emergency Management Services on the [Microsoft TechNet](http://go.microsoft.com/fwlink/p/?linkid=10111) website.

**Note**   This topic explains how to enable EMS on computers running Windows Server 2003. The boot parameters described in this section are not supported on Windows Vista or later versions of Windows.
When a boot entry is configured for EMS on a computer with BIOS firmware, the boot loader appends a bracketed phrase, \[ems enabled\], to the friendly name that appears on the boot menu. However, the boot loader omits the bracketed phrase from the boot menu when the friendly name and the bracketed phrase together exceed 70 characters. To restore the bracketed phrase, shorten the friendly name.

To determine whether a computer has ACPI firmware, use Device Manager (devmgmt.msc). In Device Manager, expand the **Computer** node. On computers with ACPI firmware, the name of node under **Computer** includes the word, **ACPI**.

 

### <span id="enabling_ems_on_a_computer_without_an_acpi_spcr_table_in_operating_sys"></span><span id="ENABLING_EMS_ON_A_COMPUTER_WITHOUT_AN_ACPI_SPCR_TABLE_IN_OPERATING_SYS"></span>Enabling EMS on a computer without an ACPI SPCR table in operating systems prior to Windows Server 2008

To enable EMS console redirection on a computer that has BIOS firmware, but does not have an ACPI Serial Port Console Redirection (SPCR) table, add the **redirect=COM***x* and the **redirectbaudrate=** parameters to the \[boot loader\] section of the Boot.ini file. These parameters set the port and transmission rate for EMS console redirection. Use the same port and transmission rate that are established for out-of-band communication in the BIOS. Then, add the [**/redirect**](https://msdn.microsoft.com/library/windows/hardware/ff557180) parameter to a boot entry.

The following Bootcfg command enables EMS console redirection on the first boot entry in the list. It sets the port for COM2 and sets the transmission rate to 115,200 kilobits per second (Kbps). These are the same port and baud rate settings that the administrator set in the BIOS for the out-of-band port.

```
bootcfg /ems ON /port COM2 /baud 115200 /id 1
```

The following Bootcfg display shows the result of the command. The newly added parameters are displayed in bold type.

```
## Boot Loader Settings
timeout:          3
default:          multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
redirect:         COM2
redirectbaudrate: 115200

Boot Entries
------------
Boot entry ID:   1
Friendly Name:   "Windows Server 2003, Standard with EMS"
Path:            multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
OS Load Options: /fastdetect /redirect
```

The following sample shows the result of the same command on a sample Boot.ini file.

```
[boot loader]
timeout=1
default=multi(0)disk(0)rdisk(0)partition(2)\WINDOWS
redirect=COM2
redirectbaudrate=115200
[operating systems]
multi(0)disk(0)rdisk(0)partition(2)\WINDOWS="EMS boot" /fastdetect /redirect
multi(0)disk(0)rdisk(0)partition(2)\WINDOWS="Windows Server 2003, Standard" /fastdetect
```

### <span id="enabling_ems_on_a_computer_without_an_acpi_spcr_table_in_windows_serve"></span><span id="ENABLING_EMS_ON_A_COMPUTER_WITHOUT_AN_ACPI_SPCR_TABLE_IN_WINDOWS_SERVE"></span>Enabling EMS on a Computer without an ACPI SPCR Table in Windows Server 2008

To enable EMS console redirection on a computer that has BIOS firmware, but does not have an ACPI Serial Port Console Redirection (SPCR) table, use the [**BCDEdit /emssettings**](https://msdn.microsoft.com/library/windows/hardware/ff542198) command to set the COM port and baud rate.

These parameters set the global port and transmission rate for EMS console redirection. Use the same port and transmission rate that are established for out-of-band communication in the BIOS.

Then, use the [**BCDEdit /ems**](https://msdn.microsoft.com/library/windows/hardware/ff542193) command to enable EMS for a boot entry.

The following commands set the global EMS redirection settings to use COM2 and a baud rate of 115200, and enable EMS for the specified boot entry.

```
bcdedit /emssettings EMSPORT:2 EMSBAUDRATE:115200
```

```
bcdedit /ems {18b123cd-2bf6-11db-bfae-00e018e2b8db} on
```

### <span id="enabling_ems_on_a_computer_with_an_spcr_table_in_operating_systems_pri"></span><span id="ENABLING_EMS_ON_A_COMPUTER_WITH_AN_SPCR_TABLE_IN_OPERATING_SYSTEMS_PRI"></span>Enabling EMS on a computer with an SPCR table in operating systems prior to Windows Server 2008

To enable EMS on a computer with ACPI BIOS firmware and an ACPI SPCR table, you can either use the **redirect=USEBIOSSETTINGS** parameter or the **redirect=COM***x* and **redirectbaudrate=** parameters. Then, you can add the [**/redirect**](https://msdn.microsoft.com/library/windows/hardware/ff557180) parameter to a boot entry.

The following example demonstrates use of the **redirect=USEBIOSSETTINGS** parameter. The following Bootcfg command enables EMS console redirection on the first boot entry in the list.

```
bootcfg /ems ON /port BIOSSET /id 1
```

The following Bootcfg display shows the result of the command. The newly added parameters are displayed in bold type.

```
## Boot Loader Settings
timeout: 1
default: multi(0)disk(0)rdisk(0)partition(2)\WINDOWS
redirect:USEBIOSSETTINGS

Boot Entries
------------
Boot entry ID:    1
OS Friendly Name: EMS boot
Path:             multi(0)disk(0)rdisk(0)partition(2)\WINDOWS
OS Load Options:  /fastdetect /redirect

Boot entry ID:    2
OS Friendly Name: Windows Server 2003, Standard
Path:             multi(0)disk(0)rdisk(0)partition(2)\WINDOWS
OS Load Options:  /fastdetect
```

The following sample shows the result of the same command on a sample Boot.ini file.

```
[boot loader]
timeout=1
default=multi(0)disk(0)rdisk(0)partition(2)\WINDOWS
redirect=USEBIOSSETTINGS
[operating systems]
multi(0)disk(0)rdisk(0)partition(2)\WINDOWS="EMS boot" /fastdetect /redirect
multi(0)disk(0)rdisk(0)partition(2)\WINDOWS="Windows Server 2003, Standard" /fastdetect
```

### <span id="enabling_ems_on_a_computer_with_an_spcr_table_in_windows_server_2008"></span><span id="ENABLING_EMS_ON_A_COMPUTER_WITH_AN_SPCR_TABLE_IN_WINDOWS_SERVER_2008"></span>Enabling EMS on a Computer with an SPCR Table in Windows Server 2008

To enable EMS on a computer with ACPI BIOS firmware and an ACPI SPCR table, you can use the [**BCDEdit /emssettings**](https://msdn.microsoft.com/library/windows/hardware/ff542198) and specify either the **BIOS** parameter or the **emsport** and **emsbaudrate** parameters. To enable EMS for a boot entry, use the [**BCDEdit /ems**](https://msdn.microsoft.com/library/windows/hardware/ff542193) command.

The following example demonstrates how to use the **BIOS** parameter. The following BCDEdit command enables EMS console redirection on the current boot entry.

```
bcdedit /emssettings bios
bcdedit /ems on 
```

### <span id="enabling_ems_on_a_computer_with_efi_firmware_in_operating_systems_prio"></span><span id="ENABLING_EMS_ON_A_COMPUTER_WITH_EFI_FIRMWARE_IN_OPERATING_SYSTEMS_PRIO"></span>Enabling EMS on a computer with EFI firmware in operating systems prior to Windows Server 2008

To enable EMS on a computer with EFI firmware, use Bootcfg to add the [**/redirect**](https://msdn.microsoft.com/library/windows/hardware/ff557180) parameter to a boot entry. Windows finds the out-of-band port and its settings in the firmware by reading the SPCR table and uses the same port and rate for EMS console redirection.

The following Bootcfg command enables EMS redirection on an Itanium-based computer. It uses the Bootcfg **/ems** switch with the ON argument to add the **/redirect** parameter to the boot entry. The **/id** switch identifies the boot entry.

```
bootcfg /ems ON /id 1
```

The following Bootcfg display of boot options in EFI NVRAM shows the result of the Bootcfg command. The first boot entry is configured to load the operating system with EMS console redirection enabled.

```
Boot Options
------------
Timeout:             30
Default:             \Device\HarddiskVolume3\WINDOWS
CurrentBootEntryID:  1

Boot Entries
------------
Boot entry ID:    1
OS Friendly Name: Windows Server 2003, Enterprise with EMS
OsLoadOptions:     /fastdetect /redirect
BootFilePath:     \Device\HarddiskVolume1\EFI\Microsoft\WINNT50\ia64ldr.efi
OsFilePath:       \Device\HarddiskVolume3\WINDOWS
```

### <span id="enabling_ems_on_a_computer_with_efi_firmware_in_windows_server_2008"></span><span id="ENABLING_EMS_ON_A_COMPUTER_WITH_EFI_FIRMWARE_IN_WINDOWS_SERVER_2008"></span>Enabling EMS on a Computer with EFI Firmware in Windows Server 2008

To enable EMS on a computer with EFI firmware, use the [**BCDEdit /ems**](https://msdn.microsoft.com/library/windows/hardware/ff542193) command and specify a boot entry. Windows finds the out-of-band port and its settings in the firmware by reading the SPCR table and uses the same port and rate for EMS console redirection.

The following command enables EMS console redirection on the specified boot entry that has the identifier of {18b123cd-2bf6-11db-bfae-00e018e2b8db}.

```
bcdedit /ems {18b123cd-2bf6-11db-bfae-00e018e2b8db} on
```

### <span id="changing_ems_settings_on_a_computer_with_bios_firmware_in_operating_sy"></span><span id="CHANGING_EMS_SETTINGS_ON_A_COMPUTER_WITH_BIOS_FIRMWARE_IN_OPERATING_SY"></span>Changing EMS Settings on a Computer with BIOS Firmware in Operating Systems prior to Windows Server 2008

When you configure EMS on a single boot entry, add the **redirect=** parameter to the \[boot loader\] section of the Boot.ini file. However, when you enable EMS on additional boot entries, you do not need to add the **redirect=** parameter again. Like all entries in the \[boot loader\] section, **redirect=** (and **redirectbaudrate=)** applies to all boot entries on the computer.

The following Bootcfg command enables EMS on the second boot entry. Because the port and baud rate are already set, there are no **/port** or **/baud** switches in the command.

```
bootcfg /ems ON /id 2
```

To change the port and baud rate settings, use the Bootcfg **/ems** switch with the EDIT argument. The following command changes the EMS port to COM1 and changes the baud rate to 57,600 Kbps.

```
bootcfg /ems EDIT /port COM1 /baud 57600
```

To disable EMS on a boot entry, use the Bootcfg **/ems** switch with the OFF argument. The following command disables EMS on the first boot entry.

```
bootcfg /ems OFF /id 1
```

If EMS is not enabled on any other boot entries, Bootcfg also deletes the EMS port and baud rate settings from the \[boot loader\] section of the Boot.ini file.

### <span id="changing_ems_settings_on_a_computer_running_windows_server_2008"></span><span id="CHANGING_EMS_SETTINGS_ON_A_COMPUTER_RUNNING_WINDOWS_SERVER_2008"></span>Changing EMS Settings on a Computer running Windows Server 2008

When you configure EMS on a boot entry on a computer that has ACPI BIOS firmware and an ACPI SPCR table, you can use the [**BCDEdit /emssettings**](https://msdn.microsoft.com/library/windows/hardware/ff542198) command and specify either the **BIOS** option or the **emsport** and **emsbaudrate** options. If you use the **BIOS** option, do not set the **emsport** or **emsbaudrate** options.

When you configure EMS on a computer that has EFI firmware, or with ACPI BIOS firmware and without an ACPI SPCR table, you can use the **BCDEdit /emssettings** command and specify the **emsport** and **emsbaudrate** options.

The **emsport** and **emsbaudrate** options set the serial port and transmission rate for EMS console redirection. These settings apply to all boot entries on the computer. To use **emsbaudrate**, you must also set the **emsport** option. By default, the transmission rate is set to 9600 (9,600 Kbps).

For example, the following command changes the EMS port to COM2 and changes the baud to 57,600 Kbps.

```
bcdedit /emssettings EMSPORT:2 EMSBAUDRATE:57600
```

To enable or disable EMS on a boot entry, use the [**BCDEdit /ems**](https://msdn.microsoft.com/library/windows/hardware/ff542193) command.

For example, the following command enables EMS on a specific boot entry that has an identifier of {173075c9-2cb2-11dc-b426-001558c41f5c}..

```
bcdedit /ems {173075c9-2cb2-11dc-b426-001558c41f5c} on
```

To disable EMS on the current boot entry, use the following command.

```
bcdedit /ems off
```

**Note**   Each boot entry uses a GUID as an identifier. If you do not specify an identifier, the **BCDEdit** command modifies the current operating system boot entry. If a boot entry is specified, the GUID associated with the boot entry must be enclosed in braces **{ }**. To view the GUID identifiers for all the active boot entries, use the **bcdedit /enum** command.

 

 

 





