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

 

 

 





