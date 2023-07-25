---
title: IPrinterScriptUsbWritePrintDataProgress ProcessedByteCount method (in)
description: Sets the number of bytes that the IHV JavaScript function has processed at the time this method was called.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["ProcessedByteCount method Print Devices", "ProcessedByteCount method Print Devices , IPrinterScriptUsbWritePrintDataProgress interface", "IPrinterScriptUsbWritePrintDataProgress interface Print Devices , ProcessedByteCount method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbWritePrintDataProgress.ProcessedByteCount
api_type:
- COM
ms.date: 07/14/2023
---

# IPrinterScriptUsbWritePrintDataProgress::ProcessedByteCount method (in)

Sets the number of bytes that the IHV JavaScript function has processed at the time this method was called.

## Syntax

```cpp
HRESULT ProcessedByteCount(
  [in]  UINT32 value
);
```

## Parameters

*value* \[in\]  
The number of bytes processed at the time this method was called.

## Return valueS

This method returns an **HRESULT** value.

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2

**Target platform:** Desktop

## See also

[**IPrinterScriptUsbWritePrintDataProgress**](iprinterscriptusbwriteprintdataprogress.md)
