---
title: GetPostScanJobElementsResponse Example
description: GetPostScanJobElementsResponse Example
ms.assetid: 3b0fcd15-930d-4fcb-99da-60cf444aae92
keywords: ["GetPostScanJobElementsResponse Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GetPostScanJobElementsResponse Example


The following is an example of a SOAP message from a DSM scan server that contains a **GetPostScanJobElementsResponse** element:

```
<soap:Envelope 
 xmlns:soap="http://www.w3.org/2003/05/soap-envelope" 
        xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
   xmlns:dsp="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing">
 <soap:Header>
    <wsa:To>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:To>
 <wsa:Action>
http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing/GetPostScanJobElementsResponse
 </wsa:Action>
    <wsa:MessageID>urn:uuid:fe5ee298-6fbf-4f6a-847d-55c3f15a3487</wsa:MessageID>
    <wsa:RelatesTo>urn:uuid:a79fe111-170d-4699-95d8-a896564aa7d6</wsa:RelatesTo> </soap:Header>
 <soap:Body>
    <dsp:GetPostScanJobElementsResponse>
      <dsp:JobElements>
        <dsp:ElementData dsp:Name="dsp:JobStatus" dsp:Valid="true">
          <dsp:JobStatus>
            <dsp:JobToken>0c349cb0-59ed-4d02-b6d5-ebc729c73830</dsp:JobToken>
            <dsp:JobState>Creating</dsp:JobState>
            <dsp:FilterStatuses>
              <dsp:FilterStatus>
                <dsp:Dialect>
 http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/fileshare
 </dsp:Dialect>
                <dsp:FilterState>Pending</dsp:FilterState>
              </dsp:FilterStatus>
            </dsp:FilterStatuses>
            <dsp:ImagesReceived>1</dsp:ImagesReceived>
            <dsp:JobCreatedTime>2009-04-28T18:37:19.519</dsp:JobCreatedTime>
          </dsp:JobStatus>
        </dsp:ElementData>
        <dsp:ElementData dsp:Name="dsp:JobDescription" dsp:Valid="true">
          <dsp:JobDescription>
            <dsp:PSP_Identifier>614655A4-38A5-46C4-B768-B6329EC5F318</dsp:PSP_Identifier>
            <dsp:PSP_DisplayName>FileShare Process</dsp:PSP_DisplayName>
            <dsp:JobOriginatingUserName>User1@contoso.com</dsp:JobOriginatingUserName>
          </dsp:JobDescription>
        </dsp:ElementData>
      </dsp:JobElements>
    </dsp:GetPostScanJobElementsResponse>
 </soap:Body>
</soap:Envelope>
```

 

 





