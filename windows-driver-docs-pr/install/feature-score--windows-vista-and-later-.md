---
title: Feature Score
description: Feature Score
ms.assetid: cc7f2cd1-85aa-43be-9c4e-abdba3a4310a
keywords:
- feature score WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Feature Score


A driver rank is formatted as 0x*SSGGTHHH*, where the value of 0x*SS*000000 is the [signature score](signature-score--windows-vista-and-later-.md), the value of 0x00*GG*0000 is the feature score, and the value of 0x0000*THHH* is the [identifier score](identifier-score--windows-vista-and-later-.md).

The feature score provides a way to rank drivers based on the features that a driver supports. For example, feature scores might be defined for a [device setup class](device-setup-classes.md) that distinguishes between drivers based on class-specific criteria. The feature score supplements the identifier score, making it possible for driver writers to more easily and precisely distinguish between different drivers for a device that is based on well-defined criteria.

Microsoft defines feature score usage for particular device classes. Feature score is not required, so many device classes will not have feature score usage specified. In this case, the default feature score (0xFF) is expected, and will be assigned in the absence of a feature score defined in the INF of a driver.

When Microsoft does not explicitly require feature score for a device class, the driver should:

-   Not define a feature score in the driver INF (Windows will default to 0xFF)

    or

-   Explicitly define a feature score of 0xFF in the driver INF

The feature score for a driver is set by the [**INF FeatureScore Directive**](inf-featurescore-directive.md) in the [**INF DDInstall section**](inf-ddinstall-section.md) of the INF file that installs a device. The feature score is set as follows:

```cpp
[DDInstallSectionName]
. . .
FeatureScore=featurescore
```

where *DDInstallSectionName* is the name of the *DDInstall* section and *featurescore* is a single-byte hexadecimal number between 0x00 and 0xFF. Windows computes the feature score for a driver based on the *featurescore* value of the **FeatureScore** directive:

```cpp
feature score = (featurescore * 0x10000)
```

If the [**INF FeatureScore Directive**](inf-featurescore-directive.md) is not specified in the INF file, Windows uses a default feature score is 0x00FF0000 for the driver, which indicates that there is no preference based on the features of the driver. The lower the feature score, the better the rank, where the best feature score is 0x00000000.

For example, the following sets the feature score of a driver to 0x00FD0000:

```cpp
[DDInstallSectionName]
. . .
FeatureScore=xFD
```

For more information about driver ranking, see [How Windows Ranks Drivers](how-setup-ranks-drivers--windows-vista-and-later-.md).

 

 





