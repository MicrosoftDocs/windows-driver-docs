---
title: Microsoft OS 1.0 Descriptors Specification
description: Microsoft OS 1.0 Descriptors Specification
ms.date: 07/08/2019
ms.localizationpriority: medium
---

# Microsoft OS 1.0 Descriptors Specification


USB devices store standard descriptors in firmware for the device, and its interfaces and endpoints. Independent hardware vendors (IHVs) can also store class and vendor-specific descriptors. However, the types of information that these descriptors can contain is limited. IHVs typically must use Windows Update or media such as a CD to provide their users with a variety of device-specific information such as pictures, icons, custom drivers and so on.

To help IHVs address this issue, Microsoft has defined Microsoft OS descriptors. These descriptors can be used by IHVs to store in firmware much of the information that is now typically provided to customers separately. Versions of Windows that are aware of Microsoft OS descriptors use control requests to retrieve the information, and use it to install and configure the device without requiring any user interaction. This white paper provides an introduction to Microsoft OS descriptors, including a discussion of how they are stored and retrieved.

**Note:** The table of compatible and sub-compatible IDs in Appendix 1 of "Extended Compat ID OS Feature Descriptor Specification" is current as of the time the specification was written, but might have since changed. The following table contains the most recent list of compatible and sub-compatible IDs. All IDs must be eight bytes, so any unused characters are filled with NULLs.

<table border="0" cellpadding="0" cellspacing="0" class="grid" width="100%" summary="table">
<thead>
<tr align="left" valign="top">
<td>
<strong>CompatibleID</strong>
</td>
<td>
<strong>Sub-compatible ID</strong>
</td>
<td>
<strong>Description</strong>
</td>
</tr>
</thead>
<tbody>
<tr align="left" valign="top">
<td>(0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00)</td>
<td>(0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00)</td>
<td>No compatible or sub-compatible ID</td>
</tr>
<tr align="left" valign="top">
<td>"RNDIS"<br>(0x52 0x4E 0x44 0x49 0x53 0x00 0x00 0x00)</td>
<td>(0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00)</td>
<td>Remote Network Driver Interface Standard (RNDIS)</td>
</tr>
<tr align="left" valign="top">
<td>"PTP"<br>(0x50 0x54 0x50 0x00 0x00 0x00 0x00 0x00)</td>
<td>(0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00)</td>
<td>Picture Transfer Protocol (PTP)</td>
</tr>
<tr align="left" valign="top">
<td>"MTP"<br>(0x4D 0x54 0x50 0x00 0x00 0x00 0x00 0x00)</td>
<td>(0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00)</td>
<td>Media Transfer Protocol (MTP)</td>
</tr>
<tr align="left" valign="top">
<td>"XUSB20"<br>(0x58 0x55 0x53 0x42 0x32 0x30 0x00 0x00)</td>
<td>(0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00)</td>
<td>XNACC (Krypton)</td>
</tr>
<tr align="left" valign="top">
<td>"BLUTUTH"<br>(0x42 0x4C 0x55 0x54 0x55 0x54 0x48 0x00)</td>
<td>
<div class="contentTableWrapper"><table border="0" cellpadding="0" cellspacing="0" class="grid" width="100%" summary="table">
<tbody>
<tr align="left" valign="top">
<td>"11"<br>(0x31 0x31 0x00 0x00 0x00 0x00 0x00 0x00)</td>
<td>Bluetooth radios compliant with v1.1 and compatible with the Microsoft driver stack</td>
</tr>
<tr align="left" valign="top">
<td>"12"<br>(0x31 0x32 0x00 0x00 0x00 0x00 0x00 0x00)</td>
<td>Bluetooth radios compliant with v1.2 and compatible with the Microsoft driver stack</td>
</tr>
<tr align="left" valign="top">
<td>"EDR"<br>(0x45 0x44 0x52 0x00 0x00 0x00 0x00 0x00)</td>
<td>Bluetooth radios compliant with v2.0 + EDR and compatible with the Microsoft driver stack</td>
</tr>
</tbody>
</table></div>
<p>
<br>
</p>
</td>
<td>Bluetooth</td>
</tr>
<tr align="left" valign="top">
<td>"SCAN"<br>(0x53 0x43 0x41 0x4E 0x00 0x00 0x00 0x00)</td>
<td>
<p>Format as follows: 2 Letter vendor code + 1-5 ASCII characters* + 0x00</p>
<p>*ASCII restricted to uppercase letters, numbers, underscores.</p>
</td>
<td>Scan</td>
</tr>
<tr align="left" valign="top">
<td>"3DPRINT"<br>(0x33 0x44 0x50 0x52 0x49 0x4E 0x54 0x00)</td>
<td>Varies</td>
<td>MS3DPRINT G-Code 3D Printer</td>
</tr>
</tbody>
</table>

  

This information applies to Windows XP and later versions of Windows.

