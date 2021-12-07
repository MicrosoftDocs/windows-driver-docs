---
title: Feature Score
description: Feature Score
keywords:
- feature score WDK device installations
ms.date: 12/03/2021
ms.localizationpriority: medium
---

# Feature Score

A driver package rank is formatted as 0x*SSGGTHHH*, where the value of 0x*SS*000000 is the [signature score](signature-score--windows-vista-and-later-.md), the value of 0x00*GG*0000 is the feature score, and the value of 0x0000*THHH* is the [identifier score](identifier-score--windows-vista-and-later-.md).

The feature score provides a way to rank driver packages based on the features that a driver package supports. For example, feature scores might be defined for a [device setup class](./overview-of-device-setup-classes.md) that distinguishes between driver packages based on class-specific criteria. The feature score supplements the identifier score, making it possible for driver package writers to more easily and precisely distinguish between different driver packages for a device that is based on well-defined criteria.

Microsoft defines feature score usage for particular device classes. Feature score is not required, so many device classes will not have feature score usage specified. In this case, the default feature score (0xFF) is expected, and will be assigned in the absence of a feature score defined in the INF of a driver package.

When Microsoft does not explicitly require feature score for a device class, the driver package should not define a feature score in the driver package INF (Windows will default to 0xFF).

The feature score for a driver package is set by the [**INF FeatureScore Directive**](inf-featurescore-directive.md) in the [**INF DDInstall section**](inf-ddinstall-section.md) of the INF file that installs a device. The feature score is set as follows:

```cpp
[DDInstallSectionName]
. . .
FeatureScore=featurescore
```

where *DDInstallSectionName* is the name of the *DDInstall* section and *featurescore* is a single-byte hexadecimal number between 0x00 and 0xFF. Windows computes the feature score for a driver package based on the *featurescore* value of the **FeatureScore** directive:

```cpp
feature score = (featurescore * 0x10000)
```

If the [**INF FeatureScore Directive**](inf-featurescore-directive.md) is not specified in the INF file, Windows uses a default feature score of 0x00FF0000 for the driver package, which indicates that there is no preference based on the features of the driver package. The lower the feature score, the better the rank, where the best feature score is 0x00000000.

For example, the following sets the feature score of a driver package to 0x00FD0000:

```cpp
[DDInstallSectionName]
. . .
FeatureScore=xFD
```

For more information about driver package ranking, see [How Windows Ranks Drivers](how-setup-ranks-drivers--windows-vista-and-later-.md).
