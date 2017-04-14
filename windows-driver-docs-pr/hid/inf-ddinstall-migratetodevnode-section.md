---
title: INF DDInstall.MigrateToDevNode Section
author: windows-driver-content
description: INF DDInstall.MigrateToDevNode Section
ms.assetid: a4edbc9e-a2d0-4012-aca9-0b357939a881
keywords: ["INF files WDK non-HID keyboard/mouse", "DDInstall.MigrateToDevNode section"]
---

# INF DDInstall.MigrateToDevNode Section


## <a href="" id="ddk-inf-ddinstall-migratetodevnode-section-kg"></a>


**\[***install-section-name***.MigrateToDevNode\]** |
**\[***install-section-name***.nt.MigrateToDevNode\]** |
**\[***install-section-name***.ntx86.MigrateToDevNode\]** |
**\[***install-section-name***.ntia64.MigrateToDevNode\]**

*ServiceName***=***value-name*\[**,***value-name*\],...
The keyboard and mouse class installers copy the entry values specified by the list of *value-name* strings from the registry key **HKLM\\System\\CurrentControlSet\\Services\\***ServiceName***\\Parameters** to the device node of the device being installed.

### Entries and Values

<a href="" id="servicename"></a>*ServiceName*  
Specifies the service name associated with a device port (for example, **i8042prt**, **sermouse**, and so on).

<a href="" id="value-name"></a>*value-name*  
Specifies an entry value under the registry key **HKLM\\System\\CurrentControlSet\\Services\\***ServiceName***\\Parameters**.

### <a href="" id="comments"></a>Remarks

Microsoft supports INF *DDinstall***.MigratetoDevNode** sections primarily to facilitate porting Windows NT 4.0 legacy devices to Windows 2000 and later.

The keyboard and mouse class installers copy all the *value-name* entry values before the system starts the device stack. The specified entry values can be any valid registry entry values. The *value-name* entry values are not deleted from the **...\\***ServiceName***\\Parameters** registry key.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20INF%20DDInstall.MigrateToDevNode%20Section%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


