---
title: Checking the Oplock State of IRP_MJ_FILE_SYSTEM_CONTROL
description: Checking the Oplock State of an IRP_MJ_FILE_SYSTEM_CONTROL operation
ms.assetid: 3651d9ed-6b6f-4b60-9dfa-1c5c0c78b1a1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Checking the Oplock State of IRP_MJ_FILE_SYSTEM_CONTROL

Certain IRP_MJ_FILE_SYSTEM_CONTROL operations check oplock state. The following operation(s) perform this check:
- **FSCTL_SET_ZERO_DATA**

This information applies when a caller wants to zero the current contents of the given stream.

|Request Type|Conditions|
|---|---|
|Level 1<br>Batch<br>Filter<br>Read-Handle<br>Read-Write<br>Read-Write-Handle|Broken on IRP_MJ_FILE_SYSTEM_CONTROL (for FSCTL_SET_ZERO_DATA) when:<ul><li>The operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</ul></li><hr>If the oplock is broken:<ul><li>Break to None</li><li>For the Read-Handle request: Although acknowledgment of the break is required, the operation continues immediately (for example, without waiting for the acknowledgment).</li><li>For all other request types: An acknowledgment must be received before the operation continues.</li></ul>|
|Read|Broken on IRP_MJ_FILE_SYSTEM_CONTROL (for FSCTL_SET_ZERO_DATA) when:<ul><li>The operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</ul></li><hr>If the oplock is broken:<ul><li>Break to None</li><li>No acknowledgment is required, the operation proceeds immediately.</li></ul>|
|Level 2|<ul><li>Always break to None.</li><li>No acknowledgment is required, the operation proceeds immediately.</li></ul>|



