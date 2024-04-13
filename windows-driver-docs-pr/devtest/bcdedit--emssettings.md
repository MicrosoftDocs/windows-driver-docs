---
title: BCDEdit /emssettings
description: The /emssettings option sets the global Emergency Management Services (EMS) settings for the computer. To enable or disable EMS, use the /ems option. The /emssettings option does not enable or disable EMS for any boot entry.
ms.date: 07/03/2018
keywords: ["BCDEdit /emssettings Driver Development Tools"]
topic_type:
- apiref
ms.topic: reference
api_name:
- BCDEdit /emssettings
api_type:
- NA
---

# BCDEdit /emssettings


The **/emssettings** option sets the global Emergency Management Services (EMS) settings for the computer. To enable or disable EMS, use the **/ems** option. The **/emssettings** option does not enable or disable EMS for any boot entry.

Syntax 

```
    bcdedit /emssettings [ BIOS ] | [ EMSPORT: port | [EMSBAUDRATE: baudrate] ] 
```

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

## Parameters

**BIOS**   
Specifies that the system will use BIOS settings for the EMS configuration. This works only on systems that have EMS support provided by the BIOS.

**EMSPORT:** *port*   
Specifies the serial port to use as the EMS port. This parameter should not be specified with the **BIOS** option.

**EMSBAUDRATE:** *baudrate*   
Specifies the serial baud rate to use for EMS. This command should not be specified with the BIOS. The *baudrate* is optional, and the default is 9,600 bps.

### Comments

To properly enable EMS console redirection after Windows is installed, Windows needs to know the port and transmission rate that the computer uses for out-of-band communication. Windows uses these same settings for EMS console redirection.

On computers with BIOS firmware and an ACPI Serial Port Console Redirection (SPCR) table, Windows can find the out-of-band settings established in the BIOS by reading entries in the SPCR table. On these systems, you can use the **BIOS** parameter to direct Windows to look in the SPCR table for the port settings, or you can use the **emsport:**<em>port</em> and **emsbaudrate:**<em>baudrate</em> parameters to override the settings in the SPCR table.

On computers that have BIOS firmware, but do not have an SPCR table, use BCDEdit and the **/emssettings** command with the **emsport:**<em>port</em> parameter to specify the port and with the **emsbaudrate:**<em>baudrate</em> parameter to specify the transmission rate.

On all systems, use the [**BCDEdit /ems**](bcdedit--ems.md) command and specify the boot entry to enable EMS console redirection on the operating system that the boot entry loads.

The boot parameters described in this section enable EMS console redirection after Windows is installed. 

For a detailed example, see [Boot Parameters to Enable EMS Redirection](./boot-parameters-to-enable-ems-redirection.md).

 

