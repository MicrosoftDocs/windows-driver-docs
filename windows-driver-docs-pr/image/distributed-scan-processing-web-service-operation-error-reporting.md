---
title: Distributed Scan Processing Web Service Operation Error Reporting
description: Distributed Scan Processing Web Service Operation Error Reporting
MS-HAID:
- 'dsm\_des\_arch\_63a002ab-1ff5-41a8-80c4-eca99cf3dc9f.xml'
- 'image.distributed\_scan\_processing\_web\_service\_operation\_error\_reporting'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d0d8f543-466e-4270-99cd-624db44bd250
---

# Distributed Scan Processing Web Service Operation Error Reporting


This section describes how a Distributed Scan Processing Web Service host generates and sends error codes when operations requested by clients fail. The common error codes are described in [Common Distributed Scan Processing Web Service Operation Error Codes](common-distributed-scan-processing-web-service-operation-error-codes.md). As an option, a vendor can use a subset of these error codes, or can define additional error codes.

As described in the [Distributed Scan Processing Web Service Protocol Summary](distributed-scan-processing-web-service-protocol-summary.md), a Distributed Scan Processing Web Service operation consists of an **XxxRequest** element, which contains a request from a client, and a corresponding **XxxResponse** element, which contains the response from the service host. If the service encounters an error while processing an **XxxRequest** message, it returns an error message instead of an **XxxResponse** message. The error message contains a SOAP **Fault** element that specifies an error code, plus additional information about the error.

All error messages that are defined for the Distributed Scan Processing Web Service protocol must be sent according to the rules described in the [Device Profile for Web Services](http://go.microsoft.com/fwlink/p/?linkid=59069) (DPWS) and [Web Services Addressing](http://go.microsoft.com/fwlink/p/?linkid=70144) (WS-Addressing) specifications. Specifically, the Distributed Scan Processing Web Service host should send a fault message to one of the following client locations, which are listed in order of preference:

1.  To the *fault endpoint*, if it is present and valid.

2.  To the *reply endpoint*, if it is present and if no fault endpoint is available.

3.  To the *source endpoint* if neither a fault endpoint nor a reply endpoint is available.

A Distributed Scan Processing Web Service host endpoint must include the required message information headers on all fault messages that it sends. A fault message uses the *relationship* property, which is defined in the WS-Addressing specification, to identify the request that failed. The following *action* property designates a fault message:

```
http://schemas.xmlsoap.org/ws/2004/08/addressing/fault
```

The **Fault** element in a fault message can contain the following property values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Fault property</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Code]</p></td>
<td><p>The fault code.</p></td>
</tr>
<tr class="even">
<td><p>[Subcode]</p></td>
<td><p>The fault subcode.</p></td>
</tr>
<tr class="odd">
<td><p>[Reason]</p></td>
<td><p>The English language reason for the fault.</p></td>
</tr>
<tr class="even">
<td><p>[Detail]</p></td>
<td><p>An additional detail. If present, the meaning of the detail depends on the fault code. If absent, no <strong>Detail</strong> element is defined for the fault.</p></td>
</tr>
</tbody>
</table>

 

For consistency with the WS-Addressing specification, this section uses square brackets to distinguish an abstract property value from a property element name. For example, a **Code** element contains a \[Code\] property value.

The following XML example shows the general structure of a SOAP 1.2 message that includes a **Fault** element that contains the four property values listed in the preceding table.

```
<S:Envelope>
   <S:Header>
      <wsa:Action>http://schemas.xmlsoap.org/ws/2004/08/addressing/fault</wsa:Action>
      <!-- Headers excluded for clarity -->
   </S:Header>
   <S:Body>
      <S:Fault>
         <S:Code>
            <S:Value>[Code]</S:Value>
            <S:Subcode>
               <S:Value>[Subcode]</S:Value>
            </S:Subcode>
         </S:Code>
         <S:Reason>
            <S:Text xml:lang="en">[Reason]</S:Text>
         </S:Reason>
         <S:Detail>[Detail]</S:Detail>
      </S:Fault>
   </S:Body>
</S:Envelope>
```

For certain values of \[Code\], a fault message omits the **Detail** element. For more information, see [Common Distributed Scan Processing Web Service Operation Error Codes](common-distributed-scan-processing-web-service-operation-error-codes.md).

The following is an example of a SOAP message that contains a **Fault** element:

```
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soapelope"
                xmlns:xml="http://www.w3.org/XML/1998/namespace"
                xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
                xmlns:dsp="http://schemas.microsoft.com/windows/2008/02/wdp/repository/processing">
  <soap:Header>
    <wsa:Action>http://schemas.xmlsoap.org/ws/2004/08/addressing/fault</wsa:Action>
    <!-- Headers excluded for brevity -->
  </soap:Header>
  <soap:Body>
    <soap:Fault>
      <soap:Code>
        <soap:Value>soap:Receiver</soap:Value>
        <soap:Subcode>
          <soap:Value>dsp:OperationFailed</soap:Value>
        </soap:Subcode>
      </soap:Code>
      <soap:Reason>
        <soap:Text xml:lang="en">Service cannot perform the requested operation</soap:Text>
      </soap:Reason>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>
```

For more information, see [Common Distributed Scan Processing Web Service Operation Error Codes](common-distributed-scan-processing-web-service-operation-error-codes.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Distributed%20Scan%20Processing%20Web%20Service%20Operation%20Error%20Reporting%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




