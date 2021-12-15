---
title: Copyright Protection Implementation
description: Copyright Protection Implementation
keywords:
- DVD decoder minidrivers WDK , copyright protection
- decoder minidrivers WDK DVD , copyright protection
- copyright protection WDK DVD decoder
- content scrambling system WDK DVD decoder
- CSS WDK DVD decoder
- DVD decrypters WDK
- key exchange WDK DVD decoder
- decryption WDK DVD decoder
- encryption WDK DVD decoder
- cryptography WDK DVD decoder
- authentication WDK DVD decoder
ms.date: 04/20/2017
---

# Copyright Protection Implementation





Microsoft provides software that facilitates the authentication process required by the content scrambling system (CSS) scheme, thus allowing a DVD-ROM drive to authenticate and transfer keys with a DVD decrypter. Microsoft does not ship a DVD decrypter. Instead, Microsoft provides operating system code that will act as the agent to allow either hardware or software decrypters to be authenticated.

The key exchange process is initiated and controlled by the DVD navigator/splitter filter. The DVD decoder minidriver only needs to implement the properties listed in the following section. The rest is handled by other components.

Each DVD input stream receives copyright protection properties. This is true even if all DVD streams are controlled by the same hardware.

The GUID of the video port property set is [KSPROPSETID\_CopyProt](./kspropsetid-copyprot.md). The following properties are available.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-chlg-key" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_CHLG_KEY&lt;/strong&gt;](./ksproperty-dvdcopy-chlg-key.md)"><strong>KSPROPERTY_DVDCOPY_CHLG_KEY</strong></a></p></td>
<td><p>Both get and set are supported on this property. A get property requests the decoder to provide its bus challenge key. A set property provides the decoder with the bus challenge key from the DVD drive. The data passed in this property is a structure of type <a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_chlgkey" data-raw-source="[&lt;strong&gt;KS_DVDCOPY_CHLGKEY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_chlgkey)"><strong>KS_DVDCOPY_CHLGKEY</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-dvd-key1" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_DVD_KEY1&lt;/strong&gt;](./ksproperty-dvdcopy-dvd-key1.md)"><strong>KSPROPERTY_DVDCOPY_DVD_KEY1</strong></a></p></td>
<td><p>Set-only property. This property provides the DVD drive bus key 1 to the decoder. The data passed is a structure of type <a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_buskey" data-raw-source="[&lt;strong&gt;KS_DVDCOPY_BUSKEY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_buskey)"><strong>KS_DVDCOPY_BUSKEY</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-dec-key2" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_DEC_KEY2&lt;/strong&gt;](./ksproperty-dvdcopy-dec-key2.md)"><strong>KSPROPERTY_DVDCOPY_DEC_KEY2</strong></a></p></td>
<td><p>Get-only property. This property requests that the decoder's bus key 2 be transferred to the DVD drive. The data passed is a structure of type <a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_buskey" data-raw-source="[&lt;strong&gt;KS_DVDCOPY_BUSKEY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_buskey)"><strong>KS_DVDCOPY_BUSKEY</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-title-key" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_TITLE_KEY&lt;/strong&gt;](./ksproperty-dvdcopy-title-key.md)"><strong>KSPROPERTY_DVDCOPY_TITLE_KEY</strong></a></p></td>
<td><p>Set-only property. This provides Title Key from Current Content. The key is a structure of type <a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_titlekey" data-raw-source="[&lt;strong&gt;KS_DVDCOPY_TITLEKEY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_titlekey)"><strong>KS_DVDCOPY_TITLEKEY</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-disc-key" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_DISC_KEY&lt;/strong&gt;](./ksproperty-dvdcopy-disc-key.md)"><strong>KSPROPERTY_DVDCOPY_DISC_KEY</strong></a></p></td>
<td><p>Set-only property. This provides Disc Key.</p>
<div>
 
</div>
The key is a structure of type <a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_disckey" data-raw-source="[&lt;strong&gt;KS_DVDCOPY_DISCKEY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_disckey)"><strong>KS_DVDCOPY_DISCKEY</strong></a>.</td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-copy-macrovision" data-raw-source="[&lt;strong&gt;KSPROPERTY_COPY_MACROVISION&lt;/strong&gt;](./ksproperty-copy-macrovision.md)"><strong>KSPROPERTY_COPY_MACROVISION</strong></a></p></td>
<td><p>Set-only property. The key is a structure of type <a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_copy_macrovision" data-raw-source="[&lt;strong&gt;KS_COPY_MACROVISION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_copy_macrovision)"><strong>KS_COPY_MACROVISION</strong></a>. This is the analog NTSC video stream and soon will handle NTSC macrovision properties.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-region" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_REGION&lt;/strong&gt;](./ksproperty-dvdcopy-region.md)"><strong>KSPROPERTY_DVDCOPY_REGION</strong></a></p></td>
<td><p>Get-only property. The DVD minidriver fits into exactly one region bit. The key is a structure of type <a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_region" data-raw-source="[&lt;strong&gt;KS_DVDCOPY_REGION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_region)"><strong>KS_DVDCOPY_REGION</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-set-copy-state" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_SET_COPY_STATE&lt;/strong&gt;](./ksproperty-dvdcopy-set-copy-state.md)"><strong>KSPROPERTY_DVDCOPY_SET_COPY_STATE</strong></a></p></td>
<td><p>Get- and set-only properties. The key is a structure of type <a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_set_copy_state" data-raw-source="[&lt;strong&gt;KS_DVDCOPY_SET_COPY_STATE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_set_copy_state)"><strong>KS_DVDCOPY_SET_COPY_STATE</strong></a>. This property uses</p>
<p>KS_DVDCOPYSTATE_AUTHENTICATION_NOT_REQUIRED,</p>
<p>KS_DVDCOPYSTATE_AUTHENTICATION_REQUIRED,</p>
<p>KS_DVDCOPYSTATE_INITIALIZE, and</p>
<p>KS_DVDCOPYSTATE_INITIALIZE_TITLE.</p></td>
</tr>
</tbody>
</table>

 

The following sequence is repeated on every open DVD input pin on the decoder. The decoder receives the keys in the following sequence:

Get KSPROPERTY\_DVDCOPY\_CHLG\_KEY

Set KSPROPERTY\_DVDCOPY\_DVD\_KEY1

Set KSPROPERTY\_DVDCOPY\_CHLG\_KEY

Get KSPROPERTY\_DVDCOPY\_DEC\_KEY2

Set KSPROPERTY\_DVDCOPY\_DISC\_KEY

Then, the following keys are received:

Get KSPROPERTY\_DVDCOPY\_CHLG\_KEY

Set KSPROPERTY\_DVDCOPY\_DVD\_KEY1

Set KSPROPERTY\_DVDCOPY\_CHLG\_KEY

Get KSPROPERTY\_DVDCOPY\_DEC\_KEY2

Set KSPROPERTY\_DVDCOPY\_TITLE\_KEY

This sequence also is repeated for every open DVD input pin on the decoder. It may occur at any time after a DVD disc key is successfully established and may occur more than once per disc key. Whenever a sector containing a Title Key is read, the authentication process must be successfully completed. If authentication fails, the read is blocked and a corresponding error message is returned.

