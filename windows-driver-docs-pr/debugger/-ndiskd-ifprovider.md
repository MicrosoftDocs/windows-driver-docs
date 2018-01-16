---
title: ndiskd.ifprovider
description: The ndiskd.ifprovider extension displays information about an NDIS interface provider (IfProvider). 
ms.assetid: 89C406E5-81D3-42AA-BA15-3D7C093BCD3C
keywords: ["ndiskd.ifprovider Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.ifprovider
api_type:
- NA
---

# !ndiskd.ifprovider


The **!ndiskd.ifprovider** extension displays information about an [NDIS interface provider](https://msdn.microsoft.com/windows/hardware/drivers/network/registering-as-an-interface-provider) (IfProvider). If you run this extension with no parameters, !ndiskd will display a list of all registered NDIS interface providers.

```
!ndiskd.ifprovider [-handle <x>] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of an IfProvider.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

Run the **!ndiskd.ifprovider** extension with no parameters to get a list of all registered IfProviders.

```
1: kd> !ndiskd.ifprovider
    IfProvider                                                                  
    ffffd20d14334180 - wanarp
    ffffd20d1264a950 - wfplwfs
    ffffd20d11deae00 - The NDIS loopback provider
    ffffd20d11deae70 - The NDIS interface provider
```

You can see from the previous example that the debugee machine has four interface providers registered. Two of them are NDIS interface providers.

**Note**  Interface providers are a generic concept and aren't required to be miniport drivers. While a miniport driver may choose to register as an interface provider if desired, most miniport drivers do not do so because NDIS has a built-in interface provider. The NDIS built-in interface provider automatically provides interfaces for every miniport driver, every Light-Weight Filter (LWF) module, and the loopback interface. For more information, see [NDIS interface provider](https://msdn.microsoft.com/windows/hardware/drivers/network/registering-as-an-interface-provider).

 

The following example shows the details for the "wanarp" interface provider in the previous example, whose handle is ffffd20d14334180.

```
1: kd> !ndiskd.ifprovider ffffd20d14334180


IF PROVIDER

    wanarp
    Ndis handle        ffffd20d14334180


INTERFACES

    Interface                                                                   
    [No interfaces found]


HANDLERS

    Protocol handler                       Function pointer   Symbol (if available)
    QueryObjectHandler                     fffff80d2f0414b0  bp wanarp!WanNdisIfQueryHandler
    SetObjectHandler                       fffff80d2f04bd10  bp wanarp!WanNdisIfSetHandler
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Registering as an Interface Provider](https://msdn.microsoft.com/windows/hardware/drivers/network/registering-as-an-interface-provider)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.ifprovider%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





