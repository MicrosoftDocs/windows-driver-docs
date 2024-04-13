---
title: Example boilerplate for handling Regular or Direct OID requests
description: This topic describes example boilerplate code for handling Regular or Direct OID requests
ms.date: 09/28/2017
---

# Example boilerplate for handling Regular or Direct OID requests

This topic provides example boilerplate code for handling Regular or Direct OID requests, to contrast against the examples in [Synchronous OID Request Interface in NDIS 6.80](synchronous-oid-request-interface-in-ndis-6-80.md). The Synchronous OID Request Interface is available on Windows 10, version 1709 and later.

```cpp
NDIS_STATUS
FilterOidRequest(
  NDIS_HANDLE     FilterModuleContext,
  PNDIS_OID_REQUEST  Request)
{
  PMS_FILTER       pFilter = (PMS_FILTER)FilterModuleContext;

  Status = NdisAllocateCloneOidRequest(pFilter->FilterHandle,
                     Request,
                     FILTER_TAG,
                    &ClonedRequest);
  if (Status != NDIS_STATUS_SUCCESS)
    return Status;

  Context = (PFILTER_REQUEST_CONTEXT)(&ClonedRequest->SourceReserved[0]);
  *Context = Request;

  ClonedRequest->RequestId = Request->RequestId;

  Status = NdisFOidRequest(pFilter->FilterHandle, ClonedRequest);

  if (Status != NDIS_STATUS_PENDING)
  {
    FilterOidRequestComplete(pFilter, ClonedRequest, Status);
    Status = NDIS_STATUS_PENDING;
  }
  return Status;
}

VOID
FilterOidRequestComplete(
  NDIS_HANDLE     FilterModuleContext,
  PNDIS_OID_REQUEST  Request,
  NDIS_STATUS     Status)
{
  PMS_FILTER             pFilter = (PMS_FILTER)FilterModuleContext;
  PNDIS_OID_REQUEST          OriginalRequest;

  Context = (PFILTER_REQUEST_CONTEXT)(&Request->SourceReserved[0]);
  OriginalRequest = (*Context);

  //
  // Copy the information from the returned request to the original request
  //
  switch(Request->RequestType)
  {
    case NdisRequestMethod:
      OriginalRequest->DATA.METHOD_INFORMATION.OutputBufferLength = Request->DATA.METHOD_INFORMATION.OutputBufferLength;
      OriginalRequest->DATA.METHOD_INFORMATION.BytesRead = Request->DATA.METHOD_INFORMATION.BytesRead;
      OriginalRequest->DATA.METHOD_INFORMATION.BytesNeeded = Request->DATA.METHOD_INFORMATION.BytesNeeded;
      OriginalRequest->DATA.METHOD_INFORMATION.BytesWritten = Request->DATA.METHOD_INFORMATION.BytesWritten;
      break;

    case NdisRequestSetInformation:
      OriginalRequest->DATA.SET_INFORMATION.BytesRead = Request->DATA.SET_INFORMATION.BytesRead;
      OriginalRequest->DATA.SET_INFORMATION.BytesNeeded = Request->DATA.SET_INFORMATION.BytesNeeded;
      break;

    case NdisRequestQueryInformation:
    case NdisRequestQueryStatistics:
    default:
      OriginalRequest->DATA.QUERY_INFORMATION.BytesWritten = Request->DATA.QUERY_INFORMATION.BytesWritten;
      OriginalRequest->DATA.QUERY_INFORMATION.BytesNeeded = Request->DATA.QUERY_INFORMATION.BytesNeeded;
      break;
  }

  NdisFreeCloneOidRequest(pFilter->FilterHandle, Request);

  NdisFOidRequestComplete(pFilter->FilterHandle, OriginalRequest, Status);
}
```

