---
title: Iasphelp get_PendingJobCount method
description: The PendingJobCount property enables an ASP Web page to determine the number of pending print jobs.
MS-HAID:
- 'webfnc_fd1cbaac-f195-4a38-8788-990eb9b3fd6c.xml'
- 'print.iasphelp_pendingjobcount'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_PendingJobCount method Print Devices", "get_PendingJobCount method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_PendingJobCount method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_PendingJobCount
api_type:
- COM
ms.date: 06/26/2023
---

# Iasphelp::get_PendingJobCount method

The **PendingJobCount** property enables an ASP Web page to determine the number of pending print jobs.

## Syntax

```cpp
HRESULT get_PendingJobCount(
  [out] long *pVal
);
```

## Parameters

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives the number of pending print jobs.

## Return value

This property returns one of the values in the following table.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

Before you query this property, call the [**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md) method to initialize the property value.

```vb
Dim objPrinter
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
objPrinter.CalcJobETA
PendingJobs = objPrinter.PendingJobCount
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)

[**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md)
