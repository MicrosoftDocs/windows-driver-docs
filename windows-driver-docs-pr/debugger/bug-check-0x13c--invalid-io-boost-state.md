---
title: Bug Check 0x13C INVALID_IO_BOOST_STATE
description: The INVALID_IO_BOOST_STATE bug check has a value of 0x0000013C. This indicates that a thread exited with an invalid I/O boost state. This should be zero when a thread exits.
ms.assetid: BDCD8A3A-1F26-41A4-95B0-9B2CEBD333AC
keywords: ["Bug Check 0x13C INVALID_IO_BOOST_STATE", "INVALID_IO_BOOST_STATE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- INVALID_IO_BOOST_STATE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x13C: INVALID\_IO\_BOOST\_STATE


The INVALID\_IO\_BOOST\_STATE bug check has a value of 0x0000013C. This indicates that a thread exited with an invalid I/O boost state. This should be zero when a thread exits.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## INVALID\_IO\_BOOST\_STATE Parameters


| Parameter | Description                                             |
|-----------|---------------------------------------------------------|
| 1         | Pointer to the thread which had the invalid boost state |
| 2         | Current boost state or throttle count                   |
| 3         | Reserved                                                |
| 4         | Reserved                                                |

 

 

 




