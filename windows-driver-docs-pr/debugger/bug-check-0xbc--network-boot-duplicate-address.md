---
title: Bug Check 0xBC NETWORK_BOOT_DUPLICATE_ADDRESS
description: The NETWORK_BOOT_DUPLICATE_ADDRESS bug check has a value of 0x000000BC. This indicates that a duplicate IP address was assigned to this machine while booting off a network.
ms.assetid: 54c45e73-7054-4dba-abe4-91f5f5a064a4
keywords: ["Bug Check 0xBC NETWORK_BOOT_DUPLICATE_ADDRESS", "NETWORK_BOOT_DUPLICATE_ADDRESS"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- NETWORK_BOOT_DUPLICATE_ADDRESS
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xBC: NETWORK\_BOOT\_DUPLICATE\_ADDRESS


The NETWORK\_BOOT\_DUPLICATE\_ADDRESS bug check has a value of 0x000000BC. This indicates that a duplicate IP address was assigned to this machine while booting off a network.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## NETWORK\_BOOT\_DUPLICATE\_ADDRESS Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>The IP address, shown as a DWORD. An address of the form <em>aa.bb.cc.dd</em> will appear as 0xDDCCBBAA.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The hardware address of the other machine. (For an Ethernet connection, see the following note.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The hardware address of the other machine. (For an Ethernet connection, see the following note.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The hardware address of the other machine. (For an Ethernet connection, this will be zero.)</p></td>
</tr>
</tbody>
</table>

 

**Note**   When Parameter 4 equals zero, this indicates an Ethernet connection. In that case, the MAC address will be stored in Parameter 2 and Parameter 3. An Ethernet MAC address of the form *aa-bb-cc-dd-ee-ff* will cause Parameter 2 to equal 0xAABBCCDD, and Parameter 3 to equal 0xEEFF0000.

 

Cause
-----

This error indicates that when TCP/IP sent out an ARP for its IP address, it got a response from another machine indicating a duplicate IP address.

When Windows is booting off a network, this is a fatal error.

 

 




