---
title: GetJobHistory
description: GetJobHistory
ms.assetid: 330351fd-8a75-4e3c-b3f0-3211144393e9
keywords: ["GetJobHistory"]
---

# GetJobHistory


The **GetJobHistory** operation requests a summary list of the scan jobs that the scanner has recently completed. The returned list contains information about the scan jobs such as **JobId**, **JobOriginatingUserName***,* and the **JobName**.

The amount of data returned in this operation is device specific and depends on the amount of scan job history data that the scanner maintains.

To retrieve more detailed information about a scan job, use the **GetJobElements** operation.

The **GetJobHistory** operation supports the following sub-elements:

[GetJobHistoryRequest](getjobhistoryrequest2.md)

[GetJobHistoryResponse](getjobhistoryresponse4.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20GetJobHistory%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




