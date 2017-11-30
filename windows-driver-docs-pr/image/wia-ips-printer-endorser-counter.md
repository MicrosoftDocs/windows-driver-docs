---
title: WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER
description: The WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER property is used to configure the starting value and incrementing step for the imprinter/endorser counter at the beginning of a new WIA application session. The WIA minidriver creates and maintains this property.
ms.assetid: 3475A0DF-58EA-4B05-96EA-5BBE44655DB0
keywords: ["WIA_IPS_PRINTER_ENDORSER_COUNTER Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_COUNTER
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

# WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER


The **WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER** property is used to configure the starting value and incrementing step for the imprinter/endorser counter at the beginning of a new WIA application session. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

The mandatory default value for the **WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER** property is 0 (first page).

The range step value describes the increment value for the printer/endorser counter value (the minidriver increments this value after each document page that gets scanned). This counter step has a different purpose and should not be confused with the step configurable through the [**WIA\_IPS\_PRINTER\_ENDORSER\_STEP**](wia-ips-printer-endorser-step.md) property.

This property is required to be supported by all Imprinter/Endorser data source items. The value of 0 (first page) is required.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PRINTER_ENDORSER_COUNTER%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




