---
title: Wi-Fi Discovery Service
description: Wi-Fi Discovery Service
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Wi-Fi Discovery Service

The Wi-Fi discovery service enables users to reduce data costs by offloading cellular traffic to Wi-Fi hotspots. The discovery service aggregates Wi-Fi hotspot data from providers, such as mobile operators, and other sources to produce a directory of known Wi-Fi hotspots. By using this directory, users can obtain information about hotspots near their current position.

Mobile operators can submit hotspot data to the service by sending an HTTP POST request, or by using a command-line tool provided by Microsoft.

## Instructions

Wi-Fi hotspot data must be in the format described in [Wi-Fi Hotspot Data Submission Format](wi-fi-hotspot-data-submission-format.md).

The discovery service requires that all of a provider's hotspots are submitted in a single batch. Each batch can contain multiple submission requests with a smaller amount of data. For example, a batch containing 1,000 hotspots can be uploaded to the discovery service by sending 10 submission requests, each containing data for 100 hotspots. Each submission request is assigned the same batch number. The final submission request must include a `X-FinalBatchRequest` header set to the total number of hotspots in the batch. The batch is not processed until a submission request with this header is received. If the header does not match the number of hotspots in the batch, the submission is not processed.

### Submitting hotspot data by using HTTP POST

The following example shows a typical submission request. The presence of the `X-FinalBatchRequest` header and the numeric value of "1" indicate that there is only one hotspot in this batch and this is the final submission request. Therefore, this is the only submission request. If the batch contained multiple hotspots, this line should be removed for all submission requests but the last one.

```http
POST https://submitwifiservice.windowsphone.com/v1/SubmitHotspots HTTP/1.1
Content-Type: application/json
X-FinalBatchRequest: 1
 [More headers…]
{
      "Header": {
            "BatchId": "2E20A8DB-9AFA-4A5A-AF6E-5F87DA639C15", 
            "TransactionId": 1, 
            "ProviderId": "FD9E5EE6-75C7-4A54-8B29-45A3FC83AD63"
      }, 
      "Hotspots": {
            "add": {
                  "Address": "123 abc street", 
                  "City": "Redmond", 
                  "CountryOrRegion": "USA", 
                  "PostalCode": "98052", 
                  "StateOrProvince": "WA"
            },

            "bssids":["00:aa:bb:cc:dd:ee"],
            "free": true, 
            "pub": true, 
            "loc": {
                  "Latitude": 47.01, 
                  "Longitude": 121.1234, 
                  "RadialUncertainty": 300, 
                  "Altitude": 638.34, 
                  "AltitudeUncertainty": 100.0 
            }, 
            "name": "Joes Coffee Shop", 
            "phid": "abcdefg", 
            "ran": 100, 
            "ssid": "JoesCoffee", 
            "phone": ["425-882-8080"]
      }
}
```

When the message is received on the destination server, **SubmitHotspots** validates the request and authenticates the sender before sending the hotspot data to the discovery service.

### Submitting hotspot data by using the command line tool

WifiProviderExe.exe is a command-line tool, provided by Microsoft, that takes as input a hotspot data file, converts it to the required format, and uploads it to a specified discovery service server.

To run WiFiProvider.exe, use the following syntax:

```cmd
WifiProviderExe –DataFile filename -ProviderId GUID -ServiceEndpoint URL -CustomTransformer filename.dll [-MappingFile filename.xml] [-CertFile filename.pfx] [-CertPassword password] [-CertSubject name]
```

For example:

```cmd
WifiProviderExe -DataFile "file.txt" -ProviderId 00000000-0000-0000-0000-000000000000 -ServiceEndpoint "https://submitwifiservice.windowsphone.com/v1/SubmitHotspots" -CustomTransformer "transformer.dll"
```

The following table contains the list of possible parameters for WiFiProvider.exe.

| Parameter | Description |
| --- | --- |
| DataFile | Required. The name of the file that contains the hotspot data. |
| ProviderId | Required. The Microsoft-assigned provider ID (a GUID). |
| ServiceEndpoint | Required. The URL of the discovery service server to which the hotspot data will be uploaded. For example, https://wifi.windowsphone.com/v1/submithotspots |
| CustomerTransformer | Required. The name of the assembly that contains the transformer. | 
| MappingFile | Optional. The mapping file that maps the provider's hotspot data to the format required by the discovery service. |
| CertFile | Optional. A pointer to the actual pfx file that contains the certificate(s) for authentication. The certificate password parameter (**CertPassword**) must be specified when using this authentication method. |
| CertPassword | Optional. The password to the certificate specified in **CertFile**. |
| CertSubject | Optional. The subject name of the certificate. It is located in current user's My Cert store. When using this authentication mechanism, **CertFile** and **CertPassword** are not required. However, it is required to create a private key for the certificate and, in the access control list, grant access rights for the key to the account that will use the certificate. |

#### Transformers

The hotspot data can be in any format. However, it is required to specify a "data transformer" that the command-line tool can access to convert the hotspot data to the format required by the discovery service.

The following table shows the sample transformers that are provided with the command-line tool. They can be used to convert specific data formats to the required format.

| Transformer | Data Format | Description |
| --- | --- | --- |
| Microsoft.Wps.WifiService.ProviderSdk.JsonHotspotDataTransformer.dll | JSON | Your data must conform to the JSON format specified in [Wi-Fi Hotspot Data Submission Format](wi-fi-hotspot-data-submission-format.md). |
| Microsoft.Wps.WifiService.ProviderSdk.JsonHotspotDataTransformer.dll | Simple Excel | You must supply a mapping file. |

#### Mapping Files

If your hotspot data is in simple Excel format, you must supply an XML file that maps columns in the Excel file to corresponding required JSON elements. The following list shows the allowed column names:

* Latitude
* Longitude
* RadialUncertainty
* Altitude
* AltitudeUncertainty
* HotspotName
* SSID
* Range
* Address
* City
* StateOrProvince
* PostalCode
* CountryOrRegion
* Bssids
* ProviderHotspotId
* IsPublic
* IsFree
* PhoneNumbers

The following example shows a portion of a mapping file. Each **MappingRule** element associates an Excel column (**PartnerColumnName** and **PartnerColumnNumber**) with a required JSON element (**MicrosoftColumnName**). The **ContainsHeaderRow** element, located after the closing Rules tag (`</Rules>`), indicates that the file contains a header row, which should be skipped when reading data.

```xml
<?xml version="1.0" encoding="utf-8"?>
<MappingRules xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <Rules>
    <MappingRule>
      <PartnerColumnName>english_hotspot_name</PartnerColumnName>
      <PartnerColumnNumber>3</PartnerColumnNumber>
      <MicrosoftColumnName>HotspotName</MicrosoftColumnName> 
    </MappingRule>
    <MappingRule>
      <PartnerColumnName>english_city_name</PartnerColumnName>
      <PartnerColumnNumber>2</PartnerColumnNumber>
      <MicrosoftColumnName>City</MicrosoftColumnName>
    </MappingRule>
    <MappingRule>
      <PartnerColumnName>ssid</PartnerColumnName>
      <PartnerColumnNumber>4</PartnerColumnNumber>
      <MicrosoftColumnName>SSID</MicrosoftColumnName>
    </MappingRule>
    <MappingRule>
      <PartnerColumnName>venue</PartnerColumnName>
      <PartnerColumnNumber>7</PartnerColumnNumber>
      <MicrosoftColumnName>HotspotType</MicrosoftColumnName>
    </MappingRule>
        .
        .
        .
        .    
  </Rules>
  <ContainsHeaderRow>true</ContainsHeaderRow>
</MappingRules>
```

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")