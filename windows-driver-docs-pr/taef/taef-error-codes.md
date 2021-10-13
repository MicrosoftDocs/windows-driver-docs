---
title: TAEF Error Codes
description: TAEF Error Codes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TAEF Error Codes


TAEF can encounter errors for a variety of reasons, such as being unable to connect to a machine for cross machine execution or receiving invalid values for well-known test metadata. When errors occur, TAEF shows an error message and often an HRESULT value associated with the error. Most of the HRESULT values are [well-known system error codes](/windows/desktop/Debug/system-error-codes), but TAEF will sometimes show custom error codes.

## <span id="Custom_TAEF_HRESULT_Values"></span><span id="custom_taef_hresult_values"></span><span id="CUSTOM_TAEF_HRESULT_VALUES"></span>Custom TAEF HRESULT Values


TAEF's custom HRESULT values will be documented in the table below as they are added. Currently, there is only one TAEF-specific HRESULT value.

| HRESULT                             | Value      | Description                                                                                                                                                                                                                                    |
|-------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TAEF\_E\_INVALID\_TEST\_ENVIRONMENT | 0x81A40001 | A TAEF test requested an invalid test environment via its metadata. Examples of metadata that affect the test environment include [RunAs](runas.md), [ThreadingModel](threading-models.md), and [ActivationContext](activation-context.md). |

 

 

