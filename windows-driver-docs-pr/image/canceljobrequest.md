---
title: CancelJobRequest element
description: The required CancelJobRequest operation enables a client to cancel a scan job.
ms.assetid: 781fae32-2827-48d8-8aed-7f437326919d
keywords: ["CancelJobRequest element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn CancelJobRequest
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CancelJobRequest element


The required **CancelJobRequest** operation enables a client to cancel a scan job.

Usage
-----

``` syntax
<wscn:CancelJobRequest>
  child elements
</wscn:CancelJobRequest>
```

Attributes
----------

There are no attributes.

Text value
----------

None

## Child elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>JobId</strong>](jobid.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

[**JobId**](jobid.md)

A client can cancel a scan job from the time the job is created up to the time it is completed, canceled, or aborted. The [**JobId**](jobid.md) element identifies the job that the client is trying to cancel.

The WSD Scan Service should move the specified job to the **Terminating** state if the job was at a **Pending** or **Active** state. It is an error to attempt to cancel a completed or canceled job or to try canceling any job that the client does not have rights to.

[**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md)[WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md)

This operation can return all of the [**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md). For more information about how to report errors, see [WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md).

**CancelJobRequest** can also return the following error code:

-   **ClientErrorJobIdNotFound**

## <span id="see_also"></span>See also


[**CancelJobResponse**](canceljobresponse.md)

[**JobId**](jobid.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20CancelJobRequest%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





