---
title: DYNAMO prepaid experience
description: This topic describes the optional prepaid experience for the DYNAMO program.
ms.assetid: 908AB4DE-A4C8-4758-9632-F7F7381FF737
keywords:
- Windows DYNAMO prepaid experience, DYNAMO prepaid experience mobile operators
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DYNAMO prepaid experience

Enabling support for an enhanced prepaid experience is optional for mobile operators who onboard with DYNAMO. This topic describes incremental changes to the primary postpaid experience described in the other topics in this section, focusing on the differences needed to light up the prepaid scenario. 

## Overview

By implementing the prepaid experience, you can offer these benefits to your consumers:

- Consumers can see how much data is available, and the amount of time left until their subscriptions expire, in the network flyout.
- Consumers can top up their prepaid subscriptions over mobile connectivity, even when they run out of prepaid balance or their subscriptions has expired.
- You can manage your network flyout offering based on the consumers’ subscription status.

To implement prepaid, follow these steps:

1. Update the Windows COSA database.
2. Implement the Get Balance API.
3. Implement a Walled Garden.
4. Validate the Get Balance API and Walled Garden.
5. Comply with API load requirements.

## Update Windows COSA database

To ensure that the DYNAMO experience is properly shown in the Windows Connections Manager, also known as the network flyout, you first need to update the Windows COSA database.

> [!TIP]
> Updating COSA on Windows devices takes a considerable amount of time and might become a project constraint, so you should submit this request as early as possible.

**IMAGE**

After you update COSA, tapping or clicking on the your connection in the network flyout will expand it with more options (shown as “Contoso Cellular” in the following image). When a user expands the cellular connection, a “Connect with a data plan” option is displayed. Tapping or clicking on this option will launch the Mobile Plans app.

**IMAGE**

The following figure shows an example of how users can see the amount of data and time they have left on a prepaid subscription.

**IMAGE**

### How to request a COSA database update

For information on the COSA database submission process, see [Planning your desktop COSA/APN database submission](planning-your-desktop-cosa-apn-database-submission.md). 

### COSA database settings details

This section explains which settings in COSA are required for DYNAMO onboarding and which are recommended.

For more info about all supported fields, see the Desktop COSA-only settings on [Desktop COSA/APN database settings](desktop-cosa-apn-database-settings.md).

