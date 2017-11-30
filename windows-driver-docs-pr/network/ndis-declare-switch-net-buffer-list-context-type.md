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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_DECLARE_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE%20macro%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


