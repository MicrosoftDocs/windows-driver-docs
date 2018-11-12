---
title: WDI TLV generator interface overview
description: This section describes an overview of function models for the WDI TLV generator interface
ms.assetid: 8A344BF7-932E-4404-9B3E-E7D3C33722C3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI TLV generator interface overview


## C++ overloaded function model


In this model, there is only one function call to generate a TLV byte array from your data structure.

```c++
WDI_INDICATION_BSS_ENTRY_LIST_PARAMETERS BssEntryList = ...;
BYTE* pOutput = NULL;
ULONG length = 0;
NDIS_STATUS ndisStatus = NDIS_STATUS_SUCCESS;

ndisStatus = Generate(
    &BssEntryList,
    cbHeaderLength,
    &Context,
    &length,
    &pOutput);
```

The second parameter can be very helpful. Sometimes, the TLV buffer is packed into a bigger data structure, and this parameter allows you to pre-reserve space at the beginning of the buffer for that header. The correct value for *cbHeaderLength* is often `sizeof(WDI_MESSAGE_HEADER)`.

For messages that have no associated data, there are still overloaded Generate APIs, but the first parameter is optional and may simply be passed in as `(EmptyMessageStructureType*)NULL`.

When you are done with the TLV data contained in *pOutput*, you must call back into the library to release the buffer.

```c++
    FreeGenerated(pOutput);
    pOutput = NULL;
```

## C-style function model


In this model, there is a specific Generate routine for each top-level message or structure because C does not support overloaded functions. Otherwise, it behaves the same as the C++ model.

```c
ndisStatus = GenerateWdiGetAdapterCapabilities(
    &adapterCapabilities,
    (ULONG)sizeof(WFC_COMMAND_HEADER),
    &Context,
    &length,
    &pOutput);
```

When you are done with the TLV byte array, call back to release the memory in the same way as the C++ model.

```c
    FreeGenerated(pOutput);
    pOutput = NULL;
```

 

 





