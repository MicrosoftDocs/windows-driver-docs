---
title: WIA\_IPS\_MULTI\_FEED\_SENSITIVITY
description: The WIA\_IPS\_MULTI\_FEED\_SENSITIVITY property is used to change the multi-feed detection trigger to a lower or higher value between the lowest and highest sensitivity supported by the device. The WIA minidriver creates and maintains this property.
ms.assetid: 04AC211B-89D5-417F-9089-1E3F30E22211
keywords: ["WIA_IPS_MULTI_FEED_SENSITIVITY Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_MULTI_FEED_SENSITIVITY
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_MULTI\_FEED\_SENSITIVITY


The **WIA\_IPS\_MULTI\_FEED\_SENSITIVITY** property is used to change the multi-feed detection trigger to a lower or higher value between the lowest and highest sensitivity supported by the device. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

This property is optional, and is valid only for the Feeder data source item (represented in the [**WIA\_IPA\_ITEM\_CATEGORY**](wia-ipa-item-category.md) property as WIA\_CATEGORY\_FEEDER) when [**WIA\_IPS\_MULTI\_FEED**](wia-ips-multi-feed.md) is supported with at least one other value besides WIA\_MULTI\_FEED\_DETECT\_DISABLED.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





