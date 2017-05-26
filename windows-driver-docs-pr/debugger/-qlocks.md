---
title: qlocks
description: The qlocks extension displays the state of all queued spin locks.
ms.assetid: fdeefedb-c840-410a-94e4-ae42923e82e7
keywords: ["qlocks Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- qlocks
api_type:
- NA
---

# !qlocks


The **!qlocks** extension displays the state of all queued spin locks.

```
    !qlocks 
```

## <span id="ddk__qlocks_dbg"></span><span id="DDK__QLOCKS_DBG"></span>


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
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about spin locks, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

Remarks
-------

This command is useful only on a multiprocessor system.

Here is an example:

```
0: kd> !qlocks
Key: O = Owner, 1-n = Wait order, blank = not owned/waiting, C = Corrupt

                       Processor Number
    Lock Name         0  1  2  3

KE   - Dispatcher               
KE   - Unused Spare             
MM   - PFN                      
MM   - System Space             
CC   - Vacb                     
CC   - Master                   
EX   - NonPagedPool             
IO   - Cancel                   
EX   - WorkQueue                
IO   - Vpb                      
IO   - Database                 
IO   - Completion               
NTFS - Struct                   
AFD  - WorkQueue                
CC   - Bcb                      
MM   - MM NonPagedPool             
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!qlocks%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




