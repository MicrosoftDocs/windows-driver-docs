---
title: DSM_Entry function
description: The DSM_Entry function provides the only entry point into the Data Source Manager.
ms.date: 03/04/2025
ms.topic: reference
api_location:
- twain_32.dll
api_name:
- DSM_Entry
topic_type:
- apiref
api_type:
- DllExport
---

# DSM_Entry function

The **DSM_Entry** function provides the only entry point into the Data Source Manager.

## Syntax

```cpp
TW_UINT16 FAR PASCAL DSM_Entry
(
    pTW_IDENTITY pOrigin,
    pTW_IDENTITY pDest,
    TW_UINT32    DG,
    TW_UINT16    DAT,
    TW_UINT16    MSG,
    TW_MEMREF    pData
);
```

## Parameters

### pOrigin

Identifies the source module of the message.<br><br>This could identify an Application, a Source, or the Source Manager.

### pDest

Identifies the destination module for the message.<br><br>This could identify an application or a data source. If this is NULL, the message goes to the Source Manager.

### DG

The Data Group<br><br>Example: DG_IMAGE

### DAT

The Data Attribute Type<br><br>Example: DAT_IMAGEMEMXFER

### MSG

The message<br><br>Messages are interpreted by the destination module with respect to the Data Group and the Data Attribute Type.<br><br>Example: MSG_GET

### pData

A pointer to the data structure or variable identified by the Data Attribute Type.<br><br>Example: (TW_MEMREF)&ImageMemXfer where ImageMemXfer is a TW_IMAGEMEMXFER structure.

## Returns

ReturnCode<br><br>Example: TWRC_SUCCESS
