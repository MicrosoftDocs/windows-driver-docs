---
title: KSPROPERTY\_DVDCOPY\_DVD\_KEY1
description: The KSPROPERTY\_DVDCOPY\_DVD\_KEY1 property retrieves the first bus key that is provided later to the decoder as part of the DVD copyright protection authentication process.
keywords: ["KSPROPERTY_DVDCOPY_DVD_KEY1 Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDCOPY_DVD_KEY1
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DVDCOPY\_DVD\_KEY1


The KSPROPERTY\_DVDCOPY\_DVD\_KEY1 property retrieves the first bus key that is provided later to the decoder as part of the DVD copyright protection authentication process.

## <span id="ddk_ksproperty_dvdcopy_dvd_key1_ks"></span><span id="DDK_KSPROPERTY_DVDCOPY_DVD_KEY1_KS"></span>


### Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_buskey" data-raw-source="[&lt;strong&gt;KS_DVDCOPY_BUSKEY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_buskey)"><strong>KS_DVDCOPY_BUSKEY</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KS\_DVDCOPY\_BUSKEY structure that describes the DVD decoders first bus key.

## Remarks

For more information about the first bus key, see [DVD Copyright Protection](./dvd-copyright-protection.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KS\_DVDCOPY\_BUSKEY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_buskey)

