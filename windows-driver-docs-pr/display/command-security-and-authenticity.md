---
title: Command Security and Authenticity
description: Command Security and Authenticity
ms.assetid: 2a70f974-c34c-4462-a772-d8253f842ed8
keywords:
- commands WDK COPP
- command exchange WDK COPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Command Security and Authenticity


## <span id="ddk_command_security_and_authenticity_gg"></span><span id="DDK_COMMAND_SECURITY_AND_AUTHENTICITY_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

The following figure shows an application sending command messages to the video miniport driver across the secure channel.

![diagram illustrating command exchange](images/coppcmnd.png)

These command messages are contained in an envelope. The envelope contains data and MAC sections. The application calculates the MAC of the command data by using the data integrity key and the OMAC. For more information about the MAC and OMAC, see [Cryptographic Primitives Used by COPP](cryptographic-primitives-used-by-copp.md).

The following table describes the values in the preceding figure.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>COMMAND</p></td>
<td align="left"><p>Variable-length command data.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MAC<sub>KDI</sub>(COMMAND)</p></td>
<td align="left"><p>128-bit MAC of the command data using the data integrity session key.</p></td>
</tr>
</tbody>
</table>

 

 

 





