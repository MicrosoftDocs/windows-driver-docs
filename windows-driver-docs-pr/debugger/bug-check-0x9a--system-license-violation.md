---
title: Bug Check 0x9A SYSTEM_LICENSE_VIOLATION
description: The SYSTEM_LICENSE_VIOLATION bug check has a value of 0x0000009A. This bug check indicates that the software license agreement has been violated.
ms.assetid: 742d864c-46f8-4d7f-8617-061c75fe833a
keywords: ["Bug Check 0x9A SYSTEM_LICENSE_VIOLATION", "SYSTEM_LICENSE_VIOLATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SYSTEM_LICENSE_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x9A: SYSTEM\_LICENSE\_VIOLATION


The SYSTEM\_LICENSE\_VIOLATION bug check has a value of 0x0000009A. This bug check indicates that the software license agreement has been violated.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SYSTEM\_LICENSE\_VIOLATION Parameters


Parameter 1 indicates the type of violation. The meaning of the other parameters depends on the value of Parameter 1.

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
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00</p></td>
<td align="left"><p><strong>0:</strong> The product should be WinNT</p>
<p><strong>1:</strong> The product should be LanmanNT or ServerNT</p></td>
<td align="left"><p>A partial serial number</p></td>
<td align="left"><p>The first two characters of the product type from the product options</p></td>
<td align="left"><p>Offline product type changes have been attempted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x01</p></td>
<td align="left"><p>The registered evaluation time from source 1</p></td>
<td align="left"><p>A partial serial number</p></td>
<td align="left"><p>The registered evaluation time from an alternate source</p></td>
<td align="left"><p>Offline changes to the Microsoft Windows evaluation unit time period have been attempted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x02</p></td>
<td align="left"><p>The status code that is associated with the open failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The setup key could not be opened.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x03</p></td>
<td align="left"><p>The status code that is associated with the key lookup failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The SetupType or SetupInProgress value from the setup key is missing, so setup mode could not be detected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x04</p></td>
<td align="left"><p>The status code that is associated with the key lookup failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The <strong>SystemPrefix</strong> value from the setup key is missing.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x05</p></td>
<td align="left"><p>(See the setup code)</p></td>
<td align="left"><p>An invalid value was found in licensed processors</p></td>
<td align="left"><p>The officially licensed number of processors</p></td>
<td align="left"><p>Offline changes to the number of licensed processors have been attempted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x06</p></td>
<td align="left"><p>The status code that is associated with the open failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The <strong>ProductOptions</strong> key could not be opened.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x07</p></td>
<td align="left"><p>The status code that is associated with the read failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The <strong>ProductType</strong> value could not be read.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x08</p></td>
<td align="left"><p>The status code that is associated with the Change Notify failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Change Notify on <strong>ProductOptions</strong> failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x09</p></td>
<td align="left"><p>The status code that is associated with the Change Notify failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Change Notify on <strong>SystemPrefix</strong> failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0A</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>An NTW system was converted to an NTS system.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0B</p></td>
<td align="left"><p>The status code that is associated with the change failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The reference of the setup key failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0C</p></td>
<td align="left"><p>The status code that is associated with the change failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The reference of the product options key failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0D</p></td>
<td align="left"><p>The status code that is associated with the failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The attempt to open <strong>ProductOptions</strong> in the worker thread failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0F</p></td>
<td align="left"><p>The status code that is associated with the failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The attempt to open the setup key failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10</p></td>
<td align="left"><p>The status code that is associated with the failure</p></td>
<td align="left"><p><strong>0:</strong> set value failed</p>
<p><strong>1:</strong> Change Notify failed</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>A failure occurred in the setup key worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x11</p></td>
<td align="left"><p>The status code that is associated with the failure</p></td>
<td align="left"><p><strong>0:</strong> set value failed</p>
<p><strong>1:</strong> Change Notify failed</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>A failure occurred in the product options key worker thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x12</p></td>
<td align="left"><p>The status code that is associated with the failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Unable to open the <strong>LicenseInfoSuites</strong> key for the suite.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x13</p></td>
<td align="left"><p>The status code that is associated with the failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Unable to query the <strong>LicenseInfoSuites</strong> key for the suite.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x14</p></td>
<td align="left"><p>The size of the memory allocation</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Unable to allocate memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x15</p></td>
<td align="left"><p>The status code that is associated with the failure</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Unable to reset the <strong>ConcurrentLimit</strong> value for the suite key.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x16</p></td>
<td align="left"><p>The status code that is associated with the failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Unable to open the license key for a suite product.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x17</p></td>
<td align="left"><p>The status code that is associated with the failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Unable to reset the <strong>ConcurrentLimit</strong> value for a suite product.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x18</p></td>
<td align="left"><p>The status code that is associated with the open failure</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Unable to start the Change Notify for the <strong>LicenseInfoSuites</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x19</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>A suite is running on a system that must be PDC.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1A</p></td>
<td align="left"><p>The status code that is associated with the failure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>A failure occurred when enumerating the suites.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1B</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Changes to the policy cache were attempted.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The Microsoft Windows operating system detects a violation of the software license agreement.

A user might have tried to change the product type of an offline system or change the trial period of an evaluation unit of Windows. For more information about the specific violation, see the parameter list.

 

 




