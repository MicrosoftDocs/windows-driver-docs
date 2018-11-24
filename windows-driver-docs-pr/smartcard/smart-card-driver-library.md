---
title: Smart Card Driver Library
description: Smart Card Driver Library
ms.assetid: 12f67a8d-9281-4f79-88c0-e1c9dff5a05d
keywords:
- smart card drivers WDK , library
- library WDK smart card
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Smart Card Driver Library


## <span id="_ntovr_smart_card_driver_library"></span><span id="_NTOVR_SMART_CARD_DRIVER_LIBRARY"></span>


Microsoft provides a driver library that contains a set of routines that standardize most of the functions that a smart card reader driver must perform. Vendor-supplied reader drivers must call these routines to perform the following actions:

-   To create device names that the smart card resource manager requires

-   To check parameters and detect errors for IOCTL calls

-   To parse ATR-strings and convert parameters

-   To support the T=0 and T=1 ISO protocols

-   To support the inverse convention

-   To log events

-   To synchronize access to the driver

The [WDM Smart Card Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff549046) section, lists the driver library routines and identifies which routine performs each action.

The driver library processes most of the IOCTL requests that the resource manager sends to the reader driver. The [Smart Card Driver IOCTLs](https://msdn.microsoft.com/library/windows/hardware/ff548988) section, lists the IOCTLs that the driver library processes on behalf of the reader driver.

The following files are used by the smart card driver library and by drivers that call smart card driver library routines.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">File</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>Smclib.h</em></p></td>
<td align="left"><p>Contains declarations and definitions required by all drivers that call smart card library routines.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Smcnt.h</em></p></td>
<td align="left"><p>Contains declarations and definitions required by a WDM driver that calls smart card library routines.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Winsmcrd.h</em></p></td>
<td align="left"><p>Global header file for all smart card reader drivers and smart card-aware applications.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Smclib.sys</em></p></td>
<td align="left"><p>The library&#39;s binary file for WDM drivers.</p></td>
</tr>
</tbody>
</table>

 

 

 





