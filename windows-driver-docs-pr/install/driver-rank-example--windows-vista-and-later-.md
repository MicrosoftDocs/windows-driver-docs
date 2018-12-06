---
title: Driver Rank Example
description: Driver Rank Example
ms.assetid: 20fe0f63-5d6c-4617-b5df-b2adb941f257
keywords:
- driver rank ranges WDK device installations
- rank ranges WDK device installations
- range ranking WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Rank Example


Consider a device that has the following lists of [device identification strings](device-identification-strings.md), where the HwID_*N* and CID_*N* names represent actual [hardware IDs](hardware-ids.md) and [compatible IDs](compatible-ids.md):

-   List of hardware IDs
    ```cpp
     HwID_1, HwID_2
    ```

-   List of compatible IDs
    ```cpp
    CID_1, and CID_2
    ```

The first hardware ID in a list of hardware IDs is the most specific identifier for the device. In this example, that is HwID_1.

Also assume there is an INF file that has an [**INF *Models* section**](inf-models-section.md) that has the following entry, where the INF_*XXX_N* names represent actual hardware IDs and compatible IDs:

```cpp
DeviceDesc1 = InstallSection1, INF_HWID_1, INF_CID_1, INF_CID_2
```

In addition, assume that the INF *DDInstall* section named *InstallSection1* has the following **FeatureScore** directive, where the corresponding feature score of the driver is 0x00*GG*0000:

```cpp
FeatureScore=0xGG
```

The following table lists the rank of each possible match between the identifiers that are reported by the device and the identifiers that are listed in the INF *Models* section entry. The rank is the sum of the [signature score](signature-score--windows-vista-and-later-.md), which is represented by 0x*SS*000000, the [feature score](feature-score--windows-vista-and-later-.md), which is represented by 0x00*GG*0000, and the [identifier score](identifier-score--windows-vista-and-later-.md), which depends, in each case, on the two identifiers that matched.

<table>
<tr>
<th>Device identifiers</th>
<th colspan="3">Identifiers in the INF <i>Models</i> section entry</th>
</tr>
<tr>
<td></td>
<td>
<p><b>INF_HwID_1</b></p>
</td>
<td>
<p><b>INF_CID_1</b></p>
</td>
<td>
<p><b>INF_CID_2</b></p>
</td>
</tr>
<tr>
<td>
<p><b>HwID_1</b></p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>0000</p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>1000</p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>1000</p>
</td>
</tr>
<tr>
<td>
<p><b>HwID_2</b></p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>0001</p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>1001</p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>1001</p>
</td>
</tr>
<tr>
<td>
<p><b>CID_1</b></p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>2000</p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>3000</p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>3100</p>
</td>
</tr>
<tr>
<td>
<p><b>CID_2</b></p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>2001</p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>3001</p>
</td>
<td>
<p>Rank 0x<i>SSGG</i>3101</p>
</td>
</tr>
</table>

 


