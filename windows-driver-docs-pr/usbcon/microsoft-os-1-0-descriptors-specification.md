---
title: Microsoft OS 1.0 Descriptors Specification
description: Microsoft OS 1.0 Descriptors Specification
ms.date: 02/07/2023
---

# Microsoft OS 1.0 Descriptors Specification

USB devices store standard descriptors in firmware for the device, and its interfaces and endpoints. Independent hardware vendors (IHVs) can also store class and vendor-specific descriptors. However, the types of information that these descriptors can contain is limited. IHVs typically must use Windows Update or media such as a CD to provide their users with a variety of device-specific information such as pictures, icons, custom drivers and so on.

To help IHVs address this issue, Microsoft has defined Microsoft OS descriptors. These descriptors can be used by IHVs to store in firmware much of the information that is now typically provided to customers separately. Versions of Windows that are aware of Microsoft OS descriptors use control requests to retrieve the information, and use it to install and configure the device without requiring any user interaction. This white paper provides an introduction to Microsoft OS descriptors, including a discussion of how they are stored and retrieved.

> [!NOTE]
> The table of compatible and sub-compatible IDs in Appendix 1 of "Extended Compat ID OS Feature Descriptor Specification" is current as of the time the specification was written, but might have since changed. The following table contains the most recent list of compatible and sub-compatible IDs. All IDs must be eight bytes, so any unused characters are filled with NULLs.

| CompatibleID | Sub-compatible ID | Description |
|---|---|---|
| (0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00) | (0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00) | No compatible or sub-compatible ID |
| "RNDIS"<br/>(0x52 0x4E 0x44 0x49 0x53 0x00 0x00 0x00) | (0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00) | Remote Network Driver Interface Standard (RNDIS) |
| "PTP"<br/>(0x50 0x54 0x50 0x00 0x00 0x00 0x00 0x00) | (0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00) | Picture Transfer Protocol (PTP) |
| "MTP"<br/>(0x4D 0x54 0x50 0x00 0x00 0x00 0x00 0x00) | (0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00) | Media Transfer Protocol (MTP) |
| "XUSB20"<br/>(0x58 0x55 0x53 0x42 0x32 0x30 0x00 0x00) | (0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00) | XNACC (Krypton) |
| "BLUTUTH"<br/>(0x42 0x4C 0x55 0x54 0x55 0x54 0x48 0x00) | "11"(0x31 0x31 0x00 0x00 0x00 0x00 0x00 0x00) | Bluetooth radios compliant with v1.1 and compatible with the Microsoft driver stack |
| "BLUTUTH"<br/>(0x42 0x4C 0x55 0x54 0x55 0x54 0x48 0x00) | "12"(0x31 0x32 0x00 0x00 0x00 0x00 0x00 0x00) | Bluetooth radios compliant with v1.2 and compatible with the Microsoft driver stack |
| "BLUTUTH"<br/>(0x42 0x4C 0x55 0x54 0x55 0x54 0x48 0x00) | "EDR"(0x45 0x44 0x52 0x00 0x00 0x00 0x00 0x00) | Bluetooth radios compliant with v2.0 + EDR and compatible with the Microsoft driver stack |
| "SCAN"<br/>(0x53 0x43 0x41 0x4E 0x00 0x00 0x00 0x00) | Format as follows: 2 Letter vendor code + 1-5 ASCII characters\* + 0x00<br/><br/>\*ASCII restricted to uppercase letters, numbers, underscores. | Scan |
| "3DPRINT"<br/>(0x33 0x44 0x50 0x52 0x49 0x4E 0x54 0x00) | Varies | MS3DPRINT G-Code 3D Printer |

This information applies to Windows XP and later versions of Windows.

Please read the license agreement before continuing.

## Microsoft OS Descriptors Specification

### Microsoft OS Descriptor Specification License Agreement

This is a legal agreement ("Agreement") between you (either an individual or single entity) ("You"), and Microsoft Corporation ("Microsoft") for the Specification.  By downloading, copying or otherwise using the Specification, You agree to be bound by the terms of this Agreement.

#### SECTION 1 &emsp;&emsp;&emsp; DEFINITIONS

