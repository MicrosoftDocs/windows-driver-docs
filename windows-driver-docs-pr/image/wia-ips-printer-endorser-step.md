---
title: WIA\_IPS\_PRINTER\_ENDORSER\_STEP
description: By default the imprinter/endorser imprints or endorses on each document page that is scanned.
ms.assetid: A4455204-6502-4BE7-9EE3-B5616089FA05
keywords: ["WIA_IPS_PRINTER_ENDORSER_STEP Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_STEP
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_PRINTER\_ENDORSER\_STEP


By default the imprinter/endorser imprints or endorses on each document page that is scanned. This mandatory default behavior can be changed by the client by using the **WIA\_IPS\_PRINTER\_ENDORSER\_STEP** property. For example, the client application can set the current value to 2 to have every other scanned page imprinted/endorsed (0, 2, 4, 6, ...). The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

The mandatory default value for the **WIA\_IPS\_PRINTER\_ENDORSER\_STEP** property is 1 (each page). A value of 0 is invalid.

As for most WIA\_PROP\_RANGE properties, the WIA minidriver can implement a range containing one single value, minimum equal with maximum and a step value of zero.

This property must be supported by all Imprinter/Endorser data source items. The value of 1 (each page) is required.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PRINTER_ENDORSER_STEP%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




