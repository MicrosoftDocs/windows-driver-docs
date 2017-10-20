---
title: Example boilerplate for handling Regular or Direct OID requests
description: This topic describes example boilerplate code for handling Regular or Direct OID requests
ms.assetid: 4C8297DD-C237-4437-A0B1-8CE0F3A6225B
ms.author: windowsdriverdev
ms.date: 09/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")