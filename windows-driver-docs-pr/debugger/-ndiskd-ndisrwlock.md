---
title: ndiskd.ndisrwlock
description: The ndiskd.ndisrwlock extension displays information about an NDIS\_RW\_LOCK\_EX lock structure.
ms.assetid: 853CBAFE-3899-4983-BFC7-933D3BC7ADA1
keywords: ["ndiskd.ndisrwlock Windows Debugging"]
topic_type:
- apiref
api_name:
- ndiskd.ndisrwlock
api_type:
- NA
---

# !ndiskd.ndisrwlock


The **!ndiskd.ndisrwlock** extension displays information about an [**NDIS\_RW\_LOCK\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff567279) lock structure.

``` syntax
    !ndiskd.ndisrwlock [-handle <x>] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Handle of the lock structure.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

Use the **!ndiskd.ndisrwlock** extension if you create your own RW lock and would want to inspect it. To obtain the handle for an RW lock, use the *poi* command to dereference the address of your driver's lock. The following snippet shows how to look at a lock that the TCIPIP protocol was using at the time of the example.

```cmd
0: kd> !ndiskd.ndisrwlock poi(tcpip!gAleHashtableLock)


NDIS READ-WRITE LOCK

    Allocated by       [NDIS generic object]
    Exclusive access   Not acquired
    Read-only access   0 references

    Set a breakpoint on acquire/release
```

To observe the driver using this RW lock, click on the "Set a breakpoint on acquire/release" link at the bottom of the RW lock's details. After setting the breakpoint, enter the **g** command to let the debugee machine run and hit the breakpoint.

```cmd
0: kd> ba r4 ffffe00bc3fc22f8
0: kd> g
Breakpoint 0 hit
nt!KeTestSpinLock+0x3:
fffff802`0d69eb53 4885c0          test    rax,rax
```

Now you can re-run the same **!ndiskd.ndisrwlock** command to see that this RW lock has one Read-only access reference.

```cmd
0: kd> !ndiskd.ndisrwlock poi(tcpip!gAleHashtableLock)


NDIS READ-WRITE LOCK

    Allocated by       [NDIS generic object]
    Exclusive access   Not acquired
    Read-only access   1 reference

    Set a breakpoint on acquire/release
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**NDIS\_RW\_LOCK\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff567279)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.ndisrwlock%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





