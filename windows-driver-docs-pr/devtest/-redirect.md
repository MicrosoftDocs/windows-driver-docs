---
title: /redirect
description: The /redirect parameter enables Emergency Management Services (EMS) console redirection on a Windows server.
ms.assetid: f03e7ddc-c9e3-48cc-a133-16d1946f5a26
keywords: ["/redirect Driver Development Tools"]
topic_type:
- apiref
api_name:
- /redirect
api_type:
- NA
---

/redirect
=========

The **/redirect** parameter enables Emergency Management Services (EMS) console redirection on a Windows server.

**Computers with ACPI BIOS firmware and an SPCR table**

In the \[boot loader\] section:

``` syntax
    redirect=COMx 
[redirectbaudrate=BaudRate]

- OR -

redirect=USEBIOSSETTINGS

   
```

In the \[operating systems\] section:

``` syntax
    /redirect 

   
```

**Computers with ACPI BIOS firmware and no SPCR table**

In the \[boot loader\] section:

``` syntax
    redirect=COMx
[redirectbaudrate=BaudRate]

   
```

In the \[operating systems\] section:

``` syntax
    /redirect 

   
```

**Computers with EFI firmware**

``` syntax
    /redirect

   
```

## Subparameters


<a href="" id="-------redirect-------"></a> **redirect=**   
Establishes a port for EMS console redirection. This should be the same port that the computer uses for out-of-band management.

This parameter is required and valid only on computers with BIOS firmware. It appears in the \[boot loader\] section of the Boot.ini file and applies to all boot entries on the computer.

The following table describes the values of the **redirect=** statement.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>COM</strong><em>x</em></p></td>
<td align="left"><p>Specifies a serial port. Valid values are COM1, COM2, COM3, and COM4. Set this value to the serial port that is designated for out-of-band management in the firmware. You cannot use the same port for debugging and for EMS console redirection.</p>
<p>This value is required on computers with BIOS firmware that do not have an ACPI Serial Port Console Redirection (SPCR) table.</p>
<p>When used on computers that have an SPCR table, this value is used instead of the settings in the SPCR table.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>USEBIOSSETTINGS</strong></p></td>
<td align="left"><p>Uses the port and connection speed that are designated for out-of-band management in the firmware.</p>
<p>Valid only on computers with a BIOS firmware and an ACPI Serial Port Console Redirection (SPCR) table.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="-------redirectbaudrate-------"></a> **redirectbaudrate=**   
Establishes the connection speed for EMS transmission. This parameter is optional and valid only with **redirect=COM***x*. If you omit this parameter on any computer with BIOS firmware, the default connection speed for EMS transmission is 9600 kilobits per second (Kbps).

When **redirect=COM***x* and **redirectbaudrate=** are used on computers with an SPCR table, the specified COM port and transmission rate are used instead of the settings in the SPCR table.

The following table describes the value of the **redirectbaudrate=** parameter.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>BaudRate</em></p></td>
<td align="left"><p>Specifies the connection speed for EMS transmission. Valid values are 9600, 19200, 57600, and 115200 in kilobits per second (Kbps). (38400 is not a valid value.) The default value is 9600 Kbps.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="--------redirect------"></a> **/redirect**   
Enables EMS console redirection on a Windows server operating system associated with the boot entry. This parameter is valid on boot entries for Windows Server 2003 and later version of Windows server systems on all computers.

### Comments

The **/redirect** parameter is supported only on Windows Server 2003, Windows XP, and Windows 2000. In Windows Vista and later versions of Windows, use BCDEdit and the **/emssettings** parameter and its subparameters to establish EMS settings for all boot entries. Then, use the **/ems** parameter to enable EMS for a particular boot entry.

EMS allows users to control particular components of a server remotely, even when the server is not connected to the network or to other standard remote-administration tools. For information about EMS, search for Emergency Management Services on the [Microsoft TechNet](http://go.microsoft.com/fwlink/p/?linkid=10111) website.

EMS is supported on all versions of Windows Server 2003 and later and versions of Windows server systems for x86-, x64-, and Itanium-based computers.

To properly enable EMS console redirection after Windows is installed, Windows needs to know the port and transmission rate that the computer uses for out-of-band communication. Windows uses these same settings for EMS console redirection.

On computers with EFI firmware, Windows automatically retrieves the out-of-band settings from the EFI firmware. On computers with BIOS firmware, Windows must find the out-of-band settings in the Boot.ini file.

On computers with BIOS firmware and an ACPI Serial Port Console Redirection (SPCR) table, Windows can find the out-of-band settings established in the BIOS by reading entries in the SPCR table. On these systems, you can add the **redirect=USEBIOSSETTINGS** parameter to the Boot.ini file to direct Windows to look in the SPCR table for the port settings, or you can use the **redirect=COM***x* and **redirectbaudrate=** parameters to override the settings in the SPCR table.

On computers that have BIOS firmware, but do not have an SPCR table, repeat the out-of-band settings in the Boot.ini file. Use the **redirect=COM***x* parameter to specify the port and the **redirectbaudrate=** parameter to specify the transmission rate.

On all systems, use the **/redirect** parameter on a boot entry to enable EMS console redirection on the operating system that the boot entry loads.

The boot parameters described in this section enable EMS console redirection after Windows is installed. For information about enabling EMS during a new installation or upgrade of Windows, search for "Enabling Emergency Management Services" on the [Microsoft TechNet](http://go.microsoft.com/fwlink/p/?linkid=10111) website.

For a detailed example, see [Boot Parameters to Enable EMS Redirection](https://msdn.microsoft.com/library/windows/hardware/ff542282).

For more information about EMS, see "Emergency Management Services" in Help and Support. Also, review the topics in the "Headless Server and Emergency Management Services Design" section of the [Server Platform Design - Overview](http://go.microsoft.com/fwlink/p/?linkid=8757) page on the Windows Hardware Developer Central website.

### Examples

**Computers with no SPCR table (or to override the SPCR table)**

```
[boot loader]
timeout=30
default=multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
redirect=COM1
redirectbaudrate=115200
[operating systems]
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Windows Server 2003, Standard" /fastdetect /redirect
```

**Computers with an SPCR table**

```
[boot loader]
timeout=2
default=multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
redirect=USEBIOSSETTINGS
[operating systems]
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Windows Server 2003, Standard" /fastdetect /redirect
```

**Computers with EFI firmware (Bootcfg display)**

```
Boot Options
------------
Timeout:             30
Default:             \Device\HarddiskVolume3\WINDOWS
CurrentBootEntryID:  1

Boot Entries
------------

Boot entry ID:    1
OS Friendly Name: Microsoft Windows .NET Enterprise Server
OsLoadOptions:     /redirect
BootFilePath:     \Device\HarddiskVolume1\EFI\Microsoft\WINNT50\ia64ldr.efi
OsFilePath:       \Device\HarddiskVolume3\WINDOWS
```

### Bootcfg Commands

```
bootcfg /ems ON /port COM1 /baud 115200 /ID 1
bootcfg /ems ON /port BIOSSET /ID 1
bootcfg /ems ON /ID 1
bootcfg /ems EDIT /port COM1 /baud 115200 /ID 1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/redirect%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




