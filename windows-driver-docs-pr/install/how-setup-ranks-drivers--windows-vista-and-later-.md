---
title: How Windows Ranks Drivers
description: How Windows Ranks Drivers
ms.assetid: 54b6f40a-e5f6-41dd-8876-c9f0fb36ee00
keywords: ["ranking drivers WDK device installations", "driver ranking WDK device installations", "driver selections WDK device installations , ranking drivers", "locating drivers for device installation WDK device installations , ranking drivers", "searching for drivers during device installation WDK devi"]
---

# How Windows Ranks Drivers


Windows assigns a rank to a driver that matches a device. The rank indicates how well the driver matches the device. A driver rank is represented by an integer that is equal to or greater than zero. The lower the rank, the better a match the driver is for the device.

The rank of a driver is a composite value that depends on how a driver is signed, the features that are supported by the driver, and the type of match between the [device identification strings](device-identification-strings.md) that are reported by a device and the device identification strings that are specified in the entries of an [**INF Models section**](inf-models-section.md) of a driver INF file.

A rank is represented by a value of type DWORD. A rank is sum of a signature score, a feature score, and an identifier score. A rank is formatted as 0x*SSGGTHHH*, where *S*, *G*, *T*, and *H* are four-bitfields and the *SS*, *GG*, and *THHH* fields represent the three ranking scores, as follows:

-   The [signature score](signature-score--windows-vista-and-later-.md) ranks a driver according to how a driver is signed. The signature score depends only on the value of the *SS* field. An unspecified signature score is represented as 0x*SS*0000000.

    For an overview on how Windows Vista and later versions of Windows use a driver's signature to determine how the driver is installed, see [Signature Categories and Driver Installation](signature-categories-and-driver-installation.md).

-   The [feature score](feature-score--windows-vista-and-later-.md) ranks a driver based on the features that the driver supports. The feature score depends only on the value of the *GG* field. An unspecified feature score is represented as 0x00*GG*0000.

-   The [identifier score](identifier-score--windows-vista-and-later-.md) ranks a driver based on the type of match between a [device identification string](device-identification-strings.md) that is reported by a device and a device identification string that is listed in an entry of an INF *Models* section of a driver INF file. The identifier score depends only on the value of the *THHH* field. An unspecified identifier score is represented as 0x0000*THHH*.

For information about entries in the SetupAPI log that indicate the rank of a driver and the type of driver signature, see [Driver Rank Information in the SetupAPI Log](driver-rank-information-in-the-setupapi-log.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20How%20Windows%20Ranks%20Drivers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




