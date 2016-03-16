---
title: Specifying the KMDF Co installer in an INF File
description: If you include a co installer in your driver package read this topic for information about sections you must provide in your driver's INF file.
ms.assetid: e4f476ad-1ab5-44e3-9368-7467479bda85
keywords: ["Kernel Mode Driver Framework WDK installing drivers", "framework based drivers WDK KMDF installing", "INF files WDK KMDF coinstallers", "coinstallers WDK KMDF", "CoInstallers section WDK KMDF", "DDInstall section WDK KMDF", "Wdf INF file section WDK KMDF"]
---

# Specifying the KMDF Co-installer in an INF File


If you include a co-installer in your [driver package](https://msdn.microsoft.com/library/windows/hardware/ff539954), read this topic for information about sections you must provide in your driver's INF file. This information does not apply if you provide your own setup application that calls Microsoft-supplied .msu redistributables.

## <a href="" id="-------------inf-file-sections-for-the-co-installer"></a> INF File Sections for the Co-installer


Your driver's INF file must contain an INF *DDInstall***.CoInstallers** section that installs the co-installer. For example this section might be named **MyDevice.ntx86.CoInstallers**. For more information about specifying a co-installer in an INF file, see [**INF DDInstall.CoInstallers Section**](https://msdn.microsoft.com/library/windows/hardware/ff547321).

In addition, your driver's INF file must contain an INF *DDInstall***.Wdf** section that the co-installer reads after it has been installed. For example, this section might be named **MyDevice.ntx86.Wdf**. After the framework's co-installer has been installed, it reads this section while it is installing your driver.

The INF *DDInstall***.Wdf** section contains the following directive:

**KmdfService =** *DriverService***,***Wdf-install-section*

*DriverService* represents the name that the operating system will assign to your driver's kernel-mode service, and *Wdf-install-section* represents the name of an INF section that the co-installer reads to obtain information about your driver.

The INF section that *Wdf-install-section* identifies must contain the following directive:

**KmdfLibraryVersion =** *WdfLibraryVersion*

*WdfLibraryVersion* represents a library version number, such as "1.0" or "1.11".

For example, the following INF *DDInstall***.Wdf** section specifies **Echo\_wdfsect** as the *Wdf-install-section* name.

```
[ECHO_Device.NT.Wdf]
KmdfService = Echo, Echo_wdfsect
[Echo_wdfsect]
KmdfLibraryVersion = 1.0
```

You can avoid creating multiple INF files for multiple versions of the framework by using INX files and the [Stampinf](https://msdn.microsoft.com/library/windows/hardware/ff552786) tool. For more information about INX files, see [Using INX Files to Create INF Files](using-inx-files-to-create-inf-files.md).

### <a href="" id="sample-inf-ddinstall-coinstallers-and-ddinstall-wdf-sections"></a>**Sample INF** ***DDInstall*.CoInstallers and** ***DDInstall*.Wdf Sections**

The following code example shows how to create the INF *DDInstall***.CoInstallers** section and INF *DDInstall***.Wdf** section of an INF file for a PnP driver. The example shows how to create an INF file that is called *MyDevice.inf* and is based on the [ECHO](http://go.microsoft.com/fwlink/p/?linkid=256129) sample driver's *Echo.inf* file. The Echo sample driver is located in the samples directory of the WDK.

To create *MyDevice.inf*, you must change all **ECHO\_Device** substrings in *Echo.inf* to a name that is appropriate for your product. The following code example uses **MyDevice**.

You should attempt to match the section layout that the *Echo.inf* sample uses. In other words, if possible, keep the co-installer-related sections together to more easily spot cut-and-paste errors.

Before you have modified *echo.inf*, the sections that install the co-installer are as follows:

```
=============== Top of Echo.inf ====================
....
....
[DestinationDirs]
DefaultDestDir = 12
ECHO_Device_CoInstaller_CopyFiles = 11
....
....
;
;--- ECHO_Device Co-installer installation ------
;
[ECHO_Device.NT.CoInstallers]
AddReg=ECHO_Device_CoInstaller_AddReg
CopyFiles=ECHO_Device_CoInstaller_CopyFiles

[ECHO_Device_CoInstaller_AddReg]
HKR,,CoInstallers32,0x00010000, "WdfCoInstaller01000.dll,WdfCoInstaller"

[ECHO_Device_CoInstaller_CopyFiles]
WdfCoInstaller01000.dll

[ECHO_Device.NT.Wdf]
KmdfService = Echo, Echo_wdfsect
[Echo_wdfsect]
KmdfLibraryVersion = 1.0

===============  End of Echo.inf ===============
```

After you have changed all **ECHO\_Device** substrings, your *MyDevice.inf* file should appear as follows:

```
=============== Top of MyDevice.inf ===============
....
....
[DestinationDirs]
DefaultDestDir = 12
MyDevice_CoInstaller_CopyFiles = 11
....
....
;
;--- MyDevice Co-installer installation ------
;
[MyDevice.NT.CoInstallers]
AddReg=MyDevice_CoInstaller_AddReg
CopyFiles=MyDevice_CoInstaller_CopyFiles

[MyDevice_CoInstaller_AddReg]
HKR,,CoInstallers32,0x00010000, "WdfCoInstaller01000.dll,WdfCoInstaller"

[MyDevice_CoInstaller_CopyFiles]
WdfCoInstaller01000.dll

[MyDevice_Device.NT.Wdf]
KmdfService = MyDevice, MyDevice_wdfsect
[MyDevice_wdfsect]
KmdfLibraryVersion = 1.0
....
....
=============== End of MyDevice.inf ===============
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Specifying%20the%20%20KMDF%20Co-installer%20in%20an%20INF%20File%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




