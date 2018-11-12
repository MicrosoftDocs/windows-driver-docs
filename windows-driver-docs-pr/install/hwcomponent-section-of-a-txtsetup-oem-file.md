---
title: HwComponent Section of a TxtSetup.oem File
description: A HwComponent section lists the drivers available for a particular component. There is a HwComponent section for each type of component supported by the file.
ms.assetid: 84ba057b-6699-4709-bee8-24cb555d4165
keywords: ["HwComponent Section of a TxtSetup.oem File Device and Driver Installation"]
topic_type:
- apiref
api_name:
- HwComponent Section of a TxtSetup.oem File
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# HwComponent Section of a TxtSetup.oem File


A *HwComponent* section lists the drivers available for a particular component. There is a *HwComponent* section for each type of component supported by the file.

``` syntax
[HwComponent]
ID = description
...
```

<a href="" id="hwcomponent"></a>*HwComponent*  
The name of the section must be one of the following system-defined values: **computer** or **scsi**.

<a href="" id="id"></a>*ID*  
Specifies a string, unique within this section, that identifies the option.

For each entry in this section, there must be a corresponding **Files.**<em>HwComponent</em>**.**<em>ID</em> section in the file.

For the **computer** component, the last three characters of the string determine which kernel Windows copies. If this string ends in "_up", Windows copies the uniprocessor kernel. If this string ends in "_mp", Windows copies the multiprocessor kernel. If the string does not end in "_Xp", Windows copies one or the other kernel, but does not guarantee which one.

<a href="" id="description"></a>*description*  
Specifies a string that Windows presents to the user in the menu of driver choices.

The following example shows a *HwComponent* section for a *TxtSetup.oem* file that supports one component (**scsi**) and offers two options:

``` syntax
; ...
[SCSI]                  ; HwComponent section
oemscsi = "OEM Fast SCSI Controller"
oemscsi2 = "OEM Fast SCSI Controller 2"
 
; ...
```

 

 