(a)&ensp;"Your Implementation" means Your: (i) firmware and/or hardware that implements the OS Descriptor set described in the Specification to interface with a Microsoft OS Descriptor enabled operating system, or other systems authorized by Microsoft to retrieve and use this information; and (ii) software drivers that implementing the OS Descriptor set described in the Specification to interface only in conjunction with the Windows Vista or Windows 7 operating systems.

(b)&ensp;"Your Licensees" means third parties licensed by You to use the Your Implementation.

(c)&ensp;"Specification" means Microsoft's OS Descriptor Specification and any accompanying materials.

#### SECTION 2 &emsp;&emsp;&emsp; GRANT OF LICENSE

(a)&ensp;**Copyright license**. Microsoft hereby grants to You, under Microsoft's copyrights in the Specification, a nonexclusive, royalty-free, nontransferable, non-sublicensable, personal worldwide license to reproduce copies of the Specification internally for You and Your contractor's use in developing Your Implementation.

(b)&ensp;**Patent license**. Microsoft hereby grants to You a nonexclusive, royalty-free, nontransferable, worldwide license under Microsoft's patents embodied solely within the Specification and that are owned or licensable by Microsoft to make, use, import, offer to sell, sell and distribute directly or indirectly to Your Licensees Your Implementation. You may sublicense this patent license to Your Licensees under the same terms and conditions.

(c)&ensp;**Reservation of Rights**. Microsoft reserves all other rights it may have in the Specification, its implementation and any intellectual property therein. The furnishing of this document does not give You or any other entity any license to any other Microsoft patents, trademarks, copyrights or other intellectual property rights.

#### SECTION 3 &emsp;&emsp;&emsp; ADDITIONAL LIMITATIONS AND OBLIGATIONS

(a)&ensp;Your license rights to the Specification are conditioned upon You not creating, modifying, or distributing your Licensed Implementation in a way that such creation, modification, or distribution may (a) create, or purport to create, obligations for Microsoft with respect to the Specification (or intellectual property therein) or (b) grant, or purport to grant, to any third party any rights or immunities to Microsoft's intellectual property or proprietary rights in the Specification.

(b)&ensp;Without prejudice to any other rights, Microsoft may terminate this Agreement if You fail to comply with the terms and conditions of this Agreement. In such event You must destroy all copies of the Specification and must not further distribute the Company Implementation.

#### SECTION 4 &emsp;&emsp;&emsp; DISCLAIMER OF WARRANTIES

The Specification is provided "AS IS" without warranty of any kind. To the maximum extent permitted by applicable law, Microsoft further disclaims all warranties, including without limitation any implied warranties of merchantability and fitness for a particular purpose, as well as warranties of title and noninfringement. The entire risk arising out of the use or performance of the Specification remains with You.

#### SECTION 5 &emsp;&emsp;&emsp; EXCLUSION OF INCIDENTAL, CONSEQUENTIAL AND CERTAIN OTHER DAMAGES

**To the maximum extent permitted by applicable law, in no event shall Microsoft or its suppliers be liable for any consequential, incidental, direct, indirect, special, punitive, or other damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the Specification, even if Microsoft has been advised of the possibility of such damages. Because some states/jurisdictions do not allow the exclusion or limitation of liability for consequential or incidental damages, the above limitation may not apply to You.**

#### SECTION 6 &emsp;&emsp;&emsp; LIMITATION OF LIABILITY AND REMEDIES

**Notwithstanding any damages that You might incur for any reason whatsoever (including, without limitation, all damages referenced above and all direct or general damages), the entire liability of Microsoft and any of its suppliers under any provision of this Agreement and your exclusive remedy for all of the foregoing shall be limited to the greater of the amount actually paid by You for the Specification or U.S.$5.00\. The foregoing limitations, exclusions and disclaimers shall apply to the maximum extent permitted by applicable law, even if any remedy fails its essential purpose.**

#### SECTION 7 &emsp;&emsp;&emsp; APPLICABLE LAW

If you acquired this Specification in the United States, this Agreement is governed by the laws of the State of Washington. In respect of any dispute which may arise hereunder, You consent to the jurisdiction of the state and federal courts sitting in King County, Washington.

#### SECTION 8 &emsp;&emsp;&emsp; ASSIGNMENT

Neither party may assign this Agreement without prior written approval of the other party.

**[I accept, download the file](https://download.microsoft.com/download/9/C/5/9C5B2167-8017-4BAE-9FDE-D599BAC8184A/OS_Desc_Ext_Prop.zip)**
