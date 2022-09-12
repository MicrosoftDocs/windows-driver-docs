---
title: WS-Discovery mobile printing support
description: Devices that support printing from Windows 10 Mobile, must add the MobilePrinter category to their WS-Discovery ThisModel response.
ms.date: 09/09/2022
---

# WS-Discovery mobile printing support

Devices that support printing from Windows 10 Mobile, must add the MobilePrinter category to their WS-Discovery ThisModel response, as shown in the following example:

```xml
<soap:Envelope
    xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
    xmlns:wsa="https://schemas.xmlsoap.org/ws/2004/08/addressing"
    xmlns:wsdisco="https://schemas.xmlsoap.org/ws/2005/04/discovery"
    xmlns:wsx="https://schemas.xmlsoap.org/ws/2004/09/mex"
    xmlns:wsd="https://schemas.xmlsoap.org/ws/2006/02/devprof"
    xmlns:pnpx="https://schemas.microsoft.com/windows/pnpx/2005/10">

    <soap:Header>
        <!-- Place SOAP header information here.-->
    </soap:Header>

    <soap:Body>
        <wsx:Metadata>
            <wsx:MetadataSection
                Dialect="https://schemas.xmlsoap.org/ws/2005/05/devprof/ThisDevice">
                <wsd:ThisDevice>
                    <!-- Place ThisDevice metadata here.-->
                </wsd:ThisDevice>
            </wsx:MetadataSection>

           <wsx:MetadataSection
                Dialect="https://schemas.xmlsoap.org/ws/2005/05/devprof/ThisModel">
                <wsd:ThisModel>
                    <!-- Place ThisModel metadata here.-->
                    <pnpx:DeviceCategory>
                        <!-- This device is in the Printers category -->
                        Printers Scanners MobilePrinter
                   </pnpx:DeviceCategory>
                </wsd:ThisModel>
            </wsx:MetadataSection>  

            <wsx:MetadataSection
                Dialect="https://schemas.xmlsoap.org/ws/2005/05/devprof/Relationship">
                <wsd:Relationship
                    Type="https://schemas.xmlsoap.org/ws/2005/05/devprof/host">

                    <wsd:Hosted>
                        <!-- Place Hosted metadata for the 
                             first service here.-->
                        <pnpx:HardwareId>
                            <!-- Place the Hardware ID for the first service here.-->
                            PnPX_SampleService1_HWID
                        </pnpx:HardwareId>
                        <pnpx:CompatibleId>
                            <!-- Place the Compatible ID for the first service here.-->
                            PnPX_SampleService1_CPID
                        </pnpx:CompatibleId>
                    </wsd:Hosted>

                </wsd:Relationship>
            </wsx:MetadataSection>

        </wsx:Metadata>
    </soap:Body>
</soap:Envelope>
```

The following table provides additional information about the MobilePrinter category keyword:

| Constant/Value | Description |
|--|--|
| PNPX_DEVICECATEGORY_PRINTER_MOBILE<br><br>L"MobilePrinter" | MobilePrinter category<br><br>Keywords: Printer |

For more information about how to add the device category to the WS-Discovery metadata exchange, see the [PnP-X specification](/previous-versions/gg463082(v=msdn.10)).
