---
title: FSCTL_LMR_QUERY_INFO control code
description: The FSCTL_LMR_QUERY_INFO control code retrieves the desired information for a remote file or directory opened locally.
keywords: ["FSCTL_LMR_QUERY_INFO control code File System Filter Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_LMR_QUERY_INFO
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_LMR_QUERY_INFO control code

The **FSCTL_LMR_QUERY_INFO** control code retrieves the desired information for a remote file or directory opened locally.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **FileObject** [in]: Parameter for [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. A file object pointer for the remote volume. This parameter is required and cannot be **NULL**.

- **FileHandle** [in]: Parameter for [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. A handle for the remote volume. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: A control code for the operation. Use **FSCTL_LMR_QUERY_INFO** for this operation.

- **InputBuffer** [in]: Pointer to a **LMR_QUERY_INFO_PARAM** structure that contains the type of information to be queried. The **LMR_QUERY_INFO_PARAM** structure is defined as follows:

  ``` syntax
  typedef struct _LMR_QUERY_INFO_PARAM { 
  
      LMR_QUERY_INFO_CLASS Operation; 
  
  } LMR_QUERY_INFO_PARAM, *PLMR_QUERY_INFO_PARAM;
  
  ```
  
  where **Operation** is a **LMR_QUERY_INFO_CLASS** enumeration value that specifies the type of information to be queried. **LMR_QUERY_INFO_CLASS** is defined as follows:
  
  ``` syntax
  typedef enum _LMR_QUERY_INFO_CLASS {
      LMRQuerySessionInfo = 1,
  } LMR_QUERY_INFO_CLASS, *PLMR_QUERY_INFO_CLASS;
  ```
  
  | Value | Meaning |
  | ----- | ------- |
  | **LMRQuerySessionInfo** (1) | Query the session ID information for the file or directory. This information is returned in a **LMR_QUERY_SESSION_INFO** structure via *OutputBuffer*. |
  
  The **LMR_QUERY_SESSION_INFO** structure is defined as follows:
  
  ``` syntax
  typedef struct _LMR_QUERY_SESSION_INFO { 
  
      UINT64 SessionId; 
  
  } LMR_QUERY_SESSION_INFO, *PLMR_QUERY_SESSION_INFO;
  ```

- **InputBufferLength** [in]: The size, in bytes, of the buffer pointed to by **InputBuffer**. This value is ```sizeof(LMR_QUERY_INFO_PARAM)```.

- **OutputBuffer** [out]: A pointer to a buffer that receives the desired information about the file or directory. The structure of the information returned in the buffer is defined by the **Operation** specified in **InputBuffer**'s **LMR_QUERY_INFO_CLASS** structure.

- **OutputBufferLength** [out]: The size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS if the operation succeeds. Otherwise, the appropriate function returns the appropriate NTSTATUS error code.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Minimum supported client | Windows 10 version 1809, and Windows 10 version 2004 and above versions |
| Minimum supported server | Windows Server 2019 |
| Header | *Ntifs.h* (include *Ntifs.h*) |
