---
title: WIA\_IPS\_MULTI\_FEED
description: The WIA\_IPS\_MULTI\_FEED property is used to configure the action to be performed by the WIA minidriver when a multiple feed condition is detected at the device. The WIA minidriver creates and maintains this property.
ms.assetid: 8BD92273-218B-4381-BCAF-ED9D227B6B94
keywords: ["WIA_IPS_MULTI_FEED Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_MULTI_FEED
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA\_IPS\_MULTI\_FEED


The **WIA\_IPS\_MULTI\_FEED** property is used to configure the action to be performed by the WIA minidriver when a multiple feed condition is detected at the device. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_MULTI\_FEED** property.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_MULTI_FEED_DETECT_DISABLED</p></td>
<td><p>Multi-feed detection is disabled. This is the required default value if the property is supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_MULTI_FEED_DETECT_STOP_ERROR</p></td>
<td><p>The device detects multi-feed, stops scanning, sets the MULTIPLE_FEED bit for [<strong>WIA_DPS_DOCUMENT_HANDLING_STATUS</strong>](wia-dps-document-handling-status.md), and returns WIA_ERROR_MULTI_FEED to [<strong>IWiaMiniDrv::drvAcquireItemData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543956).</p></td>
</tr>
<tr class="odd">
<td><p>WIA_MULTI_FEED_DETECT_STOP_SUCCESS</p></td>
<td><p>The device detects multi-feed, stops scanning, sets the MULTIPLE_FEED bit for [<strong>WIA_DPS_DOCUMENT_HANDLING_STATUS</strong>](wia-dps-document-handling-status.md), and [<strong>IWiaMiniDrv::drvAcquireItemData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543956) returns and does not fail because of the multi-feed.</p></td>
</tr>
<tr class="even">
<td><p>WIA_MULTI_FEED_DETECT_CONTINUE</p></td>
<td><p>The device detects multi-feed, beeps or produces an audible or visible signal at the hardware device (recommended but not required), and continues scanning.</p></td>
</tr>
</tbody>
</table>

 

This property is optional, and is valid only for the Feeder data source item (represented in the [**WIA\_IPA\_ITEM\_CATEGORY**](wia-ipa-item-category.md) property as WIA\_CATEGORY\_FEEDER).

When the WIA minidriver sets the MULTIPLE\_FEED bit for the [**WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS**](wia-dps-document-handling-status.md) property, the minidriver should clear this bit (flag) as soon as the minidriver detects that the feeder is unloaded, is reloaded, or a new scan job begins.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_MULTI_FEED%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




