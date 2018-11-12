---
title: ks.dumpcircuit
description: The ks.dumpcircuit extension lists details of the transport circuit associated with the given object.
ms.assetid: 34e6fa0f-7479-4616-ba7e-f2b12ccc836d
keywords: ["ks.dumpcircuit Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ks.dumpcircuit
api_type:
- NA
ms.localizationpriority: medium
---

# !ks.dumpcircuit


The **!ks.dumpcircuit** extension lists details of the transport circuit associated with the given object.

```dbgcmd
!ks.dumpcircuitextension Object [Level] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Object______"></span><span id="_______object______"></span><span id="_______OBJECT______"></span> *Object*   
Specifies a pointer to the object for which to display the transport circuit. For AVStream, *Object* must be one of the following types: CKsPin\*, CKsQueue\*, CKsRequestor\*, CKsSplitter\*, CKsSplitterBranch\*.

For PortCls, object must be one of the following types: CPortPin\*, CKsShellRequestor\*, or CIrpStream\*.

<span id="_______Level______"></span><span id="_______level______"></span><span id="_______LEVEL______"></span> *Level*   
Optional. Specifies the level of detail to display on a 0-7 scale with progressively more information displayed for higher values. To display all available details, supply a value of 7.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>winxp\Ks.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ks.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel Streaming Debugging](kernel-streaming-debugging.md).

Remarks
-------

Note that **!ks.dumpcircuit** starts walking the circuit at the specified object, which does not always correspond to the data source.

You can first use [**!ks.graph**](-ks-graph.md) with a filter address to list pin addresses, and then use these addresses with **!ks.dumpcircuit**.

Here is an example of the **!ks.dumpcircuit** display:

```dbgcmd
kd> !dumpcircuit 8293f4f0
Pin8293f4f0 0 (snk, out)
Queue82990e20 r/w/c=2489/2/0
```

 

 





