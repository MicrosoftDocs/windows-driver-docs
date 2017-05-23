---
title: Maintain a list of objects for each type
description: Maintain a list of objects for each type
ms.assetid: 845ba6cb-60b3-4053-9d54-f43ed344f82d
keywords: ["Maintain a list of objects for each type (global flag)"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Maintain%20a%20list%20of%20objects%20for%20each%20type%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




