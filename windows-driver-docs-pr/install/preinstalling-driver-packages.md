---
title: Preinstalling Driver Packages
description: Preinstalling Driver Packages
ms.assetid: aba794ac-ab24-486a-9f5a-7e8435056bb7
keywords: ["installation applications WDK , preinstall driver packages", "device installation applications WDK , preinstall driver packages", "preinstalled drivers WDK device installations"]
---

# Preinstalling Driver Packages


## <a href="" id="ddk-pre-installing-driver-files-dg"></a>


To preinstall driver files, your [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) should follow these steps:

1.  On the target system, create a directory for the driver files. If your device installation application installs an application, the driver files should be stored in a subdirectory of the application directory.

2.  Copy all files in the [driver package](driver-packages.md) from the distribution media to the directory that is created in step (1). The driver package includes the driver or drivers, the INF file, the catalog file, and other installation files.

3.  Call [SetupCopyOEMInf](http://go.microsoft.com/fwlink/p/?linkid=98735) specifying the INF file in the directory that was created in step (1). Specify SPOST\_PATH for the *OEMSourceMediaType* parameter and specify **NULL** for the *OEMSourceMediaLocation* parameter. [SetupCopyOEMInf](http://go.microsoft.com/fwlink/p/?linkid=194252) copies the INF file for the driver package into the *%SystemRoot%\\Inf* directory on the target system and directs Windows to store the source location of the INF file in its list of preprocessed INF files. [SetupCopyOEMInf](http://go.microsoft.com/fwlink/p/?linkid=194252) also processes the catalog file, so the PnP manager will install the driver the next time that it recognizes a device that is listed in the INF file.

When the user plugs in the device, the PnP manager recognizes the device, finds the INF file copied by [SetupCopyOEMInf](http://go.microsoft.com/fwlink/p/?linkid=194252), and installs the drivers copied in step (2). (For more information about copying INF files, see [Copying INFs](copying-inf-files.md).)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Preinstalling%20Driver%20Packages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




