---
title: mapped_file
description: The mapped_file extension displays the name of the file that backs the file mapping that contains a specified address.
ms.assetid: 1d6d4d14-01ca-47ce-a044-778c9a56e9a5
keywords: ["mapped_file Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- mapped_file
api_type:
- NA
ms.localizationpriority: medium
---

# !mapped\_file


The **!mapped\_file** extension displays the name of the file that backs the file mapping that contains a specified address.

```dbgcmd
!mapped_file Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the file mapping. If *Address* is not in a mapping, the command fails.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Uext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Uext.dll</p></td>
</tr>
</tbody>
</table>

 

The **!mapped\_file** extension can only be used during live, nonremote debugging.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about file mapping, see [MapViewOfFile](https://go.microsoft.com/fwlink/p/?linkid=123354) in the Windows SDK.

Remarks
-------

Here are three examples. The first two addresses used are mapped from a file, and the third is not.

```dbgcmd
0:000> !mapped_file 4121ec 
Mapped file name for 004121ec: '\Device\HarddiskVolume2\CODE\TimeTest\Debug\TimeTest.exe'

0:000> !mapped_file 77150000 
Mapped file name for 77150000: '\Device\HarddiskVolume2\Windows\System32\kernel32.dll'

0:000> !mapped_file 80310000 
No information found for 80310000: error 87
```

 

 





