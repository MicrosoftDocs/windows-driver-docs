---
title: Attachments Scenarios
description: Attachments Scenarios
ms.assetid: bd563919-961f-40eb-ad5c-26026fc1c0e6
keywords:
- WSDBIT tool WDK , test scenarios
- WSDAPI Basic Interoperability Tool WDK , test scenarios
- scenarios WDK WSDBIT
- test scenarios WDK WSDBIT
- Attachments scenario WDK WSDBIT
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attachments Scenarios


The Attachments scenario tests sending and receiving attachments.

The goal of this scenario is not the discovery of the Hosted Service endpoints. This scenario assumes that these endpoints were discovered or provided prior to starting this scenario.

In every case, the attachment that is sent to TestDevice will be Dpws1.jpg and the attachment that is received from TestDevice will be Dpws2.jpg. The attachment should be verified by loading a copy of the expected attachment into memory and doing a byte-for-byte memory comparison on the received attachment.

For more information, see the initial test device setup diagram in [WSDBIT Testing Environment](wsdbit-testing-environment.md).

Case
Client action
Server action
Pass-Fail criteria
**3.1**

**Call OneWay attachment method**

3.1.1

Calls the **OneWay** method of the AttachmentService with

-   **wsa:Action == http://schemas.example.org/AttachmentService/OneWayAttachment**

-   The http://testdevice.interop/AttachmentService1 service will be used.

-   See [AttachmentService WSDL](attachmentservice-wsdl.md).

-   Use Dpws1.jpg as data for the attachment that is sent to the device.

Validate the attachment data.

The server correctly validates the attachment data. The server receives Dpws1.jpg.

**3.2**

**Call TwoWay attachment method**

3.2.1

Calls the **TwoWay** method of the AttachmentService with:

-   **wsa:Action == http://schemas.example.org/AttachmentService/TwoWayAttachmentRequest**

-   The http://testdevice.interop/AttachmentService1 service will be used.

-   See [AttachmentService WSDL](attachmentservice-wsdl.md).

-   Use Dpws1.jpg as the data for the attachment that is sent to the device.

<!-- -->

-   Validate the attachment data.

-   Send **TwoWayAttachmentResponse**.

-   **wsa:Action == http://schemas.example.org/AttachmentService/TwoWayAttachmentResponse**

-   See [AttachmentService WSDL](attachmentservice-wsdl.md).

-   Use Dpws2.jpg as data for the attachment that is returned to the client.

The server correctly validates the attachment data and the client receives the response. The server receives Dpws1.jpg.

3.2.2

Validate the attachment data that is received in the **TwoWayAttachmentResponse**. The client receives Dpws2.jpg.

Nothing.

The client correctly validates the attachment data.

 

 

 





