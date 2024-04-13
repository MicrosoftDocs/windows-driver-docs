---
title: Bug Check 0xBB NETWORK_BOOT_INITIALIZATION_FAILED
description: The NETWORK_BOOT_INITIALIZATION_FAILED bug check has a value of 0x000000BB. This indicates that Windows failed to successfully boot off a network.
keywords: ["Bug Check 0xBB NETWORK_BOOT_INITIALIZATION_FAILED", "NETWORK_BOOT_INITIALIZATION_FAILED"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- NETWORK_BOOT_INITIALIZATION_FAILED
api_type:
- NA
---

# Bug Check 0xBB: NETWORK\_BOOT\_INITIALIZATION\_FAILED


The NETWORK\_BOOT\_INITIALIZATION\_FAILED bug check has a value of 0x000000BB. This indicates that Windows failed to successfully boot off a network.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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

 

## Cause

This error is caused when Windows is booting off a network, and a critical function fails during I/O initialization.

## See Also

[Bug Check Code Reference](bug-check-code-reference2.md) 

 

 




