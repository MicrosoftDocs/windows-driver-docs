---
title: BCDEdit /emssettings
description: The /emssettings option sets the global Emergency Management Services (EMS) settings for the computer. To enable or disable EMS, use the /ems option. The /emssettings option does not enable or disable EMS for any boot entry.
ms.assetid: 010e852d-ff97-4280-b35b-f1881e249e42
keywords: ["BCDEdit /emssettings Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /emssettings
api_type:
- NA
---

# BCDEdit /emssettings


The **/emssettings** option sets the global Emergency Management Services (EMS) settings for the computer. To enable or disable EMS, use the **/ems** option. The **/emssettings** option does not enable or disable EMS for any boot entry.

``` syntax
    bcdedit /emssettings [ BIOS ] | [ EMSPORT: port | [EMSBAUDRATE: baudrate] ] 

   
```

Parameters
----------

<a href="" id="-------bios------"></a> **BIOS**   
Specifies that the system will use BIOS settings for the EMS configuration. This works only on systems that have EMS support provided by the BIOS.

<a href="" id="-------emsport--------port------"></a> **EMSPORT:** *port*   
Specifies the serial port to use as the EMS port. This parameter should not be specified with the **BIOS** option.

<a href="" id="-------emsbaudrate---------baudrate------"></a> **EMSBAUDRATE:** *baudrate*   
Specifies the serial baud rate to use for EMS. This command should not be specified with the BIOS. The *baudrate* is optional, and the default is 9,600 bps.

### Comments

To properly enable EMS console redirection after Windows is installed, Windows needs to know the port and transmission rate that the computer uses for out-of-band communication. Windows uses these same settings for EMS console redirection.

On computers with BIOS firmware and an ACPI Serial Port Console Redirection (SPCR) table, Windows can find the out-of-band settings established in the BIOS by reading entries in the SPCR table. On these systems, you can use the **BIOS** parameter to direct Windows to look in the SPCR table for the port settings, or you can use the **emsport:***port* and **emsbaudrate:***baudrate* parameters to override the settings in the SPCR table.

On computers that have BIOS firmware, but do not have an SPCR table, use BCDEdit and the **/emssettings** command with the **emsport:***port* parameter to specify the port and with the **emsbaudrate:***baudrate* parameter to specify the transmission rate.

On all systems, use the [**BCDEdit /ems**](bcdedit--ems.md) command and specify the boot entry to enable EMS console redirection on the operating system that the boot entry loads.

The boot parameters described in this section enable EMS console redirection after Windows is installed. For information about enabling EMS during a new installation or upgrade of Windows, search for "Enabling Emergency Management Services" on the [Microsoft TechNet](http://go.microsoft.com/fwlink/p/?linkid=10111) website.

For a detailed example, see [Boot Parameters to Enable EMS Redirection](https://msdn.microsoft.com/library/windows/hardware/ff542282).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20BCDEdit%20/emssettings%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




