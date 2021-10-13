---
title: Microsoft OS 2.0 Descriptors Specification
description: Microsoft OS 2.0 Descriptors Specification
ms.date: 07/08/2019
ms.localizationpriority: medium
---

# Microsoft OS 2.0 Descriptors Specification

This document defines and describes the implementation of version 2.0 of the Microsoft OS Descriptors. The goal of Microsoft OS 2.0 Descriptors is to address the limitations and reliability problems with version 1.0 of OS descriptors and enable new Windows-specific functionality for USB devices.

This information applies to the following operating systems:

  - Windows 10
  - Windows 8.1 Preview

**Please read the license agreement before continuing.**

<table>
<colgroup>
<col />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><br />
Microsoft OS Descriptors Specification</strong><br />
</td>
</tr>
<tr class="even">
<td><div>
<h3 id="microsoft-os-descriptor-specification-license-agreement">Microsoft OS Descriptor Specification License Agreement</h3>
<p>This is a legal agreement (“Agreement”) between you (either an individual or single entity) (“You”), and Microsoft Corporation (“Microsoft”) for the Specification.  By downloading, copying or otherwise using the Specification, You agree to be bound by the terms of this Agreement.   </p>
<p><strong>SECTION 1           DEFINITIONS.</strong></p>
<p>(a)   “Your Implementation” means Your: (i) firmware and/or hardware that implements the OS Descriptor set described in the Specification to interface with a Microsoft OS Descriptor enabled operating system, or other systems authorized by Microsoft to retrieve and use this information; and (ii) software drivers that implementing the OS Descriptor set described in the Specification to interface only in conjunction with the Windows 8.1.</p>
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
<a href="https://download.microsoft.com/download/3/5/6/3563ED4A-F318-4B66-A181-AB1D8F6FD42D/MS_OS_2_0_desc.docx">I accept, Download</a></p></td>
</tr>
</tbody>
</table>
