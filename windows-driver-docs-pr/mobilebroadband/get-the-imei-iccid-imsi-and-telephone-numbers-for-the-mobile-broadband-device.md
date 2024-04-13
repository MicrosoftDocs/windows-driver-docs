---
title: Get IMEI, ICCID, IMSI, and Telephone Numbers for the MB Device
description: Get the IMEI, ICCID, IMSI and telephone numbers for the mobile broadband device
ms.date: 04/20/2017
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


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

