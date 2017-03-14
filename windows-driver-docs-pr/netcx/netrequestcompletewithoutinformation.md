---
title: NetRequestCompleteWithoutInformation method
topic_type:
- apiref
api_name:
- NetRequestCompleteWithoutInformation
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestCompleteWithoutInformation method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Completes a NETREQUEST and supplies a completion status.

Syntax
------

```cpp
VOID NetRequestCompleteWithoutInformation(
  _In_ NETREQUEST Request,
  _In_ NTSTATUS   CompletionStatus
);
```

Parameters
----------

*Request* [in]  
A handle to a network request object that represents the control (OID) request that is being completed.

*CompletionStatus* [in]  
An NTSTATUS value that represents the completion status of the request.  Valid status values include, but are not limited to, the following:

|Return code|Description|
|--|--|
|STATUS_SUCCESS|The driver successfully completed the request.|
|STATUS_CANCELLED|The driver canceled the request.|
|STATUS_UNSUCCESSFUL|The driver encountered an error while processing the request.|

Remarks
-----
Typically, the client driver calls **NetRequestCompleteWithoutInformation** from one of its control request handler routines.  For more info, see [Handling Control Requests](handling-control-requests.md#completing-requests).

After this method returns, the request handle is no longer valid.  NetAdapterCx removes it from the NETQUEUE and deletes the NETREQUEST object.

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
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

See Also
-----
[**NetRequestMethodComplete**](netrequestmethodcomplete.md)  
[**NetRequestQueryDataComplete**](netrequestquerydatacomplete.md)  
[**NetRequestSetDataComplete**](netrequestsetdatacomplete.md)  
