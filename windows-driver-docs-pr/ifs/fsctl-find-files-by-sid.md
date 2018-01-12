---
title: FSCTL\_FIND\_FILES\_BY\_SID control code
description: The FSCTL\_FIND\_FILES\_BY\_SID control code searches a directory for a file whose creator and owner matche the specified SID.
ms.assetid: fe0953d3-a009-431b-b03b-5d827dc732a1
keywords: ["FSCTL_FIND_FILES_BY_SID control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_FIND_FILES_BY_SID
api_type:
- NA
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

```
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

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_FIND_FILES_BY_SID%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





