---
title: WDI TLV parser interface overview
description: This section describes an overview of the WDI TLV parser interface
ms.assetid: FD204F24-0336-4A54-992C-ACF46565D8D1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI TLV parser interface overview


## Callee allocation model


An entry point within the driver receives a message or indication that contains TLVs. After the code extracts the message ID and determines if it is an ID that it wants to handle, it calls the generic parse routine and passes the TLV blob (after advancing past the [**WDI\_MESSAGE\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn926074)) to parse the TLVs into a C-structure.

```c
ndisStatus = Parse(
    cbBufferLength,
    pvBuffer,
    messageId,
    &Context,
    &pParsed);
```

After checking the return for errors, the code can cast the output buffer (*pParsed*) into a concrete type, such as in the below example.

```c
((WDI_INDICATION_BSS_ENTRY_LIST_PARAMETERS*)pParsed)
```

After the caller is finished with the parsed data, the caller must return the memory back to the parser. The parser needs to know the original message ID used to allocate so it frees the correct data.

```c
FreeParsed(messageId, pParsed);
pParsed = NULL;
```

## Caller allocation model


In this model, the caller has already determined the correct specific TLV to parse and is possibly using a stack local to avoid allocations on the heap. The caller creates the local and calls a specific parse routine. The API does not need the message ID, and the parameter is strongly typed with one less level of indirection.

```c
WDI_GET_ADAPTER_CAPABILITIES_PARAMETERS adapterCapabilitiesParsed;

ndisStatus = ParseWdiGetAdapterCapabilities(
    cbBufferLength,
    pvBuffer,
    &Context
    &adapterCapabilitiesParsed);
```

After the caller is finished using the structure, the caller should give the parser a chance to clean up any allocation it made during parsing, and wipe the structure so it is ready to be reused. The parameter is strongly typed, so the callee does not need any additional parameters.

```c
CleanupParsedWdiGetAdapterCapabilities(&adapterCapabilitiesParsed);
```

After calling the CleanupParse API, all data in the structure is invalid.

Some messages do not have any associated data. For completeness of the API, appropriately named Parse methods are provided. These methods validate that the byte stream is empty. Typedefs are provided for the parameter type, but callers can also pass NULL for the out parameter if they use the Caller Allocation Model. In all cases, the Parser avoids any allocations by returning a constant empty parse structure. Callers should never write into this returned empty structure (hence the only field is named **\_Reserved**). These messages are documented as "No additional data. The data in the header is sufficient".

## Message direction


Most messages have a different format for their M1 versus their M0, M3, or M4. To accommodate for this, such messages have different parse and generate APIs. For M1 messages, the APIs follow the naming convention of Parse<em>&lt;MessageName&gt;</em>ToIhv or Generate<em>&lt;MessageName&gt;</em>ToIhv. For M0, M3, or M4 messages, the APIs follow the naming convention of Parse<em>&lt;MessageName&gt;</em>FromIhv or Generate<em>&lt;MessageName&gt;</em>FromIhv. However, to simplify code in the IHV miniport, defines are added to alias Parse<em>&lt;MessageName&gt;</em> to Parse<em>&lt;MessageName&gt;</em>ToIhv and Generate<em>&lt;MessageName&gt;</em> to Generate<em>&lt;MessageName&gt;</em>FromIhv. IHV code only needs to be aware of this aliasing if it needs to parse its own M3, or generate an M1.

## Error codes


The TLV parser generator can return several different NDIS\_STATUS codes. For more information, look at the WPP trace logs. The logs should always indicate the root cause. Here is a list of the most common error codes and what they mean.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>NDIS_STATUS_INVALID_DATA</p></td>
<td align="left"><p>When parsing, this indicates that a fixed sized TLV is of the incorrect size. For lists, this means the overall size is not an even multiple of the individual element size, or there are more elements than there should be. This could also mean a list contained 0 elements, when 1 or more is required. If 0 elements is desired, then <em>Optional_IsPresent</em> should be set to false (the TLV header should not be in the byte stream).</p></td>
</tr>
<tr class="even">
<td align="left"><p>NDIS_STATUS_BUFFER_OVERFLOW</p></td>
<td align="left"><p>When generating, this indicates that due to the number of elements in an array (list), it overflows the 2 byte <strong>Length</strong> field within the TLV header. You should reduce the number of elements. This can also occur when an outer TLV has too many (or too large of) inner TLVs, again overflowing the 2 byte <strong>Length</strong> field of the header.</p>
<p>When parsing, this indicates a TLV header&#39;s <strong>Length</strong> field is larger than the outer TLV or the byte stream.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NDIS_STATUS_FILE_NOT_FOUND</p></td>
<td align="left"><p>When parsing, this indicates that a required TLV is not present in the byte stream. It is usually a bug with the generator of the byte stream.</p></td>
</tr>
<tr class="even">
<td align="left"><p>NDIS_STATUS_RESOURCES</p></td>
<td align="left"><p>When generating, this indicates that the allocator failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NDIS_STATUS_UNSUPPORTED_REVISION</p></td>
<td align="left"><p>When parsing or generating, the <strong>Context</strong> parameter is NULL, or the <strong>PeerVersion</strong> is less than <strong>WDI_VERSION_MIN_SUPPORTED</strong>.</p></td>
</tr>
</tbody>
</table>

 

 

 





