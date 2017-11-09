---
title: GetPostScanJobElementsResponse Example
description: GetPostScanJobElementsResponse Example
MS-HAID:
- 'dsm\_ref\_dsp\_fa3318a5-bbcc-4b69-bed6-57abad1bc477.xml'
- 'image.getpostscanjobelementsresponse\_example'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3b0fcd15-930d-4fcb-99da-60cf444aae92
keywords: ["GetPostScanJobElementsResponse Example"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20GetPostScanJobElementsResponse%20Example%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




