---
title: tp
description: The tp extension displays thread pool information.
ms.assetid: 33b22e04-b781-4890-8142-c2624fdc4055
keywords: ["thread pool", "tp Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- tp
api_type:
- NA
ms.localizationpriority: medium
---

# !tp


The **!tp** extension displays thread pool information.

```dbgcmd
!tp pool Address [Flags] 
!tp tqueue Address [Flags] 
!tp ItemType Address [Flags] 
!tp ThreadType [Address] 
!tp stats Address [Flags] 
!tp wfac Address 
!tp wqueue Address Priority Node 
!tp -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______pool_Address_____________"></span><span id="_______pool_address_____________"></span><span id="_______POOL_ADDRESS_____________"></span> **pool** **** *Address*   
Causes the entire thread pool at *Address* to be displayed. If *Address* is 0, then all thread pools will be displayed.

<span id="_______tqueue_______Address______"></span><span id="_______tqueue_______address______"></span><span id="_______TQUEUE_______ADDRESS______"></span> **tqueue** **** *Address*   
Causes the active timer queue at *Address* to be displayed.

<span id="_______ItemType_Address______"></span><span id="_______itemtype_address______"></span><span id="_______ITEMTYPE_ADDRESS______"></span> *ItemType Address*   
Causes the specified thread pool item to be displayed. *Address* specifies the address of the item. *ItemType* specifies the type of the item; this can include any of the following possibilities:

<span id="obj"></span><span id="OBJ"></span>**obj**  
A generic pool item (such as an IO item) will be displayed.

<span id="timer"></span><span id="TIMER"></span>**timer**  
A timer item will be displayed.

<span id="wait"></span><span id="WAIT"></span>**wait**  
A wait item will be displayed.

<span id="work"></span><span id="WORK"></span>**work**  
A work item will be displayed.

<span id="_______ThreadType__Address_"></span><span id="_______threadtype__address_"></span><span id="_______THREADTYPE__ADDRESS_"></span> *ThreadType* \[*Address*\]  
Causes threads of the specified type to be displayed. If *Address* is included and nonzero, then only the thread at this address is displayed. If *Address* is 0, all threads matching *ThreadType* are displayed. If *Address* is omitted, only the threads matching *ThreadType* associated with the current thread are displayed. *ThreadType* specifies the type of the thread to be displayed; this can include any of the following possibilities:

<span id="waiter"></span><span id="WAITER"></span>**waiter**  
A thread pool waiter thread will be displayed.

<span id="worker"></span><span id="WORKER"></span>**worker**  
A thread pool worker thread will be displayed.

<span id="stats__Address_"></span><span id="stats__address_"></span><span id="STATS__ADDRESS_"></span>**stats** **\[**<em>Address</em>**\]**  
Causes the debug statistics of the current thread to be displayed. *Address* may be omitted, but if it is specified, it must equal -1 (negative one), to represent the current thread.

<span id="_______wfac_______Address______"></span><span id="_______wfac_______address______"></span><span id="_______WFAC_______ADDRESS______"></span> **wfac** **** *Address*   
(Windows 7 and later only) Causes the worker factory at *Address* to be displayed. The specified *Address* must be a valid nonzero address.

<span id="_______wqueue_______Address______"></span><span id="_______wqueue_______address______"></span><span id="_______WQUEUE_______ADDRESS______"></span> **wqueue** **** *Address*   
(Windows 7 and later only) Causes display of a work queue and NUMA node that matche the following: a specified priority, a specified NUMA node, and the pool, at a specified address, to which the NUMA node belongs. *Address* specifies the address of the pool. When the **wqueue** parameter is used, it must be followed by *Address*, *Priority*, and *Node*.

<span id="_______Priority______"></span><span id="_______priority______"></span><span id="_______PRIORITY______"></span> *Priority*   
(Windows 7 and later only) Specifies the priority levels of the work queues to be displayed. *Priority* can be any of the following values:

<span id="0"></span>**0**  
Work queues with high priority are displayed.

<span id="1"></span>**1**  
Work queues with normal priority are displayed.

<span id="2"></span>**2**  
Work queues with low priority are displayed.

<span id="-1"></span>**-1**  
All work queues are displayed.

<span id="_______Node______"></span><span id="_______node______"></span><span id="_______NODE______"></span> *Node*   
(Windows 7 and later only) Specifies a NUMA node belonging to the pool specified by *Address*. If *Node* is -1 (negative one), all NUMA nodes are displayed.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies what the display should contain. This can be a sum of any of the following bit values (the default is 0x0):

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes the display to be single-line output. This bit value has no effect on the output when an *ItemType* is displayed.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the display to include member information.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
This flag is relevant only when the **pool** option is used. In Windows XP, Windows Server 2003, Windows Vista, and Windows Server 2008, this flag causes the display to include the pool work queue. In Windows 7 and later, this flag causes the display to include all the pool's work queues that are at normal priority, and all NUMA nodes.

<span id="_______-_______"></span> **-?**   
Displays a brief help text for this extension in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Exts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about thread pooling, see the Microsoft Windows SDK documentation.

 

 





