---
title: Maintain a list of objects for each type
description: Maintain a list of objects for each type
ms.assetid: 845ba6cb-60b3-4053-9d54-f43ed344f82d
keywords: ["Maintain a list of objects for each type (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Maintain a list of objects for each type


## <span id="ddk_maintain_a_list_of_objects_for_each_type_dtools"></span><span id="DDK_MAINTAIN_A_LIST_OF_OBJECTS_FOR_EACH_TYPE_DTOOLS"></span>


The **Maintain a list of objects for each type** flag collects and maintains a list of active objects by object type, for example, event, mutex, and semaphore.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>otl</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x4000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_MAINTAIN_OBJECT_TYPELIST</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

To display the object list, use Open Handles (oh.exe), a tool included in the Windows 2000 Resource Kit, and now available for download from the [Microsoft Windows 2000 Resource Kit](http://go.microsoft.com/fwlink/p/?linkid=11233) Web site. Because Open Handles automatically sets the OTL flag, but does not clear it, use **GFlags -otl** to clear the flag.

**Note**   The linked lists created when you set this flag use eight bytes of overhead for each object. Remember to clear this flag when your analysis is complete.

 

 

 





