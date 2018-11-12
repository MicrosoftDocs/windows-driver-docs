---
title: ndiskd.ndisref
description: The ndiskd.ndisref extension displays a debug log of a tracked reference count.
ms.assetid: 6860A567-1017-4184-B8DF-157467360FB9
keywords: ["ndiskd.ndisref Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.ndisref
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.ndisref


The **!ndiskd.ndisref** extension displays a debug log of a tracked reference count.

```console
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

```console
3: kd> !ndiskd.minidriver
    ffffdf8015a98380 - tunnel
    ffffdf801418d650 - kdnic
```

Using the miniport driver's handle, enter the **!ndiskd.ndisref -handle** command to see the refcount block for this miniport driver. The following example has the middle of the refcount block excised for brevity.

```console
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

 

 






