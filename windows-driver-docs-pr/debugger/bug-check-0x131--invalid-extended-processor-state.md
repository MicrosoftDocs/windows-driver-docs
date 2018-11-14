---
title: Bug Check 0x131 INVALID_EXTENDED_PROCESSOR_STATE
description: The INVALID_EXTENDED_PROCESSOR_STATE bug check has a value of 0x00000131. This indicates that an invalid combination of parameters was detected while saving or restoring extended processor state.
ms.assetid: 72EEA46A-1E96-4B07-A7E6-40DAE4641B20
keywords: ["Bug Check 0x131 INVALID_EXTENDED_PROCESSOR_STATE", "INVALID_EXTENDED_PROCESSOR_STATE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- INVALID_EXTENDED_PROCESSOR_STATE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x131: INVALID\_EXTENDED\_PROCESSOR\_STATE


The INVALID\_EXTENDED\_PROCESSOR\_STATE bug check has a value of 0x00000131. This indicates that an invalid combination of parameters was detected while saving or restoring extended processor state.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## INVALID\_EXTENDED\_PROCESSOR\_STATE Parameters


Parameter one indicates which validity check failed.

| Parameter | Description                                                                     |
|-----------|---------------------------------------------------------------------------------|
| 1         | 0 - Invalid feature mask was passed or extended processor state is not enabled. |
| 2         | Nonzero if extended state is enabled.                                           |
| 3         | The low 32 bits of the feature mask.                                            |
| 4         | The high 32 bits of the feature mask.                                           |

 

| Parameter | Description                                                                                    |
|-----------|------------------------------------------------------------------------------------------------|
| 1         | 1 - An attempt to save or restore extended state was made at IRQL higher than DISPATCH\_LEVEL. |
| 2         | The IRQL                                                                                       |
| 3         | Reserved                                                                                       |
| 4         | Reserved                                                                                       |

 

| Parameter | Description                                                     |
|-----------|-----------------------------------------------------------------|
| 1         | 2 - The previously saved state is for an equal or higher level. |
| 2         | The saved level.                                                |
| 3         | The current level.                                              |
| 4         | Reserved                                                        |

 

| Parameter | Description                                               |
|-----------|-----------------------------------------------------------|
| 1         | 3 - The previously saved state is for a different thread. |
| 2         | The saved thread.                                         |
| 3         | The current thread.                                       |
| 4         | Reserved                                                  |

 

| Parameter | Description                                          |
|-----------|------------------------------------------------------|
| 1         | 4 - Previously saved state is for a different level. |
| 2         | The saved level.                                     |
| 3         | The current level.                                   |
| 4         | Reserved                                             |

 

 

 




