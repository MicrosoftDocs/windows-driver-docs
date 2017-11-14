---
title: MO API integration test plan
author: windows-driver-content
description: This topic describes the MO API integration test plan for Data Marketplace.
ms.assetid: AB563225-7339-44E6-8D64-D647848D4432
keywords:
- Data Marketplace mobile operators, Data Marketplace mobile broadband WDK
ms.author: windowsdriverdev
ms.date: 11/13/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MO API integration test plan 

Mobile Operators (MO&#39;s) must execute a test plan before starting the MO API integration with Microsoft. This article also covers the scenarios that will be executed as a part of the MO API integration by Microsoft in collaboration with MO.

## Prerequisite

- Install Windows 10 Anniversary Update on the PC you will use for testing.
- Prior to general availability, get the latest Windows version by joining the [Insider Program](https://insider.windows.com/).
- For end-to-end testing, use the latest Windows Insiders build of the Paid Wi-Fi and Cellular app.

## Test cases to be executed by MO

### Walled Garden

- When the customer has no balance, ensure that the customer can access the Walled Garden sites. 

- The Data Marketplace Validator tool can be used to validate the Walled Garden access.

### Microbalance

- When the customer has zero balance and has not yet requested microbalance, the customer MUST have access to only the Walled Garden sites when accessing data over cellular connectivity.
- Once the customer has allocated microbalance, the customer MUST have full internet access immediately by performing a fast re-auth. The customer MUST NOT be disconnected from the network and reconnected to get full internet access.
- If the customer queries for balance after allocating Microbalance, the balance returned MUST be zero.
- Once the Microbalance expires (after time or data is consumed), the customer MUST have access to only Walled Garden. This transition MUST happen using fast re-auth and MUST NOT disconnect the customer from the network.

### Create Order

- When the order API is invoked, data MUST be allocated to customer immediately and a fast re-auth performed if the customer is connected to the network.
- After the order API is invoked, the Microbalance SHOULD no longer be consumed.
- After the order API is invoked, the balance returned MUST reflect the purchase made by the customer.

### Getting Balance

- When the customer is in Walled Garden state, the balance returned MUST be zero.
- When the customer has been allocated Microbalance, the balance returned MUST be zero.
- After the create order API has been invoked, the balance returned MUST reflect the customers remaining balance in the country.
- After the create order API has been invoked, the balance returned in countries not affected MUST NOT change.
- As the customer consumes data, the balance returned MUST decrement to reflect the data remaining.
- As the time lapses after the create order API has been invoked, the time remaining MUST decrement to reflect the time remaining.

### In-Country test(ICT)

MO&#39;s must validate the network connectivity on all the countries where the service is provided by using Windows-based devices. Data Marketplace Validator tool can be used to run API testing.

## Negative test cases

MO must insure that APIs are returning expected status for all negative scenarios.

### Test with expired MTLS certificate

- Validate MO APIs without MTLS certificate

>> **Expected Status:** 401 UnAuthorized

- Validate with expired MTLS certificate

>> **Expected Status:** 401 UnAuthorized

### Get balance tests

- Validate with Invalid SIM

>> **Expected Status** : 404 Not Found.

- Validate with unknown location or bad location string/number

>> **Expected Status** : 400 (Bad Request).

- Validate with filter limit -ve number and exceed limit of INT

>> **Expected Status** : 400 - Bad Request

>> **Expected Status** 200 OK for filter limit (integer)

- Validate to get balance without any location or empty location, fieldTemplate and limit and many more combination of parameters.

>> **Expected Status** : 400 (Bad Request) with any bad parameter&#39;s value.

>> **Expected Status** 200 – OK

### Microbalance test cases

- Validate with Invalid SIM

>> **Expected Status** 404 – Not Found

- Validate with unsupported location or bad location string/number

>> **Expected Status** 400 – Bad Request

>> **Expected Status** 200 – OK (for unsupported location)

- Validate to assign Microbalance multiple times for the same location with same SIM

>> **Expected Status** 200 – OK

- Validate to assign microbalance even already has purchased offer for same location.

>> **Expected Status** 200 – OK

Note: Data Marketplace will not request microbalance when the customer has a balance. But we expect to get status &#39;200&#39; so that you don&#39;t need to check if the customer has balance or not. Data Marketplace will handle that logic for you.

### Order test cases

- Invoking multiple times with same transaction Id.

>> **Expected Status** 409 – Conflict.

- Validate with Invalid purchaseDate or Future purchaseDate

>> **Expected Status** 400 – Bad Request

- Validate to purchase a Product for not supported location.

>> **Expected Status** 400 – Bad Request

- Validate to purchase same product multiple time for same location

>> **Expected Status** 200 - OK.

> [!NOTE] 
> For Windows 10 Fall Creators Update, Data Marketplace does not support top off, in which case the customer will not run into this scenario. However, we recommend this implementation for an easy upgrade (no API change on your side) once Data Marketplace supports topping off (purchasing multiple data plans for the same location from the same provider) in future releases.

- Validate Order to pass without any SIM or contains up to 20 SIMs.

>> **Expected Status** 200 – OK with #Sims

- Validate Order to pass bad provisioning data

>> **Expected Status** 400 – Bad Request

- Validate Order to injected bad characters (non-alphabet characters) with provisioning data or ms-ProvisionDataSet.

>> **Expected Status** 400 – Bad Request



## Test cases to be execute by Microsoft

### Get Balance test cases

- Validate zero balance for a SIM in US.
- Validate zero balance in countries other than US. For API level testing, Data Marketplace validator tool can be used by using the appropriate MCC/MNC value.
- Validate correct annotation in flyout.

### Get Offers test cases

- Validate correct offers are shown in US.
- Validate correct offers are shown in countries other than US. For API level testing, Data Marketplace validator tool can be used by using the appropriate MCC/MNC value.
- Validate PDP page is correct with the app title and description.
- Validate TOS/FAQ.
- Validate Microbalance is allocated enough to complete purchase.
- Validate balance remains 0.
- Validate fast re-auth.
- Validate no offers in other countries using DMValidator.

### Purchase test cases

- Validate provision data is sent correct to MO.
- Validate provisioning assigns the correct amount of data.
- Validate provisioning assigns the correct amount of time.
- Validate balance displayed is correct in flyout.
- Validate balance displayed in App is correct.
- Validate correct offer title is displayed in app.
- Validate balance reduces as data is consumed.
- Validate time remaining reduces with elapsed time.

## API Monitoring tests

Data Marketplace Service will monitor the availability of the MO API&#39;s by issuing the following requests at the specified frequency:

- Balance API with fieldsTemplate set to basic being executed twice every minute using a specified ICCID.
- Microbalance API executed twice every minute for a specified ICCID.
- Xping test to ping the MO API integration test plan portal twice every minute making sure it is accessible, if onboarded.

The expected response is HTTP 200. If we fail to receive the expected response for more than 30 minutes, we will start the escalation process and engage you for investigation.

## Load test

Before the MO API is enabled in production, we need to make sure both the Microsoft service and Mobile Operator Service are able to handle the projected load. Mobile Operator is expected to run Load test.  Once that is passed, Data Marketplace will execute Load test for 6 hours as configured below.

This test configuration is generated from projected traffic of 10,000 SIMs. The Peak RPS is calculated based on three times of traffic projection:

- Load tests will be executed from 25 test agents
- Load tests will execute for:
  - 1 hour with 100 different customers(#ICCIDs) with 1 RPS
  - 4 hours with 500 different customers(#ICCIDs)  with 1 RPS
  - 1 hours with 1000 different customers(#ICCIDs) with 3 RPS (Peak)

- The load distribution cross APIs would be:

| **API** | **Load Distribution** | **Expected RPS** | **Peak RPS** |
| --- | --- | --- | --- |
| **GetBalance** | 96% | 1 | 3 |
| **Microbalance** | 2% | 0.02 | 0.06 |
| **Order** | 2% | 0.02 | 0.06 |

During test run, the expected success rate is 99.9%. On achieving this success rate, the MO API will be enabled in Data Marketplace production service.

## Run through end-to-end scenario

Prerequisites are that you publish at least one test offer in Dev Center and you have the appropriate SIM in the machine that will be used for testing.

Confirm the following, in a country where you published a test offer and your network provides coverage:

- The mobile broadband interface appears in the network flyout. 
![Network flyout displaying the mobile broadband interface](BUGBUG NEED IMAGE)
- Click **View plans from Windows Store** to launch the Paid WiFi &amp; Cellular app, which displays your offers.
![Network flyout displaying the mobile broadband interface with the Data Marketplace annotation. This appears after selecting the interface.](BUGBUG NEED IMAGE)
- Confirm you can consume an offer which results in the expected level of network performance (bandwidth/latency).
- Confirm that after purchase your client displays remaining balance.
![Network flyout displaying remaining balance](BUGBUG NEED IMAGE)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")