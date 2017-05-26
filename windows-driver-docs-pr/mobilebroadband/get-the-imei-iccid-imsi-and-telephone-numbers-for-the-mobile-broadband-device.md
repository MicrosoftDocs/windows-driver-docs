---
title: Get IMEI, ICCID, IMSI, and telephone numbers for the MB device
description: Get the IMEI, ICCID, IMSI and telephone numbers for the mobile broadband device
ms.assetid: b604d08c-7e6f-4dad-9e1d-3f24a0da5760
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Get the IMEI, ICCID, IMSI and telephone numbers for the mobile broadband device


The following properties are available for the current network device for the account:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Property of MobileBroadbandDeviceInformation to use</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>IMEI</p></td>
<td><p>MobileEquipmentId</p></td>
</tr>
<tr class="even">
<td><p>MEID</p></td>
<td><p>MobileEquipmentId</p></td>
</tr>
<tr class="odd">
<td><p>IMSI</p></td>
<td><p>SubscriberId</p></td>
</tr>
<tr class="even">
<td><p>MIN</p></td>
<td><p>SubscriberId</p></td>
</tr>
<tr class="odd">
<td><p>IRM</p></td>
<td><p>SubscriberId</p></td>
</tr>
<tr class="even">
<td><p>ICCID</p></td>
<td><p>SimIccId</p></td>
</tr>
<tr class="odd">
<td><p>Telephone Numbers</p></td>
<td><p>TelephoneNumbers (only available after network registration)</p></td>
</tr>
</tbody>
</table>

 

``` syntax
account.currentDeviceInformation.mobileEquipmentId
```

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Get%20the%20IMEI,%20ICCID,%20IMSI%20and%20telephone%20numbers%20for%20the%20mobile%20broadband%20device%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





