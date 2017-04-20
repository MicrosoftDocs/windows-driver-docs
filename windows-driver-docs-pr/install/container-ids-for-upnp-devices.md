---
title: Container IDs for UPnP Devices
description: Container IDs for UPnP Devices
ms.assetid: 29d2ed0e-e746-4f0a-88f3-bd07d5750485
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 





