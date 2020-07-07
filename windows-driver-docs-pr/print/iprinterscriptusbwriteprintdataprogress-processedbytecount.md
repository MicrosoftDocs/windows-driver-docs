---
title: IPrinterScriptUsbWritePrintDataProgress ProcessedByteCount method (out)
description: Returns the number of bytes that the IHV JavaScript function has processed by the time this method was called.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 667DDBEA-14DA-4037-98A1-A2E7DB8B97F5
keywords: ["ProcessedByteCount method Print Devices", "ProcessedByteCount method Print Devices , IPrinterScriptUsbWritePrintDataProgress interface", "IPrinterScriptUsbWritePrintDataProgress interface Print Devices , ProcessedByteCount method"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbWritePrintDataProgress.ProcessedByteCount
api_type:
- COM
ms.date: 07/07/2020
ms.localizationpriority: medium
---

# IPrinterScriptUsbWritePrintDataProgress::ProcessedByteCount method (out)

Returns the number of bytes that the IHV JavaScript function has processed by the time this method was called.

## Syntax

```cpp
HRESULT ProcessedByteCount(
  [out, retval] UINT32 *value
);
```

## Parameters

*value* \[out, retval\]  
The number of bytes processed by the time this method was called.

## Return value

This method returns an **HRESULT** value.

## Requirements

| &nbsp; | &nbsp; |
| --- | --- |
| Minimum supported client | Windows 8.1 |
| Minimum supported server | Windows Server 2012 R2 |
| Target platform | Desktop |

## See also

[**IPrinterScriptUsbWritePrintDataProgress**](iprinterscriptusbwriteprintdataprogress.md)
