---
title: Customized Features
author: windows-driver-content
description: Customized Features
ms.assetid: a7dfed02-3505-4ed6-86cf-efb273f76ad6
keywords:
- printer features WDK Unidrv , customized
- customized printer features WDK Unidrv
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Customized Features





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

 

 




