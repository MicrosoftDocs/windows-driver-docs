---
title: Container IDs for DPWS Devices
description: Container IDs for DPWS Devices
ms.assetid: b613a25e-bedf-481c-8c86-9486af01b2ba
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Container IDs for DPWS Devices


Starting with Windows 7, a device that supports PnP extensions (PnP-X) and Device Profile for Web Services (DPWS) can specify a container ID by including the **ContainerId** XML element in the device metadata document. For more information about DPWS and the DPWS device metadata document, refer to the [DPWS specification.](http://go.microsoft.com/fwlink/p/?linkid=142400)

**Note**  Starting with Windows 10, the system ignores the container ID provided by a device and instead generates one on its own. It does this either by using the GUID from the device's endpoint reference address (EPR) or a SHA-1 hash of the device's EPR (if not a GUID).

 

The **ContainerId** XML element is declared as follows:

```cpp
<df:ContainerId xmlns:df="">
  xs:string
</df:ContainerId>
```

The **ContainerId** XML element type is a string, for which the value is a globally unique identifier ([*GUID*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-guid)) formatted. This string is formatted as *{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}*.

The following is an example of a **ContainerId** XML element.

```cpp
<df:ContainerId xmlns:df="">
  {101392d0-5e91-11dd-ad8b-0800200c9a66}
</df:ContainerId>
```

The &lt;ContainerId&gt; XML element is required to be in the &lt;ThisDevice&gt; section of the device metadata exchange Simple Object Access Protocol (SOAP) message. The following example shows the correct placement of the &lt;ContainerId&gt; element in a metadata exchange message.

**Note**   This is not a complete DPWS metadata exchange document. For more information about DPWS, refer to the [DPWS specification.](http://go.microsoft.com/fwlink/p/?linkid=142400)

 

```cpp
<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
    xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
    xmlns:wsdisco="http://schemas.xmlsoap.org/ws/2005/04/discovery"
    xmlns:wsx="http://schemas.xmlsoap.org/ws/2004/09/mex"
    xmlns:wsd="http://schemas.xmlsoap.org/ws/2006/02/devprof"
    xmlns:df="http://schemas.microsoft.com/windows/2008/09/devicefoundation">

    <soap:Header>
        <!-- Place SOAP header information here.-->
    </soap:Header> 

    <soap:Body>
        <wsx:Metadata>

           <wsx:MetadataSection
                Dialect="http://schemas.xmlsoap.org/ws/2005/05/devprof/ThisModel">
                <wsd:ThisDevice>
                    <!-- Place ThisDevice metadata here.-->
                    <df:ContainerId>
                        <!--- Place the ContainerID GUID here.--->
                        {101392d0-5e91-11dd-ad8b-0800200c9a66}
                    </df:ContainerId>
                </wsd:ThisDevice>
            </wsx:MetadataSection>

        </wsx:Metadata>
    </soap:Body>
</soap:Envelope>
```

If the DPWS device metadata document does not include the **ContainerId** XML element, the Plug and Play (PnP) manager uses the value of the device's endpoint reference address as the container ID.

 

 





