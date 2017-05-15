---
title: ndiskd.minidriver
description: The ndiskd.minidriver command displays information about an NDIS miniport driver. If you run this extension with no parameters, ndiskd will display a list of NDIS miniport drivers that are active on the system.
ms.assetid: CD349B10-8363-4D48-A830-CC9EF5EA75BF
keywords: ["ndiskd.minidriver Windows Debugging"]
topic_type:
- apiref
api_name:
- ndiskd.minidriver
api_type:
- NA
---

# !ndiskd.minidriver


The **!ndiskd.minidriver** command displays information about an NDIS miniport driver. If you run this extension with no parameters, !ndiskd will display a list of NDIS miniport drivers that are active on the system.

``` syntax
    !ndiskd.minidriver [-handle <x>] [-basic] [-miniports] [-devices] [-handlers] 
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of an NDIS miniport driver.

<span id="_______-basic______"></span><span id="_______-BASIC______"></span> *-basic*   
Displays basic information about the miniport driver.

<span id="_______-miniports______"></span><span id="_______-MINIPORTS______"></span> *-miniports*   
Displays the miniports associated with this miniport driver.

<span id="_______-devices______"></span><span id="_______-DEVICES______"></span> *-devices*   
Displays devices associated with this miniport driver.

<span id="_______-handlers______"></span><span id="_______-HANDLERS______"></span> *-handlers*   
Displays this driver's miniport handlers.

## <span id="DLL"></span><span id="dll"></span>DLL


Ndiskd.dll

Examples
--------

Enter the **!ndiskd.minidriver** command with no parameters to get a list of all NDIS miniport drivers active on the system. In the following example, look for the kdnic adapter's handle, ffffd20d12dec020

```cmd
1: kd> !ndiskd.minidriver -basic
    ffffd20d173deae0 - tunnel
    ffffd20d12dec020 - kdnic
```

Using the handle for the kdnic adapter, you can now click on the handle or enter the **!ndiskd.minidriver -handle** command to see detailed information for the tunnel miniport driver, as well as a list of miniports associated with it.

```cmd
1: kd> !ndiskd.minidriver ffffd20d12dec020


MINIPORT DRIVER

    kdnic

    Ndis handle        ffffd20d12dec020    [type it]
    Driver context     fffff80d2fa15100
    DRIVER_OBJECT      ffffd20d12dee540
    Driver image       kdnic.sys
    Registry path      \REGISTRY\MACHINE\SYSTEM\ControlSet001\Services\kdnic
    Reference Count    2
    Flags              [No flags set]


MINIPORTS

    Miniport                                                                    
    ffffd20d12dd71a0 - Microsoft Kernel Debug Network Adapter

    Handlers
    Device objects
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.minidriver%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





