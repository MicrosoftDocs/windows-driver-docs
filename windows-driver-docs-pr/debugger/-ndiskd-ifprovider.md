---
title: ndiskd.ifprovider
description: The ndiskd.ifprovider extension displays information about an NDIS interface provider (IfProvider). 
keywords: ["ndiskd.ifprovider Windows Debugging"]
ms.date: 06/15/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.ifprovider
api_type:
- NA
---

# !ndiskd.ifprovider

The **!ndiskd.ifprovider** extension displays information about an [NDIS interface provider](../network/registering-as-an-interface-provider.md) (IfProvider). If you run this extension with no parameters, !ndiskd will display a list of all registered NDIS interface providers.

```console
!ndiskd.ifprovider [-handle <x>]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters

<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Optional handle of an IfProvider.

### DLL

Ndiskd.dll

### Examples

Run the **!ndiskd.ifprovider** extension with no parameters to get a list of all registered IfProviders.

```console
1: kd> !ndiskd.ifprovider
    IfProvider                                                                  
    ffffd20d14334180 - wanarp
    ffffd20d1264a950 - wfplwfs
    ffffd20d11deae00 - The NDIS loopback provider
    ffffd20d11deae70 - The NDIS interface provider
```

You can see from the previous example that the debugee machine has four interface providers registered. Two of them are NDIS interface providers.

**Note**  Interface providers are a generic concept and aren't required to be miniport drivers. While a miniport driver may choose to register as an interface provider if desired, most miniport drivers do not do so because NDIS has a built-in interface provider. The NDIS built-in interface provider automatically provides interfaces for every miniport driver, every Light-Weight Filter (LWF) module, and the loopback interface. For more information, see [NDIS interface provider](../network/registering-as-an-interface-provider.md).

The following example shows the details for the "wanarp" interface provider in the previous example, whose handle is ffffd20d14334180.

```console
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

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Registering as an Interface Provider](../network/registering-as-an-interface-provider.md)
