---
title: Bug Check 0x112 MSRPC_STATE_VIOLATION
description: The MSRPC_STATE_VIOLATION bug check has a value of 0x00000112. This indicates that the Msrpc.sys driver has initiated a bug check.
ms.assetid: b7cd531d-518e-4d11-8edb-d52dbbe51043
keywords: ["Bug Check 0x112 MSRPC_STATE_VIOLATION", "MSRPC_STATE_VIOLATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- MSRPC_STATE_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x112: MSRPC\_STATE\_VIOLATION


The MSRPC\_STATE\_VIOLATION bug check has a value of 0x00000112. This indicates that the Msrpc.sys driver has initiated a bug check.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## MSRPC\_STATE\_VIOLATION Parameters


Parameters 1 and 2 are the only parameters of interest. Parameter 1 indicates the state violation type; the value for Parameter 2 is determined by the value of Parameter 1.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x01</p></td>
<td align="left"><p>The exception code</p></td>
<td align="left"><p>A non-continuable exception was continued by the caller.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x02</p></td>
<td align="left"><p>The error</p></td>
<td align="left"><p>The advanced local procedure call (ALPC) returned an invalid error.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x03</p></td>
<td align="left"><p>The session to the server</p></td>
<td align="left"><p>The caller unloaded the Microsoft remote procedure call (MSRPC) driver while it was still in use. It is likely that open binding handles remain.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x04 and</p>
<p>0x05</p></td>
<td align="left"><p>The session to the server</p></td>
<td align="left"><p>An invalid close command was received from the ALPC.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x06</p></td>
<td align="left"><p>The binding handle</p></td>
<td align="left"><p>An attempt was made to bind a remote procedure call (RPC) handle a second time.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x07</p></td>
<td align="left"><p>The binding handle</p></td>
<td align="left"><p>An attempt was made to perform an operation on a binding handle that was not bound.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x08</p></td>
<td align="left"><p>The binding handle</p></td>
<td align="left"><p>An attempt was made to set security information on a binding handle that was already bound.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x09</p></td>
<td align="left"><p>The binding handle</p></td>
<td align="left"><p>An attempt was made to set an option on a binding handle that was already bound.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0A</p></td>
<td align="left"><p>The call object</p></td>
<td align="left"><p>An attempt was made to cancel an invalid asynchronous remote procedure call.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0B</p></td>
<td align="left"><p>The call object</p></td>
<td align="left"><p>An attempt was made to push on an asynchronous pipe call when it was not expected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0C and</p>
<p>0x0E</p></td>
<td align="left"><p>The pipe object</p></td>
<td align="left"><p>An attempt was made to push on an asynchronous pipe without waiting for notification.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0F</p></td>
<td align="left"><p>The pipe object</p></td>
<td align="left"><p>An attempt was made to synchronously terminate a pipe a second time.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x15</p></td>
<td align="left"><p>The object closest to the error</p></td>
<td align="left"><p>An RPC internal error occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x16</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Two causally ordered calls were issued in an order that cannot be enforced by the RPC.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x17</p></td>
<td align="left"><p>The call object</p></td>
<td align="left"><p>A server manager routine did not unsubscribe from notifications prior to completing the call.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x18</p></td>
<td align="left"><p>The async handle</p></td>
<td align="left"><p>An invalid operation on the asynchronous handle occurred.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The most common cause of this bug check is that the caller of the Msrpc.sys driver violated the state semantics for such a call.

 

 




