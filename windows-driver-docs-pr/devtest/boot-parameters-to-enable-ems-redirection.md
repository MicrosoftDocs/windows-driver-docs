---
title: Boot Parameters to Enable EMS Redirection
description: Boot Parameters to Enable EMS Redirection
keywords:
- boot parameters WDK
- boot entry parameters WDK
- Emergency Management Services WDK boot parameters
- EMS redirection WDK boot parameters
- remote administration WDK boot parameters
ms.date: 03/12/2025
---

# Boot Parameters to Enable EMS Redirection

Emergency Management Services (EMS) technology allows you to control the selected components remotely, even when a the PC is not connected to the network or to other standard remote-administration tools. 

## Enabling EMS on a Computer with an SPCR Table

To enable EMS on a computer with ACPI BIOS firmware and an ACPI SPCR table, you can use the [**BCDEdit /emssettings**](./bcdedit--emssettings.md) and specify either the **BIOS** parameter or the **emsport** and **emsbaudrate** parameters. To enable EMS for a boot entry, use the [**BCDEdit /ems**](./bcdedit--ems.md) command.

The following example demonstrates how to use the **BIOS** parameter. The following BCDEdit command enables EMS console redirection on the current boot entry.

```command
bcdedit /emssettings bios
bcdedit /ems on
```

For more information on the contents of the ACPI SPCR table, see [Serial Port Console Redirection Table (SPCR)](../bringup/serial-port-console-redirection-table.md).

## Enabling EMS on a Computer with UEFI Firmware

To enable EMS on a computer with UEFI firmware, use the [**BCDEdit /ems**](./bcdedit--ems.md) command and specify a boot entry. Windows finds the out-of-band port and its settings in the firmware by reading the SPCR table and uses the same port and rate for EMS console redirection.
The following command enables EMS console redirection on the the current boot entry.

```command
bcdedit /ems {current} on
```

The following command enables EMS console redirection on the specified boot entry that has the identifier of {18b123cd-2bf6-11db-bfae-00e018e2b8db}.

```command
bcdedit /ems {18b123cd-2bf6-11db-bfae-00e018e2b8db} on
```

## Enabling EMS on a Computer without an ACPI SPCR Table

To enable EMS console redirection on a computer that has BIOS firmware, but does not have an ACPI Serial Port Console Redirection (SPCR) table, use the [**BCDEdit /emssettings**](./bcdedit--emssettings.md) command to set the COM port and baud rate.

These parameters set the global port and transmission rate for EMS console redirection. Use the same port and transmission rate that are established for out-of-band communication in the BIOS.

Then, use the [**BCDEdit /ems**](./bcdedit--ems.md) command to enable EMS for a boot entry.

The following commands set the global EMS redirection settings to use COM2 and a baud rate of 115200, and enable EMS for the specified boot entry.

```command
bcdedit /emssettings EMSPORT:2 EMSBAUDRATE:115200
```

```command
bcdedit /ems {current} on
```

## Changing EMS Settings

When you configure EMS on a boot entry on a computer that has ACPI BIOS firmware and an ACPI SPCR table, you can use the [**BCDEdit /emssettings**](./bcdedit--emssettings.md) command and specify either the **BIOS** option or the **emsport** and **emsbaudrate** options. If you use the **BIOS** option, do not set the **emsport** or **emsbaudrate** options.

When you configure EMS on a computer that has EFI firmware, or with ACPI BIOS firmware and without an ACPI SPCR table, you can use the **BCDEdit /emssettings** command and specify the **emsport** and **emsbaudrate** options.

The **emsport** and **emsbaudrate** options set the serial port and transmission rate for EMS console redirection. These settings apply to all boot entries on the computer. To use **emsbaudrate**, you must also set the **emsport** option. By default, the transmission rate is set to 9600 (9,600 Kbps).

For example, the following command changes the EMS port to COM2 and changes the baud to 57,600 Kbps.

```command
bcdedit /emssettings EMSPORT:2 EMSBAUDRATE:57600
```

To enable or disable EMS on a boot entry, use the [**BCDEdit /ems**](./bcdedit--ems.md) command.

For example, the following command enables EMS on a specific boot entry that has an identifier of {173075c9-2cb2-11dc-b426-001558c41f5c}.

```command
bcdedit /ems {173075c9-2cb2-11dc-b426-001558c41f5c} on
```

To disable EMS on the current boot entry, use the following command.

```command
bcdedit /ems off
```

> [!NOTE]
> Each boot entry uses a GUID as an identifier. If you do not specify an identifier, the **BCDEdit** command modifies the current operating system boot entry. If a boot entry is specified, the GUID associated with the boot entry must be enclosed in braces **{ }**. To view the GUID identifiers for all the active boot entries, use the **bcdedit /enum** command.

## See also

[BCDEdit /ems](./bcdedit--ems.md)

[BCDEdit /emssettings](./bcdedit--emssettings.md)

[Serial Port Console Redirection Table (SPCR)](../bringup/serial-port-console-redirection-table.md)

[Azure Serial Console](/troubleshoot/azure/virtual-machines/windows/serial-console-overview) 

