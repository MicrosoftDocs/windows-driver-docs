---
title: ndiskd.ndisref
description: The ndiskd.ndisref extension displays a debug log of a tracked reference count.
ms.assetid: 6860A567-1017-4184-B8DF-157467360FB9
keywords: ["ndiskd.ndisref Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.ndisref
api_type:
- NA
---

# !ndiskd.ndisref


The **!ndiskd.ndisref** extension displays a debug log of a tracked reference count.

``` syntax
    !ndiskd.ndisref [-handle <x>] [-tagtype <str>] [-stacks] [-tag <str>] [-refdebug] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Handle of the refcount block.

<span id="_______-tagtype______"></span><span id="_______-TAGTYPE______"></span> *-tagtype*   
Enum type of the tags.

<span id="_______-stacks______"></span><span id="_______-STACKS______"></span> *-stacks*   
Includes stack traces (if available).

<span id="_______-tag______"></span><span id="_______-TAG______"></span> *-tag*   
Limits display to a single tag.

<span id="_______-refdebug______"></span><span id="_______-REFDEBUG______"></span> *-refdebug*   
Shows detailed debug log, if available.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

The following example passes the handle of an NDIS miniport driver to the **!ndiskd.ndisref** extension to display the refcount block for that driver. First, run [**!ndiskd.minidriver**](-ndiskd-minidriver.md) with no parameters to see a list of all miniport drivers on the system. In the example output below, look for the handle for the kdnic driver, ffffdf801418d650.

```cmd
3: kd> !ndiskd.minidriver
    ffffdf8015a98380 - tunnel
    ffffdf801418d650 - kdnic
```

Using the miniport driver's handle, enter the **!ndiskd.ndisref -handle** command to see the refcount block for this miniport driver. The following example has the middle of the refcount block excised for brevity.

```cmd
3: kd> !ndiskd.ndisref ffffdf801418d650


REFCOUNT BLOCK

    Tag                                    Number of references                 
    0n0                                    0n6293             Show stacks
    0n1                                    0n1045             Show stacks
    0n2                                    0n4294966717       Show stacks
    0n5                                    0n25048            Show stacks
    0n18                                   0n4294967293       Show stacks
    0n19                                   0n4294967295       Show stacks
    0n21                                   0n4294967036       Show stacks
    0n23                                   0n30818            Show stacks
    0n24                                   0n24693            Show stacks
    0n25                                   0n25808            Show stacks

...

    0n153                                  0n7                Show stacks
    0n154                                  0n3                Show stacks
    0n156                                  0n29972            Show stacks
    0n159                                  0n4294959128       Show stacks
    0n160                                  0n30892            Show stacks
    0n161                                  0n136              Show stacks
    0n162                                  0n4294951910       Show stacks
    0n163                                  0n30892            Show stacks
    0n164                                  0n136              Show stacks
    0n167                                  0n4294965996       Show stacks

    Include inactive tags
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**!ndiskd.minidriver**](-ndiskd-minidriver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.ndisref%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





