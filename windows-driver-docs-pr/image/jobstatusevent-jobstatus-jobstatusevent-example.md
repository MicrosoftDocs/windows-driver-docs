---
title: JobStatusEvent.JobStatus.JobStatusEvent Example
description: JobStatusEvent.JobStatus.JobStatusEvent Example
ms.assetid: eee045c6-1116-4187-b0d6-e907f0699008
keywords: ["JobStatusEvent.JobStatus.JobStatusEvent Example"]
---

# JobStatusEvent.JobStatus.JobStatusEvent Example


In the following example, the scanner notifies the control point of the current state of job 253.

```
<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
    xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
    xmlns:wse="http://schemas.xmlsoap.org/ws/2004/08/eventing"
    xmlns:wscn="http://schemas.microsoft.com/windows/2006/08/wdp/scan" 
    xmlns:dsd="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/device">
  <soap:Header>
    <wsa:To>AddressofEventSink</wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/08/wdp/scan/JobStatusEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>
  <soap:Body>
    <dsd:JobStatusEvent>
      <dsd:JobStatus>
        <wscn:JobId>253</wscn:JobId>
        <wscn:JobState>Processing</wscn:JobState>
        <wscn:JobStateReasons>
          <wscn:JobStateReason>JobScanning</wscn:JobStateReason>
        </wscn:JobStateReasons>
        <wscn:ScansCompleted>4</wscn:ScansCompleted>
        <wscn:JobCreatedTime>2006-01-24T11:34:35.8345Z</wscn:JobCreatedTime>
      </dsd:JobStatus>
    </dsd:JobStatusEvent>
  </soap:Body>
</soap:Envelope>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobStatusEvent.JobStatus.JobStatusEvent%20Example%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




