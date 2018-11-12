---
title: SECURITY\_FLAG\_QUALIFIERS
description: SECURITY\_FLAG\_QUALIFIERS
ms.assetid: d5b4c3a6-1e05-497a-a0a6-be7908e61fec
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SECURITY\_FLAG\_QUALIFIERS


## <span id="ddk_security_flag_qualifiers_kr"></span><span id="DDK_SECURITY_FLAG_QUALIFIERS_KR"></span>


The SECURITY\_FLAG\_QUALIFIERS WMI property qualifier corresponds to flag values that indicate the security requirements of a target. This information is used in the Internet Key Exchange (IKE) of the IPsec authentication negotiation. These flags are derived from the portal security bitmap definition that is described in the *Internet Storage Name Service (iSNS)* specification that the Internet Engineering Task Force (IETF) publishes.

The following table describes the values that are associated with SECURITY\_FLAG\_QUALIFIERS property qualifier.

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
<td align="left"><p>ISCSI_SECURITY_FLAG_TUNNEL_MODE_PREFERRED</p></td>
<td align="left"><p>The target requests tunnel mode. The HBA initiator should log on to the target by using IPsec tunnel mode. When this value is not set, the IPsec tunnel mode is not required.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISCSI_SECURITY_FLAG_TRANSPORT_MODE_PREFERRED</p></td>
<td align="left"><p>The target requests transport mode. The HBA initiator should log on to targets by using IPsec transport mode. When this value is not set, the IPsec transport mode is not required.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISCSI_SECURITY_FLAG_PFS_ENABLED</p></td>
<td align="left"><p>The HBA initiator should log on to the target with perfect forward secrecy (PFS) mode enabled. When this value is not set, the initiator HBA should make the session connection with PFS mode disabled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISCSI_SECURITY_FLAG_AGGRESSIVE_MODE_ENABLED</p></td>
<td align="left"><p>Aggressive mode is enabled on the target, and the HBA initiator should log on to targets with aggressive mode enabled. When this value is not set, the HBA initiator should make the session connection with aggressive mode disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISCSI_SECURITY_FLAG_MAIN_MODE_ENABLED</p></td>
<td align="left"><p>Main mode is enabled on the target, and the HBA initiator should log in to targets with main mode enabled. When not set, the HBA initiator should make the session connection with main mode disabled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISCSI_SECURITY_FLAG_IKE_IPSEC_ENABLED</p></td>
<td align="left"><p>IKE/IPsec is enabled on the target, and the HBA initiator should log on to targets with the IKE/IPsec protocol enabled. When this value is not set, IKE/IPsec is disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISCSI_SECURITY_FLAG_VALID</p></td>
<td align="left"><p>The iSCSI security flags specified in this bitmask are valid. When this value is not set, security flags are not specified.</p></td>
</tr>
</tbody>
</table>

 

 

 





