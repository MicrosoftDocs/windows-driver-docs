---
title: Iasphelp getJobCompletionMinute method
description: The JobCompletionMinute property enables an ASP Web page to determine when the print jobs that are currently pending will be finished.
MS-HAID:
- 'webfnc63bca3eb-0ead-4430-8e82-9014d58c133b.xml'
- 'print.iasphelpjobcompletionminute'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_JobCompletionMinute method Print Devices", "get_JobCompletionMinute method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_JobCompletionMinute method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_JobCompletionMinute
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::getJobCompletionMinute method

The **JobCompletionMinute** property enables an ASP Web page to determine when the print jobs that are currently pending will be finished.

## Syntax

```cpp
HRESULT get_JobCompletionMinute(
  [out] long *pVal
);
```

## Parameters

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives the required time, in minutes, for all print jobs that are currently pending completion.

## Return value

This property returns one of the values in the following table.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

Before you query this property, call the [**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md) method to initialize the property value. To determine the number of pending print jobs, query the [**Iasphelp::PendingJobCount**](iasphelp-pendingjobcount.md) property.

```vb
Dim objPrinter, EndMinute
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
objPrinter.CalcJobETA
EndMinute = objPrinter.JobCompletionMinute
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)

[**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md)

[**Iasphelp::PendingJobCount**](iasphelp-pendingjobcount.md)
