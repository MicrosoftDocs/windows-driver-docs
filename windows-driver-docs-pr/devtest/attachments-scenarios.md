---
title: Attachments Scenarios
description: Attachments Scenarios
ms.assetid: bd563919-961f-40eb-ad5c-26026fc1c0e6
keywords: ["WSDBIT tool WDK , test scenarios", "WSDAPI Basic Interoperability Tool WDK , test scenarios", "scenarios WDK WSDBIT", "test scenarios WDK WSDBIT", "Attachments scenario WDK WSDBIT"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Attachments%20Scenarios%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




