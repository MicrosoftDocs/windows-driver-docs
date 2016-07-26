---
title: Container IDs for DPWS Devices
description: Container IDs for DPWS Devices
ms.assetid: b613a25e-bedf-481c-8c86-9486af01b2ba
---

# Container IDs for DPWS Devices


Starting with Windows 7, a device that supports PnP extensions (PnP-X) and Device Profile for Web Services (DPWS) can specify a container ID by including the **ContainerId** XML element in the device metadata document. For more information about DPWS and the DPWS device metadata document, refer to the [DPWS specification.](http://go.microsoft.com/fwlink/p/?linkid=142400)

**Note**  Starting with Windows 10, the system ignores the container ID provided by a device and instead generates one on its own. It does this either by using the GUID from the device's endpoint reference address (EPR) or a SHA-1 hash of the device's EPR (if not a GUID).

 

The **ContainerId** XML element is declared as follows:

```
<df:ContainerId xmlns:df="">
  xs:string
</df:ContainerId>
```

The **ContainerId** XML element type is a string, for which the value is a globally unique identifier ([*GUID*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-guid)) formatted. This string is formatted as *{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}*.

The following is an example of a **ContainerId** XML element.

```
<df:ContainerId xmlns:df="">
  {101392d0-5e91-11dd-ad8b-0800200c9a66}
</df:ContainerId>
```

The &lt;ContainerId&gt; XML element is required to be in the &lt;ThisDevice&gt; section of the device metadata exchange Simple Object Access Protocol (SOAP) message. The following example shows the correct placement of the &lt;ContainerId&gt; element in a metadata exchange message.

**Note**   This is not a complete DPWS metadata exchange document. For more information about DPWS, refer to the [DPWS specification.](http://go.microsoft.com/fwlink/p/?linkid=142400)

 

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Container%20IDs%20for%20DPWS%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




