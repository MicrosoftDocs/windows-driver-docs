---
title: NDIS_DECLARE_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NDIS_DECLARE_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE macro to define the context type that is used by the SetNetBufferListSwitchContext and GetNetBufferListSwitchContext functions to attach and retrieve context from a NET_BUFFER_LIST structure. Extensions can define as many context types as they want within their driver.
ms.assetid: 1DADD5C2-10AD-409C-9382-D98FC8789E5A
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_DECLARE_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE macro Network Drivers Starting with Windows Vista
---

# NDIS\_DECLARE\_SWITCH\_NET\_BUFFER\_LIST\_CONTEXT\_TYPE macro


Hyper-V extensible switch extensions use the **NDIS\_DECLARE\_SWITCH\_NET\_BUFFER\_LIST\_CONTEXT\_TYPE** macro to define the context type that is used by the [*SetNetBufferListSwitchContext*](https://msdn.microsoft.com/library/windows/hardware/hh846223) and [*GetNetBufferListSwitchContext*](https://msdn.microsoft.com/library/windows/hardware/hh846190) functions to attach and retrieve context from a [NET\_BUFFER\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff568412) structure. Extensions can define as many context types as they want within their driver.

Syntax
------

```ManagedCPlusPlus
 NDIS_DECLARE_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE(
   _ContextName ContextName,
   _ExtensionId ExtensionId
);
```

Parameters
----------

*ContextName*   
An identifier for the context type.

*ExtensionId*   
A GUID that matches the extension ID.

Return value
------------

None.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[*SetNetBufferListSwitchContext*](https://msdn.microsoft.com/library/windows/hardware/hh846223)

[*GetNetBufferListSwitchContext*](https://msdn.microsoft.com/library/windows/hardware/hh846190)

[NET\_BUFFER\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff568412)

 

 




