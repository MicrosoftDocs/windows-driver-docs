---
title: rpcexts.getclientcallinfo
description: The rpcexts.getclientcallinfo extension searches the system's RPC state information for client call (CCALL) information.
ms.assetid: 1b838238-63b3-4618-bc59-6b4d74274b9c
keywords: ["rpcexts.getclientcallinfo Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- rpcexts.getclientcallinfo
api_type:
- NA
---

# !rpcexts.getclientcallinfo


The **!rpcexts.getclientcallinfo** extension searches the system's RPC state information for client call (CCALL) information.

``` syntax
    !rpcexts.getclientcallinfo [ CallID | 0 [ IfStart | 0 [ ProcNum | 0xFFFF [ProcessID|0] ] ] ] 
!rpcexts.getclientcallinfo -? 
```

## <span id="ddk__rpcexts_getclientcallinfo_dbg"></span><span id="DDK__RPCEXTS_GETCLIENTCALLINFO_DBG"></span>Parameters


<span id="_______CallID______"></span><span id="_______callid______"></span><span id="_______CALLID______"></span> *CallID*   
Specifies the call ID. This parameter is optional; include it if you only want to display calls matching a specific *CallID* value.

<span id="_______IfStart______"></span><span id="_______ifstart______"></span><span id="_______IFSTART______"></span> *IfStart*   
Specifies the first DWORD of the interface UUID on which the call was made. This parameter is optional; include it if you only want to display calls matching a specific *IfStart* value.

<span id="_______ProcNum______"></span><span id="_______procnum______"></span><span id="_______PROCNUM______"></span> *ProcNum*   
Specifies the procedure number of this call. (The RPC Run-Time identifies individual routines from an interface by numbering them by position in the IDL file -- the first routine in the interface is 0, the second 1, and so on.) This parameter is optional; include it if you only want to display calls matching a specific *ProcNum* value.

<span id="_______ProcessID______"></span><span id="_______processid______"></span><span id="_______PROCESSID______"></span> *ProcessID*   
Specifies the process ID (PID) of the client process that owns the calls you want to display. This parameter is optional; omit it if you want to display calls owned by multiple processes.

<span id="_______-_______"></span> **-?**   
Displays some brief Help text for this extension in the Command Prompt window.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Rpcexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about debugging Microsoft Remote Procedure Call (RPC), see [RPC Debugging](rpc-debugging.md).

Remarks
-------

This extension can only be used with CDB or with user-mode WinDbg. It is only available if full RPC state information is being gathered.

Here is an example:

```
0:002> !rpcexts.getclientcallinfo
Searching for call info ...
## PID  CELL ID   PNO  IFSTART  TIDNUMBER CALLID   LASTTIME PS CLTNUMBER ENDPOINT
------------------------------------------------------------------------------
03d4 0000.0001 0000 19bb5061 0000.0000 00000001 0004ca9b 07 0000.0002 1118
```

For a similar example using the DbgRpc tool, see [Get RPC Client Call Information](get-rpc-client-call-information.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!rpcexts.getclientcallinfo%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




