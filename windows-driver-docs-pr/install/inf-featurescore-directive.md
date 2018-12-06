---
title: INF FeatureScore Directive
description: The FeatureScore directive provides an additional ranking criterion for drivers based on the features that a driver supports.
ms.assetid: 78e1c2cf-b3e9-43ea-b435-979360cc3e28
keywords:
- INF FeatureScore Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF FeatureScore Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF FeatureScore Directive


The **FeatureScore** directive provides an additional ranking criterion for drivers based on the features that a driver supports. For example, feature scores might be defined for a [device setup class](device-setup-classes.md) that distinguishes between drivers that are based on class-specific criteria.

```cpp
[DDInstall]
  
FeatureScore=featurescore
```

The **FeatureScore** directive is supported in Windows Vista and later versions of Windows.

**Warning**  The **FeatureScore** directive is only processed when specified directly in the **\[DDInstall\]** section.

 

## Entries


<a href="" id="featurescore"></a>*featurescore*  
This value specifies the ranking score for the driver based on its feature contents. This entry is a single-byte hexadecimal number between 0x00 and 0xFF.

A lower *featurescore* value specifies a better feature score rank, where 0x00 is the best feature score rank. If the **FeatureScore** directive is not specified, Windows uses a default feature score rank of 0xFF for the driver.

Remarks
-------

If Windows detects multiple drivers for the same device, it must first determine which driver is the best driver to install. To accomplish this, Windows assigns each driver an overall rank based on several factors, or scores, such as the following:

-   A driver-signing score ([*signature score*](signature-score--windows-vista-and-later-.md) ), based on whether the driver is signed or not.
-   A driver feature score ([*feature score*](feature-score--windows-vista-and-later-.md)), based on how the driver's features rank compared to another driver for the device.
-   A hardware identifier score ([*identifier score*](identifier-score--windows-vista-and-later-.md)), based on how closely the Plug and Play (PnP) device identification strings that is reported by the bus driver for the device matches a [device identification string](device-identification-strings.md) in the INF [***Models***](inf-models-section.md) section of the INF file.

The feature score provides a way to rank drivers based on the features that a driver supports. For example, feature scores might be defined for a [device setup class](device-setup-classes.md) that distinguishes between drivers based on class-specific criteria.

The feature score supplements the identifier score, which makes it possible for driver writers to more easily and precisely distinguish between different drivers for a device that is based on well-defined criteria.

For more information about how drivers are ranked, see [How Windows Ranks Drivers (Windows Vista and Later)](how-setup-ranks-drivers--windows-vista-and-later-.md).

## See also


[feature score](feature-score--windows-vista-and-later-.md)

[identifier score](identifier-score--windows-vista-and-later-.md)

[***Models***](inf-models-section.md)

[signature score](signature-score--windows-vista-and-later-.md)

 

 






