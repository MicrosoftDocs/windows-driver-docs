---
title: Macro Example to Filter Error Codes
author: windows-driver-content
description: Macro Example to Filter Error Codes
ms.assetid: 68aa0a75-82c7-4dd9-8f8f-eca5de6ea102
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Macro Example to Filter Error Codes

> [!IMPORTANT]  
> WSD Challenger functionality has been deprecated and all WSD Challenger-related documentation will be removed in 2018.

The following macro example filters communication failure error codes.

```
//
// Example of a macro to filter device communication errors
//
#define WSD_COMMUNICATION_ERROR(hr) \
    ((HRESULT_FROM_WIN32(ERROR_WINHTTP_CANNOT_CONNECT)) == hr) || \
    ((HRESULT_FROM_WIN32(ERROR_WINHTTP_CONNECTION_ERROR)) == hr) || \
    ((HRESULT_FROM_WIN32(ERROR_WINHTTP_TIMEOUT)) == hr) || \
    ((HRESULT_FROM_WIN32(ERROR_TIMEOUT)) == hr) || \
    ((HRESULT_FROM_WIN32(ERROR_WINHTTP_NAME_NOT_RESOLVED)) == hr))
```

 