To download the COSA/APN update spreadsheet, click [here](https://go.microsoft.com/fwlink/p/?linkid=851213).

The following COSA settings are required:

- SupportDataMarketplace (must be set to “Yes”)
- DataMarketplaceRoamingUIEnabled
- SIM ICCID range (ICCID Range – Start and ICCID Range – End)

The following settings might be applicable depending of your specific business needs:

- AccountExperienceURL
- BrandingName
- BrandingIcon (icons should be provided along with spreadsheet)
- UseBrandingNameOnRoaming

The following image shows an example MO with branding in the network flyout:

**IMAGE**

## Get Balance API

The Get Balance API queries current subscription status, controls whether the DYNAMO experience is available on the device, and shows remaining data and time in the network flyout for prepaid subscriptions. The following diagram shows the high-level flow for the Get Balance API. 

**IMAGE**

### Resource model

Communication between the DYNAMO service and the MO service involves manipulating the resources in the following diagram. Explanations for each resource are in the tables following the diagram.

**IMAGE**

#### SIM resource

> [!NOTE]
> The SIM resource does not currently support “create,” “read,” “update,” or “delete” operations.

| JSON property | Type | Description |
| --- | --- | --- |
| activationCode | String | The activation code that LPA on the client can use to download and activate the profile. |
| Iccid | String | The ICCID of the profile that has been created. |
| eId | String | The eId of the eSIM. |

#### Balance resource

| JSON property | Type | Description |
| --- | --- | --- |
| Type | Enum | Possible values: <ul><li>MODIRECT: Indicates if the user balance is MO Direct.</li><li>MODIRECTPAYG: Indicates if the user balance is MO Direct PAYG.</li><li>NONE: Indicates the user has no balance. When the remaining balance is 0 but the plan has not expired, we expect to receive "NONE" so that the user can purchase data plans.</li><li>NOTSUPPORTED: Indicates the SIM is not supported by the DYNAMO experience. "NOTSUPPORTED" is used when the SIM should not be in the DYNAMO supported range. We will turn off the DYNAMO experience in the network flyout and return a generic error message in the Mobile Plans app when we receive this type.</li></ul> |
| dataRemainingInMB | Double | The data remaining in the current user plan, in MB. |
| timeRemaining | String | The time duration specified in [ISO 8601](https://go.microsoft.com/fwlink/p/?linkid=866182). |
| locations | Collection of Strings | An array of the location in two letter ISO code. This comes from MCC or reverse IP lookup when there is no Cellular network connection. |

### Headers

The following headers may be included in every request from the DYNAMO Service to the Mobile Provider’s endpoint.

| Header name | Value | Description |
| --- | --- | --- |
| X-MS-DM-TransactionId | String | The TransactionId to uniquely identify this request/response interaction between the DYNAMO service and the MO service. |
| Authorization (optional) | String | A basic authentication string optionally provided by the MO. |

### Error codes

| Error code | Description |
| --- | --- |
| HTTP 200 (OK) | The operation completed successfully. This code should also be used to indicate if the user has 0 balance in the specified location, which should be done using dataRemainingInMB=0 and timeRemaining=”PT0S” with HTTP 200. |
  HTTP 201 (Created) | Indicates that the operation completed successfully and the resource was created successfully. |
| HTTP 400 (Bad Request) | Used for invalid an invalid query parameter, invalid header, or invalid payload. In the response body, the parameter that is incorrect should be indicated. For example, if an invalid fieldsTemplate is specified, this error code must be returned with details in the response body. |
| HTTP 401 (Unauthorized) | Authentication credentials were incorrect or invalid. This can occur when the basic auth credentials passed are incorrect. |
| HTTP 403 (Forbidden) | The client certificate is untrusted or invalid. If the client certificate included as a part of MTLS is invalid, HTTP 403 should be returned. |
| HTTP 404 (Not Found) | The MO service should return this error when the resource doesn’t exist. This can occur when an incorrect ICCID is sent. This should not be used to indicate that the user doesn’t have a balance in the specified location, which is indicated with HTTP 200 (OK). |
| HTTP 409 (Conflict) | Used if a TransactionId is repeated. |
| HTTP 429 (Too many requests) | Used by the MO service to indicate that the DYNAMO service is sending too many requests within the specified amount of time. In the response, the MO service must use the Retry-After header to indicate the time after which the DYNAMO service should retry for the resource. In the response body, optional details can be provided. |
| HTTP 500 (Internal Error) | Something unexpected happened on the MO service. The MO service should include the cause of error whenever possible so that it can be used for further debugging as needed. |

### Get Balance API specification

DYNAMO must understand the status of the subscription for several reasons, the most important of which is that DYNAMO decides where a user should be allowed to purchase a new plan based on their current balance. Users must also be able to check their current remaining balance at any time within the experience.

The Get Balance API is called when network flyout is displayed or when Mobile Plans app is launched.

The following series of examples show the call flow for the Get Balance API.

#### Example 1: Checking balance any time within the experience

HTTP request, where *moBaseUrl* is the endpoint of the MO-hosted service and *sim id* is the ICCID:

```html
GET https://{moBaseUrl}/sims/{sim id}/balances?fieldsTemplate=basic&limit=1&location=US HTTP/1.1
```

Query parameters:

| Query parameter name | Value | Description |
| --- | --- | --- |
| location | String | Optional. The location where the user balance is being queried. If not specified, all active balances are expected. |
| limit | Integer |Optional. The maximum count of balances to be returned. If not specified, all the balances should be returned. |
| fieldsTemplate | Enum |Specifies the list of fields that must be returned in the resource. <p>Possible values:</p><ul><li>Basic: *type*, *dataRemainingInMB*, and *timeRemaining* in the Balance resource must be returned.</li><li>Full: All properties in the Balance resource must be returned.</li></ul> |

#### Example 2: Returning the first balance that is available for the user in US

```html
GET https://moendpoint.com/v1/sims/iccid: 8988247000100003319/balances?fieldsTemplate=basic&limit=1&location=us HTTP/1.1
X-MS-DM-TransactionId: “MSFT-12345678-1234-1234-1234-123456789abc”
```

HTTP response:

```html
HTTP/1.1 200 OK
Content-type: application/json
X-MS-DM-TransactionId: “12345”

{
“balances”: [
    {
         “id”: “23445”,
         “type”: “MODIRECTPAYG”,
         “dataRemaininginMB”: 123.0,
         “timeRemaining”: “P23DT23H”
    }
  ]
}
```

If successful, this method will return the balance of the user.

Response JSON:

| Data | Type | Description |
| --- | --- | --- |
| Balances | Collection | A collection of Balances. |

#### Example 3: The expected response when fieldsTemplate is set as full

```html
GET https://moendpoint.com/v1/sims/iccid: 8988247000100003319/balances?fieldsTemplate=full HTTP/1.1
X-MS-DM-TransactionId: “MSFT-12345678-1234-1234-1234-123456789abc”

HTTP/1.1 200 OK
Content-type: application/json
X-MS-DM-TransactionId: “MSFT-12345678-1234-1234-1234-123456789abc”

{
“balances”: [
    {
         “id”: “23445”,
         “type”: “MODIRECTPAYG”,
         “dataRemaininginMB”: 123.0,
         “timeRemaining”: “P23DT23H”,
         “locations”: [“US”, “CA”],
         “ms-provisioningDataSet”: [“xxxxx”, “yyyyy”]
    },
    {
         “id”: “12345”,
         “type”: “MODIRECTPAYG”,
         “dataRemaininginMB”: 1367.0,
         “timeRemaining”: “P23DT23H”,
         “locations”: [“UK”, “FR”],
         “ms-provisioningDataSet”: [“xxxxx”, “yyyyy”]
    }
  ]
}
```

#### Example 4: The expected response for a SIM that is in the COSA ICCID range but should not be supported by DYNAMO

HTTP request:

```html
GET https://{moBaseUrl}/sims/{sim id}/balances?fieldsTemplate=basic&limit=1&location=US 
HTTP/1.1
```

Response JSON:

```json
HTTP/1.1 200 OK
Content-type: application/json
X-MS-DM-TransactionId: “12345”

{
“balances”: [
    {
         “id”: “23445”,
         “type”: “NOTSUPPORTED”,
         “dataRemaininginMB”: 0.0,
         “timeRemaining”: “PT0S”
    }
  ]
}
```

### Authentication

Communication between Microsoft services and your services must be authenticated using the Mutual Transport Layer Security (MTLS). Microsoft will provide a certificate that you will use to validate the identity of the requester to **moBaseUrl**.

## Walled Garden

Walled Garden is key to supporting your prepaid customers when they run out of data. It enables them to reach the MO Direct portal even when there is no alternative internet connection such as Wi-Fi. This will enable consumers to purchase additional data plans and manage their subscriptions.

The MO Direct web portal and Get Balance API end-point must be part also of this Walled Garden.

There are only a small number of required endpoints that are always accessible to end users. The following table defines the endpoints required for Walled Garden. 

| URL | HTTP/HTTPS |
| --- | --- |
| service.datamart.windows<span></span>.com | https |
| dogfood.datamart.windows<span></span>.com | https |
| windows.policies.live<span></span>.net | https |
| ctldl.windowsupdate<span></span>.com | http |
| msftncsi<span></span>.com | http |
| login.live<span></span>.com | http + https |
| storagetos.datamart.windows<span></span>.com | http + https |
| cdp1.public-trust<span></span>.com | http |
| ocsp.omniroot<span></span>.com | http |
| vassg142.ocsp.omniroot<span></span>.com | http |
| vassg142.crl.omniroot<span></span>.com | http |
| mscrl.microsoft<span></span>.com | http |
| crl.microsoft<span></span>.com | http |
| msftconnecttest<span></span>.com | http |
| crl3.digicert<span></span>.com | http |
| Ocsp.digicert<span></span>.com | http |

## Prepaid implementation validation

This section describes testing and validation that you must do to ensure that you are ready to move into the Integration phase.

### Prerequisites

1. Install Windows 10, version 1607 on the PC you will use for testing.
2. Prior to general availability, get the latest Windows version by joining the [Windows Insider Program](https://go.microsoft.com/fwlink/p/?linkid=866189).

### Test cases to be executed

#### Walled Garden

1. When the user has no balance, ensure that the user can access Walled Garden sites defined in [Walled Garden](#walled-garden).

#### Getting Balance

1. When the user is in the Walled Garden state, the balance returned must be zero.
2. When the user has been allocated Microbalance, the balance returned must be zero.
3. As the user consumes data, the balance returned must decrement to reflect the data remaining.
4. As the allotted time lapses after the Create Order API has been invoked, the time remaining must decrement to reflect the time remaining.

#### Test with expired MTLS certificate

1. Validate MO APIs without the MTLS certificate.
Expected Status: 401 Unauthorized.
2. Validate with an expired MTLS certificate.
Expected Status: 401 Unauthorized.

#### Get balance negative tests

1. Validate with an invalid SIM.
Expected Status: 404 Not Found.
2. Validate with unknown location or bad location string/number.
Expected Status: 400 (Bad Request).
3. Validate with filter limit as a negative number and exceeding the limit of an INT.
Expected Status: 400 - Bad Request.
Expected Status 200 OK for filter limit (integer).
4. Validate to get balance without any *location* (or empty location), *fieldTemplate*, *limit*, and many more combination of parameters.
Expected Status: 400 (Bad Request) with any bad parameter’s value.
Expected Status 200 – OK.

## Get Balance API load test

Before the Get Balance API is enabled in production, both Microsoft services and mobile operator services should be tested to see if they can handle the projected load. The mobile operator is expected to run a Load test.  Once that has passed, DYNAMO will execute a load test for 6 hours as configured in the following section. 

This test configuration is generated from projected traffic of 10,000 SIMs. The Peak RPS is calculated based on 3 times this traffic projection.

- Load tests will be executed from 25 test agents.
- Load tests will execute for:
    - 1 hour with 100 different users (#ICCIDs) with 1 RPS.
    - 4 hours with 500 different users (#ICCIDs) with 1 RPS.
    - 1 hour with 1000 different users (#ICCIDs) with 3 RPS (Peak).
- The load distribution cross APIs would be as follows:

| API | Load distribution | Expected RPS | Peak RPS |
| --- | --- | --- | --- |
| GetBalance | 96% | 1 | 3 |

During test runs, the expected success rate is: 99.9%. On achieving this success rate, the MO API will be enabled in the DYNAMO production service.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Mobile%20operator%20scenarios%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")