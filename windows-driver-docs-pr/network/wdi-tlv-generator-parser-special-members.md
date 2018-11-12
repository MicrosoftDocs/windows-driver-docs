---
title: WDI TLV generator/parser special members
description: This section describes special members for the WDI TLV generator/parser
ms.assetid: 2FD485E5-E2F9-4B21-A777-ABA9693B1223
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI TLV generator/parser special members


## Optional members


For any TLV that has optional child TLV members, the parent has one field named **Optional**. Within that field, there is one Boolean field for each optional child named ***&lt;child\_name&gt;*\_IsPresent**, which is set to TRUE by the parser if the child is present, and FALSE otherwise. Similarly, the generation APIs expect the field to be TRUE if it should be present in the TLV byte stream, and FALSE otherwise.

```C++
WDI_SET_FIRMWARE_CONFIGURATION_PARAMETERS fwConfig = { 0 };
NDIS_STATUS status;
status = ParseWdiSetAdapterConfiguration(
    pNdisRequest->DATA.METHOD_INFORMATION.InputBufferLength - 
        sizeof(WDI_MESSAGE_HEADER),
    (PUINT8)pNdisRequest->DATA.METHOD_INFORMATION.InformationBuffer + 
        sizeof(WDI_MESSAGE_HEADER),
    0,
    &fwConfig);

if (status == NDIS_STATUS_SUCCESS)
{
    if (fwConfig.Optional.MacAddress_IsPresent)
    {
        // Safe to use fwConfig.MacAddress
        fwConfig.MacAddress;
    }
}
```

## Array members


When multiple children of the same type appear within the same parent (for example, &lt;container /&gt;'s *isCollection* attribute), the parser and generator use a special structure to represent the array: ArrayOfElements. For C++ clients, this is a strongly typed template structure with clean up on destruction semantics. For C clients, explicitly named structures are created (for example, ArrayOfElementsOfUINT8). However, these structures are not automatically cleaned up because C does not support destructors, so users of the C APIs must be careful not to introduce memory leaks (or double-frees).

There are two important fields within ArrayOfElements: **ElementCount** and **pElements**. **ElementCount** is the count of elements within the array. **pElements** is a C-Style array of the elements. The elements can be iterated over as shown in this sample.

```C++
for (UINT32 i = 0;
    i < pConnectTaskParameters->ConnectParameters.
            MulticastCipherAlgorithms.ElementCount;
    i++)
{
    // Safe to use pElements[i]
    pConnectTaskParameters->ConnectParameters.MulticastCipherAlgorithms.
        pElements[i];
}
```

The third field, **MemoryInternallyAllocated**, is used internally by the parser/generator. It should not be modified by the IHV.

 

 





