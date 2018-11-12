---
title: Bug Check 0xBB NETWORK_BOOT_INITIALIZATION_FAILED
description: The NETWORK_BOOT_INITIALIZATION_FAILED bug check has a value of 0x000000BB. This indicates that Windows failed to successfully boot off a network.
ms.assetid: 1cc86ca0-437d-4a26-90ed-76f122c522ef
keywords: ["Bug Check 0xBB NETWORK_BOOT_INITIALIZATION_FAILED", "NETWORK_BOOT_INITIALIZATION_FAILED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- NETWORK_BOOT_INITIALIZATION_FAILED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xBB: NETWORK\_BOOT\_INITIALIZATION\_FAILED


The NETWORK\_BOOT\_INITIALIZATION\_FAILED bug check has a value of 0x000000BB. This indicates that Windows failed to successfully boot off a network.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## NETWORK\_BOOT\_INITIALIZATION\_FAILED Parameters


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
<td align="left"><p>The part of network initialization that failed. Possible values are:</p>
<p><strong>1:</strong> Failure while updating the registry.</p>
<p><strong>2:</strong> Failure while starting the network stack. Windows sends IOCTLs to the redirector and datagram receiver, then waits for the redirector to be ready. If it is not ready within a certain period of time, this error is issued.</p>
<p><strong>3:</strong> Failure while sending the DHCP IOCTL to TCP. This is how Windows informs the transport of its IP address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The failure status</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This error is caused when Windows is booting off a network, and a critical function fails during I/O initialization.

 

 




