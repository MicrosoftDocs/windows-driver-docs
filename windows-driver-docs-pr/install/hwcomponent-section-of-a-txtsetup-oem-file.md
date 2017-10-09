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

For each entry in this section, there must be a corresponding **Files.***HwComponent***.***ID* section in the file.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20HwComponent%20Section%20of%20a%20TxtSetup.oem%20File%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




