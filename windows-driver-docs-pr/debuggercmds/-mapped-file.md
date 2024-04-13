---
title: "!mapped_file"
description: "The !mapped_file extension displays the name of the file that backs the file mapping that contains a specified address."
keywords: ["!mapped_file Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- mapped_file
api_type:
- NA
---

# !mapped\_file

The **!mapped\_file** extension displays the name of the file that backs the file mapping that contains a specified address.

```dbgcmd
!mapped_file Address
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the file mapping. If *Address* is not in a mapping, the command fails.

## DLL

Uext.dll

The **!mapped\_file** extension can only be used during live, nonremote debugging.

## Additional Information

For more information about file mapping, see [MapViewOfFile](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile) in the Windows SDK.

## Remarks

Here are three examples. The first two addresses used are mapped from a file, and the third is not.

```dbgcmd
0:000> !mapped_file 4121ec 
Mapped file name for 004121ec: '\Device\HarddiskVolume2\CODE\TimeTest\Debug\TimeTest.exe'

0:000> !mapped_file 77150000 
Mapped file name for 77150000: '\Device\HarddiskVolume2\Windows\System32\kernel32.dll'

0:000> !mapped_file 80310000 
No information found for 80310000: error 87
```

 


