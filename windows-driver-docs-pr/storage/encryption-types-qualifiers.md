---
title: ENCRYPTION\_TYPES\_QUALIFIERS
description: ENCRYPTION\_TYPES\_QUALIFIERS
ms.assetid: a1caedb8-18ab-4810-ac46-691925df250e
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 

 





