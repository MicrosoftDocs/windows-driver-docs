---
title: How Windows Ranks Driver Packages
description: How Windows Ranks Driver Packages
keywords:
- ranking drivers WDK device installations
- driver ranking WDK device installations
- driver selections WDK device installations , ranking drivers
- locating drivers for device installation WDK device installations , ranking drivers
- searching for drivers during device installation WDK devi
ms.date: 12/03/2021
---

# How Windows Ranks Driver Packages

> [!NOTE]
> This page describes how Windows determines a [driver package](driver-packages.md) rank value for a given driver package that matches on a device.  To understand how driver package rank and other factors (including INF date, driver version, etc.) are used to determine which driver package Windows selects for a device, see [How Windows Selects Drivers](./overview-of-the-driver-selection-process.md).

Windows assigns a rank to a [driver package](driver-packages.md) that matches a device. The rank indicates how well the driver package matches the device. A driver rank is represented by an integer that is equal to or greater than zero. The lower the rank, the better a match the driver package is for the device.

The rank of a driver package is a composite value that depends on a driver package's signature, the features that are supported by the driver package, and the type of match between the [device identification strings](device-identification-strings.md) that are reported by a device and the device identification strings that are specified in the entries of an [**INF Models section**](inf-models-section.md) of a driver package INF file.

A rank is represented by a value of type DWORD. A rank is the sum of a signature score, a feature score, and an identifier score. A rank is formatted as 0x*SSGGTHHH*, where *S*, *G*, *T*, and *H* are four-bitfields and the *SS*, *GG*, and *THHH* fields represent the three ranking scores, as follows:

-   The [signature score](signature-score--windows-vista-and-later-.md) ranks a driver package based on whether its digital signature is trusted. The signature score depends only on the value of the *SS* field. An unspecified signature score is represented as 0x*SS*0000000.

    For an overview on how Windows Vista and later versions of Windows use a driver package's signature to determine how the driver package is installed, see [Signature Categories and Driver Installation](signature-categories-and-driver-installation.md).

-   The [feature score](feature-score--windows-vista-and-later-.md) ranks a driver package based on the features that the driver package supports. The feature score depends only on the value of the *GG* field. An unspecified feature score is represented as 0x00*GG*0000.

-   The [identifier score](identifier-score--windows-vista-and-later-.md) ranks a driver package based on the type of match between a [device identification string](device-identification-strings.md) that is reported by a device and a device identification string that is listed in an entry of an INF *Models* section of a driver package INF file. The identifier score depends only on the value of the *THHH* field. An unspecified identifier score is represented as 0x0000*THHH*.

For information about entries in the SetupAPI log that indicate the rank of a driver package and the type of driver package signature, see [Driver Rank Information in the SetupAPI Log](driver-rank-information-in-the-setupapi-log.md).
