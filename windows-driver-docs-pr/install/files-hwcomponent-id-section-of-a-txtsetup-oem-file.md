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
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Files.HwComponent.ID Section of a TxtSetup.oem File


A **Files.**<em>HwComponent</em>**.**<em>ID</em> section lists the files to be copied if the user selects a particular component option. One of these sections must be present for each option listed in each *HwComponent* section.

``` syntax
[Files.HwComponent.ID]
filetype = diskN,filename[,DriverKey]
...
```

<a href="" id="files-hwcomponent-id"></a>**Files.**<em>HwComponent</em>**.**<em>ID</em>  
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
Specifies the name of the key to be created in the registry services tree for this file, if the file is of type **driver**. This value is used to form **Config.**<em>DriverKey</em> section names. This value is required for components of type **scsi**.

The following example shows a **Files.**<em>HwComponent</em>**.**<em>ID</em> section in a *TxtSetup.oem* file:

``` syntax
; ...
[Files.SCSI.oemscsi]
driver = d1,oemfs2.sys,OEMSCSI
inf = d1,oemsetup.inf
dll = d1, oemdrv.dll
catalog = d1, oemdrv.cat
; ...
```

 

 





