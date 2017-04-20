---
title: Customized Features
author: windows-driver-content
description: Customized Features
ms.assetid: a7dfed02-3505-4ed6-86cf-efb273f76ad6
keywords:
- printer features WDK Unidrv , customized
- customized printer features WDK Unidrv
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Customized Features


## <a href="" id="ddk-customized-features-gg"></a>


Customized features are those that are specific to your hardware. You create unique names for these features. For each customized feature, you must specify a set of [customized options](customized-options.md). For example, suppose your printer provides an economy mode of operation. Because the GPD language does not provide a feature for describing this capability, you must define a customized feature and its options. The feature's specification might appear as follows:

```
*Feature: EconoMode
{
    *Name: "Economy Mode"
    *FeatureType: PRINTER_PROPERTY
    *DefaultOption: EconoModeOff
    *Option: EconoModeOff
    {
        *Name: "Off"
        *Command: CmdSelect
         {
             *Order: DOC_SETUP.5
             *Cmd: "@PJL SET ECONOMODE=OFF<0A>"
         }
    }
    *Option: EconoModeOn
    {
        *Name: "On"
        *Command: CmdSelect
        {
            *Order: DOC_SETUP.5
            *Cmd: "@PJL SET ECONOMODE=ON<0A>"
        }
    }
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customized%20Features%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


