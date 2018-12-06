---
title: Definitions
description: Definitions
ms.assetid: 904b7dd3-472d-4286-81c1-2af1109e2139
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Definitions


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IEEE 1667</p></td>
<td align="left"><p>A standard protocol for secure authentication and creation of trust between a secure host and a directly attached Transient Storage Device (TSD), such as a USB flash drive, portable hard drive, or cellular phone.&quot;</p>
<p>For more information, see <a href="http://go.microsoft.com/fwlink/p/?linkid=127997" data-raw-source="[http://standards.ieee.org/announcements/pr_IEEE1667_new.html](http://go.microsoft.com/fwlink/p/?linkid=127997)">http://standards.ieee.org/announcements/pr_IEEE1667_new.html</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1667 authentication silo</p></td>
<td align="left"><p>A 1667 silo whose function provides either authentication of host to device, device to host, or both.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1667 standard authentication silo</p></td>
<td align="left"><p>A standard certificate or password authentication silo defined in the base 1667 specification for which Microsoft is shipping drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1667 USB Flash Device (UFD)</p></td>
<td align="left"><p>USB flash device implementing the 1667 command set according to the IEEE 1667 specification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Third-party authentication silo</p></td>
<td align="left"><p>Silo not defined in the base set of 1667 specified standard authentication silos implementing the authentication function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>third-party silo</p></td>
<td align="left"><p>Silo not contained in the set of 1667 specified standard silos. The function is proprietary and not documented in the IEEE 1667 base standard. Sometimes referred to as an &quot;unknown&quot; silo.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Addressable command target (ACT)</p></td>
<td align="left"><p>Independent unit of access that accepts 1667 commands and optionally provides access to user data (see Logical Unit). According to the 1667 specification, an ACT is not required to provide a user data access function. A 1667 device may implement one or more ACTs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Authentication</p></td>
<td align="left"><p>(As it relates to IEEE 1667) the act of verifying the veracity of the identity claimed by either the host or the device. In the password authentication case, a secret password established by the user of the device is the credential that serves this purpose. In the certificate authentication case, possession of the private key must be proven by successfully decrypting a random stream of bytes encrypted with the paired public key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Authorization</p></td>
<td align="left"><p>Indication that concomitant access to the governed resource is authorized after a device or host identity has been authenticated. Host-to-device authentication governs authorized access to the user data portion of the associated ACT, whereas successful device-to-host authentication authorizes the connected data channel between the device and the host.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Certificate silo (Cert Silo)</p></td>
<td align="left"><p>Authentication silo that uses certificates and associated public-private key pairs as the basis for authentication.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Legacy mass storage (or Legacy UFD)</p></td>
<td align="left"><p>A USB mass storage (or USB flash device) not implementing the 1667 command set.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Logical unit (LUN)</p></td>
<td align="left"><p>Independent unit of access for user data contained on a device that is exposed as a single disk on the host system. A LUN is synonymous with a data-bearing 1667 ACT currently in the authorized state.</p>
<p>Some UFDs are multi-LUN-capable.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Password silo (PW Silo)</p></td>
<td align="left"><p>Authentication silo using pass-phrase matching as the basis for authentication.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Removable media bit (RMB)</p></td>
<td align="left"><p>A bit contained in the device response to the SCSI INQUIRY command (0x12) that indicates whether the media is removable (RMB=1) or fixed (RMB=0). Not to be confused with the Removable field of the DEVICE_CAPABILITIES used to indicate whether a PDO represents a hot-pluggable device, RMB refers to a property of the media rather than the device itself. Media for which RMB=1 is treated differently by the system than show media with RMB=0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Silo</p></td>
<td align="left"><p>Independent functional unit that responds to 1667 commands. To each ACT one or more silos may be attached. A 1667 silo command may be addressed to a particular ACT index and silo index.</p></td>
</tr>
</tbody>
</table>

 

 

 




