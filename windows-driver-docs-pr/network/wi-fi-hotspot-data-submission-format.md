---
title: Wi-Fi Hotspot Data Submission Format
description: Wi-Fi Hotspot Data Submission Format
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Wi-Fi Hotspot Data Submission Format

[!include[Wi-Fi Hotspot Offloading deprecation](../includes/wi-fi-hotspot-offloading-deprecation.md)]

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

