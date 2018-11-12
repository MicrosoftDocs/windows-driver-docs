---
title: ndiskd.ndisslot
description: The **!ndiskd.ndisslot** extension displays the contents of an NDIS per-processor variable.
ms.assetid: 0EF37FE7-31A1-4A71-9CAC-E2A43F0EEBCF
keywords: ["ndiskd.ndisslot Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.ndisslot
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.ndisslot


**Note**  Third party network driver developers are not expected to manually use this extension command. You can run it to see the information it displays but you are not able to reuse the details it provides in your driver.

 

The **!ndiskd.ndisslot** extension displays the contents of an NDIS per-processor variable. If you run this extension with no parameters, !ndiskd will display a list of all NDIS per-processor variables on the system.

```console
!ndiskd.ndisslot [-handle <x>] [-itemtype <str>] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of the slot.

<span id="_______-itemtype______"></span><span id="_______-ITEMTYPE______"></span> *-itemtype*   
Type of the value stored in the slot.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

Run the **!ndiskd.ndisslot** extension with no parameters to see a list of all per-processor slot variables. The following example output has excised the middle portion of the list for brevity.

```console
1: kd> !ndiskd.ndisslot
    Per-processor slot                     Summary of contents                  
    ffffc804ae060000 - NDrw                All values are zero
    ffffc804ae060008 - NDrw                All values are zero
    ffffc804ae060010 - NDrw                All values are zero
    ffffc804ae060018 - NDrw                All values are zero
    ffffc804ae060020 - NDrw                All values are zero
    ffffc804ae060028 - NDrw                All values are zero
    ffffc804ae060030 - NDrw                All values are zero
    ffffc804ae060038 - NDrw                All values are zero
    ffffc804ae060040 - NDrw                All values are zero
    ffffc804ae060048 - NDrw                All values are zero

...

    ffffc804ae060910 - NDtk                All values are zero
    ffffc804ae060918 - NDtk                All values are zero
    ffffc804ae060920 - tsR                 All values are non-zero
    ffffc804ae060928 - NDrw                All values are zero
    ffffc804ae060930 - NDtk                All values are zero
    ffffc804ae060938 - NDtk                All values are zero
    ffffc804ae060940 - NDtk                All values are zero
    ffffc804ae060948 - NDtk                All values are zero
    ffffc804ae060950 - NDrw                All values are zero
    ffffc804ae060958 - NDrw                All values are zero

    Statistics
    Descriptors        1
    Total slots        512
    Slots available    275
    Slots used         237
    Efficiency         46%
```

Clicking on one of the handles for the per-processor slot variables will show you the details for that variable. The following example uses the handle ffffc804ae060920 for the tsR variable, from the previous example.

```console
1: kd> !ndiskd.ndisslot ffffc804ae060920
    Processor          Slot value                                               
    00                 00000006
    01                 00000006
    02                 00000006
    03                 00000006
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

 

 






