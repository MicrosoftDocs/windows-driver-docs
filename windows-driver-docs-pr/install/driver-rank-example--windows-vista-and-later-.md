---
title: Driver Rank Example
description: Driver Rank Example
ms.assetid: 20fe0f63-5d6c-4617-b5df-b2adb941f257
keywords: ["driver rank ranges WDK device installations", "rank ranges WDK device installations", "range ranking WDK device installations"]
---

# Driver Rank Example


Consider a device that has the following lists of [device identification strings](device-identification-strings.md), where the HwID\_*N* and CID\_*N* names represent actual [hardware IDs](hardware-ids.md) and [compatible IDs](compatible-ids.md):

-   List of hardware IDs
    ```
     HwID_1, HwID_2
    ```

-   List of compatible IDs
    ```
    CID_1, and CID_2
    ```

The first hardware ID in a list of hardware IDs is the most specific identifier for the device. In this example, that is HwID\_1.

Also assume there is an INF file that has an [**INF *Models* section**](inf-models-section.md) that has the following entry, where the INF\_*XXX\_N* names represent actual hardware IDs and compatible IDs:

```
DeviceDesc1 = InstallSection1, INF_HWID_1, INF_CID_1, INF_CID_2
```

In addition, assume that the INF *DDInstall* section named *InstallSection1* has the following **FeatureScore** directive, where the corresponding feature score of the driver is 0x00*GG*0000:

```
FeatureScore=0xGG
```

The following table lists the rank of each possible match between the identifiers that are reported by the device and the identifiers that are listed in the INF *Models* section entry. The rank is the sum of the [signature score](signature-score--windows-vista-and-later-.md), which is represented by 0x*SS*000000, the [feature score](feature-score--windows-vista-and-later-.md), which is represented by 0x00*GG*0000, and the [identifier score](identifier-score--windows-vista-and-later-.md), which depends, in each case, on the two identifiers that matched.

Device identifiers
Identifiers in the INF *Models* section entry
**INF\_HwID\_1**

**INF\_CID\_1**

**INF\_CID\_2**

**HwID\_1**

Rank 0x*SSGG*0000

Rank 0x*SSGG*1000

Rank 0x*SSGG*1000

**HwID\_2**

Rank 0x*SSGG*0001

Rank 0x*SSGG*1001

Rank 0x*SSGG*1001

**CID\_1**

Rank 0x*SSGG*2000

Rank 0x*SSGG*3000

Rank 0x*SSGG*3100

**CID\_2**

Rank 0x*SSGG*2001

Rank 0x*SSGG*3001

Rank 0x*SSGG*3101

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Driver%20Rank%20Example%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




