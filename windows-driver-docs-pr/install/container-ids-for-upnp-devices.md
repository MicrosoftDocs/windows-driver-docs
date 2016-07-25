---
title: Container IDs for UPnP Devices
description: Container IDs for UPnP Devices
ms.assetid: 29d2ed0e-e746-4f0a-88f3-bd07d5750485
---

# Container IDs for UPnP Devices


Starting with Windows 7, a device that supports PnP extensions (PnP-X) and Universal PnP (UPnP) can specify a container ID by including the **X\_containerId** XML element in the device description document. For more information about UPnP and the UPnP device description document, refer to the [UPnP Device Architecture specification.](http://go.microsoft.com/fwlink/p/?linkid=142402)

The **X\_containerId** XML element is declared as follows:

```
<df:X_containerId xmlns:df="">
  xs:string
</df:X_containerId>
```

The **X\_containerId** XML element type is a string, for which the value is a globally unique identifier ([*GUID*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-guid)). This string is formatted as *{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}*.

The following is an example of an **X\_containerId** XML element.

```
<df:X_containerId xmlns:df="">
  {101392d0-5e91-11dd-ad8b-0800200c9a66}
</df:X_containerId>
```

The **X\_containerId** XML element is required to be in the &lt;device&gt; section of the UPnP device description document. The following example shows the correct placement of the **X\_containerId** element in a device description document.

**Note**   This is not a complete UPnP device description document. For more information about UPnP, refer to the [UPnP Device Architecture specification.](http://go.microsoft.com/fwlink/p/?linkid=142402)

 

```
<?xml version="1.0" ?> 
<root 
 xmlns="urn:schemas-upnp-org:device-1-0"
 xmlns:df=
 "http://schemas.microsoft.com/windows/2008/09/devicefoundation">

 <specVersion>
        <major>major version number</major> 
        <minor>minor version number</minor> 
    </specVersion>

    <URLBase>device URL</URLBase> 

    <device>
 <!-- Place device metadata here. See UPnP spec for details.-->
        <df:X_containerID>
 <!--- Place the ContainerID GUID here.--->
 {101392d0-5e91-11dd-ad8b-0800200c9a66}
      </ df:X_containerID >

    </device>
</root>
```

If the UPnP device description document does not include the **X\_containerId** XML element, the Plug and Play (PnP) manager generates a container ID through the device's Unique Device Name (UDN).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Container%20IDs%20for%20UPnP%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




