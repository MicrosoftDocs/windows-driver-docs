---
title: Iasphelp getMediaReady method
description: The MediaReady property enables an ASP Web page to obtain a set of strings that name all of the paper forms for the printer that are currently available for use.
MS-HAID:
- 'webfncb10e8434-7e12-4bb5-8c43-77cb890f72a8.xml'
- 'print.iasphelpmediaready'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_MediaReady method Print Devices", "get_MediaReady method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_MediaReady method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_MediaReady
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::getMediaReady method

The **MediaReady** property enables an ASP Web page to obtain a set of strings that name all of the paper forms for the printer that are currently available for use.

## Syntax

```cpp
HRESULT get_MediaReady(
  [out] VARIANT *pVal
);
```

## Parameters

*pVal* \[out\]  
A caller-supplied location to receive a pointer to a set of strings that name all of the paper forms for a printer that are currently available for use.

## Return value

This property returns one of the values in the following table.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

This method obtains a list of the names of the paper forms that are currently available for use by calling the printer driver's [**DrvDeviceCapabilities**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicecapabilities) function with the DCMEDIAREADY flag set.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::MediaReady** property can be queried.

```vb
Dim objPrinter, MediaReadyArray
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
MediaReadyArray = objPrinter.MediaReady
```

## Requirements

**Target platform:** Desktop

## See also

[**DrvDeviceCapabilities**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicecapabilities)

[**Iasphelp::Open**](iasphelp-open.md)
