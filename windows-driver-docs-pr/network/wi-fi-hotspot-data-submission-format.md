---
title: Wi-Fi Hotspot Data Submission Format
description: Wi-Fi Hotspot Data Submission Format
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Wi-Fi Hotspot Data Submission Format

> [!IMPORTANT]
> Starting in Windows 10, version 1709, the Wi-Fi Hotspot Offloading feature is deprecated and should not be used. 

Hotspot data submitted to the discovery service must be in JavaScript Object Notation (JSON) and must use the following elements.

| Element | Type | Description |
| --- | --- | --- |
| BatchId | GUID | A provider can split a single submission that contains multiple hotspots into multiple submissions. Each submission is assigned the same BatchId GUID. |
| ProviderId | GUID | The provider ID will be assigned to the provider by Microsoft. |
| TransactionId | int | An incrementing number for each request in the batch. Used for degbugging purposes. |
| Hotspots |  | A list of hotspots to upload. |
| add |  | The full address property, which includes the following sub-elements: **Address**, **City**, **StateOrProvince**, **PostalCode**, and **CountryOrRegion**. |
| bssids| List\<string> | A list of the BSSIDs that make up the hotspot. Each BSSID consists of eight two digit hexadecimal values in the in the following format: *00:aa:bb:cc:dd:ee*. |
| free | Boolean | A Boolean value that indicates whether the hotspot is free. |
| pub | Boolean | A Boolean value that indicates whether the hotspot is public. |
| loc |  | The full location property which includes the following sub-elements: **Latitude**, **Longitude**, **RadialUncertainty**, **Altitude**, and **AltitudeUncertainty**. |
| name | string | The friendly name of the hotspot. |
| phid | string | The provider's hotspot ID. Used for debugging purposes. |
| ran | uint | The range of the hotspot. |
| ssid | string | The hotspot's SSID. |
| phone | string | A list of all the phone numbers associated with the hotspot. |

**Note**

* The header and its sub-elements (**ProviderId**, **BatchId**, and **TransactionId**) are required.
* The Hotspots list must not be empty.
* If the Location element is specified then **Latitude** and **Longitude** are required.
* If the Location element is not specified then at least one BSSID must be specified. Otherwise, a warning will be returned and the discovery service will not process the hotspot.

The following example shows the complete data for a single hotspot:

```JSON
{
      "Header": {
            "BatchId": "BA85A383-5943-4D84-8ACB-B113BDEA3783", 
            "ProviderId": "AE012377-B0B4-4096-B5D5-D7EFBDC170EC", 
            "TransactionId": 1
      }, 
      "Hotspots":[{
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

The discovery service returns a simple response, also in JSON format, that includes the activity ID used for debugging purposes and a list of warnings that were generated when the discovery service validated the hotspot data. All strings returned by the discovery service are encoded in UTF-8.

The following table shows the JSON elements for a discovery service response.

| Element | Type | Description |
| --- | --- | --- |
| ActivityId | string | Required. This is a string that the provider can use to help debug issues. |
| Warnings | List\<string> | A human-readable list of warnings. |

The following example shows a typical response to a hotspot data submission:

```JSON
{
     "ActivityId": "d2856c06-e4a1-4434-90e8-ced0c9ee6e10",
     "Warnings": ["Invalid Latitude: 247.67 – Hotspot Id: abcdefg"]
}
```

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
