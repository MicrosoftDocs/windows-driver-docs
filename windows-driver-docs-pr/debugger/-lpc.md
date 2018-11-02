---
title: lpc
description: The lpc extension displays information about all local procedure call (LPC) ports and messages in the target system.
ms.assetid: d474aeca-fb12-424a-b57e-360215d0305c
keywords: ["LPC (local/light-weight procedure call)", "lpc Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- lpc
api_type:
- NA
ms.localizationpriority: medium
---

# !lpc


**Important**  
Lpc is now emulated in alpc, use the !alpc extension instead.

 
The **!lpc** extension displays information about all local procedure call (LPC) ports and messages in the target system.

```dbgcmd
!lpc message MessageID 
!lpc port Port 
!lpc scan Port 
!lpc thread Thread 
!lpc PoolSearch 
!lpc
```

## <span id="ddk__lpc_dbg"></span><span id="DDK__LPC_DBG"></span>Parameters


<span id="_______message______"></span><span id="_______MESSAGE______"></span> **message**   
(Windows Server 2003, Windows XP, and Windows 2000 only) Displays information about a message, such as the server port that contains the message in the queue, and the thread waiting for this message, if any.

<span id="_______MessageID______"></span><span id="_______messageid______"></span><span id="_______MESSAGEID______"></span> *MessageID*   
(Windows Server 2003, Windows XP, and Windows 2000 only) Specifies the message ID of the message to be displayed. If the value of this parameter is 0 or this parameter is omitted, the **!lpc message** command displays a summary list of messages. (In Windows 2000 with Service Pack 1 (SP1), the summary includes all messages in the LPC zone. In Windows 2000 with Service Pack 2 (SP2), Windows XP, and later versions of Windows, the summary includes all messages in the kernel pool. Paged-out messages are not included.)

<span id="_______port______"></span><span id="_______PORT______"></span> **port**   
(Windows Server 2003, Windows XP, and Windows 2000 only) Displays port information, such as the name of the port, its semaphore state, messages in its queues, threads in its rundown queue, its handle count, its references, and related ports.

<span id="_______scan______"></span><span id="_______SCAN______"></span> **scan**   
(Windows Server 2003, Windows XP, and Windows 2000 only) Displays summary information about the specified port and about all ports that are connected to it.

<span id="_______Port______"></span><span id="_______port______"></span><span id="_______PORT______"></span> *Port*   
(Windows Server 2003, Windows XP, and Windows 2000 only) Specifies the hexadecimal address of the port to be displayed. If the **!lpc port** command is used, and *Port* is 0 or is omitted, a summary list of all LPC ports is displayed. If the **!lpc scan** command is used, *Port* must specify the address of an actual port.

<span id="_______thread______"></span><span id="_______THREAD______"></span> **thread**   
(Windows Server 2003, Windows XP, and Windows 2000 only) Displays port information for all ports that contain the specified thread in their rundown port queues.

<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
(Windows Server 2003, Windows XP, and Windows 2000 only) Specifies the hexadecimal address of the thread. If this is 0 or omitted, the **!lpc thread** command displays a summary list of all threads that are performing any LPC operations.

<span id="_______PoolSearch______"></span><span id="_______poolsearch______"></span><span id="_______POOLSEARCH______"></span> **PoolSearch**   
(Windows Server 2003 and Windows XP only) Determines whether the **!lpc message** command searches for messages in the kernel pool. Each time **!lpc PoolSearch** is used, this setting toggles on or off (the initial setting is to not search the kernel pool). This only affects **!lpc message** commands that specify a nonzero value for *MessageID*.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP</strong></p>
<p><strong>Windows Server 2003</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about LPCs, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

This extension is not supported in Windows Vista and later versions of Windows.

In Windows Server 2003, Windows XP, and Windows 2000, using **!lpc** with no arguments displays help for this extension in the Debugger Command window.

If you have a thread that is marked as waiting for a reply to a message, use the **!lpc message** command with the ID of the delayed message. This command displays the specified message, the port that contains it, and all related threads.

If the message is not found and there were no read errors (such as "Unable to access zone segment"), the server received the message.

In this case, the server port can usually be found by using the **!lpc thread** command. Threads that are waiting for replies are linked into a server communication queue. This command will display all ports that contain the specified thread. After you know the port address, use the **!lpc port** command. More specific information about each thread can then be obtained by using the **!lpc thread**command with the address of each thread.

Here are several examples of the output from this extension from a Windows XP system:

In this example, all port LPC ports are displayed.

```dbgcmd
kd> !lpc port
Scanning 225 objects
       1  Port: 0xe1405650 Connection: 0xe1405650  Communication: 0x00000000  'SeRmCommandPort' 
       1  Port: 0xe141ef50 Connection: 0xe141ef50  Communication: 0x00000000  'SmApiPort' 
       1  Port: 0xe13c5740 Connection: 0xe13c5740  Communication: 0x00000000  'ApiPort' 
       1  Port: 0xe13d9550 Connection: 0xe13d9550  Communication: 0x00000000  'SbApiPort' 
       3  Port: 0xe13d8830 Connection: 0xe141ef50  Communication: 0xe13d8910  ' 
80000004  Port: 0xe13d8910 Connection: 0xe141ef50  Communication: 0xe13d8830  ' 
       3  Port: 0xe13d8750 Connection: 0xe13d9550  Communication: 0xe13a4030  ' 
       .....
```

In the previous example, the port at address e14ae238 has no messages; that is, all messages have been picked up and no new messages have arrived.

```dbgcmd
kd> !lpc port e14ae238

Server connection port e14ae238  Name: ApiPort
 Handles: 1   References: 107
    Server process  : 84aa0140 (csrss.exe)
    Queue semaphore : 84a96da8
 Semaphore state 0 (0x0)
    The message queue is empty
    The LpcDataInfoChainHead queue is empty
```

In the previous example, the port at 0xe14ae238 has messages which have been queued, but not yet picked up by the server.

```dbgcmd
kd> !lpc port 0xe14ae238

Server connection port e14ae238  Name: ApiPort
 Handles: 1   References: 108
    Server process  : 84aa0140 (csrss.exe)
    Queue semaphore : 84a96da8
 Semaphore state 0 (0x0)
        Messages in queue:
 0000 e20d9b80 - Busy  Id=0002249c  From: 0584.0680  Context=00000021  [e14ae248 . e14ae248]
 Length=0098007c  Type=00000001 (LPC_REQUEST)
                   Data: 00000000 0002021e 00000584 00000680 002f0001 00000007
    The message queue contains 1 messages
    The LpcDataInfoChainHead queue is empty
```

The remaining Windows XP examples concern the other options that can be used with this extension.

```dbgcmd
kd> !lpc message 222be
Searching message 222be in threads ...
Client thread 842a4db0 waiting a reply from 222be
Searching thread 842a4db0 in port rundown queues ...

Server communication port 0xe114a3c0
    Handles: 1   References: 1
    The LpcDataInfoChainHead queue is empty
        Connected port: 0xe1e7b948      Server connection port: 0xe14ae238

Client communication port 0xe1e7b948
    Handles: 1   References: 3
    The LpcDataInfoChainHead queue is empty

Server connection port e14ae238  Name: ApiPort
 Handles: 1   References: 107
    Server process  : 84aa0140 (csrss.exe)
    Queue semaphore : 84a96da8
 Semaphore state 0 (0x0)
    The message queue is empty
    The LpcDataInfoChainHead queue is empty
Done.
```

```dbgcmd
kd> !lpc thread 842a4db0
Searching thread 842a4db0 in port rundown queues ...

Server communication port 0xe114a3c0
    Handles: 1   References: 1
    The LpcDataInfoChainHead queue is empty
        Connected port: 0xe1e7b948      Server connection port: 0xe14ae238

Client communication port 0xe1e7b948
    Handles: 1   References: 3
    The LpcDataInfoChainHead queue is empty

Server connection port e14ae238  Name: ApiPort
 Handles: 1   References: 107
    Server process  : 84aa0140 (csrss.exe)
    Queue semaphore : 84a96da8
 Semaphore state 0 (0x0)
    The message queue is empty
    The LpcDataInfoChainHead queue is empty
```

```dbgcmd
kd> !lpc scan e13d8830
Scanning 225 objects
       3  Port: 0xe13d8830 Connection: 0xe141ef50  Communication: 0xe13d8910  ' 
80000004  Port: 0xe13d8910 Connection: 0xe141ef50  Communication: 0xe13d8830  ' 
Scanning 3 objects
```

 

 





