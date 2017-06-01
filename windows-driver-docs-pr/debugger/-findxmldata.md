---
title: findxmldata
description: The findxmldata extension retrieves XML data from a CAB file that contains a kernel-mode Small Memory Dump file.
ms.assetid: 6d0b5294-b086-4b33-ac0d-0428521a3489
keywords: ["XML data in CAB files", "sysdata.xml", "findxmldata Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- findxmldata
api_type:
- NA
---

# !findxmldata


The **!findxmldata** extension retrieves XML data from a CAB file that contains a kernel-mode Small Memory Dump file.

```
!findxmldata [ -d DeviceName | -h HwId ] 
!findxmldata -r Driver 
!findxmldata -chksum [ -z CabFile ]
!findxmldata -v 
```

## <span id="ddk__findxmldata_dbg"></span><span id="DDK__FINDXMLDATA_DBG"></span>Parameters


<span id="_______-d_______DeviceName______"></span><span id="_______-d_______devicename______"></span><span id="_______-D_______DEVICENAME______"></span> **-d** *DeviceName*   
Displays all devices whose device name contains the string that *DeviceName* specifies.

<span id="_______-h_______HwId______"></span><span id="_______-h_______hwid______"></span><span id="_______-H_______HWID______"></span> **-h** *HwId*   
Displays all devices whose hardware IDs contain the string that *HwId* specifies. If you use both **-d** and **-h**, the debugger displays only those devices that satisfy both matches.

<span id="_______-r_______Driver______"></span><span id="_______-r_______driver______"></span><span id="_______-R_______DRIVER______"></span> **-r** *Driver*   
Displays information about the driver that the *Driver* parameter specifies, including all devices that use this driver.

<span id="_______-chksum______"></span><span id="_______-CHKSUM______"></span> **-chksum**   
Displays the XML file's checksum.

<span id="_______-z_______CabFile______"></span><span id="_______-z_______cabfile______"></span><span id="_______-Z_______CABFILE______"></span> **-z** *CabFile*   
Enables you to perform a checksum on the CAB file that the CabFile parameter specifies, instead of on the default Sysdata.xml file.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Displays system version information.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

The **!findxmldata** extension works only on a kernel-mode Small Memory Dump file that is stored in a CAB file.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to put dump files into CAB files, see [**.dumpcab (Create Dump File CAB)**](-dumpcab--create-dump-file-cab-.md). For information more about how to debug a kernel-mode dump file, including dump files that are stored inside CAB files, see [Analyzing a Kernel-Mode Dump File](analyzing-a-kernel-mode-dump-file.md).

Remarks
-------

The **!findxmldata** extension retrieves data from the Sysdata.xml file that is stored in a CAB file that contains a kernel-mode [Small Memory Dump](small-memory-dump.md) file.

When you do not use any options, the extension displays all devices.

The following examples show you how to use **!findxmldata**.

```
kd> !findxmldata -v
SYSTEM Info:
OSVER: 5.1.2600 2.0
OSLANGUAGE: 2052
OSNAME: Microsoft Windows XP Home Edition
kd> !findxmldata -d MIDI
Node DEVICE
 DESCRIPTION    : MPU-401 Compatible MIDI Device
        HARDWAREID     : ACPI\PNPB006
        SERVICE        : ms_mpu401
        DRIVER         : msmpu401.sys

kd> !findxmldata -r msmpu
Node DRIVER
 FILENAME       : msmpu401.sys
        FILESIZE       : 2944
        CREATIONDATE   : 05-06-2005 09:18:34
        VERSION        : 5.1.2600.0
        MANUFACTURER   : Microsoft Corporation
        PRODUCTNAME    : Microsoft« Windows« Operating System
Node DEVICE
        DESCRIPTION    : MPU-401 Compatible MIDI Device
 HARDWAREID     : ACPI\PNPB006
        SERVICE        : ms_mpu401
        DRIVER         : msmpu401.sys

kd> !findxmldata -h PCI\VEN_8086&DEV_24C3&SUBSYS_24C28086
Node DEVICE
 DESCRIPTION    : Intel(R) 82801DB/DBM SMBus Controller - 24C3
        HARDWAREID     : PCI\VEN_8086&DEV_24C3&SUBSYS_24C28086&REV_01
kd> !findxmldata -h USB\ROOT_HUB&VID8086&PID24C4&REV0001
Node DEVICE
        DESCRIPTION    : USB Root Hub
 HARDWAREID     : USB\ROOT_HUB&VID8086&PID24C4&REV0001
        SERVICE        : usbhub
        DRIVER         : usbhub.sys

kd> !findxmldata -h ACPI\PNPB006
Node DEVICE
        DESCRIPTION    : MPU-401 Compatible MIDI Device
 HARDWAREID     : ACPI\PNPB006
        SERVICE        : ms_mpu401
        DRIVER         : msmpu401.sys
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!findxmldata%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




