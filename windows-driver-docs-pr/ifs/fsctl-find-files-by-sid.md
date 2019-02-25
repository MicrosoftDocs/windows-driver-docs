---
title: FSCTL_FIND_FILES_BY_SID control code
description: The FSCTL\_FIND\_FILES\_BY\_SID control code searches a directory for a file whose creator and owner matche the specified SID.
ms.assetid: fe0953d3-a009-431b-b03b-5d827dc732a1
keywords: ["FSCTL_FIND_FILES_BY_SID control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_FIND_FILES_BY_SID
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_FIND\_FILES\_BY\_SID control code


The FSCTL\_FIND\_FILES\_BY\_SID control code searches a directory for a file whose creator and owner matche the specified SID.

To perform this operation, minifilter drivers call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) with the following parameters, and file systems, redirectors, and legacy file system filter drivers call [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. The file object pointer for the directory to search. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. The file handle for the directory to search. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
A control code for the operation. Use FSCTL\_FIND\_FILES\_BY\_SID for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to an input buffer that is described by the FIND\_BY\_SID\_DATA structure. The FIND\_BY\_SID\_DATA structure is defined as follows:

```cpp
typedef struct {
  DWORD  ;
  SID  ;
} FIND_BY_SID_DATA, *PFIND_BY_SID_DATA;
```

**Members**

<a href="" id="restart"></a>**Restart**  
Indicates whether to restart the search. This member should be set to 1 on first call, so that the search will start from the root. For subsequent calls, this member should be set to zero so that the search will resume at the point where it stopped.

<a href="" id="sid-"></a>**Sid**   
A structure of type [**SID**](https://msdn.microsoft.com/library/windows/hardware/ff556740) that specifies the creator and owner.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
The length, in bytes, of the buffer at *InputBuffer*.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
A pointer to a caller-allocated array of quad-aligned FIND\_BY\_SID\_OUTPUT structures that receive the fully qualified path names for each file. The FIND\_BY\_SID\_OUTPUT structure is defined as follows:

```cpp
typedef struct _FIND_BY_SID_OUTPUT {
  DWORD  ;
  DWORD  ;
  DWORD  ;
  WCHAR  [1];
} FIND_BY_SID_OUTPUT, *PFIND_BY_SID_OUTPUT;
```

**Members**

<a href="" id="nextentryoffset"></a>**NextEntryOffset**  
Number of bytes that must be skipped to get to the next record. A value of zero indicates that this is the last record.

<a href="" id="fileindex-"></a>**FileIndex**   
Index of the file.

<a href="" id="filenamelength-"></a>**FileNameLength**   
Size of the file name, in bytes.

<a href="" id="filename-"></a>**FileName**   
A null-terminated string that specifies the file name.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Size, in bytes, of the data returned in the buffer that is pointed to by the *OutputBuffer* parameter.

Remarks
-------

When [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) and [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) process the **FSCTL\_FIND\_FILES\_BY\_SID** control code, these routines check every file and directory on the volume. This operation might be slow if there are many files on the volume, even if the directory to search is very small.

## See also


[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**SID**](https://msdn.microsoft.com/library/windows/hardware/ff556740)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 






