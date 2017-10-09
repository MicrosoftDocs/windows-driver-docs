---
title: Defaults Section of a TxtSetup.oem File
description: The Defaults section lists the default driver(s) for each hardware component supported by this file. Windows highlights the default selection when it presents a list of drivers to the user.
ms.assetid: 5f7fc7c8-543d-442a-911d-320aa19c72f0
keywords: ["Defaults Section of a TxtSetup.oem File Device and Driver Installation"]
topic_type:
- apiref
api_name:
- Defaults Section of a TxtSetup.oem File
api_type:
- NA
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Defaults%20Section%20of%20a%20TxtSetup.oem%20File%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




