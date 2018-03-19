---
title: CreatePostScanJobRequest Example
description: CreatePostScanJobRequest Example
ms.assetid: 19cd3467-1f38-4e83-b10c-432e2aaa2d77
keywords: ["CreatePostScanJobRequest Example"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 





