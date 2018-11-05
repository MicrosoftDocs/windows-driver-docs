---
title: Device Control Scenarios
description: Device Control Scenarios
ms.assetid: 9effc192-77ef-40fd-9ab6-564637019576
keywords:
- WSDBIT tool WDK , test scenarios
- WSDAPI Basic Interoperability Tool WDK , test scenarios
- scenarios WDK WSDBIT
- test scenarios WDK WSDBIT
- Device Control scenario WDK WSDBIT
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Control Scenarios


The Device Control scenario tests simple SOAP message exchanges.

The goal for this scenario is not discovery of the Hosted Service endpoints. This scenario assumes these endpoints were discovered or provided before this scenario. For this scenario, these endpoints have to be addressable on the physical network. For more information, see the initial test device setup diagram in [WSDBIT Testing Environment](wsdbit-testing-environment.md).

Case
Client action
Server action
Pass-Fail criteria
**2.1**

**OneWay method**

2.1.1

Calls the **OneWay** method of the SimpleService with:

-   **wsa:Action == http://schemas.example.org/SimpleService/OneWay**

-   The http://testdevice.interop/SimpleService1 service will be used.

-   The integer input is provided.

Displays the integer that is received from the **OneWay** method.

The integer that was sent is the integer that was displayed.

**2.2**

**TwoWay method**

2.2.1

Calls the **TwoWay** method of the SimpleService with:

-   **wsa:Action == http://schemas.example.org/SimpleService/TwoWayRequest**

-   The http://testdevice.interop/SimpleService1 service will be used.

-   The two integer inputs are provided.

Responds to the client by using the **TwoWayResponse** method with:

-   **wsa:Action == http://schemas.example.org/SimpleService/TwoWayResponse**

-   The sum parameter is calculated from the sum of the two input parameters.

The sum parameter that is received by the client is indeed the sum of the integer values sent in the **TwoWay** method.

**2.3**

**TypeCheck method**

2.3.1

Calls the **TypeCheck** method of the SimpleService with:

-   **wsa:Action == http://schemas.example.org/SimpleService/TypeCheckRequest**

-   The http://testdevice.interop/SimpleService1 service will be used.

-   The boolean, decimal, float, and list of **xs:anyURI** parameters are provided.

Responds to the client by using the **TypeCheckResponse** method with:

-   **wsa:Action == http://schemas.example.org/SimpleService/TypeCheckResponse**

-   The boolean, decimal, float, and list of **xs:anyURI** parameters are returned and echoed back to the client.

The boolean, decimal, float, and list of **xs:anyURI** parameters are displayed correctly at the device before they are echoed back to the client. The parameters are again displayed correctly as they are received at the client.

**2.4**

**AnyCheck method**

2.4.1

Calls the **AnyCheck** method of the SimpleService with:

-   **wsa:Action == http://schemas.example.org/SimpleService/AnyCheckRequest**

-   The http://testdevice.interop/SimpleService1 service will be used

-   An arbitrary XML fragment is used as a parameter.

Responds to the client by using the **TypeCheckResponse** method with:

-   **wsa:Action == http://schemas.example.org/SimpleService/AnyCheckResponse**

-   The arbitrary XML fragment is returned and echoed back to the client.

The XML fragment that was sent from the client is displayed correctly at the device before it is echoed back to the client. The XML fragment is again displayed correctly when it is received at the client.

 

 

 





