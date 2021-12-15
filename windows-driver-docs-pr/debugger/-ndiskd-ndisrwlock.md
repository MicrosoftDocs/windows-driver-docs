---
title: ndiskd.ndisrwlock
description: The ndiskd.ndisrwlock extension displays information about an NDIS_RW_LOCK_EX lock structure.
keywords: ["ndiskd.ndisrwlock Windows Debugging"]
ms.date: 06/18/2020
topic_type:
- apiref
api_name:
- ndiskd.ndisrwlock
api_type:
- NA
---

# !ndiskd.ndisrwlock

The **!ndiskd.ndisrwlock** extension displays information about an [**NDIS\_RW\_LOCK\_EX**](/previous-versions/windows/hardware/drivers/ff567279(v=vs.85)) lock structure.

```console
!ndiskd.ndisrwlock -handle <x>
```

## Parameters

<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Handle of the lock structure.

### DLL

Ndiskd.dll

### Examples

Use the **!ndiskd.ndisrwlock** extension if you create your own RW lock and would want to inspect it. To obtain the handle for an RW lock, use the *poi* command to dereference the address of your driver's lock. The following snippet shows how to look at a lock that the TCIPIP protocol was using at the time of the example.

```console
0: kd> !ndiskd.ndisrwlock poi(tcpip!gAleHashtableLock)


NDIS READ-WRITE LOCK

    Allocated by       [NDIS generic object]
    Exclusive access   Not acquired
    Read-only access   0 references

    Set a breakpoint on acquire/release
```

To observe the driver using this RW lock, click on the "Set a breakpoint on acquire/release" link at the bottom of the RW lock's details. After setting the breakpoint, enter the **g** command to let the debugee machine run and hit the breakpoint.

```console
0: kd> ba r4 ffffe00bc3fc22f8
0: kd> g
Breakpoint 0 hit
nt!KeTestSpinLock+0x3:
fffff802`0d69eb53 4885c0          test    rax,rax
```

Now you can re-run the same **!ndiskd.ndisrwlock** command to see that this RW lock has one Read-only access reference.

```console
0: kd> !ndiskd.ndisrwlock poi(tcpip!gAleHashtableLock)


NDIS READ-WRITE LOCK

    Allocated by       [NDIS generic object]
    Exclusive access   Not acquired
    Read-only access   1 reference

    Set a breakpoint on acquire/release
```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-175-Debugging-the-Network-Stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**NDIS\_RW\_LOCK\_EX**](/previous-versions/windows/hardware/drivers/ff567279(v=vs.85))
