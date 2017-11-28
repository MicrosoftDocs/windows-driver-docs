---
title: CreatePostScanJobRequest Example
description: CreatePostScanJobRequest Example
ms.assetid: 19cd3467-1f38-4e83-b10c-432e2aaa2d77
keywords: ["CreatePostScanJobRequest Example"]
---

# CreatePostScanJobRequest Example



The following is an example of a SOAP message from a DSM device that contains a **CreatePostScanJobRequest** element:

```
<soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
        xmlns:dsp="http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing"
        xmlns:psp="http://schemas.microsoft.com/windows/2008/02/imaging/postscan/psp">
  <soap:Header>
    <wsa:To>DestinationAddress</wsa:To>
    <wsa:Action>http://schemas.microsoft.com/windows/2008/12/wdp/distributedscan/processing/CreatePostScanJob</wsa:Action>
    <wsa:MessageID>urn:uuid:c7a18640-1e15-48ac-8326-0026a5719d98</wsa:MessageID>
    <wsa:ReplyTo>
      <wsa:Address>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:Address>
    </wsa:ReplyTo>
  </soap:Header>
  <soap:Body>
    <dsp:CreatePostScanJobRequest>
      <dsp:UserIdentifier>S-1-5-21-917267712-1342860078-1792151419-500</dsp:UserIdentifier>
      <dsp:PSP_Identifier>C4F199C7-6876-4549-A86E-A85035952448</dsp:PSP_Identifier>
      <dsp:PostScanInstructions>
        <psp:ContinueOnError>true</psp:ContinueOnError>
        <psp:DocumentRootName>SampleScanJob</psp:DocumentRootName>
        <psp:FiltersToProcess>
          <psp:Filter>
            <psp:Dialect>http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/fileshare</psp:Dialect>
            <psp:Instructions>
              <fsh:FileShareConfig xmlns:fsh="http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/fileshare">
                <fsh:FileShares>
                  <fsh:ShareUNC>\\contoso\scratch\_prtlab\IncomingScans</fsh:ShareUNC>
                </fsh:FileShares>
              </fsh:FileShareConfig>
            </psp:Instructions>
          </psp:Filter>
          <psp:Filter>
            <psp:Dialect>http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/sharepoint</psp:Dialect>
            <psp:Instructions>
              <shp:SharePointConfig xmlns:shp="http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/sharepoint">
                <shp:SaveToMySite>false</shp:SaveToMySite>
                <shp:SaveToSharePointSites>
                  <shp:SaveToSharePointSiteURL>http://contoso/site/scans</shp:SaveToSharePointSiteURL>
                </shp:SaveToSharePointSites>
              </shp:SharePointConfig>
            </psp:Instructions>
          </psp:Filter>
          <psp:Filter>
            <psp:Dialect>http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/email</psp:Dialect>
            <psp:Instructions>
              <eml:EmailConfig xmlns:eml="http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/email">
                <eml:SendToScanUser>false</eml:SendToScanUser>
                <eml:SendToAddresses eml:CanAddAddresses="false">
                  <eml:EmailAddress>user@contoso.com</eml:EmailAddress>
                 </eml:SendToAddresses>
              </eml:EmailConfig>
            </psp:Instructions>
          </psp:Filter>
        </psp:FiltersToProcess>
      </dsp:PostScanInstructions>
    </dsp:CreatePostScanJobRequest>
  </soap:Body>
</soap:Envelope>
 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20CreatePostScanJobRequest%20Example%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