**Please read the license agreement before continuing.**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="text-align: center;"><strong><br />
Microsoft OS Descriptors Specification</strong><br />
</td>
</tr>
<tr class="even">
<td style="text-align: center;"><div style="font-size: 100%; border: thin inset; height: 400px; overflow: scroll; text-align: left; padding: 10px;">
<h3 id="microsoft-os-descriptor-specification-license-agreement">Microsoft OS Descriptor Specification License Agreement</h3>
<p>This is a legal agreement (“Agreement”) between you (either an individual or single entity) (“You”), and Microsoft Corporation (“Microsoft”) for the Specification.  By downloading, copying or otherwise using the Specification, You agree to be bound by the terms of this Agreement.   </p>
<p><strong>SECTION 1           DEFINITIONS.</strong></p>
<p>(a)    “Your Implementation” means Your: (i) firmware and/or hardware that implements the OS Descriptor set described in the Specification to interface with a Microsoft OS Descriptor enabled operating system, or other systems authorized by Microsoft to retrieve and use this information; and (ii) software drivers that implementing the OS Descriptor set described in the Specification to interface only in conjunction with the Windows Vista or Windows 7 operating systems.</p>
<p>(b)   “Your Licensees” mean third parties licensed by You to use the Your Implementation.</p>
<p>(c)    “Specification” means Microsoft’s OS Descriptor Specification and any accompanying materials.</p>
<p><strong>SECTION 2           GRANT OF LICENSE</strong>.</p>
<p>(a)    <strong>Copyright license</strong>.  Microsoft hereby grants to You, under Microsoft’s copyrights in the Specification, a nonexclusive, royalty-free, nontransferable, non-sublicensable, personal worldwide license to reproduce copies of the Specification internally for You and Your contractor’s use in developing Your Implementation.</p>
<p>(b)   <strong>Patent license</strong>.  Microsoft hereby grants to You a nonexclusive, royalty-free, nontransferable, worldwide license under Microsoft’s patents embodied solely within the Specification and that are owned or licensable by Microsoft to make, use, import, offer to sell, sell and distribute directly or indirectly to Your Licensees Your Implementation.  You may sublicense this patent license to Your Licensees under the same terms and conditions.</p>
<p>(c)    <strong>Reservation of Rights</strong>.  Microsoft reserves all other rights it may have in the Specification, its implementation and any intellectual property therein.  The furnishing of this document does not give You or any other entity any license to any other Microsoft patents, trademarks, copyrights or other intellectual property rights. </p>
<p><strong>SECTION 3           ADDITIONAL LIMITATIONS AND OBLIGATIONS</strong>.</p>
<p>(a)    Your license rights to the Specification are conditioned upon You not creating, modifying, or distributing your Licensed Implementation in a way that such creation, modification, or distribution may (a) create, or purport to create, obligations for Microsoft with respect to the Specification (or intellectual property therein) or (b) grant, or purport to grant, to any third party any rights or immunities to Microsoft’s intellectual property or proprietary rights in the Specification.</p>
<p>(b)    Without prejudice to any other rights, Microsoft may terminate this Agreement if You fail to comply with the terms and conditions of this Agreement. In such event You must destroy all copies of the Specification and must not further distribute the Company Implementation.</p>
<p><strong>SECTION 4           DISCLAIMER OF WARRANTIES.</strong></p>
<p>The Specification is provided "AS IS" without warranty of any kind. To the maximum extent permitted by applicable law, Microsoft further disclaims all warranties, including without limitation any implied warranties of merchantability and fitness for a particular purpose, as well as warranties of title and noninfringement. The entire risk arising out of the use or performance of the Specification remains with You.</p>
<p><strong>SECTION 5           EXCLUSION OF INCIDENTAL, CONSEQUENTIAL AND CERTAIN OTHER DAMAGES.</strong></p>
<p><strong>To the maximum extent permitted by applicable law, in no event shall Microsoft or its suppliers be liable for any consequential, incidental, direct, indirect, special, punitive, or other damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the Specification, even if Microsoft has been advised of the possibility of such damages. Because some states/jurisdictions do not allow the exclusion or limitation of liability for consequential or incidental damages, the above limitation may not apply to You.</strong></p>
<p><strong>SECTION 6            LIMITATION OF LIABILITY AND REMEDIES.</strong></p>
<p><strong>Notwithstanding any damages that You might incur for any reason whatsoever (including, without limitation, all damages referenced above and all direct or general damages), the entire liability of Microsoft and any of its suppliers under any provision of this Agreement and your exclusive remedy for all of the foregoing shall be limited to the greater of the amount actually paid by You for the Specification or U.S.$5.00. The foregoing limitations, exclusions and disclaimers shall apply to the maximum extent permitted by applicable law, even if any remedy fails its essential purpose.</strong></p>
<p><strong>SECTION 7           APPLICABLE LAW</strong>.</p>
<p>If you acquired this Specification in the United States, this Agreement is governed by the laws of the State of Washington. In respect of any dispute which may arise hereunder, You consent to the jurisdiction of the state and federal courts sitting in King County, Washington.</p>
<p><strong>SECTION 8           ASSIGNMENT.</strong></p>
<p>Neither party may assign this Agreement without prior written approval of the other party.</p>
</div>
<p><br />
<a href="https://download.microsoft.com/download/9/C/5/9C5B2167-8017-4BAE-9FDE-D599BAC8184A/OS_Desc_Ext_Prop.zip">I accept, Download</a></p></td>
</tr>
</tbody>
</table>
