---
title: net_send
description: The net_send extension sends a message over a local network.
ms.assetid: 13d5fe3f-6477-4610-8928-020726ccb3c8
keywords: ["network messages", "net_send Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- net_send
api_type:
- NA
ms.localizationpriority: medium
---

# !net\_send


The **!net\_send** extension sends a message over a local network.

```dbgcmd
!net_send SendingMachine TargetMachine Sender Message
```

## <span id="ddk__net_send_dbg"></span><span id="DDK__NET_SEND_DBG"></span>Parameters


<span id="_______SendingMachine______"></span><span id="_______sendingmachine______"></span><span id="_______SENDINGMACHINE______"></span> *SendingMachine*   
Specifies the computer that will process the command. It is recommended that this be the name of the computer that the debugger is running on, since your network configuration may refuse to send the message otherwise. *SendingMachine* should not include leading backslashes (\\\).

<span id="_______TargetMachine______"></span><span id="_______targetmachine______"></span><span id="_______TARGETMACHINE______"></span> *TargetMachine*   
Specifies the computer to which the message will be sent. *TargetMachine* should not include leading backslashes (\\\).

<span id="_______Sender______"></span><span id="_______sender______"></span><span id="_______SENDER______"></span> *Sender*   
Specifies the sender of the message. It is recommended that *Sender* be identical to *SendingMachine*, since your network configuration may refuse to send the message otherwise. When the message is displayed, this string will be identified as the sender of the message.

<span id="_______Message______"></span><span id="_______message______"></span><span id="_______MESSAGE______"></span> *Message*   
Specifies the message itself. All text after the *Sender* parameter will be treated as part of *Message*, including spaces and quotation marks, although a [**semicolon**](----command-separator-.md) will terminate *Message* and begin a new command.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

 

 





