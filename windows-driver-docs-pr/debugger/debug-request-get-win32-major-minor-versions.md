---
title: DEBUG\_REQUEST\_GET\_WIN32\_MAJOR\_MINOR\_VERSIONS
description: DEBUG\_REQUEST\_GET\_WIN32\_MAJOR\_MINOR\_VERSIONS
ms.assetid: 3764add2-a96a-41c8-9747-6a1ef3d8b5af
keywords: ["DEBUG_REQUEST_GET_WIN32_MAJOR_MINOR_VERSIONS Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_REQUEST_GET_WIN32_MAJOR_MINOR_VERSIONS
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DEBUG\_REQUEST\_GET\_WIN32\_MAJOR\_MINOR\_VERSIONS


The DEBUG\_REQUEST\_GET\_WIN32\_MAJOR\_MINOR\_VERSIONS [**Request**](request.md) operation returns the version of Windows that is currently running on the target.

**Parameters**

<span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span>*InBuffer*  
Not used.

<span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span>*OutBuffer*  
The major and minor version numbers for the version of Windows that is currently running on the target. The type of the version numbers is an array containing two ULONG values; the first ULONG in the array is the major version number and the second is the minor version number

The following table lists the major and minor version numbers by operating system.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Version of Windows</th>
<th align="left">Major version number</th>
<th align="left">Minor version number</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 2000</p></td>
<td align="left"><p>5</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP</p></td>
<td align="left"><p>5</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2003</p></td>
<td align="left"><p>5</p></td>
<td align="left"><p>2</p></td>
</tr>
</tbody>
</table>

 

## <span id="see_also"></span>See also


[**Request**](request.md)

 

 






