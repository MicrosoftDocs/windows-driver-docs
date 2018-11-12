---
title: Examples of Timestamp Processing
description: Examples of Timestamp Processing
ms.assetid: e889a114-b143-4764-ab54-48888adc2a32
keywords:
- timestamps WDK TCP chimney offload , examples
- TCP timestamps WDK TCP chimney offload , examples
- drift in clock WDK TCP timestamps
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Examples of Timestamp Processing


\[The TCP chimney offload feature is deprecated and should not be used.\]

The following table provides an example of timestamp processing. This processing is synchronized between the host stack and an offload target.

<table style="width:100%;">
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Stack time</th>
<th align="left">Stack delta</th>
<th align="left">Stack processing</th>
<th align="left">NIC time</th>
<th align="left">NIC delta</th>
<th align="left">NIC processing</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>100</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Send packet:</p>
<p><em>Timestamp</em>= 100 + 0</p></td>
<td align="left"><p>200</p></td>
<td align="left"><p>0</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Offload connection:</p>
<p><em>TsTime</em>= 100</p></td>
<td align="left"></td>
<td align="left"><p>-100</p></td>
<td align="left"><p><em>NicDelta</em>= 100 - 200</p></td>
</tr>
<tr class="odd">
<td align="left"><p>105</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>205</p></td>
<td align="left"></td>
<td align="left"><p>ACK received:</p>
<p><em>TsEchoed</em>= 100</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>MRTT = (205 - 100 - 100)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>110</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>210</p></td>
<td align="left"><p>-100</p></td>
<td align="left"><p>Send packet:</p>
<p><em>Timestamp</em>= 210 -100</p></td>
</tr>
<tr class="even">
<td align="left"><p>115</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>215</p></td>
<td align="left"></td>
<td align="left"><p>ACK received:</p>
<p><em>TsEchoed</em>= 110</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>MRTT = (215 - 100 - 110)</p></td>
</tr>
<tr class="even">
<td align="left"><p>150</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>250</p></td>
<td align="left"><p>-100</p></td>
<td align="left"><p>Send packet:</p>
<p><em>Timestamp</em>= 250 - 100</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Terminate offload of connection:</p>
<p><em>TsTime</em>= 250 - 100</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>0</p></td>
<td align="left"><p><em>StackDelta</em>= 150 - 150</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>155</p></td>
<td align="left"></td>
<td align="left"><p>ACK received:</p>
<p><em>TsEchoed</em>= 150</p></td>
<td align="left"><p>255</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>MRTT = (155 + 0 - 150)</p></td>
<td align="left"></td>
<td align="left"><p>-100</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

1.  The host stack [generates a timestamp](generating-a-timestamp.md) of 100 for a TCP segment and then sends the segment.

2.  The host stack offloads the TCP connection to the offload target ( *TsTime*= 100).

3.  The offload target calculates its [timestamp delta](calculating-the-timestamp-delta.md)( *NicDelta*= 100 - 200 = -100).

4.  The offload target receives an acknowledgement from the remote TCP peer for the packet that was transmitted by the host stack before the connection was offloaded ( *TsEchoed*= 100).

5.  The offload target calculates the MRTT by using the echoed timestamp (MRTT = 205 - 100 - 100 = 5).

6.  The offload target generates a timestamp of 110 for a TCP segment ( *Timestamp*= 210 -100) and then sends the segment.

7.  The offload target receives an acknowledgement from the remote TCP peer for the transmitted packet ( *TsEchoed*= 110).

8.  The offload target [calculates the MRTT](calculating-the-merged-round-trip-time.md) by using the echoed timestamp (MRTT = 215 - 100 - 110 = 5).

9.  The offload target generates a timestamp of 150 for a TCP segment ( *Timestamp*= 210 -100) and then sends the segment.

10. The offload target terminates the offload of the TCP connection ( *TsTime*= 250 - 100).

11. The host calculates its timestamp delta ( *StackDelta*= (250 - 100) - 150 = 0).

12. The host stack receives an acknowledgement from the remote TCP peer for the packet that was transmitted by the host stack before the offload of the connection was terminated ( *TsEchoed*= 150).

13. The offload target calculates the MRTT by using the echoed timestamp (MRTT = 155 + 0 - 150 = 5).

The following table provides an example of timestamp processing that handles drift in the host stack's clock.

<table style="width:100%;">
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Stack time</th>
<th align="left">Stack delta</th>
<th align="left">Stack processing</th>
<th align="left">NIC time</th>
<th align="left">NIC delta</th>
<th align="left">NIC processing</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>100</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Send packet:</p>
<p><em>Timestamp</em>= 100 + 0</p></td>
<td align="left"><p>200</p></td>
<td align="left"><p>0</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Offload connection:</p>
<p><em>Timestamp</em>= 100 + 0</p></td>
<td align="left"></td>
<td align="left"><p>-100</p></td>
<td align="left"><p><em>NicDelta</em>= 100 - 200</p></td>
</tr>
<tr class="odd">
<td align="left"><p>105</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>205</p></td>
<td align="left"></td>
<td align="left"><p>ACK received:</p>
<p><em>TsEchoed</em>= 100</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>MRTT = (205 - 100 - 100)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>200</strong></p>
<p><strong>(clock drift)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>250</p></td>
<td align="left"><p></p>
-100</td>
<td align="left"><p>Send packet:</p>
<p><em>Timestamp</em>= 250 - 100</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Terminate offload of connection:</p>
<p><em>TsTime</em>= 250 - 100</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>-50</p></td>
<td align="left"><p><em>StackDelta</em>= 150 - 200</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>205</p></td>
<td align="left"></td>
<td align="left"><p>ACK received:</p>
<p><em>TsEchoed</em>= 150</p></td>
<td align="left"><p>255</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>MRTT = (205 - 50 - 150)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>250</p></td>
<td align="left"><p>-50</p></td>
<td align="left"><p>Send packet:</p>
<p><em>Timestamp</em>= 250 - 50</p></td>
<td align="left"><p>300</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>255</p></td>
<td align="left"></td>
<td align="left"><p>ACK received:</p>
<p><em>TsEchoed</em>= 200</p></td>
<td align="left"><p>305</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>MRTT = (255 - 50 - 200)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>400</strong></p>
<p><strong>(clock drift)</strong></p></td>
<td align="left"></td>
<td align="left"><p>Send packet:</p>
<p><em>Timestamp</em>= 400 - 50</p></td>
<td align="left"><p>320</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Offload connection:</p>
<p><em>TsTime</em>= 400 - 50</p></td>
<td align="left"></td>
<td align="left"><p>30</p></td>
<td align="left"><p><em>NicDelta</em>= 350 - 320</p></td>
</tr>
<tr class="odd">
<td align="left"><p>405</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>325</p></td>
<td align="left"></td>
<td align="left"><p>ACK received:</p>
<p><em>TsEchoed</em>= 35050</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>MRTT = (325 + 30 - 350)</p></td>
</tr>
</tbody>
</table>

 

Note the drift in the host stack clock changes from 105 to 200 and from 255 to 400. (Without the drift, these intervals would be 105 to 205 and 320 to 420.) The calculations for the generation of *TsTime*, the timestamp delta, and the MRTT properly handle this drift.

 

 





