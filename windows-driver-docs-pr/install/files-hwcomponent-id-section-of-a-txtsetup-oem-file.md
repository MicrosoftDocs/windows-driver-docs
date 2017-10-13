---
title: Files.HwComponent.ID Section of a TxtSetup.oem File
description: A Files.HwComponent.ID section lists the files to be copied if the user selects a particular component option. One of these sections must be present for each option listed in each HwComponent section.
ms.assetid: a2c48a94-18a9-4efe-bdff-6c08bbbbabf9
keywords: ["Files.HwComponent.ID Section of a TxtSetup.oem File Device and Driver Installation"]
topic_type:
- apiref
api_name:
- Files.HwComponent.ID Section of a TxtSetup.oem File
api_type:
- NA
---

# Files.HwComponent.ID Section of a TxtSetup.oem File


A **Files.***HwComponent***.***ID* section lists the files to be copied if the user selects a particular component option. One of these sections must be present for each option listed in each *HwComponent* section.

``` syntax
[Files.HwComponent.ID]
filetype = diskN,filename[,DriverKey]
...
```

<a href="" id="files-hwcomponent-id"></a>**Files.***HwComponent***.***ID*  
*HwComponent* corresponds to the name of a *HwComponent* section in the file. *ID* corresponds to an *ID* entry in that *HwComponent* section.

<a href="" id="filetype"></a>*filetype*  
Identifies the type of the file to be copied. One of these entries is present for each file to be copied for this *HwComponent*.*ID*.

The *filetype* is one of the following system-defined values:

<a href="" id="driver"></a>**driver**  
Valid for all components. Windows copies the file to %*systemroot%\\system32\\drivers.*

<a href="" id="dll"></a>**dll**  
Valid for all components. Useful for the GDI portion of a display driver. Windows copies the file to %*systemroot%\\system32.*

<a href="" id="hal"></a>**hal**  
Valid only for the **computer** component. Windows copies the file to %*systemroot%\\system32\\hal.dll* (for x86) or to *\\os\\winnt\\hal.dll* on the system partition (for non-x86).

<a href="" id="inf"></a>**inf**  
Valid for all components. Specifies the regular INF file for the device. This file is used during GUI-mode setup and for other device maintenance operations. The file is copied to %*systemroot%\\system32*.

<a href="" id="catalog"></a>**catalog**  
Valid for drivers. Specifies a catalog file for the device. Not required for any component. For example, **catalog** = d1, *mydriver.cat*. See the WHQL guidelines for more information about catalog files.

<a href="" id="detect"></a>**detect**  
Valid for the **computer** component (x86 only). If specified, replaces the standard x86 hardware recognizer. Windows copies the file to *c:\\ntdetect.com*.

<a href="" id="diskn"></a>*diskN*  
Identifies the disk from which to copy the file. This value must match an entry in the **Disks** section.

<a href="" id="filename"></a>*filename*  
Specifies the name of the file, not including the directory path or drive. To form the full file name, Windows appends the *filename* to the directory specified for the disk in the **Disks** section. File names must not exceed eight characters, and extensions must not exceed three characters.

<a href="" id="driverkey"></a>*DriverKey*  
Specifies the name of the key to be created in the registry services tree for this file, if the file is of type **driver**. This value is used to form **Config.***DriverKey* section names. This value is required for components of type **scsi**.

The following example shows a **Files.***HwComponent***.***ID* section in a *TxtSetup.oem* file:

``` syntax
; ...
[Files.SCSI.oemscsi]
driver = d1,oemfs2.sys,OEMSCSI
inf = d1,oemsetup.inf
dll = d1, oemdrv.dll
catalog = d1, oemdrv.cat
; ...
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Files.HwComponent.ID%20Section%20of%20a%20TxtSetup.oem%20File%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




