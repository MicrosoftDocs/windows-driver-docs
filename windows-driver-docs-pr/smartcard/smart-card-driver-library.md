---
title: Smart Card Driver Library
description: Smart Card Driver Library
ms.assetid: 12f67a8d-9281-4f79-88c0-e1c9dff5a05d
keywords: ["smart card drivers WDK , library", "library WDK smart card"]
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
<td align="left"><p>The library's binary file for WDM drivers.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Smart%20Card%20Driver%20Library%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




