---
title: Defaults Section of a TxtSetup.oem File
description: The Defaults section lists the default driver(s) for each hardware component supported by this file. Windows highlights the default selection when it presents a list of drivers to the user.
keywords: ["Defaults Section of a TxtSetup.oem File Device and Driver Installation"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Defaults Section of a TxtSetup.oem File
api_type:
- NA
ms.date: 10/17/2018
---

# Defaults Section of a TxtSetup.oem File


The **Defaults** section lists the default driver(s) for each hardware component supported by this file. Windows highlights the default selection when it presents a list of drivers to the user.

``` syntax
[Defaults]
component = ID
...
```

<a href="" id="component"></a>*component*  
Specifies a hardware component supported by this file. The *component* must be one of the following system-defined values: **computer** or **scsi**.

<a href="" id="id"></a>*ID*  
Specifies a string that identifies the default option. This string matches an ID specified in the corresponding *HwComponent* section.

If a *TxtSetup.oem* file fails to define a default driver for a supported component, Windows uses the first entry in the *HwComponent* section.

The following example shows a **Defaults** section (and the *HwComponent* section) for a *TxtSetup.oem* file that supports one component (**scsi**):

``` syntax
; ...
[Defaults]
SCSI = oemscsi
 
[SCSI]                  ; HwComponent section
oemscsi = "OEM Fast SCSI Controller"
oemscsi2 = "OEM Fast SCSI Controller 2"
 
; ...
```

 

 





