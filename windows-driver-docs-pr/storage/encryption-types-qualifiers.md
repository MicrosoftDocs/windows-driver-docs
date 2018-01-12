---
title: ENCRYPTION\_TYPES\_QUALIFIERS
description: ENCRYPTION\_TYPES\_QUALIFIERS
ms.assetid: a1caedb8-18ab-4810-ac46-691925df250e
---

# ENCRYPTION\_TYPES\_QUALIFIERS


## <span id="ddk_encryption_types_qualifiers_kr"></span><span id="DDK_ENCRYPTION_TYPES_QUALIFIERS_KR"></span>


The ENCRYPTION\_TYPES\_QUALIFIERS WMI property qualifier corresponds to a group of values that indicate what forms of encryption the HBA supports.

The following table describes the values that are associated with the ENCRYPTION\_TYPES\_QUALIFIERS property qualifier.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Symbolic constant</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ISCSI_ENCRYPT_NONE</p></td>
<td align="left"><p>The host bus adapter (HBA) does not support any form of encryption or authentication.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISCSI_ENCRYPT_3DES_HMAC_SHA1</p></td>
<td align="left"><p>The HBA supports 3DES HMAC/SHA1 encryption.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISCSI_ENCRYPT_AES_CTR</p></td>
<td align="left"><p>The HBA supports AES-CTR/CBC-MAC encryption with XCBC.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ENCRYPTION_TYPES_QUALIFIERS%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




