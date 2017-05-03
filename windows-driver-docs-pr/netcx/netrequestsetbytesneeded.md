---
title: NetRequestSetBytesNeeded method
topic_type:
- apiref
api_name:
- NetRequestSetBytesNeeded
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestSetBytesNeeded method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Sets the number of bytes needed to read or write for a control request (OID).

Syntax
------

```cpp
VOID NetRequestSetBytesNeeded(
  _In_ NETREQUEST Request,
  _In_ UINT       BytesNeeded
);
```

Parameters
----------

*Request* [in]  
A handle to a network request object.

*BytesNeeded* [in]  
Number of bytes to be read or written.

Remarks
---
The client calls this routine if the I/O request fails due a smaller than expected InputOutputBuffer size.  For example, to report that 8 bytes are required to support the requested OID:

```cpp
status = STATUS_BUFFER_TOO_SMALL;
NetRequestSetBytesNeeded(Request, sizeof(ULONG64));
```

Depending on the request type, *BytesNeeded* may mean space required perform a read operation or a write operation. 

After calling **NetRequestSetBytesNeeded**, the client calls one of the following methods, or  [**NetRequestCompleteWithoutInformation**](netrequestcompletewithoutinformation.md):

    * [**NetRequestMethodComplete**](netrequestmethodcomplete.md)
    * [**NetRequestQueryDataComplete**](netrequestquerydatacomplete.md)
    * [**NetRequestSetDataComplete**](netrequestsetdatacomplete.md)

For general info about control requests, see [Handling Control Requests](handling-control-requests.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Universal</td>
</tr>
<tr class="even">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Netrequest.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;=DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





