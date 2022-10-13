---
title: DD_DXAPI_ADDVPCAPTUREBUFFER control code (Windows Drivers)
description: Learn more about the DD_DXAPI_ADDVPCAPTUREBUFFER control code.
keywords:
- DD_DXAPI_ADDVPCAPTUREBUFFER
- ddkmapi/DD_DXAPI_ADDVPCAPTUREBUFFER
ms.date: 10/12/2022
---

# DD\_DXAPI\_ADDVPCAPTUREBUFFER control code

A video capture driver passes DD\_DXAPI\_ADDVPCAPTUREBUFFER in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to add a new capture buffer to the internal video port capture queue.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDADDVPCAPTUREBUFF**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddaddvpcapturebuff) structure that contains the information required to add a new buffer.

## Output Parameters

- *lpvInBuffer*  
    Pointer to a DWORD that contains the DirectDraw return value.

## Remarks

Each time a hardware video port V-sync occurs, the kernel-mode video transport determines whether the previous field needs to be captured and if so, initiates a bus master to the next buffer in the queue.

This function identifier can be called at raised IRQL.

## Requirements

| | |
| --- | --- |
| Header | Ddkmapi.h (include Ddkmapi.h) |

## See also

[**DDADDVPCAPTUREBUFF**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddaddvpcapturebuff)
